
#!/bin/bash
mkdir -p results

for k in {1..20}; do
    for x in {920..931..2}; do
        lmp -in Al_in.eim -var Teq ${x} -var Teq_top 3000.0 -var Seed $(( RANDOM % 13514 ))
        mv temp${x}_3000.0_pe.profile results/temp${x}_${k}_3000.0_pe.profile 2>/dev/null
    done
done

for k in {1..6}; do
    for x in 905 910 940 945; do
        lmp -in Al_in.eim -var Teq ${x} -var Teq_top 3000.0 -var Seed $(( RANDOM % 13514 ))
        mv temp${x}_3000.0_pe.profile results/temp${x}_${k}_3000.0_pe.profile 2>/dev/null
    done
done

for k in {1..20}; do
    for x in 915 935; do
        lmp -in Al_in.eim -var Teq ${x} -var Teq_top 3000.0 -var Seed $(( RANDOM % 13514 ))
        mv temp${x}_3000.0_pe.profile results/temp${x}_${k}_3000.0_pe.profile 2>/dev/null
    done
done


