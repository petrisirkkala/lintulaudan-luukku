// Versio 7: millimetrit. Vain yläreuna R9.5, alareuna 90 astetta.
$fn=96;
paksuus=10;
reunapyoristys=9.5;
kulmasade=10;
reikavali=168;
siipireika=6.8;
lukitusreika=12.6;
mutterireika=12.6;
mutterisyvyys=7;
// Jokainen profiili: [sisennys, korkeus].
profiilit=concat([[0,0]],[for(j=[0:32]) [reunapyoristys*(1-cos(90*j/32)),paksuus-reunapyoristys+reunapyoristys*sin(90*j/32)]]);
module aihio(){
    for(j=[0:len(profiilit)-2]) hull(){
        for(k=[j:j+1]) translate([0,0,profiilit[k][1]])
            linear_extrude(0.001)
                translate([-31+profiilit[k][0],-5+profiilit[k][0]])
                    offset(r=kulmasade-profiilit[k][0])
                        offset(delta=-(kulmasade-profiilit[k][0]))
                            square([194-2*profiilit[k][0],85-2*profiilit[k][0]]);
    }
}
// OpenSCAD-esikatselussa kerrokset ulottuvat 0.001 mm yli profiilin.
// Tarkka tulostusmalli: luukku_v7.stl, lähde tee_luukku_v7.py.
difference(){
    aihio();
    translate([-18,30,-0.01]) cylinder(h=paksuus+0.02,d=siipireika);
    translate([-18+reikavali,30,-0.01]) cylinder(h=paksuus+0.02,d=lukitusreika);
    translate([-18,30,-0.01]) cylinder(h=mutterisyvyys+0.01,d=mutterireika);
}
