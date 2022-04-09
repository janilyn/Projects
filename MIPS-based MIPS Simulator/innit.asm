.eqv	inst		$a0
.eqv count 	$a0
.eqv pc		$s0
.eqv	sp		$s1

.eqv opcode 	$s2
.eqv rs 		$s3
.eqv rt 		$s4
.eqv rd 		$s5
.eqv shamt 	$s6
.eqv func 	$s7
.eqv	imm		$s5
.eqv	jta 		$s3

.macro	_syscall(%n)
	li	$v0, %n
	syscall
.end_macro

.macro allocate ()
	addiu $sp, $sp, -0x100000
	addiu sp, $sp, 0x1fffc
	move pc, $sp
.end_macro 

.macro assemble()
	move $t0, count
	move	$t2, pc

assemble_loop:
	beqz	$t0, assemble_end
	
	# gets instruction from user 
	_syscall(5)
	move	$t1, $v0
	
	# stores instruction in memory
	addiu $t2, $t2, 4
	sw	$t1, 0($t2)
	
	# loop 
	subiu $t0, $t0, 1
	j	assemble_loop
	
assemble_end:
		
.end_macro 

