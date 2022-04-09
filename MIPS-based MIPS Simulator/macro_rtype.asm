.macro rtype_bits(%inst)
	srl	rs,	%inst,21
	srl	rt,	%inst,16
	srl	rd,	%inst,11
	srl	shamt, %inst, 6

	andi	rs, rs, 0x1f
	andi	rt, rt, 0x1f
	andi	rd, rd, 0x1f
	andi	shamt, shamt, 0x1f
	andi func, %inst, 0x3F
.end_macro 

.macro rtype(%inst)
	rtype_bits(%inst)
	
	load_reg(rs)
	load_reg(rt)
	
	get_reg_add(rd)
	
	is_add:
		bne	func, 0x20, is_sub
		add	$t0, rs, rt
		sw	$t0, (rd)
		j end_rtype
		
	is_sub:
		bne	func, 0x22, is_and
		sub	$t0, rs, rt
		sw	$t0, (rd)
		j end_rtype
		
	is_and:
		bne	func, 0x24, is_or
		and	$t0, rs, rt
		sw	$t0, (rd)
		j end_rtype
	
	is_or:
		bne	func, 0x25, is_slt
		or	$t0, rs, rt
		sw	$t0, (rd)
		j end_rtype
		
	is_slt:
		bne	func, 0x2a, is_jr
		slt	$t0, rs, rt
		sw	$t0, (rd)
		j end_rtype
		
	is_jr:
		bne	func, 0x8, is_syscall
		addiu rs, $0, 31
		load_reg(rs)
		addu	pc, $0, rs
		jr $ra
		
	is_syscall:
		bne	func, 0xC, not_rtype
		
		li	$v0, 2
		load_reg($v0)
		
		li	$a0, 4
		load_reg($a0)
		
		is_10:
			bne	$v0, 10, is_1
			_syscall(10)
		is_1:
			bne	$v0, 1, is_11
			_syscall(1)
		is_11:
			bne	$v0, 11, end_rtype
			_syscall(11)
.end_macro
