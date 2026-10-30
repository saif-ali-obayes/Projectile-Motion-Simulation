import numpy as np
import matplotlib.pyplot as plt


g = 9.81            
m = 1.0               
rho0 = 1.225          
C_d = 0.47            
radius = 0.05         
A = np.pi * radius**2 

v0 = 50.0             
v_wind = 10.0         
dt = 0.001            
angles = [15, 30, 45, 60, 75] 

plt.figure(figsize=(10, 6))


for angle in angles:
    rad = np.radians(angle)
    x, y = 0.0, 0.0
    vx = v0 * np.cos(rad)
    vy = v0 * np.sin(rad)
    
    x_list, y_list = [x], [y]
    
    while y >= 0:
        
        rho_current = rho0 * np.exp(-0.000125 * y)
        
        
        vx_rel = vx - v_wind
        vy_rel = vy
        v_rel = np.sqrt(vx_rel**2 + vy_rel**2)
        
        
        if v_rel > 0:
            F_drag = 0.5 * C_d * rho_current * A * v_rel**2
            F_drag_x = F_drag * (vx_rel / v_rel)
            F_drag_y = F_drag * (vy_rel / v_rel)
        else:
            F_drag_x, F_drag_y = 0.0, 0.0
        
        
        ax = -F_drag_x / m
        ay = -g - (F_drag_y / m)
        
        vx += ax * dt
        vy += ay * dt
        
        x += vx * dt
        y += vy * dt
        
        x_list.append(x)
        y_list.append(y)
        
    plt.plot(x_list, y_list, label=f'Angle {angle}° (Wind = +10 m/s)')


plt.title('Advanced Simulation: Projectile Motion with Variable Density & Wind Effect', fontsize=11)
plt.xlabel('Horizontal Distance (m)', fontsize=10)
plt.ylabel('Vertical Height (m)', fontsize=10)
plt.axhline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.savefig('projectile_with_wind.png', dpi=300)
plt.show()