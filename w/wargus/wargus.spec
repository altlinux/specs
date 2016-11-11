%define game_name Warcraft2
Name: wargus
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
Requires: %name-data = %version

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
%make_build -C BUILD

%install
%makeinstall_std -C BUILD
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
%doc COPYING* README.md doc/
%exclude %_pixmapsdir/%name.png
%_liconsdir/%name.png
%_niconsdir/%name.png
%_miconsdir/%name.png
%_gamesdatadir/stratagus/%name
%_man6dir/*.6.*

%changelog
* Fri Nov 11 2016 Anton Midyukov <antohami@altlinux.org> 2.4.1-alt1
- new version 2.4.1-alt1

* Wed Jul 27 2016 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt2
- Fix arch-dep-package-has-big-usr-share.

* Sat Jul 02 2016 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt1
- Initial build for ALT Linux Sisyphus.
