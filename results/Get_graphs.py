import matplotlib.pyplot as plt
import os
import numpy as np

j = 0



def get_energy_line1(temp):
    return -3.42515 + 0.000166414 * temp

def get_energy_line2(temp):
    return -3.30556 + 0.000174869 * temp

output_folder = "Graphs"
os.makedirs(output_folder, exist_ok=True)

#Colors
simulation_colors = [
    'red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'cyan', 'magenta',
    'darkred', 'darkblue', 'darkgreen', 'gold', 'indigo', 'violet', 'coral', 'lime', 'teal', 'navy',
    'crimson', 'royalblue', 'limegreen', 'tomato', 'mediumpurple', 'chocolate', 'hotpink', 'darkcyan', 'steelblue', 'yellowgreen',
    'sienna', 'orchid', 'peru', 'skyblue', 'salmon'
]

def make(temperatures, last, it):
    for w in range(it): #So that there are only 10 sims on one graph - easier to count
    
      for temp in temperatures:
          plt.figure(figsize=(12, 7))
          
          for k in range(1 + 10 * w, last + 10 * w):
              filepath = f"temp{temp}_{k}_3000.0_pe.profile"
              
              times = []
              potentials = []
              
              try:
                  with open(filepath, 'r') as f:
                      for line in f:
                          if line.startswith('#') or line.startswith('Time'):
                              continue
                          
                          parts = line.split()
                          if len(parts) >= 2:
                              time_val = float(parts[0])
                              if time_val >= 40000 and time_val <= 100000:
                                  times.append(time_val)
                                  potentials.append(float(parts[4]))
              except FileNotFoundError:
                  print(f"Файл не найден: {filepath}")
                  continue
              
              if times:
                  plt.plot(times, potentials, linewidth=1, alpha=0.7, 
                          color=simulation_colors[k-1], label=f'simulation {k}')
              j = k
    
    
          energy_line1 = get_energy_line1(temp)
          energy_line2 = get_energy_line2(temp)
          
          distance = abs(energy_line1 - energy_line2)
          shift = distance / 8
          shifted_line1 = energy_line1 + shift
          shifted_line2 = energy_line2 - shift
          
          
          plt.axhline(y=shifted_line1, color='darkred', linestyle='--', 
                      linewidth=2, label=f'Line 1 shifted ({temp}K): {shifted_line1:.4f}')
          plt.axhline(y=shifted_line2, color='darkblue', linestyle='--', 
                      linewidth=2, label=f'Line 2 shifted ({temp}K): {shifted_line2:.4f}')
          
          plt.xlabel('Time, fs', fontsize=12)
          plt.ylabel('Potential energy (per atom), eV', fontsize=12)
          plt.ylim(-3.35, -3.10)
          plt.xlim(40000, 100000)
          plt.legend(loc='center right', bbox_to_anchor=(1.15, 0.5), fontsize=8)
          plt.grid(True, alpha=0.3)
          plt.tight_layout()
          
          save_path = os.path.join(output_folder, f'temperature_{temp}_{w}.png')
          plt.savefig(save_path, dpi=150, bbox_inches='tight')
          plt.close()


temperatures = [i for i in range(920, 931, 2)]
make(temperatures, 11, 2)
temperatures = [905, 910, 915, 935, 940, 945]
make(temperatures, 7, 1)
print(f'\nDone')
