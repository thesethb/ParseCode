initialize
make only speaker and only house
create array of every icpsr

for(every row)
    n=0
    m=0
    String partycode
    icpsr=row.icpsr
    if(icpsr.party=100)
        set party leader to pelosi
    else
        set party leader to mccarthy
    for(every line)
        if(icpsr of line=member icpsr)
            if(partycode.row(line.rollnumber).cast_code==line.cast_code)
                n++
                m++
            else if(line.cast_code=!9)
                n++
    int average=n/m
    Print(icpsr, average)