%define oname org.armagetronad.armagetronad

Name: armagetronad
Version: 0.2.9.3.0
Release: alt1
Summary: 3D Tron-like high speed game

Group: Games/Arcade
License: GPL-2.0-or-later

Url: https://www.armagetronad.org/
Vcs: https://gitlab.com/armagetronad/armagetronad

Source: %name-%version.tar

BuildRequires: libxml2-devel libSDL-devel libGL-devel libGLU-devel
BuildRequires: zlib-devel libpng-devel libSDL_image-devel gcc-c++
BuildRequires: libjpeg-devel pkgconfig(libcurl)

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
rm -v %buildroot/%_bindir/%{name}-master

%files
%_sysconfdir/games/%name
%_iconsdir/hicolor/*/apps/%oname.png
%_desktopdir/%oname.desktop
%_bindir/%name
%_datadir/doc/games/%name
%_datadir/games/%name
%_datadir/appdata/%oname.appdata.xml
%exclude %_datadir/games/%name/scripts

%files dedicated
%_sysconfdir/games/%name-dedicated
%_bindir/%name-dedicated
%_desktopdir/%{oname}-dedicated.desktop
%_datadir/doc/games/%name-dedicated
%_datadir/games/%name-dedicated
%_datadir/appdata/%{oname}-dedicated.appdata.xml
%_iconsdir/hicolor/*/apps/%{oname}-dedicated.png
%exclude %_datadir/games/%name-dedicated/scripts

%changelog
* Wed Jun 10 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.2.9.3.0-alt1
- 0.2.8.3.4 -> 0.2.9.3.0
- changed license
- changed url && added vcs

* Mon Jul 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.8.3.4-alt1
- Updated to upstream version 0.2.8.3.4

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8.3.2-alt1.1
- Rebuilt with libpng15

* Tue Oct 04 2011 Vladimir Lettiev <crux@altlinux.ru> 0.2.8.3.2-alt1
- new version 0.2.8.3.2

* Fri Jan 14 2011 Vladimir Lettiev <crux@altlinux.ru> 0.2.8.3.1-alt1
- initial build

