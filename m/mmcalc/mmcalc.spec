Name: mmcalc
Summary: Molar Mass Calculator
Version: 20160529
Release: alt1
Group: Sciences/Chemistry
License: LGPL
URL: http://www.ogion76.name/home/mmcalc

Packager: Denis G. Samsonenko <ogion@altlinux.org>

Source: %name-%version.tar.gz

BuildArch: noarch

BuildPreReq: perl-Module-Build >= 0.36

BuildRequires: perl-File-BaseDir perl-Gtk2-Ex-Simple-List perl-Locale-Msgfmt perl-Locale-gettext perl-Gtk3 perl-Gtk3-SimpleList

%description
This program calculates molar mass and percent of each
element for the given chemical formula.

The program contains perl module MMCalc.pm and perl
script %name, a console version of calculator.

Examples of valid formulae: H2O, CuSO4*5h2o, hgcl2, c o,
In(NO3)3*4.5H2O, Rb16Cd25,39Sb36.

Acronyms are also supported: [Zn2(dabco)(bdc)2]*4DMF,
Pd(acac)2, h4edta.

Using of parentheses, square brackets as well as braces
is acceptable.

%package gui-common
Summary: Molar Mass Calculator
Group: Sciences/Chemistry
BuildArch: noarch
Requires: %name = %version-%release

%description gui-common
The program calculates molar mass and percent of each element
for the given chemical formula. This package contains common
files for GUI version of calculator.


%package gtk2
Summary: Molar Mass Calculator (Gtk+2 GUI)
Group: Sciences/Chemistry
BuildArch: noarch
Requires: %name = %version-%release, %name-gui-common = %version-%release

%description gtk2
The program calculates molar mass and percent of each element
for the given chemical formula. This package contains a Gtk+2
GUI version of calculator.

Examples of valid formulae: H2O, CuSO4*5h2o, hgcl2, c o,
In(NO3)3*4.5H2O, Rb16Cd25,39Sb36.

Acronyms are also supported: [Zn2(dabco)(bdc)2]*4DMF,
Pd(acac)2, h4edta. It is possible to add, remove and
change the acronyms.

Using of parentheses, square brackets as well as braces
is acceptable.


%package gtk3
Summary: Molar Mass Calculator (Gtk+3 GUI)
Group: Sciences/Chemistry
BuildArch: noarch
Requires: %name = %version-%release, %name-gui-common = %version-%release

%description gtk3
The program calculates molar mass and percent of each element
for the given chemical formula. This package contains a Gtk+3
GUI version of calculator.

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
%find_lang %name

%files
%doc README ChangeLog
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/*.dat
%perl_vendor_privlib/*.pm

%files gui-common -f %name.lang
%_datadir/icons/hicolor/scalable/apps/%name.svg

%files gtk2
%_bindir/g%name-gtk2
%_desktopdir/g%name-gtk2.desktop

%files gtk3
%_bindir/g%name-gtk3
%_desktopdir/g%name-gtk3.desktop

%changelog
* Sun May 29 2016 Denis G. Samsonenko <ogion@altlinux.org> 20160529-alt1
- new version
- devided into several subpackages

* Tue May 14 2013 Denis G. Samsonenko <ogion@altlinux.org> 20130514-alt1
- new version

* Sun Dec 02 2012 Denis G. Samsonenko <ogion@altlinux.org> 20121202-alt1
- new version

* Thu Aug 30 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120830-alt1
- new version
- mmcalc.desktop and mmcalc.svg are now packed into source tar.gz

* Tue Aug 21 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120821-alt1
- new version
- changelog fixed

* Wed Aug 15 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120815-alt1
- new version

* Tue Aug 14 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120814-alt1
- new version

* Mon Aug 13 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120813-alt1
- new version

* Sun Aug 12 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120811-alt2
- ChangeLog fixed

* Sun Aug 12 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120811-alt1
- new version

* Wed Aug 08 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120808-alt1
- new version

* Fri Aug 03 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120802-alt1
- new version

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
