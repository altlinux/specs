%define _unpackaged_files_terminate_build 1

Name: pingus
Version: 0.7.6
Release: alt3

Summary: A free Lemmings clone
Summary(ru_RU.UTF8): Свободный клон Lemmings
License: GPL
Group: Games/Arcade
Url: http://pingus.seul.org

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: %name-%version.tar
Source1: %name.16.xpm
Source2: %name.32.xpm
Source3: %name.48.xpm
Source4: CMakeLists.txt

Patch8:  pingus-0.7.6-alt-VERSION.patch
Patch9:  pingus-0.7.6-upstream-std-header.patch
Patch10: pingus-0.7.6-upstream-boost-compat.patch

# Automatically added by buildreq on Fri Sep 28 2007
BuildRequires: esound flex gcc-c++ ghostscript-utils libSDL-devel
BuildRequires: libSDL_mixer-devel libSDL_image-devel boost-devel libpng-devel
BuildRequires: libphysfs-devel boost-signals-devel
BuildRequires: cmake

%description
Pingus is a free Lemmings clone covered under the GPL. Pingus uses SDL,
which should make it portable over a lot of operating systems in the future. At
the moment the main target is Linux. It is possible to play Pingus in a X
window or in fullscreen.

%description -l ru_RU.UTF8
Pingus - свободный клон Lemmings, выпускаемый под GPL. Pingus использует
SDL, что должно сделать его портируемым на множество других операционных
систем в будущем. На данный момент главная цель - Linux. В Pingus возможно
играть в X в окне или в полноэкранном режиме.

%prep
%setup
%patch8 -p2
%patch9 -p1
%patch10 -p1

cp %SOURCE4 CMakeLists.txt

%build
%cmake \
	-DWARNINGS:BOOL=ON \
	-DBUILD_EXTRA:BOOL=OFF \
	-DBUILD_TESTS:BOOL=OFF \
	%nil

%cmake_build

%install
%cmakeinstall_std

install -pD -m644 %SOURCE1 %buildroot%_miconsdir/%name.xpm
install -pD -m644 %SOURCE2 %buildroot%_niconsdir/%name.xpm
install -pD -m644 %SOURCE3 %buildroot%_liconsdir/%name.xpm

install -m755 -d %buildroot%_desktopdir/
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Pingus
Comment=Guide the penguins safely home before they drop of the cliff
Exec=pingus
Icon=pingus
Terminal=false
StartupNotify=false
Categories=Game;ArcadeGame;
EOF

# revert to previous run script since just starting application without any parameters doesn't work yet
mv %buildroot%_bindir/%name %buildroot%_bindir/%{name}.bin

cat > %buildroot%_bindir/%name << EOF
#!/bin/sh
exec "%_bindir/%{name}.bin" --datadir "%_datadir/%name"
EOF

chmod +x %buildroot%_bindir/%name

# remove unnecessary files since they just create unnecessary dependencies
rm -f %buildroot%_datadir/%name/images/fonts/buildset.py
rm -f %buildroot%_datadir/%name/images/fonts/substractchars.py
rm -f %buildroot%_datadir/%name/po/extract-levels.guile
rm -f %buildroot%_datadir/%name/po/extract-po.sh
rm -f %buildroot%_datadir/%name/po/pingus.pot
rm -f %buildroot%_datadir/%name/po/update-po.sh

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/%name
%_man6dir/*
%_desktopdir/%{name}.desktop
%_miconsdir/%name.xpm
%_niconsdir/%name.xpm
%_liconsdir/%name.xpm
%_iconsdir/hicolor/scalable/apps/%{name}.svg
%doc AUTHORS NEWS README TODO

%changelog
* Tue Dec 03 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.6-alt3
- Rebuilt with boost-1.71.0 using cmake.
- Spec cleanup.

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.6-alt2.1
- NMU: rebuilt with boost-1.67.0

* Wed May 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.6-alt2
- NMU: fixed build with new toolchain.

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.7.6-alt1.qa9
- NMU: rebuilt with boost 1.57.0 -> 1.58.0.

* Sat Feb 28 2015 Hihin Ruslan <ruslandh@altlinux.ru> 0.7.6-alt1.6.2
- (ALT bug #29733)
 
* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.7.6-alt1.6.1
- rebuild with boost 1.57.0

* Mon Feb 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.6-alt1.6
- Rebuilt with Boost 1.53.0

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.6-alt1.5
- Rebuilt with Boost 1.52.0

* Tue Nov 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.6-alt1.4
- Fixed build

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.6-alt1.3
- Rebuilt with libpng15

* Fri Sep 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.6-alt1.2
- Rebuilt with Boost 1.51.0

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.6-alt1.1
- Rebuilt with Boost 1.49.0

* Mon Dec 26 2011 Ilya Mashkin <oddity@altlinux.ru> 0.7.6-alt1
- New version 0.7.6
- added new 10 xmas themed levels

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.5-alt2.1
- Rebuilt with Boost 1.48.0

* Wed Nov 16 2011 Ilya Mashkin <oddity@altlinux.ru> 0.7.5-alt2
- fix path (thanks to Mykola Grechukh) (Closes: #26582)

* Tue Nov 08 2011 Ilya Mashkin <oddity@altlinux.ru> 0.7.5-alt1
- New version 0.7.5

* Mon Aug 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt3.qa4
- Rebuilt with Boost 1.47.0

* Mon Apr 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.2-alt3.qa3
- NMU: converted menu to desktop file

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt3.2
- Rebuilt with Boost 1.46.1
- Added libssl-devel into BuildPreReq

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.7.2-alt3.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Thu Jul 09 2009 Ilya Mashkin <oddity@altlinux.ru> 0.7.2-alt3
- fix gcc4.4 build

* Tue Nov 04 2008 Ilya Mashkin <oddity@altlinux.ru> 0.7.2-alt2
- fix gcc4.3 build

* Sun Nov 04 2007 Ilya Mashkin <oddity@altlinux.ru> 0.7.2-alt1
- New version 0.7.2

* Fri Sep 28 2007 Ilya Mashkin <oddity@altlinux.ru> 0.7.1-alt1
- New version 0.7.1
- Switch from ClanLib to SDL
- New Level Editor rewritten from scratch
- Spec rewritten

* Thu Dec 28 2006 Ilya Mashkin <oddity@altlinux.ru> 0.7.0-alt0.1cvs20060721
- New version from old cvs

* Wed Apr 12 2006 Andrey Brindeew <abr@altlinux.org> 0.6.0-alt7
- Fix program icon locations

* Sun Feb 20 2005 Andrey Brindeew <abr@altlinux.org> 0.6.0-alt6
- Patched for gcc3.4

* Sat Dec 04 2004 Andrey Brindeew <abr@altlinux.org> 0.6.0-alt5
- fixed broken symlink (#5618)

* Wed May 12 2004 Andrey Brindeew <abr@altlinux.ru> 0.6.0-alt4
- Dependency on gcc3.2 was removed
- Patched for gcc3.3 (thanks to Alexey Voinov)

* Sun Feb 29 2004 Andrey Brindeew <abr@altlinux.ru> 0.6.0-alt3
- Dependency on gcc3.2 added

* Mon Nov 24 2003 Andrey Brindeew <abr@altlinux.ru> 0.6.0-alt2
- Requires updated

* Tue Oct  7 2003 Andrey Brindeew <abr@altlinux.ru> 0.6.0-alt1
- 0.6.0
- Packager tag was added
- Summary was updated & translated to Russian

* Mon Oct 28 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.5.0-alt0.4pre3
- Rebuilt in new environment

* Thu Jan 23 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.5.0-alt0.3pre3
- 0.5.0pre3
- Rebuilded with clanlib 0.6.3
- Manually run autogen's apps

* Wed Jan 23 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.5.0-alt0.3pre2
- Rebuilded with clanlib 0.5.4

* Tue Nov 28 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.5.0-alt0.2pre2
- Rebuilded with clanlib 0.5.1
- Added music
- Added some Mandrake patches

* Thu Aug 30 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.5.0-alt0.1pre2
- Specfile minor cleanup.

* Wed Aug 29 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.5.0pre2-alt1
- 0.5.0pre2
- Rebuilt with new clanlib
- Some spec cleanup

* Fri Aug 17 2001 Stanislav Ievlev <inger@altlinux.ru> 0.4.0-ipl15mdk
- Rebuilt with new libSDL.

* Fri Apr  6 2001 Kostya Timoshenko <kt@altlinux.ru> 0.4.0-ipl14mdk
- will try not to crash when dsp is busy and user asked for sound/music
- use no-omit-frame-pointer to workaround g++ exceptions bug

* Wed Mar 14 2001 Kostya Timoshenko <kt@petr.kz> 0.4.0-ipl13mdk
- fix BuildPreReq

* Wed Feb 21 2001 Kostya Timoshenko <kt@petr.kz> 0.4.0-ipl12mdk
- add 48x48 icon
- fix requires on launch_x11_clanapp

* Wed Jan 31 2001 Kostya Timoshenko <kt@petr.kz> 0.4.0-ipl11mdk
- fix hermes-devel -> libhermes-devel in BuildPreReq.

* Wed Dec 27 2000 Kostya Timoshenko <kt@petr.kz>
- Build for RE

* Wed Dec 20 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.0-10mdk
- rebuild against new SDL_mixer

* Wed Nov 29 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.0-9mdk
- rebuild to follow new lib policy of clanlib and SDL_mixer
- can build with full opts now that gcc-2.96 does not suck anymore

* Fri Nov  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.0-8mdk
- recompile against newest libstdc++
- fix compile with gcc-2.96 by downgrading optimization to -O1
- against lowercased hermes and clanlib

* Tue Oct 17 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.0-7mdk
- use autoconf to get the gcc-2.96 fix in the configure script

* Wed Sep 13 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.0-6mdk
- fix sound and music

* Wed Sep  6 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.0-5mdk
- menu: now launches automatically the x11 target

* Wed Aug 30 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.0-4mdk
- fixed missing install_info

* Wed Aug 23 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.0-3mdk
- automatically added packager tag

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.4.0-2mdk
- automatically added BuildRequires

* Tue Aug  1 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.0-1mdk
- took SRPM from Pingus website
- adapted to mdk
- took the `stable' 0.4.0 out of the CVS version with the help of
  Ingo Ruhnke <grumbel@gmx.de>
- fixed the not working resource files with the help of Ingo
- fixed behaviour when not config file (patch sourcecode)
- removed the buggy themes files (made pingus segfaulting)
- menu entry

* Fri Feb 18 2000 David Philippi <david@torangan.saar.de>
- Update to version 0.3.1

* Sun Dec 26 1999 David Philippi <david@torangan.saar.de>
- Fixed again the "install-info" bug

* Sun Dec 26 1999 David Philippi <david@torangan.saar.de>
- Fixed an old bug that prevented rpm from finding the provides

* Sun Dec 26 1999 David Philippi <david@torangan.saar.de>
- Update to version 0.3.0a

* Tue Nov 09 1999 David Philippi <david@torangan.saar.de>
- Update to version 0.2.4

* Fri Oct 08 1999 David Philippi <david@torangan.saar.de>
- Fixed a bug which caused rpm to generate a file /usr/info/dir

* Sun Oct 03 1999 David Philippi <david@torangan.saar.de>
- Update to version 0.2.3

* Sat Sep 18 1999 David Philippi <david@torangan.saar.de>
- Update to version 0.2.2

* Tue Jul 13 1999 Klaus Knopper <klaus@knopper.net>
- First RPMified pingus
