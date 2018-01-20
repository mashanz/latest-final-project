library(full) {
	cell(NOT) {
    	area: 6;
    	pin(A) { direction: input; }
    	pin(Y) { direction: output; function: "(A')"; }
  	}
  	cell (MUX21) {
  		area : 6; 
  		pin(A)  { direction : input; }
  		pin(B)  { direction : input; }
  		pin(S)  { direction : input; }
  		pin(Y)  { direction : output; function : "((S*B) + ((S')*A))"; }
  	}
  	cell(NAND41) {
    	area: 8;
    	pin(A) { direction: input; }
    	pin(B) { direction: input; }
      pin(C) { direction: input; }
      pin(D) { direction: input; }
    	pin(Y) { direction: output;
    	         function: "(A*B*C*D)'"; }
  	}
	cell(NOR41) {
    	area: 8;
    	pin(A) { direction: input; }
    	pin(B) { direction: input; }
      pin(C) { direction: input; }
      pin(D) { direction: input; }
    	pin(Y) { direction: output;
    	         function: "(A+B+C+D)'"; }
  	}  	
  	cell(XOR41) {
    	area: 12;
    	pin(A) { direction: input; }
    	pin(B) { direction: input; }
      pin(C) { direction: input; }
      pin(D) { direction: input; }
    	pin(Y) { direction: output; function: "A^B^C^D"; }
  	}	  
  	cell(DFF) {
    area: 18;
    ff(IQ, IQN) { clocked_on: C;
                  next_state: D; }
    pin(C) { direction: input;
                 clock: true; }
    pin(D) { direction: input; }
    pin(Q) { direction: output;
              function: "IQ"; }
  }
  cell(DFFSR) {
    area: 20;
    ff("IQ", "IQN") { clocked_on: C;
                  next_state: D;
                      preset: S;
                       clear: R; }
    pin(C) { direction: input;
                 clock: true; }
    pin(D) { direction: input; }
    pin(Q) { direction: output;
              function: "IQ"; }
    pin(S) { direction: input; }
    pin(R) { direction: input; }
    ; // empty statement
  }
  cell(BUF) {
    area: 6;
    pin(A) { direction: input; }
    pin(Y) { direction: output;
              function: "A"; }
  }
}