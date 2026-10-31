
#!/bin/bash
mkdir -p results

for k in {1..10}; do
    for x in {920..931..2}; do
        lmp -in Al_in.eim -var Teq ${x} -var Teq_top 2948.0 -var Seed $(( RANDOM % 13514 ))
        mv temp${x}_3000.0_pe.profile results/temp${x}_${k}_3000.0_pe.profile 2>/dev/null
    done
done

cd results
sed -i '/^#/d' *.profile
echo "filename,timestep,pe" > ../AllEnergies.csv
for f in *.profile; do
    awk -v fname="$f" '{print fname "," $1 "," $2}' "$f" >> ../AllEnergies.csv
done
cd ..
