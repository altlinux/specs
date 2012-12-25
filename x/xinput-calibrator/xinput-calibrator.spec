Name: xinput-calibrator
Version: 0.7.5
Release: alt1

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
* Tue Dec 25 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.5-alt1
- initial
