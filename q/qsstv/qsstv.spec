Name: qsstv
Summary: QSSTV is an sstv app
Version: 9.5.8
Release: alt1

License: GPLv2
Group: Communications
Source0: %name-%version.tar

Requires: icon-theme-hicolor

BuildRequires(pre): qt5-base-devel
BuildRequires: gcc-c++
BuildRequires: libqwt6-qt5-devel
BuildRequires: pkgconfig(fftw3)
BuildRequires: hamlib-devel
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libopenjp2)
BuildRequires: pkgconfig(libv4l2)
BuildRequires: /usr/bin/dot
BuildRequires: /usr/bin/doxygen

ExcludeArch: %ix86

%description
qsstv is an sstv app.
You can send and receive images sent over radio using your soundcard.

%prep
%setup
sed -i "s!/usr/local!%_prefix!" src/%name.pro
sed -i "s!-O0!-O2!" src/%name.pro
sed -i "/^INSTALLS/s!target!target shortcutfiles dox!" src/%name.pro

%build
qmake-qt5 PREFIX=%_prefix CONFIG+=debug QMAKE_CXXFLAGS+="-std=c++14 %optflags" src
ln -s ../documentation src/documentation
%make_build

%install
export INSTALL_ROOT=%buildroot
make install

install -D -m0644 %name.desktop %buildroot%_datadir/applications/%name.desktop
install -D -m0644 src/icons/%name.png %buildroot%_iconsdir/hicolor/48x48/apps/%name.png

%files
%doc COPYING *.md
%_bindir/*
%_datadir/applications/%name.desktop
%_iconsdir/hicolor/48x48/apps/%name.png

%changelog
* Sun Dec 28 2025 Andrew A. Vasilyev <andy@altlinux.org> 9.5.8-alt1
- Initial build for ALT.

