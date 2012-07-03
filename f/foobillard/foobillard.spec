%define title FooBillard
%define beta %nil

Name: foobillard
Version: 3.0a
Release: alt1

Summary: A game of playing billard
License: GPL
Group: Games/Boards

Url: http://foobillard.sunsite.dk/
Source0: %name-%{version}%beta.tar.bz2
Source1: %name
Source3: %name.16.xpm
Source4: %name.32.xpm
Source5: %name.48.xpm
Patch0: foobillard-makefile.patch
Patch1: foobillard-datadir.patch
Patch2: foobillard-3.0a-alt-makefile.patch
# MDK
Patch10: foobillard-3.0-really-disable-nvidia.patch
Packager: Michael Shigorin <mike@altlinux.org>

Requires: sound_handler

# Automatically added by buildreq on Thu May 15 2008 (-bi)
BuildRequires: gcc-c++ imake libSDL-devel libXaw-devel libfreetype-devel libpng-devel xorg-cf-files

BuildRequires: xorg-x11-libs freetype2-devel gcc-c++ libGLU-devel libXi-devel
BuildRequires: libSDL-devel libpng-devel xpm zlib-devel

%description
FooBillard is an attempt to create a free OpenGL-billard for Linux.
The game is still under development but the main physics is implemented.
If you are a billard-pro and you're missing some physics, please tell me.

%prep
%setup -n %name-%version%beta
%patch2 -p1
%patch10 -p1
sed -i 's,LDFLAGS=\(.*\)\$LDFLAGS\(.*\(LIBS\|-l\).*\),LIBS=\1$LIBS\2,' configure.*

%build
%{expand:%%add_optflags %%optflags_kernel %%optflags_notraceback}

%autoreconf
%configure \
    --bindir=%_gamesbindir \
    --datadir=%_gamesdatadir \
    --enable-dependency-tracking \
    --enable-SDL \
    --enable-sound \
    --enable-nvidia=no

%make_build

%install
%makeinstall bindir=%buildroot/%_gamesbindir datadir=%buildroot/%_gamesdatadir

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=%title
Comment=Free OpenGL-billard
Icon=%name
Exec=sound_wrapper.sh %_gamesbindir/%name
Terminal=false
Categories=Game;SportsGame;
EOF

mkdir -p %buildroot/%_iconsdir/hicolor/{16x16,32x32,48x48}/apps/
install -pm0644 %SOURCE3 %buildroot/%_iconsdir/hicolor/16x16/apps/%name.xpm
install -pm0644 %SOURCE4 %buildroot/%_iconsdir/hicolor/32x32/apps/%name.xpm
install -pm0644 %SOURCE5 %buildroot/%_iconsdir/hicolor/48x48/apps/%name.xpm

%files
%doc AUTHORS INSTALL NEWS README ChangeLog TODO README.FONTS foobillardrc.example
%_gamesbindir/*
%_gamesdatadir/%name
%_iconsdir/*/*/apps/%name.xpm
%_desktopdir/%{name}.desktop

%changelog
* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 3.0a-alt1
- fix versioning (it was 3.0a already, just abusing beta macro)

* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 3.0-alt4.a.qa2
- NMU: converted menu to desktop file

* Tue Apr 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0-alt4.a.1
- fix build

* Wed Dec 03 2008 Michael Shigorin <mike@altlinux.org> 3.0-alt4.a
- applied repocop patch

* Thu May 15 2008 Michael Shigorin <mike@altlinux.org> 3.0-alt3.a
- buildreq
- minor spec cleanup

* Mon Jan 01 2007 Michael Shigorin <mike@altlinux.org> 3.0-alt2.a
- argh, spec cleanup (mainly for gcc2.96 BRs)
- Happy New Year!

* Sun Dec 31 2006 Michael Shigorin <mike@altlinux.org> 3.0-alt2.a
- fixed build (with gcc4)

* Tue Jun 29 2004 Sergey V Turchin <zerg at altlinux dot org> 3.0-alt1.a
- new version
- fix menu section

* Thu Nov 20 2003 Sergey V Turchin <zerg at altlinux dot org> 2.9-alt1
- new version

* Mon Jul 07 2003 Sergey V Turchin <zerg at altlinux dot org> 2.8-alt1
- new version

* Fri Jun 06 2003 Sergey V Turchin <zerg at altlinux dot org> 2.6-alt1
- new version

* Thu Apr 03 2003 Sergey V Turchin <zerg@altlinux.ru> 2.5-alt1
- new version

* Wed Jan 22 2003 Sergey V Turchin <zerg@altlinux.ru> 2.4-alt1
- new version

* Thu Dec 19 2002 Sergey V Turchin <zerg@altlinux.ru> 2.2-alt2
- rebuild with gcc2.96

* Thu Dec 19 2002 Sergey V Turchin <zerg@altlinux.ru> 2.2-alt1
- new version

* Thu Dec 05 2002 Sergey V Turchin <zerg@altlinux.ru> 2.0-alt1
- new version

* Wed Oct 23 2002 Sergey V Turchin <zerg@altlinux.ru> 1.8-alt1
- new version
- build with gcc3.2

* Tue Aug 06 2002 Sergey V Turchin <zerg@altlinux.ru> 1.6-alt1
- new version

* Wed May 29 2002 Sergey V Turchin <zerg@altlinux.ru> 1.5-alt1
- new version
- thanx Vyacheslav Dikonov <slava@altlinux.ru>
  for spec translation

* Sat May 18 2002 Sergey V Turchin <zerg@altlinux.ru> 1.4-alt1
- new version
- build with SDL

* Mon Apr 08 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0-alt1
- new version 

* Wed Mar 27 2002 Sergey V Turchin <zerg@altlinux.ru> 0.9-alt1
- new version 

* Mon Mar 11 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.8-alt1
- First build for Sisyphus
