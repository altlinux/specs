Name: coil64
Version: 2.3.38
Release: alt1

Summary: A inductance coil calculator
License: GPLv3
Group: Engineering
Url: https://coil32.net
VCS: https://github.com/radioacoustick/Coil64

Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: ImageMagick-tools
BuildRequires: pkgconfig(Qt5)

%description
Coil64 is inductance coil calculator, that allows to calculate the single-layer
and multi-layer air core inductors, the ferrite core inductors or chokes,
planar coils on PCB etc.

%prep
%setup

%build
%qmake_qt5 -o Makefile Coil64.pro
%make_build

%install
install -pm0755 -D Coil64 %buildroot%_bindir/coil64
install -pm0644 -D coil64.desktop %buildroot%_desktopdir/coil64.desktop
magick res/Coil64_Icon.ico coil.png
install -pm0644 -D coil-0.png %buildroot%_iconsdir/hicolor/48x48/apps/coil64.png

%files
%_bindir/coil64
%_desktopdir/coil64.desktop
%_iconsdir/*/*/*/*.png

%changelog
* Mon Nov 24 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.3.38-alt1
- 2.3.38 released

* Fri Aug 29 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.3.37-alt1
- 2.3.37 released

* Fri Aug 01 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.3.36-alt1
- 2.3.36 released

