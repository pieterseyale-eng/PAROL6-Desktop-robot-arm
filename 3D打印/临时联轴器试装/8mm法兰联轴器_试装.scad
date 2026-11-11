// PAROL6 temporary fit-check flange, based on the user's purchased-item drawing.
// Dimensions in mm. This is a printable mock-up, not the vendor's CAD.
$fn = 128;
flange_d = 32;
flange_h = 3;
hub_d = 16;
hub_h = 10;
shaft_bore_d = 8.2;   // 0.2 mm FDM allowance around nominal 8 mm shaft
bolt_pcd = 24;
bolt_hole_d = 4.2;   // clearance for nominal M4 screw; vendor drawing says 4 mm
set_screw_pilot_d = 3.3; // M4 tapping pilot in printed plastic
set_screw_z = 8;

difference() {
    union() {
        cylinder(d=flange_d, h=flange_h);
        translate([0,0,flange_h]) cylinder(d=hub_d, h=hub_h);
    }
    translate([0,0,-1]) cylinder(d=shaft_bore_d, h=flange_h+hub_h+2);
    for (a=[0:90:270])
        rotate([0,0,a]) translate([bolt_pcd/2,0,-1])
            cylinder(d=bolt_hole_d, h=flange_h+2);
    // Two radial M4 pilot holes, 90 degrees apart. Confirm actual purchased part on arrival.
    for (a=[0,90])
        rotate([0,0,a]) translate([0,0,set_screw_z]) rotate([0,90,0])
            cylinder(d=set_screw_pilot_d, h=hub_d/2+1);
}
