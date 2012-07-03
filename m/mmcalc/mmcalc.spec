Name: mmcalc
Summary: Molar Mass Calculator
Version: 20110913
Release: alt1
Group: Sciences/Chemistry
License: LGPL
URL: http://www.ogion76.name/home/mmcalc

Packager: Denis G. Samsonenko <ogion@altlinux.org>

Source: %name-%version.tar.gz
Source1: %name.svg

BuildArch: noarch

#BuildPreReq: perl-Glib
BuildPreReq: perl-Module-Build >= 0.36

# Automatically added by buildreq on Mon Jul 26 2010 (-bi)
BuildRequires: perl-Encode perl-File-BaseDir perl-Gtk2 perl-Module-Build

%description
This program calculates molar mass and percent of each
element for the given chemical formula.

The program contains perl module MMCalc.pm and two perl
scripts, mmcalc and gmmcalc.

mmcalc is a console version of calculator, while gmmcalc
is GUI version using Gtk2.

Examples of valid formulae: H2O, CuSO4*5h2o, hgcl2, c o,
In(NO3)3*4.5H2O, Rb16Cd25,39Sb36.

Acronyms are also supported: [Zn2(dabco)(bdc)2]*4DMF,
Pd(acac)2, h4edta. It is possible to add, remove and
change the acronyms.

Using of parentheses, square brackets as well as braces
is acceptable.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

install -m 755 -d %buildroot%_desktopdir

cat > %buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Name=MMCalc
Comment=Molar Mass Calculator
Exec=gmmcalc
Icon=mmcalc
Terminal=false
Type=Application
StartupNotify=true
Categories=Education;Science;Chemistry;
EOF

install -m 755 -d %buildroot%_datadir/icons/hicolor/scalable/apps
install -m 644 %SOURCE1 %buildroot%_datadir/icons/hicolor/scalable/apps/%name.svg

%files
%doc README ChangeLog
%_bindir/*
%dir %_datadir/%name
%_datadir/%name/*.dat
%_datadir/icons/hicolor/scalable/apps/%name.svg
%perl_vendor_privlib/*.pm
%_desktopdir/%name.desktop

%changelog
* Tue Sep 13 2011 Denis G. Samsonenko <ogion@altlinux.org> 20110913-alt1
- new version
- add icon
- fix Desktop Entry

* Wed Sep 07 2011 Denis G. Samsonenko <ogion@altlinux.org> 20110804-alt1
- build for Sisyphus
- adapt to use git and gear

* Fri Apr 08 2011 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20110804-alt0.sdg1
- new version

* Fri Apr 08 2011 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20110408-alt0.sdg1
- new version

* Fri Apr 01 2011 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20110330-alt0.sdg2
- little fix in files section in spec file

* Wed Mar 30 2011 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20110330-alt0.sdg1
- new version

* Sat Nov 20 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20101120-alt0.sdg1
- new version

* Mon Sep 05 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100905-alt0.sdg1
- new version

* Mon Jul 26 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100726-alt0.sdg1
- new version
- spec clean up

* Sat Jul 24 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100724-alt0.sdg1
- Build.PL (Module::Build) is used insted of Makefile.PL
- license is changed to LGPL

* Tue Jul 13 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100713-alt0.sdg1
- new version

* Sun Jul 11 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100711-alt0.sdg1
- new version

* Fri Jul 09 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100709-alt0.sdg1
- new version

* Thu Jul 08 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100708-alt0.sdg1
- new version
- minor changes in description

* Tue Jul 06 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100706-alt0.sdg1
- principle functionality realized
- README and ChangeLog added

* Fri May 07 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100507-alt0.sdg1
- new version

* Wed Mar 24 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100324-alt0.sdg1
- use Makefile.PL

* Tue Feb 16 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 20100216-alt0.sdg1
- initial build for ALTLinux
