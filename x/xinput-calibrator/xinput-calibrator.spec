Name: xinput-calibrator
Version: 0.7.5
Release: alt2

Summary: A generic touchscreen calibration program for X.Org
License: MIT
Group: System/X11 
Url: http://www.freedesktop.org/wiki/Software/xinput_calibrator

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ libXi-devel libgtkmm2-devel

%description
%summary

%prep
%setup

%build
%add_optflags -std=c++11
%autoreconf
%configure --with-gui=gtkmm
make

%install
%makeinstall

%files
%doc COPYING README

%_bindir/tester
%_bindir/xinput_calibrator

%_desktopdir/xinput_calibrator.desktop
%_pixmapsdir/xinput_calibrator.*

%_man1dir/xinput_calibrator.*

%changelog
* Mon Apr 11 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.5-alt2
- fix FTBFS with gcc5

* Sat Jun 13 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.5-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Dec 25 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.5-alt1
- initial
