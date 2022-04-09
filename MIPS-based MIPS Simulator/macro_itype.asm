.macro itype_bits(%inst)	
	srl	rs,	%inst,21
	srl	rt,	%inst,16
	
	andi	rs, rs, 0x1f
	andi	rt, rt, 0x1f
	andi imm, inst, 0xffff
	
	blt	imm, 0x8000, iend
	ori	imm, imm, 0xFFFF0000
	j	iend
	
	iend:
.end_macro 

.macro itype(%inst)
	itype_bits(%inst)
	
	is_addiu:
		bne	opcode, 0x9, is_beq
		
		load_reg(rs)
		get_reg_add(rt)
		#imm
		
		addu $t0, rs, imm
		sw	$t0, (rt)
		j end_itype
		
	is_beq:
		bne	opcode, 0x4, is_bne
		
		load_reg(rs)
		load_reg(rt)
		
		bne rs, rt, end_itype
		bta(imm)
		
		j end_branch
	
	is_bne:
		bne	opcode, 0x5, is_lw
		
		load_reg(rs)
		load_reg(rt)
		
		beq rs, rt, end_itype
		bta(imm)
		
		j end_branch
	
	is_lw:		
		bne	opcode, 0x23, is_sw
		load_word(rs,rt,imm)
		j end_itype
	
	is_sw:
		bne	opcode, 0x2B, end_itype
		store_word(rs,rt,imm)
		j end_itype
.end_macro 

.macro	store_word(%rs, %rt, %imm)
	load_reg(%rs)
	addu	%rs, %rs, %imm
	addu	%rs, %rs, $sp
	addiu %rs,%rs, 4
	
	load_reg(%rt)
	sw	%rt, (%rs)
.end_macro

.macro	load_word(%rs, %rt, %imm)
	load_reg(%rs)
	addu	%rs, %rs, %imm
	addu	%rs, %rs, $sp
	addiu %rs,%rs, 4
	lw	$t0, (%rs)
	
	get_reg_add(%rt)
	sw	$t0, (%rt)
.end_macro

.macro bta(%imm)
	addiu	pc, pc, 4
	mul		%imm, %imm, 4
	addu		pc, pc, %imm
.end_macro
