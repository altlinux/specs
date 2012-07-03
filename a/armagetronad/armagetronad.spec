Name: armagetronad
Version: 0.2.8.3.2
Release: alt1
Summary: 3D Tron-like high speed game

Group: Games/Arcade
License: GPL
Url: http://armagetronad.sourceforge.net

Source: %name-%version.tar
Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: libxml2-devel libSDL-devel libGL-devel libGLU-devel zlib-devel libpng-devel libSDL_image-devel gcc-c++ libjpeg-devel

%description
The rules are simple: you ride a lightcycle, a kind of motorbike that
can only turn 90 degrees at a time, leaves a wall behind and cannot be
stopped. Avoid running into a wall while trying to make your opponent
run into a wall.
Just in case you do not know: this idea is best known from the Disney
movie "Tron" from 1982. However, that's not the origin of the game idea.

%package dedicated
Group: Games/Arcade
Summary: 3D Tron-like high speed game. Dedicated server
%description dedicated
%summary

%prep
%setup -q

%build
# Build client
%configure --enable-glout --disable-uninstall
%make_build
mkdir .client
%make_install DESTDIR=$(pwd)/.client install
# Build dedicated server
%configure --enable-dedicated --disable-uninstall --disable-initscripts
%make_build

%install
%makeinstall_std
cp -R .client/* %buildroot/
mkdir -p %buildroot{%_miconsdir,%_niconsdir,%_liconsdir,%_desktopdir}
cp %buildroot%_datadir/games/%name/desktop/icons/small/%name.png  %buildroot%_miconsdir
cp %buildroot%_datadir/games/%name/desktop/icons/medium/%name.png %buildroot%_niconsdir
cp %buildroot%_datadir/games/%name/desktop/icons/large/%name.png  %buildroot%_liconsdir
cp %buildroot%_datadir/games/%name/desktop/%name.desktop %buildroot%_desktopdir

%files
%_sysconfdir/games/%name
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_desktopdir/%name.desktop
%_bindir/%name
%_datadir/doc/games/%name
%_datadir/games/%name
%exclude %_datadir/games/%name/scripts
%exclude %_datadir/games/%name/language/update.py

%files dedicated
%_sysconfdir/games/%name-dedicated
%_bindir/%name-dedicated
%_datadir/doc/games/%name-dedicated
%_datadir/games/%name-dedicated
%exclude %_datadir/games/%name-dedicated/scripts
%exclude %_datadir/games/%name-dedicated/language/update.py

%changelog
* Tue Oct 04 2011 Vladimir Lettiev <crux@altlinux.ru> 0.2.8.3.2-alt1
- new version 0.2.8.3.2

* Fri Jan 14 2011 Vladimir Lettiev <crux@altlinux.ru> 0.2.8.3.1-alt1
- initial build

