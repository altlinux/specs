Name: pcb2gcodeGUI
Version: 1.3.3
Release: alt2
Summary: A GUI for pcb2gcode

Group: Engineering
License: GPLv3+
Url: https://github.com/pcb2gcode/pcb2gcodeGUI/
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
#Source1: http://findicons.com/icon/download/177847/pcb/128/png
Source1: pcb.png
BuildRequires: gcc-c++ pkgconfig(Qt5) pkgconfig(Qt5Core) pkgconfig(Qt5Widgets) pkgconfig(Qt5Svg) desktop-file-utils ImageMagick-tools

Requires: pcb2gcode

ExcludeArch: %ix86 %arm

%description
A GUI for pcb2gcode, a software for the isolation, routing and drilling
of PCBs.

%prep
%setup

%build
%qmake_qt5 PREFIX=%prefix
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
    convert %SOURCE1 -resize $x'x'$x %buildroot/%_iconsdir/hicolor/$x'x'$x/apps/%name.png
done

%files
%doc README.md LICENSE
%_bindir/pcb2gcodeGUI
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Sat Sep 25 2021 Anton Midyukov <antohami@altlinux.org> 1.3.3-alt2
- ExcludeArch: %ix86 %arm

* Thu May 13 2021 Anton Midyukov <antohami@altlinux.org> 1.3.3-alt1
- new version 1.3.3

* Sun Jul 08 2018 Anton Midyukov <antohami@altlinux.org> 1.3.2-alt1.1
- Rebuilt for aarch64

* Tue Aug 22 2017 Anton Midyukov <antohami@altlinux.org> 1.3.2-alt1
- Initial build for ALT Sisyphus.
