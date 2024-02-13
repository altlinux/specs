%define game_name Warcraft2
Name: wargus
Version: 3.3.2
Release: alt1
Summary: %game_name mod for the Stratagus engine
License: GPLv2
Group: Games/Strategy
Url: https://github.com/Wargus/%name

Requires: %name-data = %version
Source: %name-%version.tar
BuildRequires(pre): cmake rpm-macros-cmake gcc-c++
BuildRequires: stratagus-devel = %version /usr/bin/convert
# Automatically added by buildreq on Fri Feb 02 2024 (-bi)
# optimized out: cmake-modules debugedit desktop-file-utils elfutils glibc-kernheaders-generic glibc-kernheaders-x86 libImageMagick7-common libctf-nobfd0 libgpg-error libp11-kit libsasl2-3 libstdc++-devel python3 python3-base python3-dev python3-module-py3dephell rpm-build-file rpm-build-python3 rpm-macros-python3 sh5 stratagus xz zlib-devel
BuildRequires: bzlib-devel cmake gcc-c++ libpng-devel python3-module-setuptools rpm-build-gir
BuildRequires: desktop-file-utils

%description
%name is a %game_name. Mod that allows you to play %game_name with the Stratagus
engine, as opposed to play it with the original %game_name one.

%package data
Summary: %game_name mod for the Stratagus engine
Group: Games/Strategy
BuildArch: noarch
Requires: stratagus = %version

%description data
%game_name mod for the Stratagus engine.
Contains data files.

%prep
%setup -n %name-%version

%build
%cmake
%cmake_build

%install
%cmake_install
mkdir -p %buildroot%_man6dir/
mv doc/*.6 %buildroot%_man6dir
desktop-file-validate %buildroot/%_desktopdir/%name.desktop
for x in 16 32 48; do
    mkdir -p %buildroot%_iconsdir/hicolor/$x'x'$x/apps/
	convert %buildroot%_pixmapsdir/%name.png -resize $x'x'$x %buildroot/%_iconsdir/hicolor/$x'x'$x/apps/%name.png
done

%files
%_gamesbindir/%name
%_bindir/pudconvert
%_bindir/wartool
%_desktopdir/%name.desktop

%files data
%doc COPYING-* README.md doc/
%exclude %_pixmapsdir/%name.png
%_liconsdir/%name.png
%_niconsdir/%name.png
%_miconsdir/%name.png
%_gamesdatadir/stratagus/%name
%_man6dir/*.6.*

%changelog
* Fri Feb 02 2024 Ildar Mulyukov <ildar@altlinux.ru> 3.3.2-alt1
- new version

* Fri Nov 11 2016 Anton Midyukov <antohami@altlinux.org> 2.4.1-alt1
- new version 2.4.1-alt1

* Wed Jul 27 2016 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt2
- Fix arch-dep-package-has-big-usr-share.

* Sat Jul 02 2016 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt1
- Initial build for ALT Linux Sisyphus.
