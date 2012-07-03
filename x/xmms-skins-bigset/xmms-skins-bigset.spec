Name: xmms-skins-bigset
Version: 0.1
Release: alt1
Summary: Set from 98 skins for xmms.
License: GPL
Group: Sound
Packager: Alexey Shentzev <ashen@altlinux.ru>
BuildArchitectures: noarch

Source0: 30057-XMMSPlastik-1.0.wsz
Source1: Absolute_Blue-XMMS.zip
Source2: AbsoluteE_Xmms.zip
Source3: AdamAmp.zip
Source4: Antares_1a.wsz
Source5: Apple_Platinum_Amp.zip
Source6: Aqua.zip
Source7: arctic_Xmms.zip
Source8: blackstar.zip
Source9: BlackXMMS.zip
Source10: blueHeart-xmms-20.zip
Source11: blueHeart_Xmms.zip
Source12: BlueIce.zip
Source13: BlueSteel_xmms.zip
Source14: BlueSteel.zip
Source15: bmXmms.zip
Source16: BrushedMetal_Xmms.zip
Source17: cart0onix.zip
Source18: chaos_XMMS.zip
Source19: cherry_best.tar.gz
Source20: cherry.zip
Source21: Cobalt-Obscura.tar.gz
Source22: ColderXMMS.tar.gz
Source23: Concept_X.zip
Source24: Coolblue.tar.gz
Source25: Covenant.zip
Source26: cracked.zip
Source27: CX2.zip
Source28: Cyrus-XMMS.zip
Source29: detone_blue.zip
Source30: detone_green.zip
Source31: Eclipse.tar.gz
Source32: eMac_Xmms_Blueberry.zip
Source33: eMac-XMMS.zip
Source34: FB_1.2.zip
Source35: fiRe.tar.gz
Source36: FreeBSD.zip
Source37: Freshmeat_Amp.zip
Source38: fyre.zip
Source39: Ghost-10.zip
Source40: gLaNDAmp-2.0.zip
Source41: GTK+.zip
Source42: HeliXMMS.zip
Source43: Helix-Sawfish-xmms.tar.gz
Source44: Inverse.zip
Source45: ions.tar.gz
Source46: LinuxDotCom.tar.gz
Source47: m2n.tar.gz
Source48: MarbleX.tar.gz
Source49: Marble.zip
Source50: maXMMS.tar.gz
Source51: minEguE-xmms-v1.tar.gz
Source52: minEguE-xmms-v2.zip
Source53: myway.zip
Source54: myxmms-default-1.01.tar.gz
Source55: NeXTAmp2-1.0pre1.zip
Source56: NeXTAmp2.4.zip
Source57: nixamp2.tar.gz
Source58: NoerdAmp-SE.tar.gz
Source59: nuance-2.0.zip
Source60: nuance-green-2.0.zip
Source61: OmniAMP-1.3.zip
Source62: Panic.zip
Source63: Plume-XMMS-v1.zip
Source64: sinistar.zip
Source65: spiffMEDIA.zip
Source66: SuedE.zip
Source67: sword.tar.gz
Source68: titanium.zip
Source69: Ultrafina2000.zip
Source70: Ultrafina-pw.zip
Source71: UltrafinaSEM.zip
Source72: UltrafinaSE.zip
Source73: Ultrafina.zip
Source74: Vegetal_Blues.zip
Source75: Vegetali_1-1.zip
Source76: Vulcan21.zip
Source77: Vulcan.zip
Source78: Winamp5.tar.bz2
Source79: Winamp_X_XMMS_1.01.tar.gz
Source80: wmp.zip
Source81: WoodPanel.zip
Source82: XawMMS.zip
Source83: xliquidxmms-default-1.0.6.tar.gz
Source84: xmmearth.tar.gz
Source85: xmms-256.zip
Source86: XMMS-AfterStep.zip
Source87: XMMS-Green.zip
Source88: X-Tra.zip
Source89: yummiyogurtxmms-default-1.tar.gz
Source90: eMac_Xmms_Bondiblue.zip
Source91: eMac_Xmms_Grape.zip
Source92: eMac_Xmms_Lime.zip
Source93: eMac_Xmms_Strawberry.zip
Source94: eMac_Xmms_Tangerine.zip
Source95: Volkodav1.wsz
Source96: Volkodav2.wsz
Source97: The_Silence_v5.wsz

Obsoletes: xmms-skin-wmp
Provides: xmms-skin-wmp
Requires: xmms
Prefix: %prefix
%description
Set from 98 skins for xmms. Install this package. Browse with Options/Skin browser.
This package contains a big set of most beautiful skins.

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE0 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE1 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE2 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE3 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE4 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE5 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE6 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE7 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE8 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE9 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE10 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE11 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE12 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE13 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE14 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE15 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE16 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE17 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE18 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE19 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE20 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE21 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE22 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE23 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE24 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE25 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE26 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE27 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE28 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE29 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE30 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE31 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE32 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE33 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE34 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE35 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE36 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE37 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE38 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE39 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE40 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE41 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE42 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE43 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE44 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE45 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE46 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE47 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE48 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE49 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE50 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE51 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE52 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE53 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE54 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE55 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE56 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE57 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE58 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE59 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE60 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE61 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE62 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE63 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE64 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE65 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE66 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE67 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE68 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE69 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE70 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE71 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE72 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE73 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE74 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE75 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE76 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE77 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE78 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE79 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE80 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE81 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE82 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE83 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE84 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE85 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE86 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE87 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE88 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE89 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE90 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE91 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE92 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE93 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE94 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE95 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE96 $RPM_BUILD_ROOT%_datadir/xmms/Skins
cp %SOURCE97 $RPM_BUILD_ROOT%_datadir/xmms/Skins

cat >README << EOF
This package is a collection of skins for xmms.
Most of them come from http://www.xmms.org
EOF

%files
%_datadir/xmms/Skins
%doc README

%changelog
* Fri Aug 18 2006 Alexey Shentzev <ashen@altlinux.ru> 0.1-alt1
- firstbuild for Sisyphus

