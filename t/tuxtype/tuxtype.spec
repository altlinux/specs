%define oname tuxtype_w_fonts
Name: tuxtype
Version: 1.8.1
Release: alt1

Summary: An educational typing tutor game starring Tux

Group: Games/Educational
License: GPLv2
Url: http://tux4kids.alioth.debian.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %oname-%version.tar.gz
Source1: %name-48x48.xpm
Source2: %name-32x32.xpm
Source3: %name-16x16.xpm
Source4: ru.po
Patch1:  %name-fix-install.patch

BuildRequires: libSDL-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libSDL_pango-devel
BuildRequires: librsvg-devel

%description
Educational typing tutor starring Tux, the Linux Penguin. Object of
the game is to catch fish as they drop from the top of the screen.
Each fish has a letter or a word written on it, and Tux eats the fish
by the player pressing the associated key or typing the appropriate
word. Intended to be cute and fun for children learning to type and
spell.

%prep
%setup -q -n %oname-%version
cp %SOURCE4 po/
%patch1 -p2

%build
#%configure --without-sdlpango --without-rsvg --prefix=/usr --exec-prefix=/usr --sysconfdir=/usr/share/tuxtype/etc/ --localstatedir=/usr/share/tuxtype/var/
%configure --localstatedir=%_localstatedir/games --sysconfdir=%_sysconfdir
%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_localstatedir/games/tuxtype

mkdir -p %buildroot%_desktopdir/
cat <<EOF > %buildroot%_desktopdir/%name.desktop
[Desktop Entry]
Name=Tux Typing
Comment=An educational typing tutor game starring Tux
Comment[ru]=Играй и учись печатать
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;Application;
EOF

install -pD -m644 %SOURCE1 %buildroot%_liconsdir/%name.xpm
install -pD -m644 %SOURCE2 %buildroot%_niconsdir/%name.xpm
install -pD -m644 %SOURCE3 %buildroot%_miconsdir/%name.xpm

%find_lang %name
rm -rf %buildroot%_docdir/%name/
rm -rf %buildroot%_prefix/doc/

%files -f %name.lang
%doc README AUTHORS TODO ChangeLog doc/OFL
%_bindir/%name
%_datadir/%name/
%_niconsdir/%name.xpm
%_liconsdir/%name.xpm
%_miconsdir/%name.xpm
%_desktopdir/%name.desktop
%config(noreplace) %_sysconfdir/tuxtype
%attr(0755,root,games) %config(noreplace) %_localstatedir/games/tuxtype

%changelog
* Thu Aug 18 2011 Andrey Cherepanov <cas@altlinux.org> 1.8.1-alt1
- New version 1.8.1 (thanks kostyalamer) (closes: #26071)
- Complete Russian translation

* Wed May 25 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.7.0-alt1.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for tuxtype

* Tue Dec 01 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.7.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for tuxtype
  * postclean-05-filetriggers for spec file

* Fri Jan 02 2009 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- new mainstream, rename package to tuxtype
- cleanup spec, update buildreq

* Thu Jul 05 2007 Vitaly Lipatov <lav@altlinux.ru> 1.5.3-alt3
- enable russian input (hack bug #8535)

* Sun May 27 2007 Vitaly Lipatov <lav@altlinux.ru> 1.5.3-alt2
- cleanup spec, change mantainer
- replace Debian menu with desktop file
- add some checks for SDL errors

* Wed Jul 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.3-alt1
- fixed menu file.

* Tue May 25 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.3-alt0.5
- tuxtype2-1.5.3 from CVS.
- fixed for none-C locale input by Anton Boyarshinov.

* Wed Apr 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.3-alt4
- rebuild with latest directfb.

* Fri Mar 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.3-alt3
- rebuild with new directfb.

* Sun Nov 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.3-alt2
- Rebuilt with new libdirectfb.

* Mon Sep 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu May 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.1-alt4
- Rebuilt (wrong dependence on oldalsa fixed, libSDL requires libalsa2)
- BuildRequires updated.

* Mon Jan 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.1-alt3
- cleanups

* Mon Jan 14 2002 Yuri N. Sedunov <aristarh@altlinux.ru> 1.0.1-alt2
- Some spec cleanups.
- Russian summary and description added.

* Fri Nov 9 2001 Yuri N. Sedunov <aristarh@altlinux.ru> 1.0.1-alt1
- First build for Sisyphus.
