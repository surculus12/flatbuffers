# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

class Gadget(object):
    NONE = 0
    FallingTub = 1
    HandFan = 2

def GadgetCreator(unionType, table):
    from flatbuffers.table import Table
    if not isinstance(table, Table):
        return None
    if unionType == Gadget().FallingTub:
        import FallingTub
        return FallingTub.FallingTubT.InitFromBuf(table.Bytes, table.Pos)
    if unionType == Gadget().HandFan:
        import HandFan
        return HandFan.HandFanT.InitFromBuf(table.Bytes, table.Pos)
    return None