Name: edfbrowser
Version: 2.14
Release: alt1

Summary: EDF+ and BDF+ viewer and toolbox
LIcense: GPLv3
Group: Engineering
Url: https://www.teuniz.net/edfbrowser/index.html

Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Core)

%description
A free, open-source, multiplatform, universal viewer, annotator and toolbox
intended for, but not limited to, time-series storage files like EEG, EMG,
ECG, BioImpedance, etc.

%prep
%setup

%build
%qmake_qt5
%make_build

%install
%make_install INSTALL_ROOT=%buildroot install
rm -v %buildroot%_datadir/*/edf.png

%define _customdocdir %_defaultdocdir/%name

%files
%doc DISCLAIMER LICENSE README
%_bindir/edfbrowser
%_desktopdir/*.desktop
%_datadir/mime/packages/*.xml
%_iconsdir/hicolor/*/*/*.png

%changelog
* Wed Oct 29 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.14-alt1
- 2.14 released

* Fri Jul 11 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.13-alt1
- 2.13 released

* Wed Jun 25 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.12-alt1
- 2.12 released
