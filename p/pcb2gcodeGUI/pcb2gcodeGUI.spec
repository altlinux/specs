Name: pcb2gcodeGUI
Version: 2.5.0
Release: alt1
Summary: A GUI for pcb2gcode
Group: Engineering
License: GPL-3.0-or-later
URL: https://github.com/pcb2gcode/pcb2gcodeGUI
VCS: https://github.com/pcb2gcode/pcb2gcodeGUI

Source: %name-%version.tar
#Source1: http://findicons.com/icon/download/177847/pcb/128/png
Source1: pcb.png
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick-tools

Requires: pcb2gcode

ExcludeArch: %ix86 %arm

%description
A GUI for pcb2gcode, a software for the isolation, routing and drilling
of PCBs.

%prep
%setup
%patch -p1

%build
%qmake_qt6 PREFIX=%prefix
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

### == desktop file
cat>%name.desktop<<END
[Desktop Entry]
Name=%name
Exec=%_bindir/%name
Icon=%name
Terminal=false
Type=Application
Categories=Development;Electronics;
END

desktop-file-install --dir=%buildroot%_desktopdir %name.desktop

#Install icons
for x in 16 32 48; do
    mkdir -p %buildroot%_iconsdir/hicolor/$x'x'$x/apps/
    magick %SOURCE1 -resize $x'x'$x %buildroot/%_iconsdir/hicolor/$x'x'$x/apps/%name.png
done

%files
%doc README.md LICENSE
%_bindir/pcb2gcodeGUI
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Sun Mar 01 2026 Anton Midyukov <antohami@altlinux.org> 2.5.0-alt1
- New version 2.5.0.
- Build with qt6.

* Sat Sep 25 2021 Anton Midyukov <antohami@altlinux.org> 1.3.3-alt2
- ExcludeArch: %ix86 %arm

* Thu May 13 2021 Anton Midyukov <antohami@altlinux.org> 1.3.3-alt1
- new version 1.3.3

* Sun Jul 08 2018 Anton Midyukov <antohami@altlinux.org> 1.3.2-alt1.1
- Rebuilt for aarch64

* Tue Aug 22 2017 Anton Midyukov <antohami@altlinux.org> 1.3.2-alt1
- Initial build for ALT Sisyphus.
