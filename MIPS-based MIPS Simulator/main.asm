# MIPS-based MIPS simulator

.include	"innit.asm"

.include	"macro_reg_manipulation.asm"
.include	"macro_rtype.asm"
.include	"macro_itype.asm"
.include	"macro_jtype.asm"

.text
main:
	# build memory  
	allocate()				

	imm_store(rs,29,0x1FFFC)
	
	# n number of instructions
	_syscall(5)
	move	count, $v0
	
	assemble()
	
	addiu pc, pc, 4
	
	jal	execute
	
	_syscall(10)

#######

execute:
	lw	inst, (pc)
	
	jal	get_inst_bits
	
	imm_store(rs,0,0)
	
	j	execute
	
end_execute:
	jr $ra

#######

get_inst_bits:
	srl	opcode, inst, 26
	bnez	opcode, not_rtype

is_rtype:
	rtype(inst)
	
	end_rtype:
		j	get_ib_end
	
not_rtype:
	beq	opcode, 2, is_jtype
	beq	opcode, 3, is_jtype
	
is_itype:
	itype(inst)
	
	end_itype:
		j	get_ib_end
		
	end_branch:
		jr $ra
	
is_jtype:
	jtype(inst)
	
	end_jtype:
		jr $ra
	
get_ib_end:
	addiu pc,pc,4
	jr $ra
	
