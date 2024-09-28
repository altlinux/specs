Name: gcodeworkshop
Version: 202409
Release: alt1

Summary: GCodeWorkShop is text editor for CNC programmers
License: GPL-3.0-or-later
Group: Engineering

Url: https://github.com/GCodeProjects/GCodeWorkShop
VCS: https://github.com/GCodeProjects/GCodeWorkShop.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: qt5-base-devel
BuildRequires: qt5-tools
BuildRequires: qt5-serialport-devel

%description
%summary.
This is a fork of EdytorNC, a text editor for CNC programmers.

%prep
%setup
%patch -p1

%build
%qmake_qt5 VERSION=%version PREFIX=%prefix
%make_build lrelease
%qmake_qt5 VERSION=%version PREFIX=%prefix
%make_build

%install
%make_install INSTALL_ROOT=%buildroot install
rm -vr %buildroot/%_datadir/doc/gcodeworkshop/

%files
%_bindir/gcodeworkshop
%_bindir/gcodefileserver
%_datadir/gcodeworkshop/
%_datadir/mime/packages/application-x-g-code.xml
%_desktopdir/gcodeworkshop.desktop
%_iconsdir/hicolor/32x32/mimetypes/application-x-g-code.png
%_iconsdir/hicolor/48x48/apps/edytornc.png
%doc LICENSE README.md doc/SerialTransmission_Help.html

%changelog
* Sat Sep 28 2024 Anton Midyukov <antohami@altlinux.org> 202409-alt1
- Initial build
