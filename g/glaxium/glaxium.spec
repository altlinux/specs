Name: glaxium
Version: 0.5
Release: alt6.1.qa3

Group: Games/Arcade
Summary: OpenGL-based space-ship "shoot-em-up"
License: GPLv2
Url: http://xhosxe.free.fr/glaxium/
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: %{name}_%version.tar.gz
Source1: glaxuim.16.png
Source2: glaxuim.32.png
Source3: glaxuim.48.png

Patch1: glaxium_0.5_gl.patch
Patch2: glaxium_0.5_fix_stencil.patch
Patch3: glaxium-0.5-gcc41.patch
Patch4: glaxium-0.5-glut_initialisation.patch
Patch5: glaxium-0.5-alt-src-crash_fix.patch
Patch6: glaxium-0.5-alt-DSO.patch

# due to desktop file
Requires: /usr/bin/sound_wrapper

# Automatically added by buildreq on Tue Jun 10 2003
BuildRequires: libX11-devel libXmu-devel libXi-devel aalib gcc-c++ libGLU-devel libSDL-devel libSDL_mixer-devel libalsa-devel libaudiofile-devel libglut-devel libogg-devel libpng-devel libslang-devel libsmpeg-devel libvorbis-devel zlib-devel

%description
Glaxium is an OpenGL-based space-ship "shoot-em-up" styled game.
It is designed to provide the same feel as the old 2D games of that
type, but with 3D for the special effects.

%prep
%setup -n %{name}_%version
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1
%patch5 -p2
%patch6 -p2

%build
%configure
%make_build

%install
install -pD -m755 %name %buildroot%_bindir/%name

mkdir -p %buildroot%_datadir/games/%name/{textures,samples}
install -p -m644 textures/* %buildroot%_datadir/games/%name/textures/
install -p -m644 samples/* %buildroot%_datadir/games/%name/samples/

# Menu entry
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Glaxium
Comment=OpenGL-based space-ship shoot-em-up
Icon=%{name}
#Exec=%_gamesbindir/%name
Exec=sound_wrapper %name
Terminal=false
Categories=Game;ArcadeGame;
EOF

install -D -m 644 %SOURCE1 %buildroot%_miconsdir/%name.png
install -D -m 644 %SOURCE2 %buildroot%_niconsdir/%name.png
install -D -m 644 %SOURCE3 %buildroot%_liconsdir/%name.png

mkdir -p %buildroot%_man6dir/

install -pD -m644 %name.6 %buildroot%_man6dir

%files
%_bindir/*
%_man6dir/*
%_miconsdir/*.png
%_niconsdir/*.png
%_liconsdir/*.png
%_desktopdir/%{name}.desktop
%_datadir/games/%name
%doc CHANGES* README*

%changelog
* Thu Jun 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt6.1.qa3
- Fixed build

* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 0.5-alt6.1.qa2
- NMU: converted menu to desktop file
- NMU: fixed build

* Tue Nov 17 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.5-alt6.1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for glaxium
  * postclean-05-filetriggers for spec file

* Tue Jun 23 2009 Slava Semushin <php-coder@altlinux.ru> 0.5-alt6.1
- NMU
- Rebuild with libpng
- Removed obsolete %%update_menus/%%clean_menus calls

* Sun Aug 17 2008 Slava Semushin <php-coder@altlinux.ru> 0.5-alt6
- NMU
- Fixed segmentaton fault at game start (Closes: #12085)
- Fixed possible buffer overflow
- Build with gcc4.1 (instead of 3.4)
- Spec cleanup

* Sat Dec 22 2007 Ilya Mashkin <oddity at altlinux dot ru> 0.5-alt5
- ReBuild with GCC-3.4
- Fix bug with not initialising Glut
- Add glaxium-0.5-gcc41.patch (but disabled now)
- Add glaxium-0.5-glut_initialisation.patch
- fixed #12085
- add man glaxium

* Wed Jan 03 2007 Ilya Mashkin <oddity at altlinux dot ru> 0.5-alt4
- Rebuild, fix spec

* Fri Aug 26 2005 Sergey V Turchin <zerg at altlinux dot org> 0.5-alt3
- Rebuilt with gcc2.96

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.5-alt2.1
- Rebuilt with libstdc++.so.6.

* Mon Jun 16 2003 Sergey V Turchin <zerg at altlinux dot org> 0.5-alt2
- fix menu

* Tue Jun 10 2003 Sergey V Turchin <zerg at altlinux dot org> 0.5-alt1
- new version

* Mon Oct 15 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.3d-alt2
- Specfile cleanup.
- Rebuilt with libpng.so.3

* Fri Jul 27 2001 Sergey V Turchin <zerg@altlinux.ru> 0.3d-alt1
- ALT adaptions.

* Wed Jul 18 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.3d-1mdk
- updated to 0.3d

* Fri Mar 30 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.3b-2mdk
- use no-omit-frame-pointer to workaround g++ exceptions bug

* Mon Mar 26 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.3b-1mdk
- updated to 0.3b

* Tue Mar 06 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.3a-1mdk
- upated to 0.3a

* Wed Feb 28 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.3-1mdk
- new in contribs
