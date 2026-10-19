Name: xinput-calibrator
Version: 0.8.0
Release: alt1

Summary: A generic touchscreen calibration program for X.Org
License: MIT
Group: System/X11 
Url: http://www.freedesktop.org/wiki/Software/xinput_calibrator
# Additional source url https://packages.debian.org/source/sid/xinput-calibrator

Source: %name-%version-%release.tar
Patch1: typo_in_man.patch
Patch2: typo_in_src.patch

BuildRequires: gcc-c++ libXi-devel libgtkmm2-devel

%description
%summary

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%add_optflags -std=c++11
%autoreconf
%configure --with-gui=gtkmm
make

%install
%makeinstall
# move icons to the icon theme dirs (IconPathsPolicy), add a menu category
install -Dm644 %buildroot%_pixmapsdir/xinput_calibrator.svg %buildroot%_iconsdir/hicolor/scalable/apps/xinput_calibrator.svg
install -Dm644 %buildroot%_pixmapsdir/xinput_calibrator.xpm %buildroot%_niconsdir/xinput_calibrator.xpm
rm -v %buildroot%_pixmapsdir/xinput_calibrator.*
sed -i 's/^Categories=System;Settings;$/Categories=System;Settings;HardwareSettings;/' %buildroot%_desktopdir/xinput_calibrator.desktop

%files
%doc COPYING README.md

%_bindir/xinput_calibrator

%_desktopdir/xinput_calibrator.desktop
%_iconsdir/hicolor/scalable/apps/xinput_calibrator.svg
%_niconsdir/xinput_calibrator.xpm

%_man1dir/xinput_calibrator.*

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt1
- new version 0.8.0
- drop patches merged upstream (tester, Russian desktop name)
- move icons to the icon theme dirs, add HardwareSettings category

* Wed Apr 20 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 0.7.5-alt4
- NMU: Adding russian translation for desktop file

* Thu Jan 14 2021 Pavel Vasenkov <pav@altlinux.org> 0.7.5-alt3
- Rebuild from newer source with patches

* Mon Apr 11 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.5-alt2
- fix FTBFS with gcc5

* Sat Jun 13 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.5-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Dec 25 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.5-alt1
- initial
