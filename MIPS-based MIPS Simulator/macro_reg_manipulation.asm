#  assigns a value to the register 
.macro	imm_store(%address, %regnum, %input)
	li	$t0, %input
	li	%address, %regnum
	get_reg_add(%address)
	sw	$t0, (%address)
.end_macro

## ----- needed ----- 
#  gets the value of the register specified
.macro	load_reg(%regnum)
	get_reg_add(%regnum)
	lw	%regnum, (%regnum)
.end_macro

#  gets the address of the register
.macro	get_reg_add(%regnum)
	mul	%regnum, %regnum, -4
	addu	%regnum, %regnum, 0x7fffeffc
.end_macro
