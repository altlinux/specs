%define game_name Warcraft
Name: war1gus
Version: 3.3.2
Release: alt1
Summary: %game_name mod for the Stratagus engine
License: GPLv2
Group: Games/Strategy
Url: https://github.com/Wargus/%name

Source: %name-%version.tar
BuildRequires(pre): cmake rpm-macros-cmake gcc-c++
BuildRequires: stratagus-devel = %version /usr/bin/convert
# Automatically added by buildreq on Mon Feb 05 2024 (-bi)
# optimized out: cmake-modules debugedit desktop-file-utils elfutils glibc-kernheaders-generic glibc-kernheaders-x86 libImageMagick7-common libctf-nobfd0 libgpg-error libp11-kit libsasl2-3 libstdc++-devel python3 python3-base python3-dev rpm-build-file rpm-build-python3 sh5 stratagus zlib-devel
BuildRequires: cmake gcc-c++ libpng-devel python3-module-setuptools rpm-build-gir stratagus-devel
BuildRequires: desktop-file-utils

%description
%name is a %game_name. Mod that allows you to play %game_name with the Stratagus
engine, as opposed to play it with the original %game_name one.

%prep
%setup -n %name-%version

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
desktop-file-validate %buildroot/%_desktopdir/%name.desktop
for x in 16 32 48; do
    mkdir -p %buildroot%_iconsdir/hicolor/$x'x'$x/apps/
	convert %buildroot%_pixmapsdir/%name.png -resize $x'x'$x %buildroot/%_iconsdir/hicolor/$x'x'$x/apps/%name.png
done

%files
%doc README.md
%_gamesbindir/%name
%_bindir/war1tool
%exclude %_pixmapsdir/%name.*
%_liconsdir/%name.png
%_niconsdir/%name.png
%_miconsdir/%name.png
%_desktopdir/%name.desktop
%_gamesdatadir/stratagus/%name

%changelog
* Tue Feb 06 2024 Ildar Mulyukov <ildar@altlinux.ru> 3.3.2-alt1
- new version

* Fri Nov 11 2016 Anton Midyukov <antohami@altlinux.org> 2.4.1-alt1
- new version 2.4.1

* Sat Jul 02 2016 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt1
- Initial build for ALT Linux Sisyphus.
