import math


def calculate_projectile(v0, angle_deg):
    
    g = 9.81
    angle_rad = math.radians(angle_deg)
    
    v0x = v0 * math.cos(angle_rad)
    v0y = v0 * math.sin(angle_rad)
    
    h_max = (v0y ** 2) / (2 * g)
    t_max = v0y / g
    t_total = 2 * v0y / g
    range_dist = (v0 ** 2 * math.sin(2 * angle_rad)) / g
    
    heights = {}
    t = 0
    while t <= t_total:
        height = v0y * t - 0.5 * g * t ** 2
        heights[t] = max(0, height)
        t += 1
    
    return {
        'v0': v0,
        'angle': angle_deg,
        'v0x': v0x,
        'v0y': v0y,
        'h_max': h_max,
        't_max': t_max,
        't_total': t_total,
        'range': range_dist,
        'heights': heights
    }


print("="*60)
print("TASK 4: Projectile Motion")
print("="*60)

test_cases = [
    (20, 45),
    (30, 30),
    (50, 45),
    (15, 60),
]

print("\nTest Cases:")
print("-"*60)

for v0, angle in test_cases:
    result = calculate_projectile(v0, angle)
    
    print(f"\nVelocity: {v0} m/s, Angle: {angle}°")
    print(f"  Max height: {result['h_max']:.2f} m")
    print(f"  Flight time: {result['t_total']:.2f} s")
    print(f"  Range: {result['range']:.2f} m")
    print(f"  Height at each second:")
    for time_key in sorted(result['heights'].keys()):
        h = result['heights'][time_key]
        print(f"    t={time_key:.0f}s: h={h:.2f}m")

# Interactive mode
print("\n" + "="*60)
print("Interactive Mode")
print("-"*60)

while True:
    try:
        v0_str = input("\nEnter velocity (m/s) or 'quit': ")
        if v0_str.lower() == 'quit':
            break
        
        angle_str = input("Enter angle (degrees 0-90): ")
        
        v0 = float(v0_str)
        angle = float(angle_str)
        
        if v0 <= 0 or not (0 <= angle <= 90):
            print("Invalid input")
            continue
        
        result = calculate_projectile(v0, angle)
        
        print(f"\nResults for {v0} m/s at {angle}°:")
        print(f"  Max height: {result['h_max']:.2f} m")
        print(f"  Range: {result['range']:.2f} m")
        print(f"  Flight time: {result['t_total']:.2f} s")
        
    except ValueError:
        print("Error: Invalid input")
