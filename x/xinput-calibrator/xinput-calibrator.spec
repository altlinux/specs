Name: xinput-calibrator
Version: 0.7.5
Release: alt4

Summary: A generic touchscreen calibration program for X.Org
License: MIT
Group: System/X11 
Url: http://www.freedesktop.org/wiki/Software/xinput_calibrator
# Additional source url https://packages.debian.org/source/sid/xinput-calibrator

Source: %name-%version-%release.tar
Patch1: do_not_install_tester.patch
Patch2: typo_in_man.patch
Patch3: typo_in_src.patch

Patch4: adding-russian-translate-desktop.patch

BuildRequires: gcc-c++ libXi-devel libgtkmm2-devel

%description
%summary

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

%patch4 -p1

%build
%add_optflags -std=c++11
%autoreconf
%configure --with-gui=gtkmm
make

%install
%makeinstall

%files
%doc COPYING README

%_bindir/xinput_calibrator

%_desktopdir/xinput_calibrator.desktop
%_pixmapsdir/xinput_calibrator.*

%_man1dir/xinput_calibrator.*

%changelog
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
