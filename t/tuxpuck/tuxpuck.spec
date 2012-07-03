Name: tuxpuck
Version: 0.8.2
Release: alt1.qa2

Group: Games/Arcade
Summary: Clone of ShufflePuck Cafe historical game
Url: http://www.efd.lth.se/~d00jkr/tuxpuck/
License: GPL

Requires: sound_handler

Source0: %name-%version.tar.gz
Source1: tuxpuck16.png
Source2: tuxpuck32.png
Source3: tuxpuck48.png
Patch0: tuxpuck-0.30-fix-includes.patch
Patch1: tuxpuck-0.7.116-fullscreen.patch
Patch3:         tuxpuck-0.8.2-mandest.patch
Patch4:         tuxpuck-0.8.2-utils-werror.patch

# Author: d00jkr@efd.lth.se

# Automatically added by buildreq on Tue Sep 17 2002
#BuildRequires: XFree86-libs aalib esound freetype2-devel libSDL-devel libSDL_net-devel libalsa2 libarts libaudiofile libjpeg-devel libogg-devel libpng-devel libslang libvorbis-devel zlib-devel

BuildRequires: aalib esound freetype2-devel
BuildRequires: libSDL-devel libSDL_net-devel libalsa2
BuildRequires: libaudiofile libjpeg-devel libogg-devel
BuildRequires: libpng-devel libslang libvorbis-devel zlib-devel

%description
Anyone remember "Shufflepuck Cafe" for the Amiga/AtariST ?

%prep
%setup -q
#%patch0 -p0
%patch1 -p1
%patch3 -p0 -z .mandest
%patch4 -p0 -z .utils-werror

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" make

%install
#%%make DESTDIR=%buildroot install
mkdir -p $RPM_BUILD_ROOT%_gamesbindir
install -m755 tuxpuck $RPM_BUILD_ROOT%_gamesbindir
mkdir -p $RPM_BUILD_ROOT%_man6dir
install -m755 man/* $RPM_BUILD_ROOT%_man6dir

mkdir -p %buildroot/%_iconsdir/hicolor/{16x16,32x32,48x48}/apps
install -m 644 %SOURCE1 %buildroot/%_iconsdir/hicolor/16x16/apps/%name.png
install -m 644 %SOURCE2 %buildroot/%_iconsdir/hicolor/32x32/apps/%name.png
install -m 644 %SOURCE3 %buildroot/%_iconsdir/hicolor/48x48/apps/%name.png

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Tuxpuck
Comment=Clone of ShufflePuck Cafe
Icon=%{name}
Exec=sound_wrapper.sh %name
#Exec=%name
Terminal=false
Categories=Game;ArcadeGame;
EOF

%files
%doc *.txt
%_man6dir/*
%_gamesbindir/*
%_desktopdir/%{name}.desktop
%_iconsdir/*/*/*/*.png

%changelog
* Thu Apr 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.2-alt1.qa2
- NMU: converted debian menu to freedesktop

* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.8.2-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for tuxpuck
  * postclean-05-filetriggers for spec file

* Sun Oct 19 2008 Ilya Mashkin <oddity@altlinux.ru> 0.8.2-alt1.1
- resurrect from orphaned

* Tue Aug 17 2004 Sergey V Turchin <zerg at altlinux dot org> 0.8.2-alt1
- new version
- add menu icons

* Mon Nov 04 2002 Sergey V Turchin <zerg@altlinux.ru> 0.8.1-alt1
- new version

* Fri Sep 20 2002 Sergey V Turchin <zerg@altlinux.ru> 0.7.118-alt1
- new version

* Tue Sep 17 2002 Sergey V Turchin <zerg@altlinux.ru> 0.7.116-alt1
- new version
- build with gcc3.2

* Wed Jul 31 2002 Sergey V Turchin <zerg@altlinux.ru> 0.7.8-alt2
- rebuild against new vorbis

* Thu Feb 21 2002 Sergey V Turchin <zerg@altlinux.ru> 0.7.8-alt1
- new version

* Tue Jan 29 2002 Sergey V Turchin <zerg@altlinux.ru> 0.7.7-alt1
- new version

* Mon Jan 21 2002 Sergey V Turchin <zerg@altlinux.ru> 0.7.4-alt1
- new version

* Wed Jan 09 2002 Sergey V Turchin <zerg@altlinux.ru> 0.6.1-alt1
- new version

* Tue Jan 08 2002 Sergey V Turchin <zerg@altlinux.ru> 0.6.0-alt1
- new version

* Tue Jan 08 2002 Sergey V Turchin <zerg@altlinux.ru> 0.5.17-alt1
- new version

* Thu Jan 03 2002 Sergey V Turchin <zerg@altlinux.ru> 0.5.10-alt1
- new version

* Sat Dec 29 2001 Sergey V Turchin <zerg@altlinux.ru> 0.5.9-alt1
- build for ALT

* Thu Dec 20 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.30-1mdk
- first mdk package
