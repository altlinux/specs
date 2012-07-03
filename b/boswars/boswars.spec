Name: boswars
Version: 2.6.1
Release: alt1
Summary: Bos Wars is a futuristic real-time strategy game
Group: Games/Strategy
License: GPLv2
Url: http://www.boswars.org/
Packager: Egor Glukhov <kaman@altlinux.org>
Requires: %name-data = %version

Source: %name-%version-%release.tar
BuildRequires: flex gcc-c++ libGL-devel libSDL-devel libX11-devel libpng-devel libvorbis-devel python-modules-email scons tolua++-devel desktop-file-utils

%description
Bos Wars is a futuristic real-time strategy game. It is possible to play
against human opponents over LAN, internet, or against the computer.
Bos Wars aims to create a completly original and fun open source RTS game.

%package data
Group: Games/Strategy
Summary: Data files to Bos Wars
BuildArch: noarch
Requires: %name = %version

%description data
Bos Wars is a futuristic real-time strategy game. It is possible to play
against human opponents over LAN, internet, or against the computer.
Bos Wars aims to create a completly original and fun open source RTS game.

This package contains data files to Bos Wars.

%prep
%setup

%build
scons opengl=1

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_datadir/%name/languages
install -m 755 %name %buildroot%_bindir
install -p -m 644 languages/*.po languages/*.pot \
%buildroot%_datadir/%name/languages
cp -a campaigns graphics intro maps scripts sounds units \
%buildroot%_datadir/%name

# below is the desktop file and icon stuff.
mkdir -p %buildroot%_desktopdir
desktop-file-install --dir %buildroot%_desktopdir %name.desktop
mkdir -p %buildroot%_iconsdir/hicolor/32x32/apps
install -p -m 644 graphics/ui/elites_claw.png \
%buildroot%_iconsdir/hicolor/32x32/apps/%name.png

%files
%doc *.txt CHANGELOG doc/*.html doc/guichan-copyright.txt
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/32x32/apps/%name.png

%files data
%_datadir/%name

%changelog
* Wed Jun 23 2010 Egor Glukhov <kaman@altlinux.org> 2.6.1-alt1
- 2.6.1 (specfile based on Fedora's)
