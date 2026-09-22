Name: edfbrowser
Version: 2.15
Release: alt1

Summary: EDF+ and BDF+ viewer and toolbox
LIcense: GPLv3
Group: Engineering
URL: https://www.teuniz.net/edfbrowser/index.html
VCS: https://gitlab.com/teuniz/edfbrowser

Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Core5Compat)

%description
A free, open-source, multiplatform, universal viewer, annotator and toolbox
intended for, but not limited to, time-series storage files like EEG, EMG,
ECG, BioImpedance, etc.

%prep
%setup

%build
%qmake_qt6
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
* Tue Sep 22 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.15-alt1
- 2.15 released

* Wed Oct 29 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.14-alt1
- 2.14 released

* Fri Jul 11 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.13-alt1
- 2.13 released

* Wed Jun 25 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.12-alt1
- 2.12 released
