def ground(weight):
  base = 20
  a = 1.50
  b = 3.00
  c = 4.00
  d = 4.75

  if weight <= 2:
    return (a * weight) + base
  elif weight > 2 and weight <= 6:
    return (b * weight) + base
  elif weight > 6 and weight <= 10:
    return (c * weight) + base
  else:
    return (d * weight) + base

#print(ground(weight))

premium_ground = 125.00

#print(premium_ground)

def drone(weight):
  a = 4.50
  b = 9.00
  c = 12.00
  d = 14.25

  if weight <= 2:
    return (a * weight)
  elif weight > 2 and weight <= 6:
    return (b * weight)
  elif weight > 6 and weight <= 10:
    return (c * weight)
  else:
    return (d * weight)

#print(drone(weight))

def bargain_calculator(weight):
  cheapest_option = ""
  ground2 = ground(weight)
  drone2 = drone(weight)
  premium_ground = 125.00

  if ground2 < drone2 and ground2 < premium_ground:
    cheapest_option = "Ground shipping is the cheapest option "
    return cheapest_option + "at $" + str(ground2)
  elif drone2 < ground2 and drone2 < premium_ground:
    cheapest_option = "Drone shipping is the cheapest option "
    return cheapest_option + "at $" + str(drone2)
  else:
    cheapest_option = "Premium ground shipping is the cheapest option "
    return cheapest_option + "at $" + str(premium_ground)

print(bargain_calculator(4.8))
print(bargain_calculator(41.5))
print(bargain_calculator(2.8))
