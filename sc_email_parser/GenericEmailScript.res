{"server_version": {"major": 32, "minor": 0, "build_number": 4502, "version": "32.0.4502"}, "export_format_version": 2, "id": 1, "export_date": 1550758484991, "fields": [{"id": 59, "name": "inc_training", "text": "Simulation", "prefix": null, "type_id": 0, "tooltip": "Whether the incident is a simulation or a regular incident. This field is read-only.", "input_type": "boolean", "hide_notification": false, "chosen": false, "default_chosen_by_server": false, "blank_option": false, "internal": false, "uuid": "c3f0e3ed-21e1-4d53-affb-fe5ca3308cca", "operations": [], "operation_perms": {}, "values": [], "read_only": true, "changeable": true, "rich_text": false, "export_key": "incident/inc_training", "templates": [], "deprecated": false}], "incident_types": [{"update_date": 1550758709844, "create_date": 1550758709844, "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0", "description": "Customization Packages (internal)", "export_key": "Customization Packages (internal)", "name": "Customization Packages (internal)", "enabled": false, "system": false, "parent_id": null, "hidden": false, "id": 0}], "phases": [], "automatic_tasks": [], "overrides": [], "message_destinations": [], "actions": [{"id": 14, "name": "Process email message", "type": 0, "object_type": "__emailmessage", "conditions": [{"method": "object_added", "field_name": null, "value": null, "type": null, "evaluation_id": null}], "automations": [{"type": "run_script", "value": null, "scripts_to_run": "Generic email script"}], "message_destinations": [], "workflows": [], "view_items": [], "timeout_seconds": 86400, "uuid": "88b88ef8-215e-42e8-bc96-ae7a120f64b8", "export_key": "Process email message", "logic_type": "all"}], "layouts": [], "notifications": null, "timeframes": null, "locale": null, "industries": null, "regulators": null, "geos": null, "task_order": [], "action_order": [], "types": [], "scripts": [{"id": 1, "name": "Generic email script", "description": "A script to perform non-specific processing on every email received.", "language": "python", "object_type": "__emailmessage", "uuid": "280dae02-a16c-40c5-9d1d-8f7bd69b443e", "actions": [], "script_text": "import re\n\n# A script to create an incident from an email message, and add artifacts to the incident based on information\n# present in the body text of the message.\n\nclass Utils:\n  \"\"\" A class to collect some utilities used by the rest of the script. \"\"\"\n\n  @staticmethod\n  def convertIPv4ToInt(address):\n    \"\"\" A static method that converts a IPv4 address to a binary representation. \"\"\"\n    addressAsBinary = 0\n    #split into octets\n    octets = address.split(\".\")\n    #startFromLeft\n    lpos = 32 - 8\n    for octet in octets:\n        octetAsInt = int(octet)\n        addressAsBinary = addressAsBinary + (octetAsInt << lpos)\n        lpos = lpos - 8\n    return addressAsBinary\n\n\n  @staticmethod\n  def convertIPV4v6ToInt(address):\n    \"\"\" A static method that converts a IPv4 and IPv6 address to a binary representation. \"\"\"\n    addressAsBinary = 0\n    # Split into hextets\n    hextets = address.split(\":\")\n    # It might be a V4 IP address in a V6 envelope\n    if \".\" in hextets[-1]:\n      return Utils.convertIPv4ToInt(hextets[-1])\n    else:\n      # Start from Left\n      lpos = 128 - 16\n      for hextet in hextets:\n          if len(hextet) == 0:\n              break\n          hextetAsInt = int(hextet,16)\n          addressAsBinary = addressAsBinary + (hextetAsInt << lpos)\n          lpos = lpos - 16\n      # If the previous loop has exited without covering all the hextets then it means there is a \"::\" present,\n      # so we have to process the reamining hextets from the right\n      if lpos > 0:\n          rpos = 0\n          for hextet in hextets[::-1]:\n              if len(hextet) == 0:\n                  break\n              hextetAsInt = int(hextet,16)\n              addressAsBinary = addressAsBinary + (hextetAsInt << rpos)\n              rpos = rpos + 16\n      return addressAsBinary\n\n\nclass WhiteListElement(object):\n  \"\"\" A class that represents a domain, IP address range or network segment that has been verified as not being suspicious. \"\"\"\n\n  # A text representation of the element\n  asString = None\n\n  def __init__(self, elementAsString):\n    \"\"\" The constructor that takes one parameter - the textual representation of the element. \"\"\"\n    self.asString = elementAsString\n\n  def __str__(self):\n    \"\"\"Method to return the text representation of the object.\"\"\"\n    return self.asString\n\n  def __repr__(self):\n    \"\"\"Method to return the text representation of the object.\"\"\"\n    return \"WhiteListElement(\\\"{0}\\\")\".format(self.asString)\n\n  def test(self, other):\n    \"\"\" A function intended to be inherited but overrided by subclasses. It should return True if the \"other\" object\n    would be matched by this white list element.\n    \"\"\"\n    return False\n\n\nclass IPAddress:\n  \"\"\" A class for IP addresses, both IPv4 and IPv6. \"\"\"\n\n  # The IP address as a String, as originally presented to the constructor\n  addressAsString = None\n\n  # The IP Address as a binary representation\n  addressAsBinary = None\n\n  def __init__(self, newAddressAsString):\n    \"\"\" The constructor, which takes one parameter - the string representation to be used to create the addressAsBinary. \"\"\"\n    self.addressAsString = newAddressAsString\n    self.addressAsBinary = Utils.convertIPV4v6ToInt(self.addressAsString)\n\n  def __str__(self):\n    \"\"\"Method to return the text representation of the object.\"\"\"\n    return self.addressAsString\n\n  def __repr__(self):\n    \"\"\"Method to return the text representation of the object.\"\"\"\n    return \"IPAddress(\\\"{0}\\\")\".format(self.addressAsString)\n\n\nclass CIDR(WhiteListElement):\n  \"\"\" A CIDR (Classless Inter-Domain Routing) is one of the possible types of white list element, representing either an explicit IP Address or\n  a subnet in the form of an IP Address and a subnet mask suffix. E.G.\n  127.0.0.1\n  10.0.0.0/8\n  fc00::/7\n  \"\"\"\n\n  # The suffix/subnet mask (defaults to 0 when not present)\n  cidrSuffix = 0\n  # Width of the address in bits (32 for IPv4, 128 for IPv6)\n  width = 32\n  # The address as a binary number\n  addressAsBinary = 0\n\n  def __init__(self, newCIDR):\n    \"\"\" CIDR constructor. This takes one parameter which is the textual representation of the CIDR. \"\"\"\n    # Store the textual representation in the base class\n    super(CIDR, self).__init__(newCIDR)\n    # Split at the subnet separator character (if present)\n    cidrParts = self.asString.split(\"/\")\n    # The first part is interpreted the IP address\n    self.addressAsBinary = Utils.convertIPV4v6ToInt(cidrParts[0])\n\n    self.width = 128 if \":\" in newCIDR else 32\n\n    # If there is a suffix, interpret it correctly\n    if len(cidrParts) > 1:\n      self.cidrSuffix = int(cidrParts[1])\n    else:\n     self.cidrSuffix = self.width\n\n  def test(self, anIPAddress):\n    \"\"\" An IP address matches the CIDR if both of them have the same binary value when both are shifted right by the\n    CIDR subnet mask suffix.\n    \"\"\"\n    log.debug(\"Going to filter IPAddress {0} against {1}\".format(anIPAddress, self))\n    return (anIPAddress.addressAsBinary >> (self.width - self.cidrSuffix) == self.addressAsBinary >> (self.width - self.cidrSuffix))\n\n\nclass IPRange(WhiteListElement):\n  \"\"\" A type of WhiteListElement that represents a range, from a lower bound to an upper bound, inclusive. \"\"\"\n  lowest = None\n  highest = None\n  \n  def __init__(self, stringRepresentation):\n    \"\"\" IPRange constructor that takes two parameters.\n    Parameter \"lowestAsText\" - the lowest IP address in the range.\n    Parameter \"highestAsText\" - the highest IP address in the range.\n    \"\"\"\n    lowestAsText, highestAsText = stringRepresentation.split(\"-\")\n    super(IPRange, self).__init__(stringRepresentation)    \n    self.lowest = IPAddress(lowestAsText)\n    self.highest = IPAddress(highestAsText)\n\n  def test(self, anIPAddress):\n    \"\"\" A method that returns true if anIPAddress is not below self.lowest and not above self.highest. \"\"\"\n    return self.highest.addressAsBinary >= anIPAddress.addressAsBinary and self.lowest.addressAsBinary <= anIPAddress.addressAsBinary\n\n  def __str__(self):\n    \"\"\"Method to return the text representation of the object.\"\"\"\n    return \"{0}-{1}\".format(self.lowest, self.highest)\n\n  def __repr__(self):\n    \"\"\"Method to return the text representation of the object.\"\"\"\n    return \"IPRange(\\\"{0}-{1}\\\")\".format(self.lowest, self.highest)\n\n\nclass Domain(WhiteListElement):\n  \"\"\" A type of WhiteListElement that represents a domain or domain pattern. E.G.\n  *.ibm.com\n  mailserver.knowngood.com\n  \"\"\"\n\n  # A regular expression to match the domain. Domains of the form \"*.customer.com\" are converted to \".*.customer.com\"\n  processedRegEx = None\n  \n  def __init__(self, stringRepresentation):\n    \"\"\" Constructor for the Domain class. This takes one parameter - the domain pattern as a String. \"\"\"\n    # Save the string representation in the superclass\n    super(Domain, self).__init__(stringRepresentation)    \n    self.processedRegEx = \"://{0}.*\".format(stringRepresentation.replace(\".\",\"\\.\").replace(\"*\", \".*\"))\n\n  def test(self, urlString):\n    \"\"\" A method that returns true if the value passed in urlString matches the regex in self.processedRegEx. \"\"\"\n    matches = re.findall(self.processedRegEx, urlString, re.IGNORECASE)\n    return (matches != None) and (len(matches) > 0)\n\n  def __str__(self):\n    \"\"\"Method to return the text representation of the object.\"\"\"\n    return \"{0}\".format(self.asString)\n\n  def __repr__(self):\n    \"\"\"Method to return the text representation of the object.\"\"\"\n    return \"Domain(\\\"{0}\\\")\".format(self.asString)\n\n\nclass EmailProcessor(object):\n  \"\"\" A class that facilitates processing the body contents of an email message.\n  Once the EmailProcessor class has been instanciated, the other methods can be used to add artifacts to the \n  incident.\n  \"\"\"\n\n  # The body text of the email\n  bodyText = \"\"\n\n  # The set of already-added artifacts. If an artifact is in the set then it will not be added to the incident\n  # a second time.\n  addedArtifacts = set()\n\n  # Standard Whitelist for IP addresses\n  ipV4WhiteList = [\n    CIDR(\"192.168.0.0/16\"),               #   Class B private network local communication (RFC 1918)\n    CIDR(\"198.18.0.0/15\"),                #  Testing of inter-network communications between subnets (RFC 2544)\n    IPRange(\"239.0.0.0-239.255.255.255\"), #   Administrative Multicast\n    CIDR(\"169.254.0.0/16\"),\n    CIDR(\"224.0.0.0/4\"),\n    CIDR(\"192.88.99.0/24\"),               #   6to4 anycast relays (RFC 3068)\n    CIDR(\"0.0.0.0/8\"),                    #   Broadcast message (RFC 1700)\n    CIDR(\"192.0.2.0/24\"),                 #   TEST-NET examples and documentation (RFC 5737)\n    CIDR(\"240.0.0.0/4\"),                  #   Reserved for  multicast assignments (RFC 5771)\n    CIDR(\"198.51.100.0/24\"),              #   TEST-NET-2 examples and documentation (RFC 5737)\n    CIDR(\"203.0.113.0/24\"),               #   TEST-NET-3 examples and documentation (RFC 5737)\n    CIDR(\"233.252.0.0/24\"),               #   Multicast test network\n    IPRange(\"234.0.0.0-238.255.255.255\"),\n    IPRange(\"225.0.0.0-231.255.255.255\"),\n    CIDR(\"127.0.0.1\")\n  ]\n\n  ipV6WhiteList = [\n    CIDR(\"fc00::/7\"),                     #   Unique Local Addresses (ULA)\n    CIDR(\"fec0::/10\"),                    #   Site Local Addresses (deprecated - RFC 3879)\n    CIDR(\"fe80::/10\"),\n    CIDR(\"ff00::/8\"),\n    CIDR(\"ff00::/12\"),\n    CIDR(\"::/8\"),\n    CIDR(\"0100::/8\"),\n    CIDR(\"0200::/7\"),\n    CIDR(\"0400::/6\"),\n    CIDR(\"0800::/5\"),\n    CIDR(\"1000::/4\"),\n    CIDR(\"4000::/3\"),\n    CIDR(\"6000::/3\"),\n    CIDR(\"8000::/3\"),\n    CIDR(\"A000::/3\"),\n    CIDR(\"C000::/3\"),\n    CIDR(\"E000::/4\"),\n    CIDR(\"F000::/5\"),\n    CIDR(\"F800::/6\"),\n    CIDR(\"FE00::/9\")    \n  ]\n\n  # Customer-specific IP address whitelists\n  # Add entries to these lists to whitelist the entries without disrupting the standard set above\n  customIPv4WhiteList = []\n  customIPv6WhiteList = []\n\n  # Standard domain whitelist\n  domainWhiteList=[Domain(\"*.ibm.com\")]\n\n  # Customer-specific domain whitelist\n  customDomainWhiteList=[]\n\n  def __init__(self, newBodyText):\n    \"\"\"The EmailProcessor constructor.\n    It takes as its only parameter the body text of email message, expected to be a string.\n    \"\"\"\n    self.bodyText = newBodyText\n    self.ipV4WhiteList.extend(self.customIPv4WhiteList)\n    self.ipV6WhiteList.extend(self.customIPv6WhiteList)\n    self.domainWhiteList.extend(self.customDomainWhiteList)\n\n\n  def addUniqueArtifact(self, theArtifact, artifactType, description):\n    \"\"\"This method adds a new unique artifact to the incident. Previously added artifacts are added to the \n    \"addedArtifacts\" set. If the new artifact as already been added to the list then it is not added to the \n    incident a second time.\n    Parameter \"theArtifact\" - the value of the artifact to create.\n    Parameter \"artifactType\" - the type of the artifact.\n    Parameter \"description\" - the description of the artifact.\n    No return value.\n    \"\"\"\n    if (theArtifact, artifactType) in self.addedArtifacts:\n      log.debug(u\"Skipping previously added artifact {0} of type {1}, description {2}\".format(theArtifact, artifactType, description))\n    else:\n      log.info(u\"Adding artifact {0} of type {1}, description {2}\".format(theArtifact, artifactType, description))\n      incident.addArtifact(artifactType, theArtifact, description)\n      self.addedArtifacts.add((theArtifact, artifactType))\n\n  def addRecipient(self, recipient):\n    \"\"\"A method to add the email address of the recipient of the email message to the incident as an artifact.\n    If the recipient has a name as well as an address, the name is added as part of the artifact.\n    Parameter \"recipient\" - an object with a String \"address\" and \"name\" attribute.\n    No return value.\n    \"\"\"\n    fullData = recipient.address\n    if recipient.name:\n      fullData = \"{0} <{1}>\".format(recipient.name, recipient.address)\n    log.debug(\"Adding recipient {0}\".format(fullData))\n    self.addUniqueArtifact(fullData, \"Email Recipient\", \"Suspicious email recipient\")        \n\n\n  def printList(self, name, list):\n    \"\"\"A convenience method to log the contents of a list. The method will log each element in a list, along with\n    its name and ordinal in the list.\n    Parameter \"name\" - the name of the elements in the list e.g. \"IP Address\".\n    Parameter \"list\" - the list to iterate through.\n    No return value.\n    \"\"\"\n    for num, value in enumerate(list):\n      log.debug(\"{0} {1} {2}\".format(name, num, value))  \n\n  @staticmethod\n  def makeUrlPattern(scheme = \"http\"):\n    \"\"\"A method to return a regex pattern that includes a full URL including scheme, domain, path, hash and \n    query string. It starts the match from the scheme name with optional \"s\", followed by \"://\" and continues until\n    it finds a character that is not permitted in a URL. Because of the expectation that potentially harmful URLs\n    are being modified for safety, the URL-invalid characters \"[\" and \"]\" will not terminate the match.\n    Parameter \"scheme\" - the scheme (protocol) of the URL, defaults to \"http\".\n    Returns the requested pattern as a string.\n    \"\"\"\n    return scheme + \"s?://[^^|~`\\\\s<>\\\"'{}]*\"\n\n  @staticmethod\n  def fixURL(theURL):\n    \"\"\"Method to fix a list of bowdlerized URLs. Many systems attempts to make potentially dangerous URLs into\n    unopenable but human-readible strings. Resilient will reject URL artifacts that do not conform to spec.\n    In this case we are converting \"www[.]dangerous[.]nasty\" to \"www.dangerous.nasty\".\n    Parameter \"list\" - the list of URLs to fix.\n    Returns a new list containing fixed versions of the original list.\n    \"\"\"\n    return re.sub(r\"\\[\\.\\]\",\".\",theURL)\n\n  @staticmethod\n  def makeIPv4Pattern():\n    \"\"\"A method to return a pattern that matches valid IPv4 addresses.\n    Returns a string containing a pattern that matches 4 instances of 1-3 decimal digits, separated by \".\".\n    \"\"\"\n    return \"(?:[\\d]{1,3}\\.){3}[\\d]{1,3}\"\n\n  @staticmethod\n  def cleanIPv4(anAddress):\n    \"\"\"A method to filter out impossible IP4 addresses from a list of strings that have been matched by the pattern\n    from makeIPv4Pattern(). \n    First each address is split into its component octets. If the maximum int value of an octet in an address is\n    less than 256 then the address is valid. The return value is a set, to avoid unnecessary duplication.\n    Parameter \"addressList\" - the list of addresses to filter.\n    Returns a new set of valid addresses.\n    \"\"\"\n    octets = anAddress.split(\".\")\n    octetsAsIntArray = map(int, octets)\n    if (len(octets) != 4) or max(octetsAsIntArray) > 255:\n      return None\n    else:\n      return \".\".join(map(str, octetsAsIntArray)) # eliminate leading zeros.\n\n  @staticmethod\n  def makeIPv6Pattern():\n    \"\"\"A method to return a pattern that will match IPv6 addresses.\n    The pattern will match strings of the form:\n    abcd:abcd:1234:abcd:abcd:abcd:abcd:abcd:abcd\n    abcd:abcd::abcd:abcd:abcd:abcd:abcd\n    abcd:abcd:abcd:abcd:abcd:abcd::abcd\n    ::1\n    ::ffff:192.0.1.1\n    but it will also match strings such as\n    16:38:37\n    This necessitates a second cleaning stage, performed by cleanIPv6().\n    \"\"\"\n    return \"((?:(?:[A-Fa-f0-9]){0,4}:){1,7}(?:[A-Fa-f0-9]){1,4}(?:\\\\.[0-9]{1,3}){0,3})\"\n\n  @staticmethod\n  def cleanIP(anAddress):\n    \"\"\"A method to filter invalid IP addresses from the addressList parameter. The list is presumed to derive\n    from matching text based on the output of makeIPv6Pattern() or makeIPv4Pattern().\n    If the method discovers that the address is encapsulated IPv4 then the method will return the result from calling\n    cleanIPv4() on the IPv4 section. If the address is IPv6 the method will reject strings with more than 7 \":\"s or\n    more than one instance of \"::\". If there is no \"::\" then there must be 7 \":\"s.\n    \"\"\"\n    log.debug(\"Going to clean IP address {0}\".format(anAddress))\n    hextets = anAddress.split(\":\")\n    # It might be a V4 IP address in a V6 envelope\n    if \".\" in hextets[-1]:\n      return EmailProcessor.cleanIPv4(hextets[-1])\n    # At most 7 \":\"\n    if anAddress.count(\":\") < 8:\n      # At most one instance of \"::\"\n      if anAddress.count(\"::\") < 2:\n        if anAddress.count(\"::\") == 1 or anAddress.count(\":\") == 7:\n            return anAddress\n    return None\n\n\n  @staticmethod\n  def makeHexPattern(length):\n    \"\"\"A method that returns a regex pattern that matches a case-insensitive hexadecimal number of exactly a specified\n    length.\n    Parameter \"length\" - the length of the pattern in digits/characters/nibbles\n    Returns the corresponding pattern.\n    \"\"\"\n    return \"[^0-9a-zA-Z]([0-9a-fA-F]{\" + str(length) + \"})[^0-9a-zA-Z]\"\n\n\n  def processArtifactCategory(self, regex, artifactType, description, *optionalListModifierFn):\n    \"\"\"A method to process a category of artifact, based on a regular expression. Each match of the regex in the\n    bodyText is added as an artifact of the same type and description. The optional list modifier function, if present,\n    is run against the list of matches before the artifact addition takes place.\n    Parameter \"regex\" - the regular expression to use to pick out the text to interpret as an artifact\n    Parameter \"artifactType\" - the type of the artifact\n    Parameter \"description\" - the description of the artifact\n    Parameter \"optionalListModifierFn\" - a function to run across the list of matches to filter inappropriate values\n    No return value.\n    \"\"\"\n    if self.bodyText is None:\n      log.debug(\"Body is empty so not able to find artifact {0} for regex {1}\".format(artifactType,regex))\n    else:\n      dataList = set(re.findall(regex, self.bodyText))\n      if dataList is not None and len(dataList) > 0 :\n        if optionalListModifierFn is not None:\n          for aFunction in optionalListModifierFn:\n            dataList = map(aFunction, dataList)\n            dataList = [x for x in dataList if x is not None]\n\n        self.printList(\"Found {0} ( {1} )\".format(artifactType,description), dataList)\n        map(lambda theArtifact: self.addUniqueArtifact(theArtifact, artifactType, description), dataList)\n      else:\n        log.debug(\"Could not find artifact {0} for regex {1}\".format(artifactType,regex))\n\n\n  def checkIsItemNotOnWhiteList(self, anItem, whiteList):\n    \"\"\" A method that checks if an IP Address should be removed from the artifact list because if matches a whitelist element.\n    Parameter \"anItem\" - the item in question.\n    Return value: True if the item should be kept, false if it should be removed.\n    \"\"\"\n    for whiteListEntry in whiteList:\n      if whiteListEntry.test(anItem):\n        log.info(\"Filtering out IP Address {0} because it matched with whitelist entry {1}\".format(anItem, whiteListEntry))\n        return None\n    return anItem\n\n\n  def checkIPWhiteList(self, anAddress):\n    \"\"\" A method to check a list of IP Addresses aginst the whitelist. \"\"\"\n    whiteList = self.ipV4WhiteList if \".\" in anAddress.addressAsString else self.ipV6WhiteList\n    log.debug(\"Going to filter {0} against whitelist \".format(anAddress, whiteList))\n    return self.checkIsItemNotOnWhiteList(anAddress, whiteList)\n\n\n  def checkDomainWhiteList(self, aURL):\n    \"\"\" A method to check a list of URLs aginst a whitelist. \"\"\"\n    log.debug(\"Going to filter {0} against whitelist \".format(aURL, self.domainWhiteList))\n    return self.checkIsItemNotOnWhiteList(aURL,self.domainWhiteList)\n\n\n  def processIPFully(self, theAddressAsString):\n    \"\"\" A method to filter inadvertantly matched IP strings and then filter out IP addresses that appear on the whitelist.\n    Parameter \"theAddressAsString\" - The address in question as a string \n    Return value - if the address passes the tests then it is returned, otherwise None.\n    \"\"\"\n    theAddressAsString = self.cleanIP(theAddressAsString)        # Remove invalid address matches\n    if theAddressAsString is not None:\n      theAddressAsObj = IPAddress(theAddressAsString)            # Convert to IPAddress object\n      if theAddressAsObj is not None:\n        theAddressAsObj = self.checkIPWhiteList(theAddressAsObj) # Check against whitelist\n        if theAddressAsObj is not None:\n          return theAddressAsObj.addressAsString                 # Convert back to String\n    return None                                                  # The address was filtered out\n\n\n  def processAttachments(self):\n    \"\"\" A method to process the email attachments, if present. Each non-inline email attachment is added as an \n    attachment to the incident, and its name is added as an artifact. Inline attachments are assumed to be unimportant.\n    No return value.\n    \"\"\"\n    for attachment in emailmessage.attachments:\n      if not attachment.inline:\n        incident.addEmailAttachment(attachment.id)\n        incident.addArtifact(\"Email Attachment Name\", attachment.suggested_filename, \"\")\n\n\n  def addBasicInfoToIncident(self):\n    \"\"\"A method to perform basic information extraction from the email message.\n    The email message sender address, including personal name if present, is set as the reporter field\n    in the incident. An artifact is created from the email message subject with the type \"Email Subject\".\n    No return value.\n    \"\"\" \n  \n    newReporterInfo = emailmessage.from.address\n    if emailmessage.from.name is not None:\n      newReporterInfo = u\"{0} <{1}>\".format(emailmessage.from.name, emailmessage.from.address)\n    log.info(\"Adding reporter field \\\"{0}\\\"\".format(newReporterInfo))\n    incident.reporter = newReporterInfo\n\n    if emailmessage.subject is not None:\n      self.addUniqueArtifact(u\"{0}\".format(emailmessage.subject), \"Email Subject\", \"Suspicious email subject\")\n\n###\n# Mainline starts here\n###\n\n# Create the email processor object, loading it with the email message body content.\nprocessor = EmailProcessor(emailmessage.body.content)\n\n# The new incident owner\nnewIncidentOwner = \"admin@co3sys.com\"\n\n# Create a suitable title for an incident based on the email\nnewIncidentTitle = u\"Incident generated from email \\\"{0}\\\" via mailbox {1}\".format(emailmessage.subject, emailmessage.inbound_mailbox)\n\n# Check to see if a similar incident already exists\n# We will search for an incident which has the same name as we would give a new incident\nquery_builder.equals(fields.incident.name, newIncidentTitle)\nquery_builder.equals(fields.incident.plan_status, \"Active\")\nquery = query_builder.build()\nincidents = helper.findIncidents(query)\n\nif len(incidents) == 0:\n  # A similar incident does not already exist. Create a new incident and associate the email with it.\n  log.info(u\"Creating new incident {0}\".format(newIncidentTitle))\n  \n  # Create an incident with a title based on the email subject, owned by user admin@co3sys.com\n  emailmessage.createAssociatedIncident(newIncidentTitle, newIncidentOwner)\n\n  # Add the subject to the incident as an artifact, and set the incident reporter.\n  # This does not need to be done for an existing incident.\n  processor.addBasicInfoToIncident()\n\nelse:\n\n   # A similar incident already exists. Associate the email with this preexisting incident.\n  log.info(\"Associating with existing incident {0}\".format(incidents[0].id))\n  emailmessage.associateWithIncident(incidents[0])\n\n# Capture any URLs present in the email body text and add them as artifacts\nprocessor.processArtifactCategory(processor.makeUrlPattern(), \"URL\", \"Suspicious URL\", processor.fixURL, processor.checkDomainWhiteList)\n\n# Capture any IPv4 addresses present in the email body text and add them as artifacts\nprocessor.processArtifactCategory(processor.makeIPv4Pattern(), \"IP Address\", \"Suspicious IP Address\", processor.processIPFully)\n\n# Capture any IPv6 addresses present in the email body text and add them as artifacts\nprocessor.processArtifactCategory(processor.makeIPv6Pattern(), \"IP Address\", \"Suspicious IP Address\", processor.processIPFully)\n\n# Capture 32-character hexadecimal substrings in the email body text and add them as MD5 hash artifacts\nprocessor.processArtifactCategory(processor.makeHexPattern(32), \"Malware MD5 Hash\", \"MD5 hash of potential malware file\")\n\n# Capture 40-character hexadecimal substrings in the email body text and add them as SHA-1 hash artifacts\nprocessor.processArtifactCategory(processor.makeHexPattern(40), \"Malware SHA-1 Hash\", \"SHA-1 hash of potential malware file\")\n\n# Capture 64-character hexadecimal substrings in the email body text and add them as SHA-256 hash artifacts\nprocessor.processArtifactCategory(processor.makeHexPattern(64), \"Malware SHA-256 Hash\", \"SHA-256 hash of potential malware file\")\n\n# Add email message attachments to incident\nprocessor.processAttachments()", "creator_id": "a@example.com", "last_modified_by": "a@example.com", "last_modified_time": 1550756214520, "export_key": "Generic email script"}], "incident_artifact_types": [], "workflows": [], "roles": [], "workspaces": [], "functions": []}