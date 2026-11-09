---
kicker: SHOP SERVICE MANUAL · CLIMATE CONTROL (FORD GROUP 412)
title: A/C Compressor Removal and Installation
subtitle: 2019 Lincoln Navigator and Navigator L · 3.5L Twin-Turbo EcoBoost V6
header: 2019 Lincoln Navigator · A/C Compressor R&I
revision: Rev A · 2026-11-09
footer: For trained technicians. Confirm every VERIFY item in Ford service information for the VIN before you start.
author: Robb's Body Shop
meta.vehicle: 2019 Lincoln Navigator (SWB) and Navigator L (LWB), all trims
meta.engine: 3.5L twin-turbo EcoBoost V6 (only engine for 2019)
meta.system: R-1234yf A/C, front and rear (auxiliary) evaporators
meta.job: Replace the A/C compressor, balance the oil, evacuate and charge
meta.labor: About 3.0 h. Ford allowance in CSP 19B01 to recover, replace the compressor and the desiccant bag, and recharge.
meta.skill_level: Professional · EPA Section 609 certificate required
meta.document: Rev A · 2026-11-09 · written in ASD-STE100 style
cover_warning: R-1234yf is a flammable refrigerant (ASHRAE class A2L). Use only R-1234yf equipment (SAE J2843). Do not release refrigerant to the air. Wear eye protection and gloves.
cover_note: The 2018 and later Navigator has no air-suspension compressor. It has coil springs with Adaptive Suspension (Continuously Controlled Damping). On this vehicle, "air compressor" means the A/C compressor, which this manual covers.
---

# A/C Compressor Removal and Installation

## 1. Scope and Applicability

This manual gives the procedure to remove and install the A/C compressor on a 2019 Lincoln Navigator. It also gives the checks before and after the repair.

| Item | Data |
|---|---|
| Vehicle | 2019 Lincoln Navigator and Navigator L (U554 platform, shared with the 2018–2021 Ford Expedition) |
| Engine | 3.5L twin-turbo EcoBoost V6 |
| Refrigerant | R-1234yf (build code G3FAD) |
| Compressor | Belt-driven, with an A/C clutch and two electrical connectors. Driven by its own stretch belt (Ford tool 303-1419). Mounted low on the passenger side of the engine, from technician reports [VERIFY]. Variable displacement with an external control valve [VERIFY]. |
| Not covered | Air-suspension compressor (not installed on 2018 and later models), HVAC module, evaporator replacement |

> **NOTE:** The 2007–2017 Navigator has a rear air-suspension compressor. The 2018 and later Navigator does not. If the customer complaint is "air compressor noise" on a 2019 model, examine the A/C compressor and the A/C clutch first.

> **NOTE:** After a front-end collision, examine the condenser, the condenser lines and the compressor mounts for damage. A damaged condenser can let air and moisture into the system. This can cause compressor failure later.

### 1.1 How to use this manual

- Do the procedures in sequence: A, B, C, D, E, F.
- Each step has one action. Do the step, then go to the next step.
- A **[VERIFY]** tag shows a value that this manual could not confirm from a Ford source for this vehicle. Get the value from the Ford Workshop Manual (WSM) for the VIN before you use it.
- Ford service information is available by subscription at motorcraftservice.com. The A/C procedures are in WSM section 412-00 and Group 412.
- Before you start, use the VIN to find open Field Service Actions. Ford had two A/C programs on this platform (see section 14).

| Signal word | Meaning |
|---|---|
| WARNING | A risk of injury or death. |
| CAUTION | A risk of damage to the vehicle or the equipment. |
| NOTE | Information only. A NOTE does not contain an instruction. |

[[FLOW: Sec. 6: Diagnose > A: Recover refrigerant > B: Remove compressor > C: Balance oil > D: Install compressor > E: Evacuate and charge > F: Test]]

<!-- pagebreak -->

## 2. Safety

> **WARNING:** R-1234yf is flammable (ASHRAE class A2L). Keep sparks, flames and hot surfaces away from refrigerant leaks. Do not smoke near the vehicle. Make sure that the shop has good airflow.

> **WARNING:** Liquid refrigerant can freeze skin and eyes. Wear safety glasses with side shields and refrigerant-resistant gloves when you open the system.

> **WARNING:** Do not release refrigerant to the air. Section 608 of the Clean Air Act prohibits venting. Recover all refrigerant with certified equipment.

> **WARNING:** Let the engine cool before you work near the exhaust and turbochargers. Hot parts can cause burns.

> **WARNING:** Keep the key fob away from the vehicle. Make sure that the engine cannot start while your hands are near the drive belts.

> **WARNING:** Support the vehicle on a lift or on jack stands. Do not work below a vehicle that only a jack holds.

> **CAUTION:** Do not use R-134a equipment, oil or hoses on this system. Use only Motorcraft R-1234yf PAG oil (YN-35). Other oil damages the compressor and contaminates the system.

> **CAUTION:** Install caps on all open refrigerant ports immediately. PAG oil absorbs moisture from the air.

> **CAUTION:** Small particles can damage the turbocharger compressor wheel. Cover all open air-intake parts. Do not let dirt into the intake.

### 2.1 Technician qualification

- In the United States, a technician who services motor vehicle A/C systems for payment must have an EPA Section 609 certificate. This rule applies to all refrigerants.
- Use refrigerant equipment that is certified for R-1234yf. Use an SAE J2843 recovery, recycling and recharging machine.
- If the refrigerant is contaminated, use SAE J2851 recovery-only equipment and a separate tank.
- Use an electronic leak detector that meets SAE J2913 for R-1234yf.

## 3. Tools, Equipment and Consumables

| Item | Specification or use |
|---|---|
| R-1234yf A/C service machine | SAE J2843 certified. Ford-approved equipment has a built-in refrigerant analyzer. |
| Refrigerant identifier | R-1234yf capable, if the machine does not have one |
| Electronic leak detector | SAE J2913 (R-1234yf) |
| Scan tool | Ford IDS / FDRS or equal. Reads PCM and HVAC DTCs and A/C PIDs. |
| Stretch-belt tool | Ford special tool 303-1419 (stretchy belt tool) |
| Sockets and wrenches | Ford CSP 19B01 list: 7, 8, 10, 11 and 13 mm sockets (deep 10, 11 and 13 mm), T50 TORX socket, 10 and 13 mm ratcheting wrenches, 1/4 in and 3/8 in extensions |
| Torque wrenches | 1/4 in and 3/8 in drive |
| Trim tools | Plastic trim tool, metal push-pin tool, 6 in right-angle pick, snap-ring pliers |
| Graduated cylinder | Clean, marked in mL, 250 mL minimum. Measures the compressor oil. |
| Oil injector | For the low-side service port, or use the oil function of the A/C machine |
| Lift, or jack and jack stands | Rated for the vehicle weight |
| Probe thermometer | For the center-vent temperature |
| Caps, plugs and cable ties | To seal open ports and to hold parts away from the work area |

## 4. Parts

| Part | Ford / Motorcraft number | Notes |
|---|---|---|
| A/C compressor | KL1Z-19703-A (replaces JL1Z-19703-AB, Motorcraft YCC-453) | Parts-catalog supersession. Ford CSPs 19B01 and 20N08 list JL1Z-19703-AB. Fits 2018–2021 Navigator and Expedition 3.5L. |
| Desiccant bag (in the condenser) | FC3Z-19C836-A | Ford replaces this bag with the compressor in CSP 19B01 |
| O-ring kit | HL3Z-19B596-A | Listed in CSP 19B01 (2019 model year) |
| Compressor gasket kit | DS7Z-19B596-A | Listed in CSP 20N08 (2018 model year). Use the seal kit that matches the line fittings. |
| A/C compressor stretch belt | Get from the VIN [VERIFY] | Do not install the old belt again |
| A/C clutch (service) | L1MZ-19D786-E | Only for a clutch-only repair |
| Refrigerant | Motorcraft YN-33-A, R-1234yf | 37 oz (1.05 kg) for a full charge |
| Refrigerant oil | Motorcraft YN-35, R-1234yf PAG oil | For the oil balance |

> **NOTE:** Part numbers change through supersession. Confirm each number with the VIN at a Lincoln parts counter before you order.

## 5. Specifications

| Specification | Value | Source |
|---|---|---|
| Refrigerant | R-1234yf, Motorcraft YN-33-A, Ford spec. WSS-M17B21-A | 2019 Navigator Owner's Manual, p. 431 |
| Refrigerant charge | 37 oz (1.05 kg), all variants (Navigator and Navigator L) | 2019 Navigator Owner's Manual, p. 431 |
| Refrigerant oil | Motorcraft R-1234yf PAG Oil YN-35, Ford spec. WSS-M2C300-A2 | 2019 Navigator Owner's Manual, p. 431 |
| Total system oil | 6.1 fl oz (180 mL) | 2019 Navigator Owner's Manual, p. 431 |
| Oil in a new service compressor | Full system oil charge | Ford WSM 412-00, Refrigerant Oil Adding |
| Evacuation | Minimum 29.5 inHg (99.4 kPa) vacuum. Pump for a minimum of 45 min after you reach it. Vacuum must hold for 10 min. | Ford WSM 412-00 general procedure [VERIFY] for U554 |
| Compressor mounting bolts (3) | [VERIFY] | Not found. Use the Ford WSM. |
| Refrigerant line manifold bolt | [VERIFY] | Not found. Use the Ford WSM. |
| Compressor oil drain bolt | 9, 20 or 30 N·m, by compressor type [VERIFY] | Ford WSM 412-00 gives one value for each compressor type |
| Clutch coil resistance | [VERIFY] | Not found. Use the Ford WSM. |
| A/C performance (outlet temperature and pressures) | [VERIFY] | Not found. Use the Ford WSM chart. |

> **NOTE:** The under-hood A/C label shows the refrigerant type and the factory charge quantity for this vehicle. If the label and this manual are different, use the label.

<!-- pagebreak -->

## 6. Diagnosis Before Replacement

Do not replace the compressor until you know that the compressor is the cause. Many "no cold air" complaints come from a low charge, a fuse, a relay, a sensor or a blend door.

### 6.1 Checks

1. Get the customer complaint. Record the conditions when the fault occurs.
2. Connect the scan tool. Read and record all DTCs in the PCM and the HVAC module.
3. Examine the A/C fuse and the A/C clutch relay (if equipped). Replace a blown fuse only after you find the short circuit.
4. Connect the A/C machine or a gauge set to the high-side and low-side service ports. Record the static pressure with the engine off.
   - If the static pressure is less than the saturation pressure for the ambient temperature, the system is low on refrigerant. Find the leak first.
5. Start the engine. Set the A/C to MAX, recirculation, high blower.
6. Examine the compressor clutch. Make sure that the clutch engages.
   - If the clutch does not engage, measure the voltage at the clutch connector.
   - If voltage is present, measure the clutch coil resistance. Compare it with the Ford value [VERIFY].
7. Record the high-side and low-side pressures. Compare them with the Ford chart for the ambient temperature [VERIFY].
   - If the clutch is engaged, the low side is high and the high side is low, the compressor does not pump.
8. Listen for noise from the compressor. Use a mechanic's stethoscope on the compressor body and on the clutch bearing.
   - If the noise stops when the A/C is OFF, the noise is from the compressor or the clutch.
   - If the noise continues when the A/C is OFF, examine the clutch pulley bearing and the drive belts.
9. Examine the compressor shaft seal and the body joints for oil and refrigerant leaks.

### 6.2 Decision

| Condition | Action |
|---|---|
| Clutch coil, clutch plate or pulley bearing fault only | Replace the A/C clutch (L1MZ-19D786-E). Use the Ford clutch procedure in Group 412. |
| Shaft-seal leak, no internal damage | Replace the compressor. Use procedures A to F. |
| Compressor does not pump, oil is clean | Replace the compressor. Use procedures A to F. |
| Internal failure: metal particles, or black or grey oil | Replace the compressor and do section 6.3. |
| Air or moisture in the system (for example, after collision damage) | Replace the compressor and the desiccant bag. Repair the cause. |

<!-- pagebreak -->

### 6.3 Internal failure (debris)

Debris from a failed compressor goes into the condenser, the lines and the evaporators. If the debris stays, it damages the new compressor. Do these steps in addition to procedures A to F.

1. Remove and discard the desiccant bag, the front thermostatic expansion valve (TXV) and the rear TXV.
2. Remove and discard all refrigerant hoses that have a muffler.
3. Flush the condenser and the front and rear evaporators in the direction opposite to the refrigerant flow.
   - Use only the Ford A/C Flush and Purge Service Unit with Motorcraft A/C System Flushing Solvent (YN-23).
   - Use a new 1 gal (3.78 L) container of YN-23 and a new FL1-A filter for each vehicle.
4. Purge the flushed parts with the service unit to remove all solvent.
5. Examine the hoses without mufflers. If a hose is clogged, replace the hose.
6. Install a new desiccant bag, new TXVs and new muffler hoses.
7. Install the new compressor with its full oil charge. Do not do the oil balance in Procedure C.

> **CAUTION:** Do not flush the compressor, the desiccant bag, the TXVs or hoses with mufflers. Solvent stays inside these parts.

> **CAUTION:** Do not push shop air directly through the A/C system. Shop air has moisture and dirt in it. Use the purge function of the service unit.

<!-- pagebreak -->

## 7. Procedure A — Recover the Refrigerant

1. Park the vehicle on a level floor. Apply the parking brake.
2. Let the engine cool.
3. Connect the A/C machine to the high-side and low-side service ports.
4. Do a test of the refrigerant with the analyzer. Make sure that the refrigerant is R-1234yf with no contamination.
   - If the refrigerant is contaminated, do not recover it into the shop machine. Use J2851 recovery-only equipment and a dedicated tank.
5. Recover the refrigerant through both service ports.
6. Record the quantity of refrigerant that the machine recovers.
7. Record the quantity of oil that the machine removes during recovery.
8. Wait 2 minutes. Look at the vacuum gauge.
   - If the vacuum decreases, recover again. Do this until the vacuum stays stable for 2 minutes.
9. Disconnect the machine. Install the service port caps.

> **NOTE:** Solenoid valves in the system can stop a full recovery from one port. Ford tells you to recover from both the high-side and the low-side ports.

<!-- pagebreak -->

## 8. Procedure B — Remove the Compressor

> **NOTE:** The access sequence below comes from a technician repair on a 2019 Ford Expedition, which has the same platform and engine. The Ford WSM (Group 412) is the official procedure. If the WSM sequence is different, use the WSM sequence.

1. Make sure that Procedure A is complete and that the system pressure is zero.
2. Disconnect the battery negative cable.
3. If you cannot reach the line manifold bolt from above, remove the battery and the battery tray.
4. Disconnect the A/C clutch electrical connector from above.
5. Remove the bolt that attaches the refrigerant line manifold to the compressor.
6. Disconnect the line manifold from the compressor.
7. Install caps on the line manifold and the compressor ports immediately.
8. Discard the old seals.
9. Raise the vehicle and support it.
10. Remove the lower front splash shield. Keep the push pins and the bolts.
11. Disconnect the second compressor connector (control valve) from below.
12. Take a photo of the drive belt routing.
13. Release the tension on the main drive belt. Remove the main drive belt from the pulleys.
14. Cut the A/C compressor stretch belt. Discard the belt.
15. If the air intake tube blocks the rear mounting bolt, release the clip and move the tube away.
   - Cover all open intake parts. This prevents damage to the turbocharger.
16. Hold the compressor. Loosen the three mounting bolts (two upper and one lower).
17. Lower the compressor out below the vehicle.

> **CAUTION:** When you cut the stretch belt, do not cut or scratch the pulleys, hoses or wires.

> **NOTE:** On the reference vehicle, the three mounting bolts stay in the compressor body when you loosen them. The compressor comes out from below.

<!-- pagebreak -->

## 9. Procedure C — Balance the Oil

The total oil quantity in the system must stay the same after the repair. Too little oil damages the new compressor. Too much oil decreases cooling. The new service compressor contains the full system oil charge (180 mL). The old compressor contains only part of the oil. The remaining oil stays in the condenser, the lines and the evaporators.

> **NOTE:** Do this procedure only if you did not flush the system. If you flushed the system (section 6.3), install the new compressor with its full oil charge.

> **CAUTION:** Turn the compressor shaft, not only the pulley. If only the pulley turns, the oil does not drain fully.

1. Find the compressor type and the oil drain bolt location in Ford WSM 412-00, Refrigerant Oil Adding [VERIFY].
2. Put the old compressor on a clean bench above a clean graduated cylinder.
3. Remove the oil drain bolt from the old compressor.
4. Turn the compressor shaft 6 to 8 turns. Collect all the oil.
5. Record the quantity of oil from the old compressor.
6. Examine the oil. If the oil has metal particles, or is black or grey, stop. Do section 6.3.
7. Install the drain bolt in the old compressor. Tag the old compressor for core return.
8. Remove the caps from the suction and discharge ports of the new compressor.
9. Remove the oil drain bolt from the new compressor.
10. Turn the compressor shaft 6 to 8 turns. Drain all the oil into a separate container.
11. Put new YN-35 oil into the new compressor. Use the same quantity that you drained from the old compressor.
12. Install the drain bolt in the new compressor. Tighten it to the value for the compressor type [VERIFY].
13. Install the caps on the new compressor ports.
14. Calculate the oil to add through the low-side port in Procedure E. Use the table below.

| Part replaced with the compressor | Oil to add through the low-side port in Procedure E |
|---|---|
| Compressor only | The oil that the machine removed in Procedure A, step 7 |
| Desiccant bag (receiver drier element) | 1 fl oz (30 mL) plus the oil from Procedure A |
| Condenser | 1.5 fl oz (45 mL) plus the oil from Procedure A |
| Condenser and desiccant bag | 2 fl oz (60 mL) plus the oil from Procedure A |
| Thermostatic expansion valve | The oil from Procedure A only |
| Refrigerant hose or line | 2 fl oz (60 mL) plus the oil from Procedure A |

> **NOTE:** The values in this table come from the Ford WSM 412-00 general procedure for R-1234yf systems [VERIFY] for U554. Add oil only once for each part. Do not add the values for parts that you did not replace.

<!-- pagebreak -->

## 10. Procedure D — Install the Compressor

1. Compare the new compressor with the old compressor. Make sure that the mounts, the ports, the connectors and the pulley are the same.
2. Make sure that Procedure C is complete on the new compressor.
3. If you replace the desiccant bag, replace it now. Use the Ford WSM procedure for the condenser desiccant bag.
4. Put the compressor in position from below.
5. Install the three mounting bolts by hand.
6. Tighten the three mounting bolts to the Ford value [VERIFY].
7. Connect the control valve electrical connector (lower connector).
8. Install a new A/C stretch belt with the stretch-belt tool 303-1419.
9. Make sure that the stretch belt is fully in the grooves of both pulleys.
10. Install the main drive belt. Use the routing photo from Procedure B, step 12, and the under-hood belt label.
11. Make sure that the main drive belt is fully in the grooves of each pulley.
12. If you moved the air intake tube, remove the covers. Install the tube and the clip.
13. Make sure that no dirt or tools are in the air intake.
14. Install the lower front splash shield with all push pins and bolts.
15. Lower the vehicle.
16. Remove the caps from the line manifold and the compressor ports.
17. Clean the sealing surfaces with a lint-free cloth.
18. Install new seals from the seal kit. If the seals are O-rings, lubricate them with clean YN-35 oil [VERIFY].
19. Connect the line manifold to the compressor.
20. Install the line manifold bolt. Tighten it to the Ford value [VERIFY].
21. Connect the A/C clutch electrical connector.
22. If you removed the battery and the battery tray, install them.
23. Connect the battery negative cable.

> **CAUTION:** Do not start the engine with the A/C on before the system is charged. A compressor that runs without refrigerant can be damaged.

<!-- pagebreak -->

## 11. Procedure E — Evacuate, Leak Test and Charge

1. Connect the A/C machine to the high-side and low-side service ports.
2. Evacuate the system to a minimum of 29.5 inHg (99.4 kPa).
3. Operate the vacuum pump for a minimum of 45 minutes after you reach this vacuum.
4. Stop the vacuum pump. Look at the low-side gauge for 10 minutes.
   - If the vacuum decreases, find and repair the leak. Do not charge the system.
5. Add the oil quantity from Procedure C, step 14, through the low-side port.
6. Charge the system with 37 oz (1.05 kg) of R-1234yf. Charge by weight.
7. Disconnect the machine. Install the service port caps.
8. Do a leak test of all joints that you opened. Use the J2913 leak detector with the engine off.
   - Use the leak-search method in SAE J1628 and the detector instructions.

> **NOTE:** The charge quantity on the under-hood label overrides the value in step 6.

## 12. Procedure F — Performance Test and Return to Service

1. Clear all DTCs.
2. Start the engine.
3. Set the climate control to A/C MAX, recirculation, high blower, rear A/C on.
4. Close the doors and the windows.
5. Run the engine at the speed and for the time that the Ford performance chart specifies [VERIFY].
6. Measure the center-vent outlet temperature with the probe thermometer.
7. Compare the temperature and the pressures with the Ford performance chart for the ambient temperature and humidity [VERIFY].
8. Make sure that the compressor clutch engages and that the compressor makes no unusual noise.
9. Make sure that the rear outlets also supply cold air.
10. Read the DTCs again. Make sure that no new DTCs are present.
11. Do a second leak test after the system cools.
12. Fill in the record sheet in section 13. Attach it to the repair order.

<!-- pagebreak -->

## 13. Record Sheet and Final Check

[[SIGNOFF]]

### 13.1 Final checklist

- [ ] Open Field Service Actions checked for the VIN
- [ ] Refrigerant identified as R-1234yf before recovery
- [ ] Recovered refrigerant and oil quantities recorded
- [ ] Oil balanced (Procedure C) or system flushed (section 6.3). Quantities recorded.
- [ ] New seals installed at every opened joint
- [ ] All bolts tightened to the Ford values
- [ ] New A/C stretch belt installed with tool 303-1419
- [ ] Main drive belt routed correctly and fully in the pulley grooves
- [ ] Both compressor connectors connected and locked
- [ ] Air intake clean, tube and clip installed
- [ ] Splash shield and all fasteners installed
- [ ] Vacuum held for 10 minutes. Charge is 37 oz (1.05 kg) or the label value.
- [ ] Leak test passed at all opened joints
- [ ] Outlet temperature within the Ford chart, front and rear
- [ ] No DTCs present
- [ ] Old compressor tagged for core return or warranty

## 14. References

| Reference | Used for |
|---|---|
| Lincoln, *2019 Navigator Owner's Manual*, 2nd printing (Aug 2018), Capacities and Specifications, p. 431. fordservicecontent.com | Refrigerant and oil type, charge, total oil |
| Ford Customer Satisfaction Program 19B01 (Jan 17, 2019): certain 2019 Expedition and Navigator, A/C evacuation. static.nhtsa.gov/odi/tsbs/2019/MC-10153987-9999.pdf | Tool list, WSM section 412-00, compressor, desiccant bag and O-ring kit part numbers, 3.0 h labor, turbocharger debris notice |
| Ford Customer Satisfaction Program 20N08 (Mar 18, 2021): certain 2018 Expedition and Navigator, contaminated refrigerant. static.nhtsa.gov/odi/tsbs/2021/MC-10189756-0001.pdf | Gasket kit part number. For 2018 vehicles built Jan 27 to Feb 6, 2018 only: do not connect shop equipment unless the program tells you to. |
| Ford WSM 412-00 General Procedures (published text for the 2020 and later Escape): Refrigerant Oil Adding, Recovery Evacuation and Charging, A/C System Flushing | Oil balance method, oil-add table, evacuation values, flushing rules |
| EPA, "Regulatory Requirements for MVAC System Servicing." epa.gov/mvac/regulatory-requirements-mvac-system-servicing | Section 609 certificate, venting prohibition |
| EPA, "Section 609 Certified Equipment." epa.gov/mvac/section-609-certified-equipment | SAE J2843, J2851 and J3030 equipment standards |
| SAE J2913 (R-1234yf leak detectors), SAE J1628 (leak-search procedure) | Leak test |
| Ford parts catalog (dealer listing), KL1Z-19703-A and L1MZ-19D786-E | Current compressor and clutch numbers |
| Technician video, 2019 Ford Expedition MAX A/C compressor replacement. youtube.com/watch?v=2q0jK7a6Pm0 | Access sequence in Procedure B (not an official source) |

> **NOTE:** This manual is a shop work aid. It does not replace the Ford Workshop Manual. Ford and Lincoln publish the official procedure, torque values and capacities for each VIN. If this manual and the Ford information are different, use the Ford information.
