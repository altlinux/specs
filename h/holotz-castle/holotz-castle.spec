Name: holotz-castle
Version: 1.3.14
Release: alt2

%define Sum Holotz's Castle - A puzzle/arcade platform scroller
Summary: %Sum
License: GPLv2+
Group: Games/Arcade
Url: http://www.mainreactor.net/holotzcastle/en/index_en.html
Source0: http://www.mainreactor.net/holotzcastle/download/%name-%version-src.tar.gz
Source10: hc-48x48.png
Source11: hc-32x32.png
Source12: hc-16x16.png
Source20: holotz-castle-editor-48x48.png
Source21: holotz-castle-editor-32x32.png
Source22: holotz-castle-editor-16x16.png
Patch0: holotz-castle-1.3.6-install.patch
Patch1: holotz-castle-1.3.14-compile-fixes.patch
Patch2: holotz-castle-1.3.13-JLib-shared.patch

Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Sat Nov 29 2008
BuildRequires: gcc-c++ libGL-devel libSDL-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel zlib-devel

%package editor
License: GPLv2+
Group: Games/Arcade
Summary: Holotz's Castle level editor
Requires: %name == %version

%package data
License: GPLv2+
Group: Games/Arcade
Summary: Holotz's Castle level editor
Requires: %name == %version
BuildArch: noarch

%package -n libJLib
License: GPLv2+
Summary: Jacob's Library
Group: System/Libraries

%package -n libJLib-devel
License: GPLv2+
Summary: Jacob's Library (develompent environment)
Group: Development/C++
Requires: libJLib == %version

%description
A great mystery is hidden beyond the walls of Holotz's Castle. Will you be
able to help Ybelle and Ludar to escape alive from the castle?

Test your dexterity with this tremendously exciting platform game!

%description editor
This package contains a level editor for Holotz's Castle.

%description data
This package contains a level set for Holotz's Castle.

%description -n libJLib
Jacob's Library is multimedia c++ library created by Juan Carlos Seijo Paerez (aka Jacob) for Holotz Caslte game.

%description -n libJLib-devel
Jacob's Library is multimedia c++ library created by Juan Carlos Seijo Paerez (aka Jacob) for Holotz Caslte game.

This is development environment for programming with JLib.

%prep
%setup -q -n %name-%version-src
%patch0 -p0
%patch1 -p1
%patch2 -p1
sed -i s"|\r\n|\n|g" res/playlist.txt
rm -f res/savedata/empty.txt

%build
%make_build

%install
rm -rf %buildroot
%makeinstall INSTALL_ROOT=%buildroot

install -d -m 755 %buildroot%_mandir/man6/
install -m 644 man/%name.6 %buildroot%_mandir/man6/
install -d -m 755 %buildroot%_liconsdir
install -d -m 755 %buildroot%_miconsdir
install -m 644 %_sourcedir/hc-48x48.png -D %buildroot%_liconsdir/%name.png
install -m 644 %_sourcedir/hc-32x32.png -D %buildroot%_niconsdir/%name.png
install -m 644 %_sourcedir/hc-16x16.png -D %buildroot%_miconsdir/%name.png

mkdir -p %buildroot/%_libdir
install JLib/libJLib.so %buildroot/%_libdir/
( cd JLib; find JLib -type f -name \*.h | cpio -pdvm %buildroot/%_includedir )

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=Holotz's Castle
Comment=%Sum
Exec=%_gamesbindir/%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

#editor
install -m 644 man/%name-editor.6 %buildroot%_mandir/man6/
install -m 644 %_sourcedir/holotz-castle-editor-48x48.png -D %buildroot%_liconsdir/%name-editor.png
install -m 644 %_sourcedir/holotz-castle-editor-32x32.png -D %buildroot%_niconsdir/%name-editor.png
install -m 644 %_sourcedir/holotz-castle-editor-16x16.png -D %buildroot%_miconsdir/%name-editor.png

#editor, xdg
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name-editor.desktop << EOF
[Desktop Entry]
Name=Holotz's Castle Editor
Comment=Level editor for Holotz's Castle
Exec=%_gamesbindir/%name-editor
Icon=%name-editor
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%files
%defattr(644,root,games,755)
%doc LICENSE.txt doc/*
%attr(0755,root,games) %_gamesbindir/%name
%dir %_gamesdatadir/%name
%_mandir/man6/%name.6*
%_liconsdir/%name.png
%_niconsdir/%name.png
%_miconsdir/%name.png
%_desktopdir/%name.desktop

%files editor
%defattr(644,root,games,755)
%doc LICENSE.txt
%attr(0755,root,games) %_gamesbindir/%name-editor
%_gamesdatadir/%name/editor
%_mandir/man6/%name-editor.6*
%_liconsdir/%name-editor.png
%_niconsdir/%name-editor.png
%_miconsdir/%name-editor.png
%_desktopdir/%name-editor.desktop

%files data
%_gamesdatadir/%name/game

%files -n libJLib
%_libdir/libJLib.so*

%files -n libJLib-devel
%dir %_includedir/JLib
%_includedir/JLib/*

%changelog
* Wed Jun 03 2009 Fr. Br. George <george@altlinux.ru> 1.3.14-alt2
- Repocop fixes

* Mon May 25 2009 Fr. Br. George <george@altlinux.ru> 1.3.14-alt1
- Version up
- GCC4.4 build fixup

* Sat Mar 28 2009 Fr. Br. George <george@altlinux.ru> 1.3.13-alt2
- Remove "mandriva" desktop file prefix

* Sat Nov 29 2008 Fr. Br. George <george@altlinux.ru> 1.3.13-alt1
- Version up

* Sat Nov 29 2008 Fr. Br. George <george@altlinux.ru> 1.3.12-alt1
- Initial build from MDK

* Mon Sep 08 2008 Guillaume Bedot <littletux@mandriva.org> 1.3.12-1mdv2009.0
+ Revision: 282547
- Release 1.3.12 (with additional levels already included)
- Rediffed patch1
- Dropped unneeded buildrequires
- Fixed license, and some more cleanup

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Jan 11 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.3.10-1mdv2008.1
+ Revision: 148217
- drop old menu
- kill re-definition of %%buildroot on Pixel's request
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Aug 10 2007 Guillaume Bedot <littletux@mandriva.org> 1.3.10-1mdv2008.0
+ Revision: 61436
- Release 1.3.10

* Wed Apr 18 2007 Guillaume Bedot <littletux@mandriva.org> 1.3.9-1mdv2008.0
+ Revision: 14714
- New release 1.3.9

* Tue Aug 01 2006 Guillaume Bedot <littletux@mandriva.org> 1.3.8-3mdv2007.0
- patch from debian fixing warnings instead of ignoring them and endianess
 (trying to fix bug #24005)

* Mon Jul 31 2006 Guillaume Bedot <littletux@mandriva.org> 1.3.8-2mdv2007.0
- fix menu + xdg

* Wed Mar 15 2006 Guillaume Bedot <littletux@mandriva.org> 1.3.8-1mdk
- 1.3.8

* Sun Jan 22 2006 Nicolas Laecureuil <neoclust@mandriva.org> 1.3.7-2mdk
- Add BuildRequires: MesaGLU-devel

* Mon Nov 28 2005 Guillaume Bedot <littletux@mandriva.org> 1.3.7-1mdk
- New release

* Wed May 18 2005 Guillaume Bedot <littletux@mandriva.org> 1.3.6-2mdk
- Well, a package from David Black aka dblackia already existed in the club...
 the best of both is now kept in this new release, i hope.
- New descriptions, summary, and a additional icon, used for the editor
 new menu entry.
- And finally, the package is split into game and editor packages.

* Tue May 17 2005 Guillaume Bedot <littletux@mandriva.org> 1.3.6-1mdk
- first package for Holotz Castle.

