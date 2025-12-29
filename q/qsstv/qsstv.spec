Name: qsstv
Version: 9.5.11
Release: alt1

Summary: Qt-based SSTV and HamDRM
License: GPLv2
Group: Communications

Source0: %name-%version.tar
Source1: qsstv.1
Source2: index.html

Patch0: qsstv-9.5.8-rigcontrol.cpp.patch
Patch1: qsstv-9.5.11-Fix-broken-DRM-decode.patch

Requires: icon-theme-hicolor

BuildRequires(pre): qt5-base-devel
BuildRequires: gcc-c++
BuildRequires: libqwt6-qt5-devel
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(hamlib)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libopenjp2)
BuildRequires: pkgconfig(libv4l2)
BuildRequires: /usr/bin/dot
BuildRequires: /usr/bin/doxygen

ExcludeArch: %ix86

%description
QSSTV 9 is a program for receiving and transmitting Slow Scan TV and HAMDRM
(sometimes called DSSTV). It is compatible with most of MMSSTV and EasyPal
The User's Guide is in the program Help.

%prep
%setup
%autopatch -p1
mv documentation src/documentation

sed -i "s!/usr/local!%_prefix!" src/%name.pro
sed -i "s!-O0!-O2!" src/%name.pro
sed -i "/^INSTALLS/s!target!target shortcutfiles dox!" src/%name.pro

%build
qmake-qt5 PREFIX=%_prefix CONFIG+='debug and release' QMAKE_CXXFLAGS+="-std=c++14 %optflags" src/%name.pro
%make_build

%install
export INSTALL_ROOT=%buildroot
make install

install -D -m0644 %name.desktop %buildroot%_datadir/applications/%name.desktop
install -D -m0644 src/icons/%name.png %buildroot%_iconsdir/hicolor/48x48/apps/%name.png
install -D -m0644 %SOURCE2 %buildroot%_docdir/%name/manual/index.html
install -D -m0644 %SOURCE1 %buildroot%_man1dir/%name.1

%files
%doc COPYING *.md
%_bindir/*
%_datadir/applications/%name.desktop
%_iconsdir/hicolor/48x48/apps/%name.png
%_docdir/%name/manual/index.html
%_man1dir/%name.1*

%changelog
* Mon Dec 29 2025 Andrew A. Vasilyev <andy@altlinux.org> 9.5.11-alt1
- new version

* Mon Dec 29 2025 Andrew A. Vasilyev <andy@altlinux.org> 9.5.8-alt2
- add some documentation

* Sun Dec 28 2025 Andrew A. Vasilyev <andy@altlinux.org> 9.5.8-alt1
- Initial build for ALT.

