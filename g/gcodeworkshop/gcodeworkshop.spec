Name: gcodeworkshop
Version: 202504
Release: alt1

Summary: GCodeWorkShop is text editor for CNC programmers
License: GPL-3.0-or-later
Group: Engineering

URL: https://github.com/GCodeProjects/GCodeWorkShop
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
%make_build
%make_build i18n

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
%doc COPYING COPYING.LESSER NEWS.md README.md doc/SerialTransmission_Help.html

%changelog
* Sun May 18 2025 Anton Midyukov <antohami@altlinux.org> 202504-alt1
- New version 202504.

* Sat Feb 08 2025 Anton Midyukov <antohami@altlinux.org> 202502-alt1
- New version 202502.

* Tue Oct 22 2024 Anton Midyukov <antohami@altlinux.org> 202410-alt1
- New version 202410.

* Sat Sep 28 2024 Anton Midyukov <antohami@altlinux.org> 202409-alt1
- Initial build
