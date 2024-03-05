from dataclasses import dataclass
from enum import Enum, auto
import array

# https://stackoverflow.com/questions/35988/c-like-structures-in-python
@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0


p = Point(1.5, 2.5)

#print(p)  # Point(x=1.5, y=2.5, z=0.0)





def sign_extend(value, bits):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val                         # return positive value as is





class InstructionType(Enum):
    UNKNOWN = auto()
    LUI = auto()
    AUIPC = auto()         
    JAL = auto()      
    JALR = auto()
    BEQ = auto()
    BNE = auto()
    BLT = auto()
    BGE = auto()
    BLTU = auto()
    BGEU = auto()
    LB = auto()
    LH = auto()
    LW = auto()
    LBU = auto()
    LHU = auto()
    SB = auto()
    SH = auto()
    SW = auto()
    ADDI = auto()
    SLTI = auto()
    SLTIU = auto()
    XORI = auto()
    ORI = auto()
    ANDI = auto()
    SLLI = auto()
    SRLI = auto()
    SRAI = auto()
    ADD = auto()
    SUB = auto()
    SLL = auto()
    SLT = auto()
    SLTU = auto()
    XOR = auto()
    SRL = auto()
    SRA = auto()
    OR = auto()
    AND = auto()
    FENCE = auto()
    FENCE_I = auto()
    ECALL = auto()
    EBREAK = auto()
    CSRRW = auto()
    CSRRS = auto()
    CSRRC = auto()
    CSRRWI = auto()
    CSRRSI = auto()
    CSRRCI = auto()

#instr = Instruction.CSRRW

#print(instr)


@dataclass
class Instruction:
    type: InstructionType = InstructionType.UNKNOWN
    rd: str = ''
    rs1: str = ''
    imm_11_0: str = ''
    imm_31_12: str = ''
    
    def __str__(self):
         return "type: " + str(self.type) + \
            "\n[rd] decimal: " + str(rd) + " binary: " + '{0:05b}'.format(rd) + " hex: 0x" + '{0:04X}'.format(rd) + \
            "\n[rs1] decimal: " + str(rs1) + " binary: " + '{0:05b}'.format(rs1) + " hex: 0x" + '{0:04X}'.format(rs1) + \
            "\n[imm_11_0] decimal: " + str(imm_11_0) + " binary: " + '{0:012b}'.format(imm_11_0) + " hex: 0x" + '{0:04X}'.format(imm_11_0) + \
            "\n[imm_31_12] decimal: " + str(imm_31_12) + " binary: " + '{0:020b}'.format(imm_31_12) + " hex: 0x" + '{0:04X}'.format(imm_31_12)




# LUI
# lui x0, 0
# 0x00000037
#x = int("00000037", 16)

# AUIPC
# auipc x0, 0
# 0x00000017
#x = int("00000017", 16)

# JAL
# jal x0, 0
# 0x0000006f
#x = int("0000006f", 16)

# JALR
# jalr x0, 0(x0)
# 0x00000067
#x = int("00000067", 16)

# BEQ
# beq x0, x0, 0
# 0x00000063
#x = int("00000063", 16)

# BNE
# bne x0, x0, 0
# 0x00001063
#x = int("00001063", 16)

# BLT
# blt x0, x0, 0
# 0x00004063
#x = int("00004063", 16)

# BGE
# bge x0, x0, 0
# 0x00005063
#x = int("00005063", 16)

# BLTU
# bltu x0, x0, 0
# 0x00006063
#x = int("00006063", 16)

# BGEU
# bgeu x0, x0, 0
# 0x00007063
#x = int("00007063", 16)

# LB
# lb x0, 0(x0)
# 0x00000003
#x = int("00000003", 16)

# LH
# lh x0, 0(x0)
# 0x00001003
#x = int("00001003", 16)

# LW
# lw x0, 0(x0)
# 0x00002003
#x = int("00002003", 16)

# LBU
# lbu x0, 0(x0)
# 0x00004003
#x = int("00004003", 16)

# LHU
# lhu x0, 0(x0)
# 0x00005003
#x = int("00005003", 16)

# SB
# sb x0, 0(x0)
# 0x00000023
#x = int("00000023", 16)

# SH
# sh x0, 0(x0)
# 0x00001023
#x = int("00001023", 16)

# SW
# sw x0, 0(x0)
# 0x00002023
#x = int("00002023", 16)

# ADDI
# addi x1, x0, 1000
# 0x3e800093
#x = int("3e800093", 16)

# SLTI
# slti x0, x0, 0
# 0x00002013
#x = int("00002013", 16)

# SLTIU
# sltiu x0, x0, 0
# 0x00003013
#x = int("00003013", 16)

# XORI
# xori x0, x0, 0
#x = int("00004013", 16)

# ORI
# ori x0, x0, 0
# 0x00006013
#x = int("00006013", 16)

# ANDI
# andi x0, x0, 0
# 0x00007013
#x = int("00007013", 16)

# SLLI
# slli x0, x0, 0
# 0x00001013
#x = int("00001013", 16)

# SRLI
# srli x0, x0, 0
# 0x00005013
#x = int("00005013", 16)

# SRAI
# srai x0, x0, 0
# 0x40005013
#x = int("40005013", 16)

# ADD
# add x0, x0, x0
# 0x00000033
#x = int("00000033", 16)

# SUB
# sub x0, x0, x0
# 0x40000033
#x = int("40000033", 16)

# SLL
# sll x0, x0, x0
# 0x00001033
#x = int("00001033", 16)

# SLT
# slt x0, x0, x0
# 0x00002033
#x = int("00002033", 16)

# SLTU
# sltu x0, x0, x0
# 0x00003033
#x = int("00003033", 16)

# XOR
# xor x0, x0, x0
# 0x00004033
#x = int("00004033", 16)

# SRL
# srl x0, x0, x0
# 0x00005033
#x = int("00005033", 16)

# SRA
# sra x0, x0, x0
# 0x40005033
#x = int("40005033", 16)

# OR
# or x0, x0, x0
# 0x00006033
#x = int("00006033", 16)

# AND
# and x0, x0, x0
# 0x00007033
#x = int("00007033", 16)

# FENCE - NOK
# fence iorw, iorw
# 0x0ff0000f
#x = int("0ff0000f", 16)

# FENCE.I
# fence iorw, iorw
# 0x0ff0000f
#x = int("0ff0000f", 16)

# ECALL
# ecall
# 0x00000073
#x = int("00000073", 16)

# EBREAK
# ebreak
# 0x00100073
#x = int("00100073", 16)

# CSRRW
# csrrw x0, cycle, x0
# 0xc0001073
#x = int("c0001073", 16)

# CSRRS
# csrrs x0, cycle, x0
# 0xc0002073
#x = int("c0002073", 16)

# CSRRC
# csrrc x0, cycle, x0
# 0xc0003073
#x = int("c0003073", 16)

# CSRRWI
# csrrwi x0, cycle, 0
# 0xc0005073
#x = int("c0005073", 16)

# CSRRSI
# csrrsi x0, cycle, 0
# 0xc0006073
#x = int("c0006073", 16)

# CSRRCI
# csrrci x0, cycle, 0
# 0xc0007073
#x = int("c0007073", 16)





#print(x)

#y = '0x{0:08X}'.format(x)
#print(y)

# There are 31 general-purpose
# registers x1–x31, which hold integer values. Register x0 is hardwired to the constant 0. There is
# no hardwired subroutine return address link register, but the standard software calling convention
# uses register x1 to hold the return address on a call. For RV32, the x registers are 32 bits wide,
# and for RV64, they are 64 bits wide. This document uses the term XLEN to refer to the current
# width of an x register in bits (either 32 or 64).
# There is one additional user-visible register: the program counter pc holds the address of the current
# instruction.

# x0 - hardwired to always return 0, does not change it's value when written to
# x1 - aka. link register
# x2 - aka. stack pointer register (sp)
# x3 - aka. 

# Chapter 20 - page 109 - https://riscv.org/wp-content/uploads/2017/05/riscv-spec-v2.2.pdf
# 
# Register      ABI Name        Description                                 Saver
# x0            zero            Hard-wired zero                             —
# x1            ra              Return address                              Caller
# x2            sp              Stack pointer                               Callee
# x3            gp              Global pointer                              —
# x4            tp              Thread pointer                              —
# x5            t0              Temporary/alternate link register           Caller
# x6–7          t1–2            Temporaries                                 Caller
# x8            s0/fp           Saved register/frame pointer                Callee
# x9            s1              Saved register                              Callee
# x10–11        a0–1            Function arguments/return values            Caller
# x12–17        a2–7            Function arguments                          Caller
# x18–27        s2–11           Saved registers                             Callee
# x28–31        t3–6            Temporaries                                 Caller
# f0–7          ft0–7           FP temporaries                              Caller
# f8–9          fs0–1           FP saved registers                          Callee
# f10–11        fa0–1           FP arguments/return values                  Caller
# f12–17        fa2–7           FP arguments                                Caller
# f18–27        fs2–11          FP saved registers                          Callee
# f28–31        ft8–11          FP temporaries                              Caller


# https://riscvasm.lucasteske.dev/#

# ADDI rd rs1 imm[11:0]
# addi x1, x0, 1000
# effectively the same as li ra,1000
#x = int("3e800093", 16)

# ADDI rd rs1 imm[11:0]
# addi x2, x1, 2000
#x = int("7d008113", 16)

# ADDI rd rs1 imm[11:0]
# addi x3, x2, -1000
#x = int("c1810193", 16)

# addi x4, x3, -2000
#x = int("83018213", 16)

# addi x5, x4, 1000
#x = int("3e820293", 16)

# auipc	x6, 0x10
#x = int("00010317", 16)

# addi x6, x6, -20
#x = int("fec30313", 16)

# addi x6, x6, 4
#x = int("00430313", 16)


# https://docs.python.org/3/library/array.html
hex_code = array.array('L')
hex_code.append(0x3e800093)
hex_code.append(0x7d008113)
hex_code.append(0xc1810193)
hex_code.append(0x83018213)
hex_code.append(0x3e820293)
hex_code.append(0x00010317)
hex_code.append(0xfec30313)
hex_code.append(0x00430313)




# opcode > func3 > func7
opcode_dict = {
    
    0b0110111: 'LUI',
    
    0b0010111: 'AUIPC',
    
    0b1101111: 'JAL',
    
    0b1100111: 'JALR',
    
    0b1100011: {
        0b000: 'BEQ',
        0b001: 'BNE',
        0b100: 'BLT',
        0b101: 'BGE',
        0b110: 'BLTU',
        0b111: 'BGEU'
    },
    
    0b0000011: {
        0b000: 'LB',
        0b001: 'LH',
        0b010: 'LW',
        0b100: 'LBU',
        0b101: 'LHU',
    }, 
    
    0b0100011: {
        0b000: 'SB',
        0b001: 'SH',
        0b010: 'SW',
    },
    
    0b0010011: {
        0b000 : 'ADDI',
        0b010 : 'SLTI',
        0b011 : 'SLTIU',
        0b100 : 'XORI',
        0b110 : 'ORI',
        0b111 : 'ANDI',
        0b001 : 'SLLI',
        0b101 : {
            0b0000000: 'SRLI',
            0b0100000: 'SRAI',
        }
    },
    
    0b0110011: {
        0b000 : {
            0b0000000: 'ADD',
            0b0100000: 'SUB',
        },
        0b001 : 'SLL',
        0b010 : 'SLT',
        0b011 : 'SLTU',
        0b100 : 'XOR',
        0b101 : {
            0b0000000: 'SRL',
            0b0100000: 'SRA',
        },
        0b110 : 'OR',
        0b111 : 'AND',
    },
    
    0b0001111: {
        0b000 : 'FENCE',
        0b001 : 'FENCE.I'
    },
    
    0b1110011: {
        0b000 : {
            # ECALL and EBREAK are processed later because they
            # are not identified by a funct7 value but by a imm11_0 value
        },
        0b001 : 'CSRRW',
        0b010 : 'CSRRS',
        0b011 : 'CSRRC',
        0b101 : 'CSRRWI',
        0b110 : 'CSRRSI',
        0b111 : 'CSRRCI',
    }
    
}




#x = hex_code[0]




for x in hex_code:

    funct7 = x & 0b11111110000000000000000000000000
    funct7 >>= 25
    #print("[funct7] decimal:", funct7, "binary:", '{0:07b}'.format(funct7))

    opcode = x & 0b1111111
    #print("[opcode] decimal:", opcode, "binary:", '{0:07b}'.format(opcode))

    funct3 = x & 0b111000000000000
    funct3 >>= 12
    #print("[funct3] decimal:", funct3, "binary:", '{0:03b}'.format(funct3))

    imm11_0 = x & 0b11111111111100000000000000000000
    imm11_0 >>= 20

    instruction_type_as_string = 'UNKNOWN'

    # further resolve the lowest level if necessary
    # Some instructions need func7 to be distinguished from each other, others do not!
    opcode_map_result = opcode_dict[opcode]
    if isinstance(opcode_map_result, dict):
        
        funct3_map_result = opcode_map_result[funct3]
        if isinstance(funct3_map_result, dict):
            
            if (funct7 in funct3_map_result):        
                dict_func7 = funct3_map_result[funct7]        
                if dict_func7:            
                    #print(funct3_map_result[funct7])
                    instruction_type_as_string = funct3_map_result[funct7]
            else:
                if imm11_0 == 0b000000000000:
                    #print('ECALL')
                    instruction_type_as_string = 'ECALL'
                elif imm11_0 == 0b000000000001:
                    #print('EBREAK')
                    instruction_type_as_string = 'EBREAK'
                
        else:
            #print(funct3_map_result)
            instruction_type_as_string = funct3_map_result
        
    else:
        #print(opcode_map_result)
        instruction_type_as_string = opcode_map_result

    rd = x & 0b111110000000
    rd >>= 7
    #print("[rd] decimal:", rd, "binary:", '{0:05b}'.format(rd))

    rs1 = x & 0b11111000000000000000
    rs1 >>= 15
    #print("[rs1] decimal:", rs1, "binary:", '{0:05b}'.format(rs1))

    imm_11_0 = x & 0b11111111111100000000000000000000
    imm_11_0 >>= 20
    # check if the number is a negative number and perform sign-extension 
    # so that the negative number is not interpreted as a positive number
    if imm_11_0 & 0b100000000000:
        imm_11_0 = sign_extend(imm_11_0, 12)
    #print("[imm_11_0] decimal:", imm_11_0, "binary:", '{0:012b}'.format(imm_11_0))

    imm_31_12 = x & 0b11111111111111111111000000000000
    imm_31_12 >>= 12
    # check if the number is a negative number and perform sign-extension 
    # so that the negative number is not interpreted as a positive number
    if imm_31_12 & 0b10000000000000000000:
        imm_31_12 = sign_extend(imm_31_12, 20)
    #print("[imm_31_12] decimal: ", imm_31_12, " binary: ", '{0:020b}'.format(imm_31_12), " hex: 0x", '{0:04X}'.format(imm_31_12), sep='')

    instr = Instruction()
    instr.type = InstructionType[instruction_type_as_string]
    instr.rd = rd
    instr.rs1 = rs1
    instr.imm_11_0 = imm_11_0
    instr.imm_31_12 = imm_31_12    

    print('')
    print(instr)
