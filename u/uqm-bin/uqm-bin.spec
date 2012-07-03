%define _unpackaged_files_terminate_build 1

%define rname uqm
%define what bin
Name: %rname-%what
Version: 0.6.2
Release: alt3.1

Group: Games/Adventure
Summary: The Ur-Quan Masters (port of the classic space game StarControl 2).
Url: http://sc2.sourceforge.net
License: GPLv2+

Requires: %rname-content = 0.6.0
Requires: %rname-common = %version
Obsoletes: %rname-game

Source0: %rname-%version.tar

Source10: %rname.16.png
Source11: %rname.32.png
Source12: %rname.48.png

BuildPreReq: libGL-devel libmikmod-devel libopenal-devel libSDL-devel
BuildPreReq: libSDL_image-devel libvorbis-devel zlib-devel

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

%description
The project started in August 2002, when Toys For Bob <http://toysforbob.com/>
released the partially ported sources of Star Control 2 <http://star-control.com>
3DO version to the fan community. Our goal is to port this wonderful game
to current personal computers and operating systems. It is and will remain
100%% free of charge, and anyone can contribute to the project and thus
help make it even better.

This package contains binary executable program for this game.


%prep
%setup -n %rname-%version

%build
export CFLAGS="%optflags" LDFLAGS="%optflags"

cd sc2
./build.sh %rname <<__EOF__
1
1
2
2
3
2
4
2
5
1
10
1
/usr
4
\$prefix/share/games


__EOF__

%install
mkdir -p %buildroot/{%_gamesbindir,%_desktopdir}
mkdir -p %buildroot/%_gamesdatadir/%rname/content/packages/addons
install -m 755 sc2/%rname %buildroot/%_gamesbindir
install -m 644 sc2/content/version %buildroot/%_gamesdatadir/%rname/content/version

cat > %buildroot%_desktopdir/%rname.desktop <<__EOF__
[Desktop Entry]
Version=1.0
Type=Application
Name=The Ur-Quan Masters
Exec=%_gamesbindir/%rname
Icon=%rname
Categories=Game;AdventureGame;
Comment=Port of the classic space game StarControl 2.
__EOF__

cat > %buildroot%_desktopdir/%rname-hires.desktop <<__EOF__
[Desktop Entry]
Version=1.0
Type=Application
Name=The Ur-Quan Masters - High Resolution
Exec=%_gamesbindir/%rname -q high -f -o -c hq -r 1024x768
Icon=%rname
Categories=Game;AdventureGame;
Comment=Port of the classic space game StarControl 2 (high resolution mode).
__EOF__

mkdir -p %buildroot/%_iconsdir/hicolor/{16x16,32x32,48x48}/apps/
install -m 644 %SOURCE10 %buildroot/%_iconsdir/hicolor/16x16/apps/%rname.png
install -m 644 %SOURCE11 %buildroot/%_iconsdir/hicolor/32x32/apps/%rname.png
install -m 644 %SOURCE12 %buildroot/%_iconsdir/hicolor/48x48/apps/%rname.png


%files
%doc sc2/{AUTHORS,BUGS,COPYING,ChangeLog,README,WhatsNew,uqm.lsm}
%doc sc2/doc/users/manual* sc2/doc/devel
%_gamesbindir/%rname
%_gamesdatadir/%rname
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/%rname.png

%changelog
* Tue Mar 02 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.2-alt3.1
- change OpenAL buildreq back to libopenal-devel

* Mon Mar 01 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.2-alt3
- rebuild with libopenal1

* Thu Nov 20 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.2-alt2
- remove update_*/clean_* invocations

* Sat Sep 13 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.2-alt1
- remove menu files, add desktop files (closes: #17115)
- hires menu entry:
  + switch from bilinear to hq scaler
  + use 1024x768 resolution
  + remove uqmremix addon support, as it is plugged in automatically

* Thu Apr 05 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.2-alt0.1
- 0.6.2
- take from orphaned

* Mon May 23 2005 Sergey V Turchin <zerg at altlinux dot org> 0.4.0-alt1
- new version

* Tue Nov 18 2003 Sergey V Turchin <zerg at altlinux dot org> 0.3-alt1
- initial spec
