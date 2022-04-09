.macro jtype_bits(%inst)
	andi	jta, %inst, 0x3FFFFFF
.end_macro

.macro jump(%jta)
	mul	jta, jta, 4
	addu	pc, $sp, jta
	addu pc, pc, 4
.end_macro

.macro jtype(%inst)
	jtype_bits(%inst)
	
	is_j:
		bne	opcode, 0x2, is_jal
		
		jump(jta)
		
		j end_jtype
		
	is_jal:
		bne	opcode, 0x3, end_jtype
		
		addiu $t0, $0, 31
		get_reg_add($t0)
		addi	$t1, pc, 4
		sw	$t1, ($t0)
		
		jump(jta)
		
		j end_jtype
.end_macro
