# SPEC file for gltron game

%define version 0.70
%define release alt4

Name: gltron
Version: %version
Release: %release

Summary: a 3d lightcycle game using OpenGL
Summary(ru_RU.UTF-8): трехмерная игра с использованием OpenGL

License: GPL
Group: Games/Arcade
URL: http://www.gltron.org/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source:  %name-%version-source.tar.gz
Source1: %name.desktop
Source2: armagetronad-16.png
Source3: armagetronad-32.png
Source4: armagetronad-48.png
Patch0:  %name-0.70-alt-build_warnings_fix.patch

BuildRequires: gcc-c++ libSDL-devel libSDL_sound-devel libsmpeg-devel libmikmod-devel libpng-devel libvorbis-devel

%description
A 3D lightcycle Tron game using OpenGL.

Player controls a  'Light Cycle' which leaves a wall behind
it wherever the  cycle it goes,  turning only at  90 degree 
angles. The player must then get the AI to crash into their 
wall while avoiding hitting the AI's own wall themselves.

%description -l ru_RU.UTF-8
Трехмерная игра Tron с использованием OpenGL.

Игрок управляет "световым мотоциклом", который при движении
оставляет  за собой стену  и может  только поворачивать под 
прямыми углами. Требуется заставить соперников (управляемых 
компьютером) врезаться в стены,  в то же время избегая стен 
самому.


%prep
%setup
%patch0

/bin/mv -f COPYING COPYING.GPL.orig
/bin/ln -s $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
%configure
%make_build  

%install
/bin/mkdir -p %buildroot
%make_install DESTDIR=%buildroot install

/bin/mkdir -p %buildroot%_desktopdir
/bin/install -m 0644 %SOURCE1 %buildroot%_desktopdir

/bin/mkdir -p -- %buildroot%_miconsdir %buildroot%_liconsdir %buildroot%_niconsdir
/bin/install -m0644 -- %SOURCE2 %buildroot%_miconsdir/%name.png
/bin/install -m0644 -- %SOURCE3 %buildroot%_niconsdir/%name.png
/bin/install -m0644 -- %SOURCE4 %buildroot%_liconsdir/%name.png

%files
%doc ChangeLog README
%doc --no-dereference COPYING

%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop

%_miconsdir/%{name}*
%_niconsdir/%{name}*
%_liconsdir/%{name}*


%changelog
* Tue May 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.70-alt4
- fix build

* Fri Dec 12 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.70-alt3
- Removing obsolete %%update_menus calls
- Fix .desktop file to meet standards
- Add pre-scaled icons, fix icons location

* Mon Dec 04 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.70-alt2
- Adding fixes for build with 'warn_unused_result' flag.

* Tue May 23 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.70-alt1
- Revival from orphaned
- New version 0.70
- Icons from Armagetronad project
- Adding desktop file
- Spec file cleanup

* Mon Sep 30 2002 Stanislav Ievlev <inger@altlinux.ru> 0.61-alt1
- 0.61

* Thu Oct 11 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.59-ipl12mdk
- Rebuilt with libpng.so.3

* Fri Aug 17 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.59-ipl11mdk
- Rebuild with new SDL
- Fixed optflags
- Some spec cleanup

* Fri Apr  6 2001 Kostya Timoshenko <kt@altlinux.ru> 0.59-ipl10mdk
- Rebuild with SDL-1.2.0

* Wed Mar 14 2001 Kostya Timoshenko <kt@petr.kz> 0.59-ipl9mdk
- fix BuildPreReq

* Wed Dec 27 2000 Kostya Timoshenko <kt@petr.kz> 0.59-ipl8mdk
- Build for RE

* Sun Dec 17 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 0.59-8mdk
- updated BuildRequires

* Tue Nov 14 2000 Fran�ois Pons <fpons@mandrakesoft.com> 0.59-7mdk
- updated icons transparancy.

* Fri Sep 15 2000 David BAUDENS <baudens@mandrakesoft.com> 0.59-6mdk
- Fix Title in Menu entry

* Thu Sep  7 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.59-5mdk
- use alpha trails by default, to workaround a display bug with some
  3d hardware
- use our compiling flags

* Sun Sep 03 2000 Fran�ois Pons <fpons@mandrakesoft.com> 0.59-4mdk
- using right macros for games.
- added missing icons.

* Tue Aug 29 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.59-3mdk
- added a patch to change default cam type (follows motorcycle)

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.59-2mdk
- automatically added BuildRequires

* Mon Jul 31 2000 Fran�ois Pons <fpons@mandrakesoft.com> 0.59-1mdk
- added menu entry.
- created patch to allow starting even if no sound available.
- initial release.

