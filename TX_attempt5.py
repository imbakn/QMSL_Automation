import ctypes
from ctypes.wintypes import *
import os
import time
from argparse import *
os.chdir('C:\\Program Files (x86)\\Qualcomm\\QDART\\bin')
lib = ctypes.CDLL('QMSL_MSVC10R')

#delcare a char array
libVersion = ctypes.create_string_buffer(b"",25)
#pass a char array to a function by reference (via a pointer)
lib.QLIB_GetLibraryVersion(ctypes.byref(libVersion))
#dereference the pointer libVersion to read a value
# print(libVersion.value)

#QPST is the library mode = true
libMode = ctypes.c_uint8(1)
#libMode = ctypes.c_wchar_p('true')
#libMode = ctypes.create_string_buffer(b"true")
#libMode = ctypes.create_string_buffer(b"TRUE")
lib.QLIB_SetLibraryMode(libMode)
libMode.value

#APQ = 1
targetType = ctypes.c_uint8(1)
#targetType = ctypes.c_wchar_p(1)
#targetType = ctypes.create_string_buffer(b"1")
lib.QLIB_SetTargetType(targetType)

#iWait_ms = ctypes.c_ulong(25)
iComPort = ctypes.c_uint(4)
#to double check that connection with com_port_auto returns the same result (handle) as the one with a known port
com_port_auto=ctypes.c_int(0xFFFF)
handle = lib.QLIB_ConnectServer(iComPort)
gResourceContext = HANDLE(handle)
time.sleep(3)
print('wait for connection 5s')
#################################################################################################

#Set the WLAN module type if not called assumes a wrong module
eModuletype = ctypes.c_uint32(1)
lib.QLIB_FTM_WLAN_SetModuleType(gResourceContext, eModuletype)

#try creating string_buffer and pass byref
#dllID = ctypes.c_wchar_p('qc6180')
dllID = ctypes.create_string_buffer(b"qc6180")
chipID = ctypes.c_uint(255)
#try creating string_buffer and pass byref
#bin_file = ctypes.c_wchar_p('C:\\Qualcomm\\WCN\\ProdTests\\refDesigns\\BoardData\\fakeBoardData_AR6180.bin')
bin_file = ctypes.create_string_buffer(b"C:\\Qualcomm\\WCN\\ProdTests\\refDesigns\\BoardData\\fakeBoardData_AR6180.bin")
iNVMem = ctypes.c_int(5)
# the call below should return 1 if returns zero, load is not successfull
lib.QLIB_FTM_WLAN_Atheros_LoadDUT(gResourceContext, dllID, bin_file,iNVMem, chipID)


# ################################################################################################
#start tx
#phyId create
# OP2_SETCHIP = ctypes.c_uint(200)
# lib.QLIB_FTM_WLAN_TLV2_Create(gResourceContext, OP2_SETCHIP)
# lib.QLIB_FTM_WLAN_TLV2_Complete(gResourceContext)
#phyRFMode create
OP2_SETPHYRFMODE = ctypes.c_uint(169)
lib.QLIB_FTM_WLAN_TLV2_Create(gResourceContext, OP2_SETPHYRFMODE)
pKphyRFMode = ctypes.create_string_buffer(b'phyRFMode')
pDphyRFMode = ctypes.create_string_buffer(b'0')
lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKphyRFMode, pDphyRFMode)
lib.QLIB_FTM_WLAN_TLV2_Complete(gResourceContext)

OP2_SYNC = ctypes.c_uint(114)
lib.QLIB_FTM_WLAN_TLV2_Create(gResourceContext, OP2_SYNC)
pKphyId = ctypes.create_string_buffer(b'phyId')
pDphyId = ctypes.create_string_buffer(b'0')
lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKphyId, pDphyId)
lib.QLIB_FTM_WLAN_TLV2_Complete(gResourceContext)

#OP_TX
# OP_TX = ctypes.c_uint(1)
# lib.QLIB_FTM_WLAN_TLV2_Create(gResourceContext, OP_TX)
# lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKphyId, pDphyId)

#channel
pKchannel = ctypes.create_string_buffer(b'channel')
pDchannel = ctypes.create_string_buffer(b'5170')
#2412, 5170, 5500, 5900
lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKchannel, pDchannel)

#txMode
pKtxMode = ctypes.create_string_buffer(b'txMode')
pDtxMode = ctypes.create_string_buffer(b'3')
lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKtxMode, pDtxMode)

#wlanMode
pKwlanMode = ctypes.create_string_buffer(b'wlanMode')
pDwlanMode = ctypes.create_string_buffer(b'5')
lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKwlanMode, pDwlanMode)

# #rateBitIndex0
# pKrateBitIndex0 = ctypes.create_string_buffer(b'rateBitIndex0')
# pDrateBitIndex0 = ctypes.create_string_buffer(b'16')
# lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKrateBitIndex0, pDrateBitIndex0)

# #wlanMode
# pKwlanMode = ctypes.create_string_buffer(b'wlanMode')
# pDwlanMode = ctypes.create_string_buffer(b'5')
# lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKwlanMode, pDwlanMode)

#bandwidth
pKbandwidth = ctypes.create_string_buffer(b'bandwidth')
pDbandwidth = ctypes.create_string_buffer(b'0')
lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKbandwidth, pDbandwidth)

#txPower0
pKtxPower0 = ctypes.create_string_buffer(b'txPower0')
pDtxPower0 = ctypes.create_string_buffer(b'10')
lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKtxPower0, pDtxPower0)

#tpcm
pKtpcm = ctypes.create_string_buffer(b'tpcm')
pDtpcm = ctypes.create_string_buffer(b'0')
lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKtpcm, pDtpcm)

#rateBitIndex0
pKrateBitIndex0 = ctypes.create_string_buffer(b'rateBitIndex0')
pDrateBitIndex0 = ctypes.create_string_buffer(b'16')
lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKrateBitIndex0, pDrateBitIndex0)

#enANI
pKenANI = ctypes.create_string_buffer(b'enANI')
pDenANI = ctypes.create_string_buffer(b'0')
lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKenANI, pDenANI)

#scramblerOff
pKscramblerOff = ctypes.create_string_buffer(b'scramblerOff')
pDscramblerOff = ctypes.create_string_buffer(b'0')
lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKscramblerOff, pDscramblerOff)

#aifsn
pKaifsn = ctypes.create_string_buffer(b'aifsn')
pDaifsn = ctypes.create_string_buffer(b'0')
lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKaifsn, pDaifsn)

#agg
pKagg = ctypes.create_string_buffer(b'agg')
pDagg = ctypes.create_string_buffer(b'0')
lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKagg, pDagg)

#dutyCycle
pKdutyCycle = ctypes.create_string_buffer(b'dutyCycle')
pDdutyCycle = ctypes.create_string_buffer(b'50')
lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKdutyCycle, pDdutyCycle)

#pktLen0
pKpktLen0 = ctypes.create_string_buffer(b'pktLen0')
pDpktLen0 = ctypes.create_string_buffer(b'200')
lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKpktLen0, pDpktLen0)

#antenna
pKantenna = ctypes.create_string_buffer(b'antenna')
pDantenna = ctypes.create_string_buffer(b'0')
lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKantenna, pDantenna)

#txChain0
pKtxChain0 = ctypes.create_string_buffer(b'txChain0')
pDtxChain0 = ctypes.create_string_buffer(b'3')
lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKtxChain0, pDtxChain0)

#broadcast
pKbroadcast = ctypes.create_string_buffer(b'broadcast')
pDbroadcast = ctypes.create_string_buffer(b'0')
lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKbroadcast, pDbroadcast)

#shortGuard
pKshortGuard = ctypes.create_string_buffer(b'shortGuard')
pDshortGuard = ctypes.create_string_buffer(b'0')
lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKshortGuard, pDshortGuard)

#numPackets
pKnumPackets = ctypes.create_string_buffer(b'numPackets')
pDnumPackets = ctypes.create_string_buffer(b'0')
lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKnumPackets, pDnumPackets)

#txPattern
pKtxPattern = ctypes.create_string_buffer(b'txPattern')
pDtxPattern = ctypes.create_string_buffer(b'4')
lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKtxPattern, pDtxPattern)

#flags
pKflags = ctypes.create_string_buffer(b'flags')
pDflags = ctypes.create_string_buffer(b'28')
lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKflags, pDflags)


# #gainIdx
# pKgainIdx = ctypes.create_string_buffer(b'gainIdx')
# pDgainIdx = ctypes.create_string_buffer(b'5')
# lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKgainIdx, pDgainIdx)
#
# #dacGain
# pKdacGain = ctypes.create_string_buffer(b'dacGain')
# pDdacGain = ctypes.create_string_buffer(b'0')
# lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKdacGain, pDdacGain)
#
# #paConfig
# pKpaConfig = ctypes.create_string_buffer(b'paConfig')
# pDpaConfig = ctypes.create_string_buffer(b'1')
# lib.QLIB_FTM_WLAN_TLV2_AddParam(gResourceContext, pKpaConfig, pDpaConfig)

lib.QLIB_FTM_WLAN_TLV2_Complete(gResourceContext)


time.sleep(5)
print('wait to disconnect 5s')
#close all connections
lib.QLIB_DisconnectAllServers()





























