# vim:set ft=spec: -*- rpm-spec -*-
Name: briquolo
Version: 0.5.7
Release: alt5

Group: Games/Arcade
Summary: OpenGL-based 3D breakout
Summary(ru_RU.UTF-8): Трёхмерный арканоид использующий OpenGL
Summary(be_BY.UTF-8): Трохмерны арканоід, які карыстае OpenGL
License: GPL
Url: http://briquolo.free.fr
Packager: Gleb Stiblo <ulfr@altlinux.ru>

Source: %name-%version.tar
Source1: briquolo.16.png
Source2: briquolo.32.png
Source3: briquolo.48.png
Patch01: briquolo-0.5.7-strncmp.patch

# Automatically added by buildreq on Thu Sep 04 2008
BuildRequires: gcc-c++ imake libSDL_sound-devel libSDL_mixer-devel libSDL_ttf-devel libX11-devel libfreetype-devel libpng-devel xorg-cf-files

%description
BRIQUOLO is a breakout with 3D representation based on OpenGL.

%description -l ru_RU.UTF-8
BRIQUOLO это трёхмерный арканоид. Кубики и бита находятся в бассейне
с водой. Виды от первого и третьего лица, бонусы, различные виды
кубиков, трёхмерная графика делают игру достаточно интересной и
привлекательной.

%description -l be_BY.UTF-8
BRIQUOLO гэта трохмерны арканоід. Цагліны і біта знаходзяцца ў басэйне
з вадой. Віды ад першага і трэцяга ліку, бонусы, розныя тыпы цэглы,
трохмерная графіка робяць гульню дастаткова цікавай і прывабнай.

%prep
%setup
%patch01 -p1

%build
%configure --bindir=%_gamesbindir --datadir=%_gamesdatadir
%make_build

%install
mkdir -p %buildroot%_gamesdatadir/applications
%makeinstall_std
mv %buildroot/%_gamesdatadir/locale %buildroot%_datadir/
rm -rf %buildroot%_gamesdatadir/applications
rm -rf %buildroot%buildroot

mkdir -p %buildroot/{%_miconsdir,%_liconsdir,%_niconsdir,%_pixmapsdir,%_desktopdir}
cat > %buildroot/%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Name=Briquolo
GenericName=BreakOut
Comment=An OpenGL breakout

Type=Application
Categories=ArcadeGame;Game;

TryExec=briquolo
Exec=briquolo

Icon=briquolo
Terminal=false
EOF

install -m 644 %SOURCE1 %buildroot/%_miconsdir/%name.png
install -m 644 %SOURCE2 %buildroot/%_niconsdir/%name.png
install -m 644 %SOURCE3 %buildroot/%_liconsdir/%name.png
install -m 644 %SOURCE3 %buildroot/%_pixmapsdir/%name.png
%find_lang %name

%files -f %name.lang
%_desktopdir/%name.desktop
%_gamesbindir/%name
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_gamesdatadir/%name
%_pixmapsdir/%name.png
%doc README*

%changelog
* Sun Apr 17 2011 Lenar Shakirov <snejok@altlinux.ru> 0.5.7-alt5
- fixed build: libmesa-devel removed from BuildReqs
- Spec cleaned: thanks to rpmcs!

* Fri Nov 28 2008 Gleb Stiblo <ulfr@altlinux.ru> 0.5.7-alt4
- gcc 4.3 fixes

* Fri Nov 28 2008 Gleb Stiblo <ulfr@altlinux.ru> 0.5.7-alt3
- removed deprecated posts

* Fri Sep 05 2008 Gleb Stiblo <ulfr@altlinux.ru> 0.5.7-alt2
- some repocop errors fixed

* Thu Sep 04 2008 Gleb Stiblo <ulfR@altlinux.ru> 0.5.7-alt1
- new version
- some repocop errors fixed
- builddeps fixed

* Thu May 24 2007 Gleb Stiblo <ulfR@altlinux.ru> 0.5.6-alt1
- new translations and minor fixes

* Mon May 15 2006 Gleb Stiblo <ulfR@altlinux.ru> 0.5.5-alt1
- new upstream version

* Sun Aug 28 2005 Gleb Stiblo <ulfR@altlinux.ru> 0.5.4-alt1
- new upstream version

* Sat May 14 2005 Gleb Stiblo <ulfR@altlinux.ru> 0.5.3-alt1
- new translations
- icon and menu file

* Wed Mar 02 2005 Gleb Stiblo <ulfR@altlinux.ru> 0.5.2-alt1
- new version
- russian and belarussian translation

* Wed Feb 02 2005 Gleb Stiblo <ulfR@altlinux.ru> 0.5.1-alt1
- fixes

* Mon Dec 13 2004 Gleb Stiblo <ulfR@altlinux.ru> 0.5-alt1
- 5682 fixed
- new version

* Tue Aug 03 2004 Gleb Stiblo <ulfR@altlinux.ru> 0.4.2-alt4
- russian and belorussian summary/description

* Mon May 10 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.4.2-alt3
- glibc 2.3
- summary fixed

* Mon Feb 02 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.4.2-alt2
- binary file moved to games
- fr, nl locales added
- spec cleanup

* Mon Jan 26 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.4.2-alt1
- ALT adaptions.

