# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_google_maps_directions"""

from __future__ import print_function
from resilient_circuits.util import *


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     google_maps_destination
    #     google_maps_origin
    #   Message Destinations:
    #     fn_google_maps_directions
    #   Functions:
    #     fn_google_maps_directions
    #   Workflows:
    #     example_google_maps_directions
    #   Rules:
    #     Get Directions


    yield ImportDefinition(u"""
eyJ0YXNrX29yZGVyIjogW10sICJ3b3JrZmxvd3MiOiBbeyJwcm9ncmFtbWF0aWNfbmFtZSI6ICJl
eGFtcGxlX2dvb2dsZV9tYXBzX2RpcmVjdGlvbnMiLCAib2JqZWN0X3R5cGUiOiAiaW5jaWRlbnQi
LCAiZXhwb3J0X2tleSI6ICJleGFtcGxlX2dvb2dsZV9tYXBzX2RpcmVjdGlvbnMiLCAidXVpZCI6
ICIxYzY4NmNlMS1kNWI4LTQ3MDEtOTJkNy1kNGE3Y2FiMDZlZDMiLCAibGFzdF9tb2RpZmllZF9i
eSI6ICJhZG1pbkByZXMuY29tIiwgIm5hbWUiOiAiRXhhbXBsZTogR29vZ2xlIE1hcHMgRGlyZWN0
aW9ucyIsICJjb250ZW50IjogeyJ4bWwiOiAiPD94bWwgdmVyc2lvbj1cIjEuMFwiIGVuY29kaW5n
PVwiVVRGLThcIj8+PGRlZmluaXRpb25zIHhtbG5zPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMv
QlBNTi8yMDEwMDUyNC9NT0RFTFwiIHhtbG5zOmJwbW5kaT1cImh0dHA6Ly93d3cub21nLm9yZy9z
cGVjL0JQTU4vMjAxMDA1MjQvRElcIiB4bWxuczpvbWdkYz1cImh0dHA6Ly93d3cub21nLm9yZy9z
cGVjL0RELzIwMTAwNTI0L0RDXCIgeG1sbnM6b21nZGk9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3Bl
Yy9ERC8yMDEwMDUyNC9ESVwiIHhtbG5zOnJlc2lsaWVudD1cImh0dHA6Ly9yZXNpbGllbnQuaWJt
LmNvbS9icG1uXCIgeG1sbnM6eHNkPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWFc
IiB4bWxuczp4c2k9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZVwi
IHRhcmdldE5hbWVzcGFjZT1cImh0dHA6Ly93d3cuY2FtdW5kYS5vcmcvdGVzdFwiPjxwcm9jZXNz
IGlkPVwiZXhhbXBsZV9nb29nbGVfbWFwc19kaXJlY3Rpb25zXCIgaXNFeGVjdXRhYmxlPVwidHJ1
ZVwiIG5hbWU9XCJFeGFtcGxlOiBHb29nbGUgTWFwcyBEaXJlY3Rpb25zXCI+PGRvY3VtZW50YXRp
b24+QW4gRXhhbXBsZSB3b3JrZmxvdyBzaG93aW5nIGhvdyB0byB1c2UgdGhlIEdvb2dsZSBNYXBz
IERpcmVjdGlvbnMgRnVuY3Rpb248L2RvY3VtZW50YXRpb24+PHN0YXJ0RXZlbnQgaWQ9XCJTdGFy
dEV2ZW50XzE1NWFzeG1cIj48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzBxcGFhMnY8L291dGdvaW5n
Pjwvc3RhcnRFdmVudD48c2VydmljZVRhc2sgaWQ9XCJTZXJ2aWNlVGFza18xMTZsZTlwXCIgbmFt
ZT1cImZuX2dvb2dsZV9tYXBzX2RpcmVjdGlvbnNcIiByZXNpbGllbnQ6dHlwZT1cImZ1bmN0aW9u
XCI+PGV4dGVuc2lvbkVsZW1lbnRzPjxyZXNpbGllbnQ6ZnVuY3Rpb24gdXVpZD1cImQ5YzhjMmEw
LWFjMzQtNGY2Zi1hMDkxLWZiZDFmZjAxOWJmZlwiPntcImlucHV0c1wiOnt9LFwicHJlX3Byb2Nl
c3Npbmdfc2NyaXB0XCI6XCIjIFNldCBPcmlnaW5cXG5pbnB1dHMuZ29vZ2xlX21hcHNfb3JpZ2lu
ID0gXFxcIklCTSwgQXJtb25rLCBOZXcgWW9ya1xcXCJcXG5cXG4jIEdldCBkZXN0aW5hdGlvbiBm
cm9tIEluY2lkZW50IERldGFpbHNcXG5kZXN0aW5hdGlvbiA9IFxcXCJ7MH0sIHsxfSwgezJ9XFxc
Ii5mb3JtYXQoaW5jaWRlbnQuYWRkciwgaW5jaWRlbnQuY2l0eSwgaW5jaWRlbnQuY291bnRyeSlc
XG5cXG4jIFNldCBEZXN0aW5hdGlvblxcbmlucHV0cy5nb29nbGVfbWFwc19kZXN0aW5hdGlvbiA9
IGRlc3RpbmF0aW9uXCIsXCJwb3N0X3Byb2Nlc3Npbmdfc2NyaXB0XCI6XCJpZiAocmVzdWx0cy5z
dWNjZXNzKTpcXG4gIFxcbiAgbm90ZVRleHQgPSBcXFwiXFxcIlxcXCImbHQ7YnImZ3Q7Jmx0O2Im
Z3Q7RXhhbXBsZTogR29vZ2xlIE1hcHMgRGlyZWN0aW9ucyBXb2tmbG93IGhhcyBjb21wbGV0ZSZs
dDsvYiZndDtcXG4gICAgICAgICAgICAgICAgJmx0O2ImZ3Q7RGlyZWN0aW9ucyBMaW5rOiZsdDsv
YiZndDsgJmx0O2EgaHJlZj0nezB9JyZndDt7MH0mbHQ7L2EmZ3Q7XFxcIlxcXCJcXFwiLmZvcm1h
dChyZXN1bHRzLmRpcmVjdGlvbnNfbGluaylcXG4gIFxcbiAgaW5jaWRlbnQuYWRkTm90ZShoZWxw
ZXIuY3JlYXRlUmljaFRleHQobm90ZVRleHQpKVwifTwvcmVzaWxpZW50OmZ1bmN0aW9uPjwvZXh0
ZW5zaW9uRWxlbWVudHM+PGluY29taW5nPlNlcXVlbmNlRmxvd18wcXBhYTJ2PC9pbmNvbWluZz48
b3V0Z29pbmc+U2VxdWVuY2VGbG93XzAxcTk5ZTQ8L291dGdvaW5nPjwvc2VydmljZVRhc2s+PGVu
ZEV2ZW50IGlkPVwiRW5kRXZlbnRfMHRxd3d5Y1wiPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMDFx
OTllNDwvaW5jb21pbmc+PC9lbmRFdmVudD48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93
XzAxcTk5ZTRcIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18xMTZsZTlwXCIgdGFyZ2V0UmVmPVwi
RW5kRXZlbnRfMHRxd3d5Y1wiLz48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzBxcGFh
MnZcIiBzb3VyY2VSZWY9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiB0YXJnZXRSZWY9XCJTZXJ2aWNl
VGFza18xMTZsZTlwXCIvPjx0ZXh0QW5ub3RhdGlvbiBpZD1cIlRleHRBbm5vdGF0aW9uXzFreHhp
eXRcIj48dGV4dD5TdGFydCB5b3VyIHdvcmtmbG93IGhlcmU8L3RleHQ+PC90ZXh0QW5ub3RhdGlv
bj48YXNzb2NpYXRpb24gaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4XCIgc291cmNlUmVmPVwiU3Rh
cnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiLz48
L3Byb2Nlc3M+PGJwbW5kaTpCUE1ORGlhZ3JhbSBpZD1cIkJQTU5EaWFncmFtXzFcIj48YnBtbmRp
OkJQTU5QbGFuZSBicG1uRWxlbWVudD1cInVuZGVmaW5lZFwiIGlkPVwiQlBNTlBsYW5lXzFcIj48
YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIGlkPVwi
U3RhcnRFdmVudF8xNTVhc3htX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRo
PVwiMzZcIiB4PVwiMTYyXCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91
bmRzIGhlaWdodD1cIjBcIiB3aWR0aD1cIjkwXCIgeD1cIjE1N1wiIHk9XCIyMjNcIi8+PC9icG1u
ZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxl
bWVudD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIiBpZD1cIlRleHRBbm5vdGF0aW9uXzFreHhp
eXRfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjMwXCIgd2lkdGg9XCIxMDBcIiB4PVwiOTlc
IiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVt
ZW50PVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OF9kaVwi
PjxvbWdkaTp3YXlwb2ludCB4PVwiMTY5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIy
MjBcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIxNTNcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIg
eT1cIjI1NFwiLz48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVu
dD1cIlNlcnZpY2VUYXNrXzExNmxlOXBcIiBpZD1cIlNlcnZpY2VUYXNrXzExNmxlOXBfZGlcIj48
b21nZGM6Qm91bmRzIGhlaWdodD1cIjgwXCIgd2lkdGg9XCIxMDBcIiB4PVwiMzA3XCIgeT1cIjE2
NlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJF
bmRFdmVudF8wdHF3d3ljXCIgaWQ9XCJFbmRFdmVudF8wdHF3d3ljX2RpXCI+PG9tZ2RjOkJvdW5k
cyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiNTI5XCIgeT1cIjE4OFwiLz48YnBtbmRp
OkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjU0
N1wiIHk9XCIyMjdcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBt
bmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzAxcTk5ZTRcIiBpZD1cIlNl
cXVlbmNlRmxvd18wMXE5OWU0X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCI0MDdcIiB4c2k6dHlw
ZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjUyOVwiIHhz
aTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdk
YzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNDY4XCIgeT1cIjE4NFwiLz48
L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1ORWRnZSBicG1u
RWxlbWVudD1cIlNlcXVlbmNlRmxvd18wcXBhYTJ2XCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMHFwYWEy
dl9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTk4XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwi
IHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIzMDdcIiB4c2k6dHlwZT1cIm9tZ2RjOlBv
aW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1c
IjEzXCIgd2lkdGg9XCIwXCIgeD1cIjI1Mi41XCIgeT1cIjE4NFwiLz48L2JwbW5kaTpCUE1OTGFi
ZWw+PC9icG1uZGk6QlBNTkVkZ2U+PC9icG1uZGk6QlBNTlBsYW5lPjwvYnBtbmRpOkJQTU5EaWFn
cmFtPjwvZGVmaW5pdGlvbnM+IiwgIndvcmtmbG93X2lkIjogImV4YW1wbGVfZ29vZ2xlX21hcHNf
ZGlyZWN0aW9ucyIsICJ2ZXJzaW9uIjogNn0sICJ3b3JrZmxvd19pZCI6IDcsICJhY3Rpb25zIjog
W10sICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNTM5ODY3NjMxNzcxLCAiY3JlYXRvcl9pZCI6ICJh
ZG1pbkByZXMuY29tIiwgImRlc2NyaXB0aW9uIjogIkFuIEV4YW1wbGUgd29ya2Zsb3cgc2hvd2lu
ZyBob3cgdG8gdXNlIHRoZSBHb29nbGUgTWFwcyBEaXJlY3Rpb25zIEZ1bmN0aW9uIn1dLCAiYWN0
aW9ucyI6IFt7ImxvZ2ljX3R5cGUiOiAiYWxsIiwgIm5hbWUiOiAiR2V0IERpcmVjdGlvbnMiLCAi
dmlld19pdGVtcyI6IFtdLCAidHlwZSI6IDEsICJ3b3JrZmxvd3MiOiBbImV4YW1wbGVfZ29vZ2xl
X21hcHNfZGlyZWN0aW9ucyJdLCAib2JqZWN0X3R5cGUiOiAiaW5jaWRlbnQiLCAidGltZW91dF9z
ZWNvbmRzIjogODY0MDAsICJ1dWlkIjogIjlhZDE0NTA1LTMyZWItNDhkZi05YTk2LTM0OTRhM2Iy
ZGJjMyIsICJhdXRvbWF0aW9ucyI6IFtdLCAiZXhwb3J0X2tleSI6ICJHZXQgRGlyZWN0aW9ucyIs
ICJjb25kaXRpb25zIjogW10sICJpZCI6IDIwLCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbXX1d
LCAibGF5b3V0cyI6IFtdLCAiZXhwb3J0X2Zvcm1hdF92ZXJzaW9uIjogMiwgImlkIjogMywgImlu
ZHVzdHJpZXMiOiBudWxsLCAicGhhc2VzIjogW10sICJhY3Rpb25fb3JkZXIiOiBbXSwgImdlb3Mi
OiBudWxsLCAic2VydmVyX3ZlcnNpb24iOiB7Im1ham9yIjogMzAsICJ2ZXJzaW9uIjogIjMwLjAu
MzQ3NiIsICJidWlsZF9udW1iZXIiOiAzNDc2LCAibWlub3IiOiAwfSwgInRpbWVmcmFtZXMiOiBu
dWxsLCAid29ya3NwYWNlcyI6IFtdLCAiYXV0b21hdGljX3Rhc2tzIjogW10sICJmdW5jdGlvbnMi
OiBbeyJkaXNwbGF5X25hbWUiOiAiZm5fZ29vZ2xlX21hcHNfZGlyZWN0aW9ucyIsICJ1dWlkIjog
ImQ5YzhjMmEwLWFjMzQtNGY2Zi1hMDkxLWZiZDFmZjAxOWJmZiIsICJjcmVhdG9yIjogeyJkaXNw
bGF5X25hbWUiOiAiQWRtaW4gVXNlciIsICJ0eXBlIjogInVzZXIiLCAiaWQiOiAzLCAibmFtZSI6
ICJhZG1pbkByZXMuY29tIn0sICJ2aWV3X2l0ZW1zIjogW3sic2hvd19pZiI6IG51bGwsICJmaWVs
ZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAiZWxlbWVu
dCI6ICJmaWVsZF91dWlkIiwgImNvbnRlbnQiOiAiMjg3MDlmODAtNDMyNS00NjY4LWFjNjQtZjlh
MmM4ZTlhMGYxIiwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJzaG93X2lmIjogbnVsbCwgImZpZWxk
X3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJlbGVtZW50
IjogImZpZWxkX3V1aWQiLCAiY29udGVudCI6ICJiOWVjYTZlYS02M2ZlLTQ5OTEtYTM5OS04Mzll
ODc4YzMyMDEiLCAic3RlcF9sYWJlbCI6IG51bGx9XSwgImV4cG9ydF9rZXkiOiAiZm5fZ29vZ2xl
X21hcHNfZGlyZWN0aW9ucyIsICJsYXN0X21vZGlmaWVkX2J5IjogeyJkaXNwbGF5X25hbWUiOiAi
QWRtaW4gVXNlciIsICJ0eXBlIjogInVzZXIiLCAiaWQiOiAzLCAibmFtZSI6ICJhZG1pbkByZXMu
Y29tIn0sICJuYW1lIjogImZuX2dvb2dsZV9tYXBzX2RpcmVjdGlvbnMiLCAidmVyc2lvbiI6IDAs
ICJ3b3JrZmxvd3MiOiBbeyJwcm9ncmFtbWF0aWNfbmFtZSI6ICJleGFtcGxlX2dvb2dsZV9tYXBz
X2RpcmVjdGlvbnMiLCAib2JqZWN0X3R5cGUiOiAiaW5jaWRlbnQiLCAidXVpZCI6IG51bGwsICJh
Y3Rpb25zIjogW10sICJuYW1lIjogIkV4YW1wbGU6IEdvb2dsZSBNYXBzIERpcmVjdGlvbnMiLCAi
d29ya2Zsb3dfaWQiOiA3LCAiZGVzY3JpcHRpb24iOiBudWxsfV0sICJsYXN0X21vZGlmaWVkX3Rp
bWUiOiAxNTM5ODYzNzY5NDE1LCAiZGVzdGluYXRpb25faGFuZGxlIjogImZuX2dvb2dsZV9tYXBz
X2RpcmVjdGlvbnMiLCAiaWQiOiA3LCAiZGVzY3JpcHRpb24iOiB7ImNvbnRlbnQiOiAiQSBGdW5j
dGlvbiB0aGF0IHRha2VzIGFuIE9yaWdpbiBhbmQgYSBEZXN0aW5hdGlvbiBhbmQgcmV0dXJucyBh
IEdvb2dsZSBNYXBzIExpbmsgd2l0aCBEaXJlY3Rpb25zIiwgImZvcm1hdCI6ICJ0ZXh0In19XSwg
Im5vdGlmaWNhdGlvbnMiOiBudWxsLCAicmVndWxhdG9ycyI6IG51bGwsICJpbmNpZGVudF90eXBl
cyI6IFt7ImNyZWF0ZV9kYXRlIjogMTUzOTg2Nzc5NDI2MSwgImRlc2NyaXB0aW9uIjogIkN1c3Rv
bWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJleHBvcnRfa2V5IjogIkN1c3RvbWl6YXRp
b24gUGFja2FnZXMgKGludGVybmFsKSIsICJpZCI6IDAsICJuYW1lIjogIkN1c3RvbWl6YXRpb24g
UGFja2FnZXMgKGludGVybmFsKSIsICJ1cGRhdGVfZGF0ZSI6IDE1Mzk4Njc3OTQyNjEsICJ1dWlk
IjogImJmZWVjMmQ0LTM3NzAtMTFlOC1hZDM5LTRhMDAwNDA0NGFhMCIsICJlbmFibGVkIjogZmFs
c2UsICJzeXN0ZW0iOiBmYWxzZSwgInBhcmVudF9pZCI6IG51bGwsICJoaWRkZW4iOiBmYWxzZX1d
LCAic2NyaXB0cyI6IFtdLCAidHlwZXMiOiBbXSwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW3si
dXVpZCI6ICIwZjEyMjRiZC1lNGI3LTQwMjQtYjFjNy1lNDYxZDJhNzRmYzMiLCAiZXhwb3J0X2tl
eSI6ICJmbl9nb29nbGVfbWFwc19kaXJlY3Rpb25zIiwgIm5hbWUiOiAiZm5fZ29vZ2xlX21hcHNf
ZGlyZWN0aW9ucyIsICJkZXN0aW5hdGlvbl90eXBlIjogMCwgInByb2dyYW1tYXRpY19uYW1lIjog
ImZuX2dvb2dsZV9tYXBzX2RpcmVjdGlvbnMiLCAiZXhwZWN0X2FjayI6IHRydWUsICJ1c2VycyI6
IFsiaW50ZWdyYXRpb25zQGV4YW1wbGUuY29tIl19XSwgImluY2lkZW50X2FydGlmYWN0X3R5cGVz
IjogW10sICJyb2xlcyI6IFtdLCAiZmllbGRzIjogW3sib3BlcmF0aW9ucyI6IFtdLCAicmVhZF9v
bmx5IjogdHJ1ZSwgInV1aWQiOiAiYzNmMGUzZWQtMjFlMS00ZDUzLWFmZmItZmU1Y2EzMzA4Y2Nh
IiwgInRlbXBsYXRlcyI6IFtdLCAidHlwZV9pZCI6IDAsICJjaG9zZW4iOiBmYWxzZSwgInRleHQi
OiAiU2ltdWxhdGlvbiIsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImV4cG9y
dF9rZXkiOiAiaW5jaWRlbnQvaW5jX3RyYWluaW5nIiwgInRvb2x0aXAiOiAiV2hldGhlciB0aGUg
aW5jaWRlbnQgaXMgYSBzaW11bGF0aW9uIG9yIGEgcmVndWxhciBpbmNpZGVudC4gIFRoaXMgZmll
bGQgaXMgcmVhZC1vbmx5LiIsICJyaWNoX3RleHQiOiBmYWxzZSwgIm9wZXJhdGlvbl9wZXJtcyI6
IHt9LCAicHJlZml4IjogbnVsbCwgImludGVybmFsIjogZmFsc2UsICJ2YWx1ZXMiOiBbXSwgImJs
YW5rX29wdGlvbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJib29sZWFuIiwgImNoYW5nZWFibGUi
OiB0cnVlLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzgsICJuYW1lIjogImlu
Y190cmFpbmluZyJ9LCB7Im9wZXJhdGlvbnMiOiBbXSwgInR5cGVfaWQiOiAxMSwgIm9wZXJhdGlv
bl9wZXJtcyI6IHt9LCAidGV4dCI6ICJnb29nbGVfbWFwc19vcmlnaW4iLCAiYmxhbmtfb3B0aW9u
IjogZmFsc2UsICJwcmVmaXgiOiBudWxsLCAiY2hhbmdlYWJsZSI6IHRydWUsICJpZCI6IDk0LCAi
cmVhZF9vbmx5IjogZmFsc2UsICJ1dWlkIjogIjI4NzA5ZjgwLTQzMjUtNDY2OC1hYzY0LWY5YTJj
OGU5YTBmMSIsICJjaG9zZW4iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAidGV4dCIsICJ0b29sdGlw
IjogIlRoZSBzdGFydGluZyBsb2NhdGlvbiIsICJpbnRlcm5hbCI6IGZhbHNlLCAicmljaF90ZXh0
IjogZmFsc2UsICJ0ZW1wbGF0ZXMiOiBbXSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9nb29n
bGVfbWFwc19vcmlnaW4iLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgInBsYWNlaG9sZGVy
IjogIklCTSwgQXJtb25rLCBOZXcgWW9yayIsICJuYW1lIjogImdvb2dsZV9tYXBzX29yaWdpbiIs
ICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgInZhbHVlcyI6IFtdfSwgeyJvcGVy
YXRpb25zIjogW10sICJ0eXBlX2lkIjogMTEsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInRleHQi
OiAiZ29vZ2xlX21hcHNfZGVzdGluYXRpb24iLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJwcmVm
aXgiOiBudWxsLCAiY2hhbmdlYWJsZSI6IHRydWUsICJpZCI6IDk1LCAicmVhZF9vbmx5IjogZmFs
c2UsICJ1dWlkIjogImI5ZWNhNmVhLTYzZmUtNDk5MS1hMzk5LTgzOWU4NzhjMzIwMSIsICJjaG9z
ZW4iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAidGV4dCIsICJ0b29sdGlwIjogIlRoZSBlbmQgbG9j
YXRpb24iLCAiaW50ZXJuYWwiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGVtcGxhdGVz
IjogW10sICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vZ29vZ2xlX21hcHNfZGVzdGluYXRpb24i
LCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgInBsYWNlaG9sZGVyIjogIklCTSwgQXJtb25r
LCBOZXcgWW9yayIsICJuYW1lIjogImdvb2dsZV9tYXBzX2Rlc3RpbmF0aW9uIiwgImRlZmF1bHRf
Y2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAidmFsdWVzIjogW119XSwgIm92ZXJyaWRlcyI6IFtd
LCAiZXhwb3J0X2RhdGUiOiAxNTM5ODY3NjgwMjk5fQ==
"""
    )