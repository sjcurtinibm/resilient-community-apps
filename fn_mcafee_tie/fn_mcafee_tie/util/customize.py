# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_mcafee_tie"""

from __future__ import print_function
from resilient_circuits.util import *


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     mcafee_tie_hash
    #     mcafee_tie_hash_type
    #   DataTables:
    #     tie_results
    #   Message Destinations:
    #     mcafee_tie_md
    #   Functions:
    #     mcafee_tie_search_hash
    #   Workflows:
    #     mcafee_tie_hash_search_workflow
    #   Rules:
    #     (Example) McAfee artifact hash search


    yield ImportDefinition(u"""
eyJ0YXNrX29yZGVyIjogW10sICJ3b3JrZmxvd3MiOiBbeyJwcm9ncmFtbWF0aWNfbmFtZSI6ICJt
Y2FmZWVfdGllX2hhc2hfc2VhcmNoX3dvcmtmbG93IiwgIm9iamVjdF90eXBlIjogImFydGlmYWN0
IiwgImV4cG9ydF9rZXkiOiAibWNhZmVlX3RpZV9oYXNoX3NlYXJjaF93b3JrZmxvdyIsICJ1dWlk
IjogIjRlZDY1MDk0LWUxNmQtNDczMi04ODYyLTA4Y2UxNWE3NWE4NSIsICJsYXN0X21vZGlmaWVk
X2J5IjogImJ3YWxzaEByZXNpbGllbnRzeXN0ZW1zLmNvbSIsICJuYW1lIjogIihFeGFtcGxlKSBN
Y0FmZWUgVElFIGhhc2ggc2VhcmNoIHdvcmtmbG93IiwgImNvbnRlbnQiOiB7InhtbCI6ICI8P3ht
bCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9XCJVVEYtOFwiPz48ZGVmaW5pdGlvbnMgeG1sbnM9
XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L01PREVMXCIgeG1sbnM6YnBt
bmRpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9ESVwiIHhtbG5zOm9t
Z2RjPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQvRENcIiB4bWxuczpvbWdk
aT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RJXCIgeG1sbnM6cmVzaWxp
ZW50PVwiaHR0cDovL3Jlc2lsaWVudC5pYm0uY29tL2JwbW5cIiB4bWxuczp4c2Q9XCJodHRwOi8v
d3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYVwiIHhtbG5zOnhzaT1cImh0dHA6Ly93d3cudzMub3Jn
LzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlXCIgdGFyZ2V0TmFtZXNwYWNlPVwiaHR0cDovL3d3dy5j
YW11bmRhLm9yZy90ZXN0XCI+PHByb2Nlc3MgaWQ9XCJtY2FmZWVfdGllX2hhc2hfc2VhcmNoX3dv
cmtmbG93XCIgaXNFeGVjdXRhYmxlPVwidHJ1ZVwiIG5hbWU9XCIoRXhhbXBsZSkgTWNBZmVlIFRJ
RSBoYXNoIHNlYXJjaCB3b3JrZmxvd1wiPjxkb2N1bWVudGF0aW9uPldvcmtmbG93IHRvIHRyaWdn
ZXIgZnVuY3Rpb24gdG8gc2VhcmNoIGhhc2ggaW4gVElFLjwvZG9jdW1lbnRhdGlvbj48c3RhcnRF
dmVudCBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMTU5
a2IzeTwvb3V0Z29pbmc+PC9zdGFydEV2ZW50PjxzZXJ2aWNlVGFzayBpZD1cIlNlcnZpY2VUYXNr
XzB0cm5wZWtcIiBuYW1lPVwiTWNBZmVlIFRJRSBzZWFyY2ggaGFzaFwiIHJlc2lsaWVudDp0eXBl
PVwiZnVuY3Rpb25cIj48ZXh0ZW5zaW9uRWxlbWVudHM+PHJlc2lsaWVudDpmdW5jdGlvbiB1dWlk
PVwiNDRhOWNmNWItMTZiNy00Y2VhLWFkYzQtMzk1NmIwNzlhMWFiXCI+e1wiaW5wdXRzXCI6e30s
XCJwcmVfcHJvY2Vzc2luZ19zY3JpcHRcIjpcImlmIGFydGlmYWN0LnR5cGUgPT0gXFxcIk1hbHdh
cmUgTUQ1IEhhc2hcXFwiOlxcbiAgaW5wdXRzLm1jYWZlZV90aWVfaGFzaF90eXBlID0gXFxcIm1k
NVxcXCJcXG4gIGlucHV0cy5tY2FmZWVfdGllX2hhc2ggPSBhcnRpZmFjdC52YWx1ZVxcbmVsaWYg
YXJ0aWZhY3QudHlwZSA9PSBcXFwiTWFsd2FyZSBTSEEtMSBIYXNoXFxcIjpcXG4gIGlucHV0cy5t
Y2FmZWVfdGllX2hhc2hfdHlwZSA9IFxcXCJzaGExXFxcIlxcbiAgaW5wdXRzLm1jYWZlZV90aWVf
aGFzaCA9IGFydGlmYWN0LnZhbHVlXFxuZWxpZiBhcnRpZmFjdC50eXBlID09IFxcXCJNYWx3YXJl
IFNIQS0yNTYgSGFzaFxcXCI6XFxuICBpbnB1dHMubWNhZmVlX3RpZV9oYXNoX3R5cGUgPSBcXFwi
c2hhMjU2XFxcIlxcbiAgaW5wdXRzLm1jYWZlZV90aWVfaGFzaCA9IGFydGlmYWN0LnZhbHVlXFxu
ZWxzZTpcXG4gIGhlbHBlci5mYWlsKFxcXCJBcnRpZmFjdCBoYXNoIHdhcyBub3Qgc2V0IGNvcnJl
Y3RseVxcXCIpXFxuXCIsXCJyZXN1bHRfbmFtZVwiOlwiXCIsXCJwb3N0X3Byb2Nlc3Npbmdfc2Ny
aXB0XCI6XCJcXFwiXFxcIlxcXCJcXG5EYXRhIHJldHVybmVkIHdpbGwgYmUgaW4gdGhlIGZvbGxv
d2luZyBzdHJ1Y3R1cmVcXG5cXG5cXG57ICBcXG4gICBcXFwiR1RJXFxcIjp7ICBcXG4gICAgICBc
XFwiRmlsZSBQcm92aWRlclxcXCI6XFxcIkdUSVxcXCIsXFxuICAgICAgXFxcIkF0dHJpYnV0ZXNc
XFwiOnsgIFxcblxcbiAgICAgIH0sXFxuICAgICAgXFxcIkNyZWF0ZSBEYXRlXFxcIjpcXFwiMjAx
OC0wMi0yMSAxMjoxNzoxMFxcXCIsXFxuICAgICAgXFxcIlRydXN0IExldmVsXFxcIjpcXFwiS25v
d24gTWFsaWNpb3VzXFxcIlxcbiAgIH0sXFxuICAgXFxcIkFURFxcXCI6eyAgXFxuICAgICAgXFxc
IkZpbGUgUHJvdmlkZXJcXFwiOlxcXCJBVERcXFwiLFxcbiAgICAgIFxcXCJDcmVhdGUgRGF0ZVxc
XCI6XFxcIjIwMTgtMDMtMTQgMTE6NTM6MDlcXFwiLFxcbiAgICAgIFxcXCJUcnVzdCBMZXZlbFxc
XCI6XFxcIk1vc3QgTGlrZWx5IE1hbGljaW91c1xcXCJcXG4gICB9LFxcbiAgIFxcXCJNV0dcXFwi
OnsgIFxcbiAgICAgIFxcXCJGaWxlIFByb3ZpZGVyXFxcIjpcXFwiTVdHXFxcIixcXG4gICAgICBc
XFwiQ3JlYXRlIERhdGVcXFwiOlxcXCIyMDE4LTAzLTE0IDExOjUzOjU1XFxcIixcXG4gICAgICBc
XFwiVHJ1c3QgTGV2ZWxcXFwiOlxcXCJNb3N0IExpa2VseSBNYWxpY2lvdXNcXFwiXFxuICAgfSxc
XG4gICBcXFwiRW50ZXJwcmlzZVxcXCI6eyAgXFxuICAgICAgXFxcIkZpbGUgUHJvdmlkZXJcXFwi
OlxcXCJFbnRlcnByaXNlXFxcIixcXG4gICAgICBcXFwiQXR0cmlidXRlc1xcXCI6eyAgXFxuICAg
ICAgICAgXFxcIkF2ZXJhZ2UgTG9jYWwgUmVwXFxcIjpcXFwiTW9zdCBMaWtlbHkgTWFsaWNpb3Vz
XFxcIixcXG4gICAgICAgICBcXFwiRmlyc3QgQ29udGFjdFxcXCI6XFxcIjIwMTgtMDItMjEgMTI6
MTc6MTBcXFwiLFxcbiAgICAgICAgIFxcXCJNaW4gTG9jYWwgUmVwXFxcIjpcXFwiTW9zdCBMaWtl
bHkgTWFsaWNpb3VzXFxcIixcXG4gICAgICAgICBcXFwiSXMgUHJldmFsZW50XFxcIjpcXFwiMFxc
XCIsXFxuICAgICAgICAgXFxcIkZpbGUgTmFtZSBDb3VudFxcXCI6XFxcIjFcXFwiLFxcbiAgICAg
ICAgIFxcXCJNYXggTG9jYWwgUmVwXFxcIjpcXFwiTW9zdCBMaWtlbHkgTWFsaWNpb3VzXFxcIlxc
biAgICAgIH0sXFxuICAgICAgXFxcIkNyZWF0ZSBEYXRlXFxcIjpcXFwiMjAxOC0wMi0yMSAxMjox
NzoxMFxcXCIsXFxuICAgICAgXFxcIlRydXN0IExldmVsXFxcIjpcXFwiTW9zdCBMaWtlbHkgTWFs
aWNpb3VzXFxcIlxcbiAgIH1cXG4gICBcXFwic3lzdGVtX2xpc3RcXFwiOlt7XFxuICAgICBcXFwi
ZGF0ZVxcXCI6IDE1MTkyMzM1NjMsXFxuICAgICBcXFwiYWdlbnRHdWlkXFxcIjoge2EwMDcyOGZm
LTMxODctNDZjMS05N2QyLThlMGYyNmVhOTQwYn1cXG4gICB9XVxcbn1cXG5cXFwiXFxcIlxcXCJc
XG5cXG5yb3cgPSBpbmNpZGVudC5hZGRSb3coXFxcInRpZV9yZXN1bHRzXFxcIilcXG5yb3dbXFxc
Imhhc2hfdHlwZVxcXCJdID0gYXJ0aWZhY3QudHlwZVxcbnJvd1tcXFwiaGFzaFxcXCJdID0gYXJ0
aWZhY3QudmFsdWVcXG5yb3dbXFxcImZpbGVfcHJvdmlkZXJcXFwiXSA9IHJlc3VsdHNbXFxcIkVu
dGVycHJpc2VcXFwiXVtcXFwiRmlsZSBQcm92aWRlclxcXCJdXFxucm93W1xcXCJ0cnVzdF9sZXZl
bFxcXCJdID0gcmVzdWx0c1tcXFwiRW50ZXJwcmlzZVxcXCJdW1xcXCJUcnVzdCBMZXZlbFxcXCJd
XFxucm93W1xcXCJ0aWVfY3JlYXRlX2RhdGVcXFwiXSA9IHJlc3VsdHNbXFxcIkVudGVycHJpc2Vc
XFwiXVtcXFwiQ3JlYXRlIERhdGVcXFwiXVxcblxcblxcblxcblxcblwifTwvcmVzaWxpZW50OmZ1
bmN0aW9uPjwvZXh0ZW5zaW9uRWxlbWVudHM+PGluY29taW5nPlNlcXVlbmNlRmxvd18xNTlrYjN5
PC9pbmNvbWluZz48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzE3cTF2ZTk8L291dGdvaW5nPjwvc2Vy
dmljZVRhc2s+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18xNTlrYjN5XCIgc291cmNl
UmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiU2VydmljZVRhc2tfMHRybnBl
a1wiLz48ZW5kRXZlbnQgaWQ9XCJFbmRFdmVudF8xYWhmMWtiXCI+PGluY29taW5nPlNlcXVlbmNl
Rmxvd18xN3ExdmU5PC9pbmNvbWluZz48L2VuZEV2ZW50PjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1
ZW5jZUZsb3dfMTdxMXZlOVwiIHNvdXJjZVJlZj1cIlNlcnZpY2VUYXNrXzB0cm5wZWtcIiB0YXJn
ZXRSZWY9XCJFbmRFdmVudF8xYWhmMWtiXCIvPjx0ZXh0QW5ub3RhdGlvbiBpZD1cIlRleHRBbm5v
dGF0aW9uXzFreHhpeXRcIj48dGV4dD5TdGFydCB5b3VyIHdvcmtmbG93IGhlcmU8L3RleHQ+PC90
ZXh0QW5ub3RhdGlvbj48YXNzb2NpYXRpb24gaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4XCIgc291
cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiVGV4dEFubm90YXRpb25f
MWt4eGl5dFwiLz48L3Byb2Nlc3M+PGJwbW5kaTpCUE1ORGlhZ3JhbSBpZD1cIkJQTU5EaWFncmFt
XzFcIj48YnBtbmRpOkJQTU5QbGFuZSBicG1uRWxlbWVudD1cInVuZGVmaW5lZFwiIGlkPVwiQlBN
TlBsYW5lXzFcIj48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlN0YXJ0RXZlbnRfMTU1
YXN4bVwiIGlkPVwiU3RhcnRFdmVudF8xNTVhc3htX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9
XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiMTYyXCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJl
bD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjBcIiB3aWR0aD1cIjkwXCIgeD1cIjE1N1wiIHk9XCIy
MjNcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5T
aGFwZSBicG1uRWxlbWVudD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIiBpZD1cIlRleHRBbm5v
dGF0aW9uXzFreHhpeXRfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjMwXCIgd2lkdGg9XCIx
MDBcIiB4PVwiOTlcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5F
ZGdlIGJwbW5FbGVtZW50PVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIGlkPVwiQXNzb2NpYXRpb25f
MXNldWo0OF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTY5XCIgeHNpOnR5cGU9XCJvbWdkYzpQ
b2ludFwiIHk9XCIyMjBcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIxNTNcIiB4c2k6dHlwZT1cIm9t
Z2RjOlBvaW50XCIgeT1cIjI1NFwiLz48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5TaGFw
ZSBicG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzB0cm5wZWtcIiBpZD1cIlNlcnZpY2VUYXNrXzB0
cm5wZWtfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjgwXCIgd2lkdGg9XCIxMDBcIiB4PVwi
MzU0XCIgeT1cIjE2NlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1u
RWxlbWVudD1cIlNlcXVlbmNlRmxvd18xNTlrYjN5XCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMTU5a2Iz
eV9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTk4XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwi
IHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIzNTRcIiB4c2k6dHlwZT1cIm9tZ2RjOlBv
aW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1c
IjEzXCIgd2lkdGg9XCIwXCIgeD1cIjI3NlwiIHk9XCIxODQuNVwiLz48L2JwbW5kaTpCUE1OTGFi
ZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJFbmRF
dmVudF8xYWhmMWtiXCIgaWQ9XCJFbmRFdmVudF8xYWhmMWtiX2RpXCI+PG9tZ2RjOkJvdW5kcyBo
ZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiNjM2XCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQ
TU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjY1NFwi
IHk9XCIyMjdcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRp
OkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzE3cTF2ZTlcIiBpZD1cIlNlcXVl
bmNlRmxvd18xN3ExdmU5X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCI0NTRcIiB4c2k6dHlwZT1c
Im9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjYzNlwiIHhzaTp0
eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpC
b3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNTQ1XCIgeT1cIjE4NC41XCIvPjwv
YnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48L2JwbW5kaTpCUE1OUGxhbmU+PC9i
cG1uZGk6QlBNTkRpYWdyYW0+PC9kZWZpbml0aW9ucz4iLCAid29ya2Zsb3dfaWQiOiAibWNhZmVl
X3RpZV9oYXNoX3NlYXJjaF93b3JrZmxvdyIsICJ2ZXJzaW9uIjogNTJ9LCAid29ya2Zsb3dfaWQi
OiAzLCAiYWN0aW9ucyI6IFtdLCAibGFzdF9tb2RpZmllZF90aW1lIjogMTUyMzQ1MDgyNjMyNCwg
ImNyZWF0b3JfaWQiOiAiYndhbHNoQHJlc2lsaWVudHN5c3RlbXMuY29tIiwgImRlc2NyaXB0aW9u
IjogIldvcmtmbG93IHRvIHRyaWdnZXIgZnVuY3Rpb24gdG8gc2VhcmNoIGhhc2ggaW4gVElFLiJ9
XSwgImFjdGlvbnMiOiBbeyJsb2dpY190eXBlIjogImFsbCIsICJuYW1lIjogIihFeGFtcGxlKSBN
Y0FmZWUgYXJ0aWZhY3QgaGFzaCBzZWFyY2giLCAidmlld19pdGVtcyI6IFtdLCAidHlwZSI6IDEs
ICJ3b3JrZmxvd3MiOiBbIm1jYWZlZV90aWVfaGFzaF9zZWFyY2hfd29ya2Zsb3ciXSwgIm9iamVj
dF90eXBlIjogImFydGlmYWN0IiwgInRpbWVvdXRfc2Vjb25kcyI6IDg2NDAwLCAidXVpZCI6ICI1
ZTM1MDU3Zi05MjFiLTQzY2MtYjI4Zi02ZDRlNzkwODYzMGMiLCAiYXV0b21hdGlvbnMiOiBbXSwg
ImV4cG9ydF9rZXkiOiAiKEV4YW1wbGUpIE1jQWZlZSBhcnRpZmFjdCBoYXNoIHNlYXJjaCIsICJj
b25kaXRpb25zIjogW3sidHlwZSI6IG51bGwsICJldmFsdWF0aW9uX2lkIjogbnVsbCwgImZpZWxk
X25hbWUiOiAiYXJ0aWZhY3QudHlwZSIsICJtZXRob2QiOiAiaW4iLCAidmFsdWUiOiBbIk1hbHdh
cmUgTUQ1IEhhc2giLCAiTWFsd2FyZSBTSEEtMSBIYXNoIiwgIk1hbHdhcmUgU0hBLTI1NiBIYXNo
Il19XSwgImlkIjogMTQsICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFtdfV0sICJsYXlvdXRzIjog
W10sICJleHBvcnRfZm9ybWF0X3ZlcnNpb24iOiAyLCAiaWQiOiA2LCAiaW5kdXN0cmllcyI6IG51
bGwsICJwaGFzZXMiOiBbXSwgImFjdGlvbl9vcmRlciI6IFtdLCAiZ2VvcyI6IG51bGwsICJzZXJ2
ZXJfdmVyc2lvbiI6IHsibWFqb3IiOiAzMCwgInZlcnNpb24iOiAiMzAuMC4zNDEwIiwgImJ1aWxk
X251bWJlciI6IDM0MTAsICJtaW5vciI6IDB9LCAidGltZWZyYW1lcyI6IG51bGwsICJ3b3Jrc3Bh
Y2VzIjogW10sICJhdXRvbWF0aWNfdGFza3MiOiBbXSwgImZ1bmN0aW9ucyI6IFt7ImRpc3BsYXlf
bmFtZSI6ICJNY0FmZWUgVElFIHNlYXJjaCBoYXNoIiwgInV1aWQiOiAiNDRhOWNmNWItMTZiNy00
Y2VhLWFkYzQtMzk1NmIwNzlhMWFiIiwgImNyZWF0b3IiOiB7ImRpc3BsYXlfbmFtZSI6ICJSZXNp
bGllbnQgU3lzYWRtaW4iLCAidHlwZSI6ICJ1c2VyIiwgImlkIjogMiwgIm5hbWUiOiAiYndhbHNo
QHJlc2lsaWVudHN5c3RlbXMuY29tIn0sICJ2aWV3X2l0ZW1zIjogW3sic2hvd19pZiI6IG51bGws
ICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAi
ZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImNvbnRlbnQiOiAiODhjMzgyNzgtNzA3OC00NTViLTkw
MjktMGVjNDdkMjFhM2Q4IiwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJzaG93X2lmIjogbnVsbCwg
ImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJl
bGVtZW50IjogImZpZWxkX3V1aWQiLCAiY29udGVudCI6ICIxZmJkOTE1Ni1iMmM0LTQ5YzItODJl
OC0wNDE4MzJlOTkwYjYiLCAic3RlcF9sYWJlbCI6IG51bGx9XSwgImV4cG9ydF9rZXkiOiAibWNh
ZmVlX3RpZV9zZWFyY2hfaGFzaCIsICJsYXN0X21vZGlmaWVkX2J5IjogeyJkaXNwbGF5X25hbWUi
OiAiUmVzaWxpZW50IFN5c2FkbWluIiwgInR5cGUiOiAidXNlciIsICJpZCI6IDIsICJuYW1lIjog
ImJ3YWxzaEByZXNpbGllbnRzeXN0ZW1zLmNvbSJ9LCAibmFtZSI6ICJtY2FmZWVfdGllX3NlYXJj
aF9oYXNoIiwgInZlcnNpb24iOiA0LCAid29ya2Zsb3dzIjogW3sicHJvZ3JhbW1hdGljX25hbWUi
OiAibWNhZmVlX3RpZV9oYXNoX3NlYXJjaF93b3JrZmxvdyIsICJvYmplY3RfdHlwZSI6ICJhcnRp
ZmFjdCIsICJ1dWlkIjogbnVsbCwgImFjdGlvbnMiOiBbXSwgIm5hbWUiOiAiKEV4YW1wbGUpIE1j
QWZlZSBUSUUgaGFzaCBzZWFyY2ggd29ya2Zsb3ciLCAid29ya2Zsb3dfaWQiOiAzLCAiZGVzY3Jp
cHRpb24iOiBudWxsfV0sICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNTIyMDc2NjQzNzE3LCAiZGVz
dGluYXRpb25faGFuZGxlIjogIm1jYWZlZV90aWVfbWQiLCAiaWQiOiAzLCAiZGVzY3JpcHRpb24i
OiB7ImNvbnRlbnQiOiAiQSBmdW5jdGlvbiB3aGljaCB0YWtlcyB0d28gaW5wdXRzOlxuXG5tY2Fm
ZWVfdGllX2hhc2hfdHlwZTogVGhlIHR5cGUgb2YgZmlsZSBoYXNoIChtZDUsIHNoYTEsIHNoYTI1
NikuXG5tY2FmZWVfdGllX2hhc2g6IFRoZSB2YWx1ZSBvZiB0aGUgaGFzaC5cblxuVGhlIGZ1bmN0
aW9uIHJldHVybnMgYmFjayBhIGRpY3Qgb2YgYWxsIHRoZSBhdmFpbGFibGUgaW5mb3JtYXRpb24g
ZnJvbSB0aGUgZGlmZmVyZW50IGZpbGUgcHJvdmlkZXJzIChFbnRlcnByaXNlLCBHVEksIEFURCwg
TVdHKSBhbG9uZyB3aXRoIHRoZSBsaXN0IG9mIHN5c3RlbXMgcmVsYXRlZCB0byBpdC4iLCAiZm9y
bWF0IjogInRleHQifX1dLCAibm90aWZpY2F0aW9ucyI6IG51bGwsICJyZWd1bGF0b3JzIjogbnVs
bCwgImluY2lkZW50X3R5cGVzIjogW3siY3JlYXRlX2RhdGUiOiAxNTIzNTU5Mzk4NzUxLCAiZGVz
Y3JpcHRpb24iOiAiQ3VzdG9taXphdGlvbiBQYWNrYWdlcyAoaW50ZXJuYWwpIiwgImV4cG9ydF9r
ZXkiOiAiQ3VzdG9taXphdGlvbiBQYWNrYWdlcyAoaW50ZXJuYWwpIiwgImlkIjogMCwgIm5hbWUi
OiAiQ3VzdG9taXphdGlvbiBQYWNrYWdlcyAoaW50ZXJuYWwpIiwgInVwZGF0ZV9kYXRlIjogMTUy
MzU1OTM5ODc1MSwgInV1aWQiOiAiYmZlZWMyZDQtMzc3MC0xMWU4LWFkMzktNGEwMDA0MDQ0YWEw
IiwgImVuYWJsZWQiOiBmYWxzZSwgInN5c3RlbSI6IGZhbHNlLCAicGFyZW50X2lkIjogbnVsbCwg
ImhpZGRlbiI6IGZhbHNlfV0sICJzY3JpcHRzIjogW10sICJ0eXBlcyI6IFt7ImRpc3BsYXlfbmFt
ZSI6ICJUSUUgUmVzdWx0cyIsICJ1dWlkIjogIjA2ODJiNjYzLWQ4MjEtNDMwYy1iZmQwLTNjNmQ0
ZTRjMzVlYyIsICJ0eXBlX2lkIjogOCwgImZpZWxkcyI6IHsiZmlsZV9wcm92aWRlciI6IHsib3Bl
cmF0aW9ucyI6IFtdLCAidHlwZV9pZCI6IDEwMDMsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInRl
eHQiOiAiRmlsZSBQcm92aWRlciIsICJibGFua19vcHRpb24iOiB0cnVlLCAicHJlZml4IjogbnVs
bCwgImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiAxNzksICJyZWFkX29ubHkiOiBmYWxzZSwgInV1
aWQiOiAiYTUxZjZiZDktYWIyMS00ZmY1LTliMTMtZDU1ZjQ4NWRhMDJjIiwgImNob3NlbiI6IHRy
dWUsICJpbnB1dF90eXBlIjogInRleHQiLCAidG9vbHRpcCI6ICIiLCAid2lkdGgiOiA4OCwgImlu
dGVybmFsIjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAiZXhw
b3J0X2tleSI6ICJ0aWVfcmVzdWx0cy9maWxlX3Byb3ZpZGVyIiwgImhpZGVfbm90aWZpY2F0aW9u
IjogZmFsc2UsICJwbGFjZWhvbGRlciI6ICIiLCAibmFtZSI6ICJmaWxlX3Byb3ZpZGVyIiwgImRl
ZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAidmFsdWVzIjogW10sICJvcmRlciI6IDJ9
LCAiaGFzaCI6IHsib3BlcmF0aW9ucyI6IFtdLCAidHlwZV9pZCI6IDEwMDMsICJvcGVyYXRpb25f
cGVybXMiOiB7fSwgInRleHQiOiAiSGFzaCIsICJibGFua19vcHRpb24iOiBmYWxzZSwgInByZWZp
eCI6IG51bGwsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImlkIjogMjgwLCAicmVhZF9vbmx5IjogZmFs
c2UsICJ1dWlkIjogIjczOGMwYmZlLTA2ZDctNDc2Ni1hNWMzLTcyYjlmN2FiYmNiMCIsICJjaG9z
ZW4iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAidGV4dCIsICJ0b29sdGlwIjogIiIsICJ3aWR0aCI6
IDI1NCwgImludGVybmFsIjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6
IFtdLCAiZXhwb3J0X2tleSI6ICJ0aWVfcmVzdWx0cy9oYXNoIiwgImhpZGVfbm90aWZpY2F0aW9u
IjogZmFsc2UsICJwbGFjZWhvbGRlciI6ICIiLCAibmFtZSI6ICJoYXNoIiwgImRlZmF1bHRfY2hv
c2VuX2J5X3NlcnZlciI6IGZhbHNlLCAidmFsdWVzIjogW10sICJvcmRlciI6IDF9LCAiaGFzaF90
eXBlIjogeyJvcGVyYXRpb25zIjogW10sICJ0eXBlX2lkIjogMTAwMywgIm9wZXJhdGlvbl9wZXJt
cyI6IHt9LCAidGV4dCI6ICJIYXNoIFR5cGUiLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJwcmVm
aXgiOiBudWxsLCAiY2hhbmdlYWJsZSI6IHRydWUsICJpZCI6IDI3OSwgInJlYWRfb25seSI6IGZh
bHNlLCAidXVpZCI6ICI1M2E5ODliMi1kNjIyLTQxYzYtOTg0Mi0xODUzYzAzMWRlYTEiLCAiY2hv
c2VuIjogZmFsc2UsICJpbnB1dF90eXBlIjogInRleHQiLCAidG9vbHRpcCI6ICIiLCAid2lkdGgi
OiAxNTksICJpbnRlcm5hbCI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0ZW1wbGF0ZXMi
OiBbXSwgImV4cG9ydF9rZXkiOiAidGllX3Jlc3VsdHMvaGFzaF90eXBlIiwgImhpZGVfbm90aWZp
Y2F0aW9uIjogZmFsc2UsICJwbGFjZWhvbGRlciI6ICIiLCAibmFtZSI6ICJoYXNoX3R5cGUiLCAi
ZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJ2YWx1ZXMiOiBbXSwgIm9yZGVyIjog
MH0sICJ0cnVzdF9sZXZlbCI6IHsib3BlcmF0aW9ucyI6IFtdLCAidHlwZV9pZCI6IDEwMDMsICJv
cGVyYXRpb25fcGVybXMiOiB7fSwgInRleHQiOiAiVHJ1c3QgTGV2ZWwiLCAiYmxhbmtfb3B0aW9u
IjogdHJ1ZSwgInByZWZpeCI6IG51bGwsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImlkIjogMTgwLCAi
cmVhZF9vbmx5IjogZmFsc2UsICJ1dWlkIjogIjljYzM0YTliLTBmZjEtNGNkMy05MGQxLTU4OGQ0
MThlOGU2NiIsICJjaG9zZW4iOiB0cnVlLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgInRvb2x0aXAi
OiAiIiwgIndpZHRoIjogOTAsICJpbnRlcm5hbCI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2Us
ICJ0ZW1wbGF0ZXMiOiBbXSwgImV4cG9ydF9rZXkiOiAidGllX3Jlc3VsdHMvdHJ1c3RfbGV2ZWwi
LCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgInBsYWNlaG9sZGVyIjogIiIsICJuYW1lIjog
InRydXN0X2xldmVsIiwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAidmFsdWVz
IjogW10sICJvcmRlciI6IDN9LCAidGllX2NyZWF0ZV9kYXRlIjogeyJvcGVyYXRpb25zIjogW10s
ICJ0eXBlX2lkIjogMTAwMywgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidGV4dCI6ICJDcmVhdGUg
RGF0ZSIsICJibGFua19vcHRpb24iOiB0cnVlLCAicHJlZml4IjogbnVsbCwgImNoYW5nZWFibGUi
OiB0cnVlLCAiaWQiOiAxODEsICJyZWFkX29ubHkiOiBmYWxzZSwgInV1aWQiOiAiYmJmNjdlY2Mt
MjQ1ZC00OTZjLWE0NDgtM2M3N2ExOGJjODhmIiwgImNob3NlbiI6IHRydWUsICJpbnB1dF90eXBl
IjogInRleHQiLCAidG9vbHRpcCI6ICIiLCAid2lkdGgiOiA4MiwgImludGVybmFsIjogZmFsc2Us
ICJyaWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAiZXhwb3J0X2tleSI6ICJ0aWVf
cmVzdWx0cy90aWVfY3JlYXRlX2RhdGUiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgInBs
YWNlaG9sZGVyIjogIiIsICJuYW1lIjogInRpZV9jcmVhdGVfZGF0ZSIsICJkZWZhdWx0X2Nob3Nl
bl9ieV9zZXJ2ZXIiOiBmYWxzZSwgInZhbHVlcyI6IFtdLCAib3JkZXIiOiA0fX0sICJwYXJlbnRf
dHlwZXMiOiBbImluY2lkZW50Il0sICJ0eXBlX25hbWUiOiAidGllX3Jlc3VsdHMiLCAiZXhwb3J0
X2tleSI6ICJ0aWVfcmVzdWx0cyIsICJmb3JfY3VzdG9tX2ZpZWxkcyI6IGZhbHNlLCAiYWN0aW9u
cyI6IFtdLCAicHJvcGVydGllcyI6IHsiZm9yX3dobyI6IFtdLCAiY2FuX2Rlc3Ryb3kiOiBmYWxz
ZSwgImNhbl9jcmVhdGUiOiBmYWxzZX0sICJmb3JfYWN0aW9ucyI6IGZhbHNlLCAiZm9yX25vdGlm
aWNhdGlvbnMiOiBmYWxzZSwgInNjcmlwdHMiOiBbXSwgImlkIjogbnVsbH1dLCAibWVzc2FnZV9k
ZXN0aW5hdGlvbnMiOiBbeyJ1dWlkIjogImJhM2I4M2EzLWUyNmUtNGZiMi04MDI3LTE4MDMwODdj
MWIxZCIsICJleHBvcnRfa2V5IjogIm1jYWZlZV90aWVfbWQiLCAibmFtZSI6ICJNY0FmZWUgVElF
IE1EIiwgImRlc3RpbmF0aW9uX3R5cGUiOiAwLCAicHJvZ3JhbW1hdGljX25hbWUiOiAibWNhZmVl
X3RpZV9tZCIsICJleHBlY3RfYWNrIjogdHJ1ZSwgInVzZXJzIjogWyJid2Fsc2hAcmVzaWxpZW50
c3lzdGVtcy5jb20iXX1dLCAiaW5jaWRlbnRfYXJ0aWZhY3RfdHlwZXMiOiBbXSwgInJvbGVzIjog
W10sICJmaWVsZHMiOiBbeyJvcGVyYXRpb25zIjogW10sICJyZWFkX29ubHkiOiB0cnVlLCAidXVp
ZCI6ICJjM2YwZTNlZC0yMWUxLTRkNTMtYWZmYi1mZTVjYTMzMDhjY2EiLCAidGVtcGxhdGVzIjog
W10sICJ0eXBlX2lkIjogMCwgImNob3NlbiI6IGZhbHNlLCAidGV4dCI6ICJTaW11bGF0aW9uIiwg
ImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJpbmNpZGVu
dC9pbmNfdHJhaW5pbmciLCAidG9vbHRpcCI6ICJXaGV0aGVyIHRoZSBpbmNpZGVudCBpcyBhIHNp
bXVsYXRpb24gb3IgYSByZWd1bGFyIGluY2lkZW50LiAgVGhpcyBmaWVsZCBpcyByZWFkLW9ubHku
IiwgInJpY2hfdGV4dCI6IGZhbHNlLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJwcmVmaXgiOiBu
dWxsLCAiaW50ZXJuYWwiOiBmYWxzZSwgInZhbHVlcyI6IFtdLCAiYmxhbmtfb3B0aW9uIjogZmFs
c2UsICJpbnB1dF90eXBlIjogImJvb2xlYW4iLCAiY2hhbmdlYWJsZSI6IHRydWUsICJoaWRlX25v
dGlmaWNhdGlvbiI6IGZhbHNlLCAiaWQiOiAzNywgIm5hbWUiOiAiaW5jX3RyYWluaW5nIn0sIHsi
b3BlcmF0aW9ucyI6IFtdLCAidHlwZV9pZCI6IDExLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJ0
ZXh0IjogIm1jYWZlZV90aWVfaGFzaF90eXBlIiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAicHJl
Zml4IjogbnVsbCwgImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiA4MCwgInJlYWRfb25seSI6IGZh
bHNlLCAidXVpZCI6ICI4OGMzODI3OC03MDc4LTQ1NWItOTAyOS0wZWM0N2QyMWEzZDgiLCAiY2hv
c2VuIjogZmFsc2UsICJpbnB1dF90eXBlIjogInRleHQiLCAidG9vbHRpcCI6ICJUaGUgdHlwZSBv
ZiBmaWxlIGhhc2ggKG1kNSwgc2hhMSwgc2hhMjU2KSIsICJpbnRlcm5hbCI6IGZhbHNlLCAicmlj
aF90ZXh0IjogZmFsc2UsICJ0ZW1wbGF0ZXMiOiBbXSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlv
bi9tY2FmZWVfdGllX2hhc2hfdHlwZSIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAicGxh
Y2Vob2xkZXIiOiAiIiwgIm5hbWUiOiAibWNhZmVlX3RpZV9oYXNoX3R5cGUiLCAiZGVmYXVsdF9j
aG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJ2YWx1ZXMiOiBbXX0sIHsib3BlcmF0aW9ucyI6IFtd
LCAidHlwZV9pZCI6IDExLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJ0ZXh0IjogIm1jYWZlZV90
aWVfaGFzaCIsICJibGFua19vcHRpb24iOiBmYWxzZSwgInByZWZpeCI6IG51bGwsICJjaGFuZ2Vh
YmxlIjogdHJ1ZSwgImlkIjogNzksICJyZWFkX29ubHkiOiBmYWxzZSwgInV1aWQiOiAiMWZiZDkx
NTYtYjJjNC00OWMyLTgyZTgtMDQxODMyZTk5MGI2IiwgImNob3NlbiI6IGZhbHNlLCAiaW5wdXRf
dHlwZSI6ICJ0ZXh0IiwgInRvb2x0aXAiOiAiVGhlIHZhbHVlIG9mIHRoZSBoYXNoIiwgImludGVy
bmFsIjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAiZXhwb3J0
X2tleSI6ICJfX2Z1bmN0aW9uL21jYWZlZV90aWVfaGFzaCIsICJoaWRlX25vdGlmaWNhdGlvbiI6
IGZhbHNlLCAicGxhY2Vob2xkZXIiOiAiIiwgIm5hbWUiOiAibWNhZmVlX3RpZV9oYXNoIiwgImRl
ZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAidmFsdWVzIjogW119XSwgIm92ZXJyaWRl
cyI6IFtdLCAiZXhwb3J0X2RhdGUiOiAxNTIzNDUxNjk1MDc2fQ==
"""
    )
