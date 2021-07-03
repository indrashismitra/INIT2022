#!/bin/bash

sleepUntil() {
    local slp tzoff now quiet=false
    [ "$1" = "-q" ] && shift && quiet=true
    local hms=(${1//:/ })
    printf -v now '%(%s)T' -1
    printf -v tzoff '%(%z)T\n' $now
    tzoff=$((0${tzoff:0:1}(3600*${tzoff:1:2}+60*${tzoff:3:2})))
    slp=$(((86400+(now-now%86400)+10#$hms*3600+10#${hms[1]}*60+${hms[2]}-tzoff-now)%86400))
    $quiet || printf 'Sleeping for %ss until %(%c)T\n' $slp $((now+slp))
    sleep $slp
}

sleepUntil "07:00"

a=1
a_offset=0

b=3
b_offset=0

c=2
c_offset=0

while [[ 1 ]]; do
    a=$(perl -e "printf(\"%.2f\n\", rand())")
    a_offset=$(perl -e "printf(\"%.2f\n\", rand()*${a})")

    b=$(perl -e "printf(\"%.2f\n\", rand()*5)")
    b_offset=$(perl -e "printf(\"%.2f\n\", rand()*${b})")

    c=$(perl -e "printf(\"%.2f\n\", rand()*5)")
    c_offset=$(perl -e "printf(\"%.2f\n\", rand()*${c})")

    echo "Mood multipliers set to [$a $a_offset] [$b $b_offset] [$c $c_offset]"

    x=1
    while [ $x -le 35 ]; do
        file=$(ls samples/ | shuf -n 1)
        echo -e "${x}\t${file}"
        duration=$(perl -e "printf(\"%.2f\n\", rand()*${a}+${a_offset})")
        volume=$(perl -e "printf(\"%.2f\n\", rand()*${b}+${b_offset})")
        speed=$(perl -e "printf(\"%.2f\n\", rand()*${c}+${c_offset})")
        play "samples/${file}" -q vol ${volume} speed ${speed} &>/dev/null &
        sleep $duration
        x=$(( $x + 1 ))
    done
    echo "Switching mood multipliers"
done
