Name: dsremote
Version: 0.46
Release: alt1

Summary: Rigol DS1000 series oscilloscope tool
License: GPLv3
Group: Engineering
Url: https://www.teuniz.net/DSRemote/

Source: %name-%version-%release.tar

BuildRequires: pkgconfig(Qt5)

%description
DSRemote is a program to control and visualize your Rigol DS6000 or DS1000Z
series oscilloscope from your Linux desktop via USB or LAN.

%prep
%setup

%build
%qmake_qt5
%make_build

%install
%install_qt5

%files
%doc LICENSE README
%_bindir/dsremote
%_udevrulesdir/*.rules
%_desktopdir/dsremote.desktop
%_iconsdir/hicolor/*/*/*.png

%changelog
* Tue Jul 29 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.46-alt1
- 0.46 released

* Mon Apr 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.40-alt1
- initial
