def seperate_section(filename):
    cnt=0
    with open(filename,'r') as f1, open("data.txt",'a') as f2:
        for line in f1:
            if ".bss" in line:
                 f2.close()
                 break
            cnt=cnt+1
            f2.write(line)
        with open("bss.txt",'a') as f3:
            cnt=cnt+1
            f3.write(line)
            for line in f1:
                if ".text" in line:
                    f3.close()
                    break
                cnt=cnt+1
                f3.write(line)

        with open("text.txt",'a') as f4:
            f4.write(str(cnt)+"\n")
            while line!="":
                f4.write(line)
                line=f1.readline()
            f4.close()

def create_sym_tab():
    sym_name=[]
    sym_type=[]
    sym_values=[]
    sym_def_undef=[]
    sym_size=[]
    sym_section=[]
    f2=open("data.txt",'r')
    line=f2.readline()
    while line!="":
        words=line.split()
        if len(words)>2:
            if words[0] in sym_name: 
                print ("Error:  symbol",words[0]," repeated")
                exit()
            else:
                if (words[1]== "dd" or words[1]=="db" or words[1]=="dw" or words[1]=="dq" or words[1]=="equ"):
                    sym_name.append(words[0])
                    sym_type.append(words[1])
                    sym_def_undef.append("def")
                    sym_section.append("data")
                    if words[1]=="dd":
                        valuepart=str(words[2:])
                        valuepart=valuepart[2:-2]
                        sym_values.append(valuepart)
                        comma_cnt=valuepart.count(',')
                        n=comma_cnt+1
                        size=4*n
                        sym_size.append(size)
                    elif words[1]=="db":
                        valuepart=str(words[2:])
                        valuepart=valuepart[2:-2]
                        sym_values.append(valuepart)
                        string=''.join(words[2:])
                        n=len(string)
                        size=1*n
                        sym_size.append(size)
                    elif words[1]=="dw":
                        sym_values.append(words[2:])
                        n=len(words[2:])
                        size=2*n
                        sym_size.append(size)
                    elif words[1]=="dq":
                        sym_values.append(words[2:])
                        n=len(words[2:])
                        size=8*n
                        sym_size.append(size)
                    else:
                        print (words[2],"is directives")
                else:
                    print ("invalid data type ", words[1], "in data section")
                    exit()

        line=f2.readline()
    f2.close()
    
    f3=open("bss.txt",'r')
    line=f3.readline()
    while line!="":
        words=line.split()
        if len(words)>2:
            if words[0] in sym_name: 
                print ("Error:  symbol",words[0]," repeated")
                exit()
            else:
                if words[1]== "resd" or words[1]=="resb" or words[1]=="resw" or words[1]=="resq":
                    sym_name.append(words[0])
                    sym_type.append(words[1])
                    sym_def_undef.append("undef")
                    sym_section.append("bss")
                    sym_values.append('-')
                    if words[1]=="resd":
                        n=int(words[2])
                        size=4*n
                        sym_size.append(size)
                    elif words[1]=="resb":
                        n=int(words[2])
                        size=1*n
                        sym_size.append(size)
                    elif words[1]=="resw":
                        n=int(words[2])
                        size=2*n
                        sym_size.append(size)
                    else:
                        n=int(words[2])
                        size=8*n
                        sym_size.append(size)
                else:
                    print ("invalid data type ", words[1], "in bss section")
                    exit()
        line=f3.readline()
    f3.close()
    f4=open("text.txt","r")
    line=f4.readline()
    line=f4.readline()
    while line!="":
        if "main:" in line:
            break
        line=f4.readline()
    line=f4.readline()
    while line!="":
        sep=line.split()
        if len(sep)>0:
            if sep[0][-1]==":":
                sym_name.append(sep[0][:-1])
                sym_type.append("lable")
                sym_values.append("-")
                sym_def_undef.append("undef")
                sym_section.append("text")
                sym_size.append("-")
        line=f4.readline()


    #with open("intermediate_code.txt","w") as f5:
    f5=open("intermediate_code.txt","w")
    f5.write("sym_no\t sym_name\t  sym_type\tsym_def_undef\tsection\t   sym_size\tsym_values\n")
    for i in range(len(sym_name)):
        f5.write(str(i))
        f5.write("\t")
        f5.write(sym_name[i])
        f5.write("\t\t")
        f5.write(sym_type[i])
        f5.write("\t\t")
        f5.write(sym_def_undef[i])
        f5.write("\t\t")
        f5.write(sym_section[i])
        f5.write("\t\t")
        f5.write(str(sym_size[i]))
        f5.write("\t\t")
        f5.write(str(sym_values[i]))
        f5.write("\n")



#def generate_intermediate_code():
    f=open("opcode.txt","r")
    opcode=[]
    l=f.readline().strip('\n')
    while l!="":
        opcode.append(l.split())
        l=f.readline().strip('\n')
    f.close()
    #print (opcode)
    #print (opcode[3][2])
    
    #opcode table
    opcode_table=["mov reg reg","mov reg mem","mov mem reg","mov mem imm","mov reg imm","add reg reg","add reg mem","add mem reg","add mem imm","add reg imm"]
    #opcode_value=[89,B8,A3]


    #for intermediate code
    line_no=[]
    address=[]
    original_line=[]
    lst_line=[]
    instruction=["mov","add","sub"]
    registers=["eax","al","ax","ebx","bl","bx","ecx","cl","ex","edx","dl","dx","esi","edi","ebp","esp"]
    adr=0
    #for literal table
    literal_line=[]
    literal_type=[]
    literal_name=[]
    literal_hex=[]
    with open("text.txt","r") as f4:
        line=f4.readline()
        cnt=int(line)
        cnt=cnt+1
        line=f4.readline()
        while line!="":
            if "main:" in line:
                cnt=cnt+1
                break
            cnt=cnt+1
            line=f4.readline()
        line=f4.readline()
        while line!="":
            sep=line.split()
            if len(sep)>0:
                if sep[0] in instruction:
                    remain="".join(sep[1:])
                    oprands=remain.split(',')
                    if len(oprands)==2:
                        if oprands[0] in registers:
                            oprands[0]="reg"
                            if oprands[1] in registers:
                                string="reg reg"
                                opcode_line=sep[0]+" "+string
                                opcode_no=opcode_table.index(opcode_line)
                                sep[0]="op#"+str(opcode_no)
                                newline=sep[0]+" "+string
                                line_no.append(cnt)
                                add='{0:04}'.format(adr)
                                address.append(add)
                                adr=adr+2
                                line=line[:-1]
                                original_line.append(line)
                                lst_line.append(newline)
                            elif oprands[1] in sym_name:
                                string="reg mem"
                                opcode_line=sep[0]+" "+string
                                opcode_no=opcode_table.index(opcode_line)
                                sep[0]="op#"+str(opcode_no)
                                i=sym_name.index(oprands[1])
                                oprands[1]="sym#"+str(i)
                                newline=sep[0]+" "+" ".join(oprands)
                                line_no.append(cnt)
                                add='{0:04}'.format(adr)
                                address.append(add)
                                adr=adr+6
                                line=line[:-1]
                                original_line.append(line)
                                lst_line.append(newline)
                            else:
                                literal_name.append(oprands[1])
                                literal_line.append(cnt)
                                val=oprands[1].strip("'")
                                if ord(str(val[0]))>=48 and ord(str(val[0]))<=57:
                                    literal_type.append("integer")
                                    literal_hex.append(hex(ord(str(val[0]))))
                                elif (ord(val[0])>=65 and ord(val[0])<=90) or (ord(val[0])>=97 and ord(val[0])<=122):
                                        literal_type.append("char")
                                        literal_hex.append(hex(ord(val[0])))
                                        lenght=len(val)
                                        adr=adr+lenght
                                else:
                                    print ("invalid oprand 2",oprands[1])
                                    exit()
                                string="reg imm"
                                opcode_line=sep[0]+" "+string
                                opcode_no=opcode_table.index(opcode_line)
                                sep[0]="op#"+str(opcode_no)
                                i=literal_name.index(oprands[1])
                                oprands[1]="literal#"+str(i)
                                newline=sep[0]+" "+" ".join(oprands)
                                line_no.append(cnt)
                                add='{0:04}'.format(adr)
                                address.append(add)
                                adr=adr+4
                                line=line[:-1]
                                original_line.append(line)
                                lst_line.append(newline)

                        elif oprands[0] in sym_name:
                            i=sym_name.index(oprands[0])
                            oprands[0]="sym#"+str(i)
                            if oprands[1] in registers:
                                oprands[1]="reg"
                                string="mem reg"
                                opcode_line=sep[0]+" "+string
                                opcode_no=opcode_table.index(opcode_line)
                                sep[0]="op#"+str(opcode_no)
                                newline=sep[0]+" "+" ".join(oprands)
                                line_no.append(cnt)
                                add='{0:04}'.format(adr)
                                address.append(add)
                                adr=adr+6
                                line=line[:-1]
                                original_line.append(line)
                                lst_line.append(newline)
                                ####handle the condition mov sym literal
                            else:
                                print ("invalid combination of opcode oprands or symbol",oprands[1]," not in sym_tab")
                                exit()
                        else:
                            print ("invalid line",line)
                            exit()


                    else:
                        print ("invalid oprands at line" ,line)
                        exit()
                elif sep[0][-1]==":":
                    if sep[0][:-1] in sym_name:
                        i=sym_name.index(sep[0][:-1])
                        sep[0]="sym#"+str(i)
                        if sep[1] in instruction:
                            remain="".join(sep[2:])
                            oprands=remain.split(',')
                            if len(oprands)==2:
                                if oprands[0] in registers:
                                    oprands[0]="reg"
                                    if oprands[1] in registers:
                                        string="reg reg"
                                        opcode_line=sep[1]+" "+string
                                        opcode_no=opcode_table.index(opcode_line)
                                        sep[1]="op#"+str(opcode_no)
                                        newline=" ".join(sep[0:2])+" "+string
                                        line_no.append(cnt)
                                        add='{0:04}'.format(adr)
                                        address.append(add)
                                        adr=adr+2
                                        line=line[:-1]
                                        original_line.append(line)
                                        lst_line.append(newline)
                                    elif oprands[1] in sym_name:
                                        string="reg mem"
                                        opcode_line=sep[1]+" "+string
                                        opcode_no=opcode_table.index(opcode_line)
                                        sep[1]="op#"+str(opcode_no)
                                        i=sym_name.index(oprands[1])
                                        oprands[1]="sym#"+str(i)
                                        newline=" ".join(sep[0:2])+" "+" ".join(oprands)
                                        line_no.append(cnt)
                                        add='{0:04}'.format(adr)
                                        address.append(add)
                                        adr=adr+6
                                        line=line[:-1]
                                        original_line.append(line)
                                        lst_line.append(newline)
                                    else:
                                        literal_name.append(oprands[1])
                                        literal_line.append(cnt)
                                        val=oprands[1].strip("'")
                                        if ord(str(val[0]))>=48 and ord(str(val[0]))<=57:
                                            literal_type.append("integer")
                                            literal_hex.append(hex(ord(str(val[0]))))
                                        elif (ord(val[0])>=65 and ord(val[0])<=90) or (ord(val[0])>=97 and ord(val[0])<=122):
                                                literal_type.append("char")
                                                literal_hex.append(hex(ord(val[0])))
                                                lenght=len(val)
                                                adr=adr+lenght
                                        else:
                                            print ("invalid oprand 2",oprands[1])
                                            exit()
                                        string="reg imm"
                                        opcode_line=sep[1]+" "+string
                                        opcode_no=opcode_table.index(opcode_line)
                                        sep[1]="op#"+str(opcode_no)
                                        i=literal_name.index(oprands[1])
                                        oprands[1]="literal#"+str(i)
                                        newline=" ".join(sep[0:2])+" "+" ".join(oprands)
                                        line_no.append(cnt)
                                        add='{0:04}'.format(adr)
                                        address.append(add)
                                        adr=adr+4
                                        line=line[:-1]
                                        original_line.append(line)
                                        lst_line.append(newline)
        
                                elif oprands[0] in sym_name:
                                    i=sym_name.index(oprands[0])
                                    oprands[0]="sym#"+str(i)
                                    if oprands[1] in registers:
                                        line_no.append(cnt)
                                        add='{0:04}'.format(adr)
                                        address.append(add)
                                        adr=adr+6
                                        line=line[:-1]
                                        original_line.append(line)
                                        newline=sep[0]+" "+sep[1]+" "+" ".join(oprands)
                                        lst_line.append(newline)
                                    else:
                                        print ("invalid combination of opcode oprands or symbol",oprands[1]," not in sym_tab")
                                        exit()
                                else:
                                    print ("invalid line",line)
                                    exit()
        
        
                            else:
                                print ("invalid oprands at line" ,line)
                            
                else:
                    print (sep[0],"is not a instruction")
                    #exit()
            cnt=cnt+1
            line=f4.readline()
        f5.write("\n\t literal table\n\n")
        f5.write("literalno\tline no\t    literal name\tliteral hex\tliteral type\n")
        for i in range(len(literal_name)):
            f5.write(str(i))
            f5.write("\t\t")
            f5.write(str(literal_line[i]))
            f5.write("\t\t")
            f5.write(literal_name[i])
            f5.write("\t\t")
            f5.write(str(literal_hex[i]))
            f5.write("\t\t")
            f5.write(literal_type[i])
            f5.write("\n")
        
        f5.write("\n\tintermediate code\n\n")
        f5.write("no\tline number\taddress\t\toriginal line\t\tinst line\n")
        for i in range(len(line_no)):
            f5.write(str(i))
            f5.write("\t")
            f5.write(str(line_no[i]))
            f5.write("\t\t")
            f5.write(str(address[i]))
            f5.write("\t")
            f5.write(original_line[i])
            f5.write("\t")
            f5.write(lst_line[i])
            f5.write("\n")

    f4.close()
    f5.close()
    os.remove("bss.txt")
    os.remove("data.txt")
    os.remove("text.txt")
import os
from sys import argv
scriptname,filename=argv
fname=filename.split( '.' )
if (fname[1]=='asm'):
    seperate_section(filename)
    create_sym_tab()
else:
    print ("invalid file")
    exit()

