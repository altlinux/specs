%define game_name Warcraft
Name: war1gus
Version: 2.4.1
Release: alt1
Summary: %game_name mod for the Stratagus engine
License: GPLv2
Group: Games/Strategy
Url: https://github.com/Wargus/%name
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
BuildRequires(pre): cmake rpm-macros-cmake gcc-c++
BuildRequires: stratagus-devel libX11-devel libgtk+2-devel libpng-devel zlib-devel ImageMagick-tools desktop-file-utils
Requires: stratagus = %version

%description
%name is a %game_name. Mod that allows you to play %game_name with the Stratagus
engine, as opposed to play it with the original %game_name one.

%prep
%setup -n %name-%version

%build
%cmake
%make_build -C BUILD

%install
%makeinstall_std -C BUILD
desktop-file-validate %buildroot/%_desktopdir/%name.desktop
for x in 16 32 48; do
    mkdir -p %buildroot%_iconsdir/hicolor/$x'x'$x/apps/
	convert %buildroot%_pixmapsdir/%name.png -resize $x'x'$x %buildroot/%_iconsdir/hicolor/$x'x'$x/apps/%name.png
done

%files
%doc COPYING* README.md
%_gamesbindir/%name
%_bindir/war1tool
%exclude %_pixmapsdir/%name.*
%_liconsdir/%name.png
%_niconsdir/%name.png
%_miconsdir/%name.png
%_desktopdir/%name.desktop
%_gamesdatadir/stratagus/%name

%changelog
* Fri Nov 11 2016 Anton Midyukov <antohami@altlinux.org> 2.4.1-alt1
- new version 2.4.1

* Sat Jul 02 2016 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt1
- Initial build for ALT Linux Sisyphus.
