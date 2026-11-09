---
kicker: SHOP SERVICE MANUAL · CLIMATE CONTROL
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
meta.labor: {{LABOR}}
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
| Refrigerant | R-1234yf |
| Compressor | {{COMP_TYPE}} |
| Not covered | Air-suspension compressor (not installed on 2018 and later models), HVAC module, rear evaporator replacement |

> **NOTE:** The 2007–2017 Navigator has a rear air-suspension compressor. The 2018 and later Navigator does not. If the customer complaint is "air compressor noise" on a 2019 model, examine the A/C compressor and the A/C clutch first.

### 1.1 How to use this manual

- Do the procedures in sequence: A, B, C, D, E, F.
- Each step has one action. Do the step, then go to the next step.
- A **[VERIFY]** tag shows a value that this manual could not confirm from an official Ford source. Get the value from the Ford Workshop Manual for the VIN before you use it.
- Ford service information is available by subscription at motorcraftservice.com.

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

> **WARNING:** Do not release refrigerant to the air. Federal law prohibits venting. Recover all refrigerant with an SAE J2843 machine.

> **WARNING:** Let the engine cool before you work near the exhaust and turbochargers. Hot parts can cause burns.

> **WARNING:** Remove the key fob from the vehicle area. Make sure that the engine cannot start while your hands are near the accessory drive belt.

> **CAUTION:** Do not use R-134a equipment, oil or hoses on this system. Mixed refrigerant or oil can damage the compressor and contaminate the shop machine.

> **CAUTION:** Install caps on all open refrigerant ports immediately. PAG oil absorbs moisture from the air.

### 2.1 Technician qualification

- In the United States, a technician who services motor vehicle A/C systems for payment must have an EPA Section 609 certificate. {{EPA609_NOTE}}
- Use a recovery, recycling and recharging machine that is certified to SAE J2843 for R-1234yf.
- Use an electronic leak detector that is certified to SAE J2913 for R-1234yf. {{J2913_NOTE}}

## 3. Tools, Equipment and Consumables

| Item | Specification or use |
|---|---|
| R-1234yf recovery / recharge machine | SAE J2843 certified |
| Electronic leak detector | Approved for R-1234yf (SAE J2913) |
| Refrigerant identifier | R-1234yf capable. Do a test of the refrigerant before recovery. |
| Scan tool | Ford IDS / FDRS or equal. Reads HVAC and PCM DTCs and A/C PIDs. |
| Belt tensioner tool | Serpentine belt tool with long handle |
| Torque wrench | Range to cover the line-fitting bolts and the mount bolts |
| Graduated cylinder | 250 mL minimum, marked in mL. Measures oil drained from the old compressor. |
| Clean drain pan | For the compressor oil |
| Lift or ramps and jack stands | Vehicle must be safe on supports |
| Thermometer | Probe type, for the center-vent temperature test |
| PAG oil | {{OIL_SPEC}} |
| O-rings / gasket seals | New, R-1234yf approved, from the compressor kit or Ford dealer |
| Port caps and plugs | To seal open lines |
| Lint-free cloths | To clean the line fittings |

## 4. Parts

| Part | Ford / Motorcraft number | Notes |
|---|---|---|
{{PARTS_ROWS}}

> **NOTE:** Part numbers change through supersession. Confirm each number with the VIN at a Lincoln parts counter before you order.

## 5. Specifications

| Specification | Value | Status |
|---|---|---|
{{SPEC_ROWS}}

> **NOTE:** The under-hood A/C label shows the refrigerant type and the factory charge quantity for this vehicle. The label value overrides any value in this manual.

<!-- pagebreak -->

## 6. Diagnosis Before Replacement

Do not replace the compressor until you know that the compressor is the cause. Many "no cold air" complaints come from a low charge, a fuse, a relay, a sensor or a blend door.

### 6.1 Checks

1. Get the customer complaint. Record the conditions when the fault occurs.
2. Connect the scan tool. Read and record all DTCs in the PCM and the HVAC module.
3. Examine the A/C fuse and the A/C clutch relay (if equipped). Replace a blown fuse only after you find the short circuit.
4. Connect the J2843 machine or a gauge set to the service ports. Record the static pressure with the engine off.
   - If the static pressure is less than the saturation pressure for the ambient temperature, the system is low on refrigerant. Find the leak first.
5. Start the engine. Set the A/C to MAX, high blower, recirculation.
6. Examine the compressor clutch. Make sure that the clutch engages.
   - If the clutch does not engage, measure the voltage at the clutch connector. If voltage is present, measure the clutch coil resistance against the Ford specification [VERIFY].
7. Record the high-side and low-side pressures. Compare the pressures with the Ford pressure chart for the ambient temperature.
   - If the low side is high and the high side is low with the clutch engaged, the compressor does not pump.
8. Listen for noise from the compressor. Use a stethoscope on the compressor body and on the clutch bearing.
   - If the noise stops when the A/C is OFF, the noise is from the compressor or the clutch.
   - If the noise continues when the A/C is OFF, examine the clutch pulley bearing and the accessory drive.
9. Examine the compressor shaft seal and the body joints for oil and refrigerant leaks.

### 6.2 Decision

| Condition | Action |
|---|---|
| Clutch coil, pulley bearing or air gap fault only | {{CLUTCH_ACTION}} |
| Shaft-seal leak, no internal damage | Replace the compressor. Use procedures A to F. |
| Compressor does not pump, oil is clean | Replace the compressor. Use procedures A to F. |
| Internal failure: metal particles, black or grey oil | Replace the compressor, the condenser (with desiccant), the thermostatic expansion valves and the suction-line muffler/screen if equipped. Flush the lines and evaporators. See 6.3. |

### 6.3 Internal failure (debris)

{{DEBRIS_TEXT}}

> **CAUTION:** Do not flush the condenser or the compressor. Debris stays in the small passages of a parallel-flow condenser. Replace the condenser after an internal compressor failure.

<!-- pagebreak -->

## 7. Procedure A — Recover the Refrigerant

1. Park the vehicle on a level floor. Apply the parking brake.
2. Let the engine cool.
3. Connect the refrigerant identifier to the low-side service port. Make sure that the refrigerant is R-1234yf with no contamination.
   - If the identifier shows contamination, do not recover into the shop machine. Use a dedicated recovery tank for contaminated refrigerant.
4. Connect the J2843 machine to the high-side and low-side service ports.
5. Recover all refrigerant. Follow the instructions of the machine manufacturer.
6. Record the quantity of refrigerant that the machine recovers.
7. Record the quantity of oil that the machine removes during recovery.
8. Disconnect the machine couplers from the service ports. Install the service port caps.

<!-- pagebreak -->

## 8. Procedure B — Remove the Compressor

{{REMOVE_STEPS}}

<!-- pagebreak -->

## 9. Procedure C — Balance the Oil

The total system oil quantity must be correct after the repair. Too little oil damages the new compressor. Too much oil decreases cooling.

{{OIL_BALANCE}}

<!-- pagebreak -->

## 10. Procedure D — Install the Compressor

{{INSTALL_STEPS}}

<!-- pagebreak -->

## 11. Procedure E — Evacuate, Leak Test and Charge

1. Connect the J2843 machine to the high-side and low-side service ports.
2. Evacuate the system for a minimum of {{EVAC_TIME}}.
3. Close the machine valves. Monitor the vacuum for a minimum of 5 minutes [VERIFY].
   - If the vacuum decreases, find and repair the leak. Do not charge the system.
4. Add oil with the machine only if Procedure C tells you to add oil through the system.
5. Charge the system with the exact quantity of R-1234yf on the under-hood label. Charge by weight.
6. Disconnect the machine. Install the service port caps.
7. Do a leak test of all joints that you opened. Use the electronic leak detector with the engine OFF.
   - Move the probe at 25–50 mm/s (1–2 in/s), 5 mm (0.25 in) or less from each joint.

## 12. Procedure F — Performance Test and Return to Service

1. Clear all DTCs. Start the engine.
2. Set the climate control to A/C MAX, recirculation, high blower, rear A/C ON.
3. Close the doors and windows. Run the engine at 1500 rpm for 5 minutes.
4. Measure the center-vent outlet temperature with the probe thermometer.
5. Compare the outlet temperature and the pressures with the Ford performance chart for the ambient temperature and humidity [VERIFY].
6. Make sure that the compressor clutch engages and that the compressor makes no unusual noise.
7. Make sure that the rear outlets also blow cold air.
8. Read the DTCs again. Make sure that no new DTCs are present.
9. Do a second leak test after the system cools.
10. Fill in the record sheet in section 13. Attach it to the repair order.

<!-- pagebreak -->

## 13. Record Sheet and Final Check

[[SIGNOFF]]

### 13.1 Final checklist

- [ ] Refrigerant identified as R-1234yf before recovery
- [ ] Recovered refrigerant and oil quantities recorded
- [ ] Oil balanced to Procedure C. Quantities recorded.
- [ ] New, R-1234yf-approved seals installed at every opened joint
- [ ] All bolts tightened to specification
- [ ] Accessory drive belt routed correctly and seated on every pulley
- [ ] Electrical connectors connected and locked
- [ ] Splash shield and all fasteners installed
- [ ] Vacuum held. Charge quantity matches the under-hood label.
- [ ] Leak test passed at all opened joints
- [ ] Outlet temperature within the Ford chart, front and rear
- [ ] No DTCs present
- [ ] Old compressor tagged for core return or warranty

## 14. References

{{REFERENCES}}

> **NOTE:** This manual is a shop work aid. It does not replace the Ford Workshop Manual. Ford and Lincoln publish the official procedure, torque values and capacities for each VIN. If this manual and the Ford information are different, use the Ford information.
