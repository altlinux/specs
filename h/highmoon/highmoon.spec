Name:		highmoon
Version: 	1.2.4
Release:	alt2.qa1
Summary:	Artillery/Worms-like Game in Open Space
Source0:	http://highmoon.gerdsmeier.net/%name-%version.tar.gz
Patch1:		%name-1.2.3-mdkconf.patch.bz2
Url:		http://highmoon.gerdsmeier.net/
Group:		Games/Arcade
License:	GPL
Packager:	Fr. Br. George <george@altlinux.ru>
# Automatically added by buildreq on Sat Mar 14 2009
BuildRequires: gcc-c++ libSDL-devel libSDL_image-devel

BuildRequires:	ImageMagick

%description
HighMoon is an Artillery/Worms-like duel game in which two spaceships fight
each other in open space. All shots are deflected by the gravitation of
planets and moons, so be careful not to destroy your own UFO.

%prep
%setup -q -n HighMoon
%patch1 -b .mdkconf
find -type f| xargs chmod 644

%build
%make_build	OPTFLAGS="$RPM_OPT_FLAGS -O3" \
	INSTALLPATH="%_gamesdatadir/%name" \
	INSTALLBIN="%_gamesbindir"

%install
make	INSTALLPATH="%buildroot%_gamesdatadir/%name" \
	INSTALLBIN="%buildroot%_gamesbindir" \
	install
mv %buildroot%_gamesdatadir/%name/ufo %buildroot%_gamesbindir/%name.ufo
cat<<EOF > %buildroot%_gamesbindir/%name
#!/bin/sh
cd %_gamesdatadir/%name
\$0.ufo \$@
EOF
chmod 755 %buildroot%_gamesbindir/%name

mkdir -p %buildroot%_datadir/applications/
cat << EOF > %buildroot%_datadir/applications/%name.desktop
[Desktop Entry]
Type=Application
Exec=%_gamesbindir/%name
Icon=%name
Categories=Game;ActionGame;
Name=HighMoon
Comment=%summary
EOF

install -d %buildroot{%_niconsdir,%_miconsdir,%_liconsdir}
install -D icon.png %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
convert -size 16x16 icon.png %buildroot%_miconsdir/%name.png
convert -size 32x32 icon.png %buildroot%_niconsdir/%name.png
convert -size 48x48 icon.png %buildroot%_liconsdir/%name.png

%files
%doc AUTHORS NEWS README

%_gamesbindir/%{name}*
%dir %_gamesdatadir/%name
%dir %_gamesdatadir/%name/gfx
%_gamesdatadir/%name/gfx/*
%dir %_gamesdatadir/%name/snd
%_gamesdatadir/%name/snd/*
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_iconsdir/hicolor/64x64/apps/%name.png
%_datadir/applications/%name.desktop

%changelog
* Tue Nov 17 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.4-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for highmoon
  * postclean-05-filetriggers for spec file

* Sat Mar 28 2009 Fr. Br. George <george@altlinux.ru> 1.2.4-alt2
- Remove "mandriva" desktop file prefix

* Sat Mar 14 2009 Fr. Br. George <george@altlinux.ru> 1.2.4-alt1
- Initial build from MDV

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2.4-3mdv2009.0
+ Revision: 246860
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jan 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2.4-1mdv2008.1
+ Revision: 141863
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- import highmoon

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Jérôme Soyer <saispo@mandriva.org>
    - New release

* Thu Feb 16 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.2.3-1mdk
- initial release based on suse package
