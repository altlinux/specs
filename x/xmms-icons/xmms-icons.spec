Name: xmms-icons
Version: 0.1
Release: alt3
Summary: Set of icons for xmms
License: GPL
Group: Sound
Packager: Alexey Shentzev <ashen@altlinux.ru>
BuildArchitectures: noarch

Source0: xmms-alban.png
Source1: xmms-andy_fox-blue.png
Source2: xmms-andy_fox-gold.png
Source3: xmms-andy_fox-green.png
Source4: xmms-andy_fox-orange.png
Source5: xmms-andy_fox-purple.png
Source6: xmms-andy_fox-red.png
Source7: xmms-benjamin_p_jung.png
Source8: xmms-benjamin_p_jung.svg
Source9: xmms-bryce_corkins.png
Source10: xmms-ghostman.png
Source11: xmms-icon10.png
Source12: xmms-icon10.xpm
Source13: xmms-icon11.png
Source14: xmms-icon11.xpm
Source15: xmms-icon12.png
Source16: xmms-icon12.xpm
Source17: xmms-icon13.png
Source18: xmms-icon13.xpm
Source19: xmms-icon14.png
Source20: xmms-icon14.xpm
Source21: xmms-icon15.png
Source22: xmms-icon15.xpm
Source23: xmms-icon1.png
Source24: xmms-icon1.xpm
Source25: xmms-icon2.png
Source26: xmms-icon2.xpm
Source27: xmms-icon3.png
Source28: xmms-icon3.xpm
Source29: xmms-icon4.png
Source30: xmms-icon4.xpm
Source31: xmms-icon5.png
Source32: xmms-icon5.xpm
Source33: xmms-icon6.png
Source34: xmms-icon6.xpm
Source35: xmms-icon7.png
Source36: xmms-icon7.xpm
Source37: xmms-icon8.png
Source38: xmms-icon8.xpm
Source39: xmms-icon9.png
Source40: xmms-icon9.xpm
Source41: xmms-james_blachly.png
Source42: xmms-karzac.png
Source43: xmms-liknockzr1.png
Source44: xmms-liknockzr2.png
Source45: xmms-liknockzr3.png
Source46: xmms-liknockzr4.png
Source47: xmms-liknockzr5.png
Source48: xmms-liknockzr6.png
Source49: xmms-liknockzr7.png
Source50: xmms-liknockzr8.png
Source51: xmms-liknockzr9.png
Source52: xmms-mike.png
Source53: xmms_norteo.png
Source54: xmms_norteo.xpm
Source55: xmms-otto.png
Source56: xmms-otto.xpm
Source57: xmms-peter_wagenet.png
Source58: xmms-port001.png
Source59: xmms-rmckenzie.png
Source60: xmms-scourger.png
Source61: xmms-scourger.xpm
Source62: xmms-stimuli.png
Source63: xmms-tal.png
Source64: xmms-tlailax.png
Source65: xmms-tlailax.xpm
Source66: xmms-tony1.png
Source67: xmms-tony2.png
Source68: xmms-tony3.png
Source69: xmms-tony4.png

Obsoletes: xmms-icons
Provides: xmms-icons
Requires: xmms
Prefix: %prefix

%description
Icons for xmms. More 60 icons.

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE0 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE1 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE2 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE3 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE4 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE5 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE6 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE7 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE8 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE9 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE10 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE11 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE12 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE13 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE14 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE15 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE16 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE17 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE18 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE19 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE20 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE21 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE22 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE23 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE24 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE25 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE26 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE27 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE28 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE29 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE30 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE31 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE32 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE33 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE34 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE35 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE36 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE37 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE38 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE39 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE40 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE41 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE42 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE43 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE44 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE45 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE46 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE47 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE48 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE49 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE50 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE51 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE52 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE53 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE54 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE55 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE56 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE57 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE58 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE59 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE60 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE61 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE62 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE63 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE64 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE65 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE66 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE67 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE68 $RPM_BUILD_ROOT%_datadir/xmms/Icons
cp %SOURCE69 $RPM_BUILD_ROOT%_datadir/xmms/Icons

cat >README << EOF
This package is a collection of icons for xmms.
Most of them come from http://www.xmms.org
EOF

%files
%_datadir/xmms/Icons
%doc README

%changelog
* Fri Aug 18 2006 Alexey Shentzev <ashen@altlinux.ru> 0.1-alt3
the description in a spec-file is corrected

* Thu Aug 17 2006 Alexey Shentzev <ashen@altlinux.ru> 0.1-alt2
- correct section descriptions

* Tue Aug 15 2006 Alexey Shentzev <ashen@altlinux.ru> 0.1-alt1
- first build for sisyphus

