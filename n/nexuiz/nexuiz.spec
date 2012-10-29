Name: nexuiz
Version: 2.5.2
Release: alt2

Summary: 3D deathmatch shooter game
License: GPL
Group: Games/Arcade
Url: http://alientrap.org/nexuiz/

Packager: Igor Zubkov <icesik@altlinux.org>

Source0: enginesource20091001.zip

Patch0: nexuiz-2.5.2-watercrash.patch

# Automatically added by buildreq on Mon Oct 29 2012
BuildRequires: libSDL-devel libXext-devel libXpm-devel libXxf86dga-devel libXxf86vm-devel libalsa-devel unzip

%description
Nexuiz is a 3d deathmatch shooter based on a darkplaces engine.

%package client-sdl
Group: Games/Arcade
Summary: Nexuiz SDL client
Requires: %name-client-common = %version-%release
Requires: %name-data = %version

%description client-sdl
Nexuiz is a 3d deathmatch shooter based on a darkplaces engine.
This package contains SDL version of Nexuiz client.

%package client-glx
Group: Games/Arcade
Summary: Nexuiz GLX client
Requires: %name-client-common = %version-%release
Requires: %name-data = %version

%description client-glx
Nexuiz is a 3d deathmatch shooter based on a darkplaces engine.
This package contains GLX version of Nexuiz client.

%package client-common
Group: Games/Arcade
Summary: Nexuiz clients common files

%description client-common
Nexuiz is a 3d deathmatch shooter based on a darkplaces engine.
This package contains clients' common files.

%package server
Group: Games/Arcade
Summary: Nexuiz dedicated server
Requires: %name-data = %version

%description server
Nexuiz is a 3d deathmatch shooter based on a darkplaces engine.
This package contains dedicated server for Nexuiz.

%prep
%setup -q -n darkplaces
%patch0 -p0
sed -i 's/\r//' darkplaces.txt
sed -i 's,/usr/X11R6/,/usr/,g' makefile makefile.inc

%build
export DP_FS_BASEDIR=%_datadir/nexuiz
%make nexuiz OPTIM_RELEASE="%optflags" STRIP=:

%install
mkdir -p %buildroot%_bindir/
mkdir -p %buildroot%_iconsdir/

install -pm755 nexuiz-sdl %buildroot%_bindir/
install -pm755 nexuiz-glx %buildroot%_bindir/
install -pm755 nexuiz-dedicated %buildroot%_bindir/
install -D -pm644 darkplaces16x16.png %buildroot%_iconsdir/hicolor/16x16/apps/nexuiz.png
install -D -pm644 darkplaces24x24.png %buildroot%_iconsdir/hicolor/24x24/apps/nexuiz.png
install -D -pm644 darkplaces32x32.png %buildroot%_iconsdir/hicolor/32x32/apps/nexuiz.png
install -D -pm644 darkplaces48x48.png %buildroot%_iconsdir/hicolor/48x48/apps/nexuiz.png
install -D -pm644 darkplaces64x64.png %buildroot%_iconsdir/hicolor/64x64/apps/nexuiz.png
install -D -pm644 darkplaces72x72.png %buildroot%_iconsdir/hicolor/72x72/apps/nexuiz.png

mkdir -p %buildroot%_desktopdir/

cat > %buildroot%_desktopdir/%name-sdl.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Nexuiz (SDL client)
Comment=3D DeathMatch shooter
Icon=%name
Exec=%_bindir/%name-sdl
Terminal=false
Categories=Game;ActionGame;
EOF

cat > %buildroot%_desktopdir/%name-glx.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Nexuiz (GLX client)
Comment=3D DeathMatch shooter
Icon=%name
Exec=%_bindir/%name-glx
Terminal=false
Categories=Game;ActionGame;
EOF

%files client-glx
%doc darkplaces.txt
%_bindir/nexuiz-glx
%_desktopdir/%name-glx.desktop

%files client-sdl
%doc darkplaces.txt
%_bindir/nexuiz-sdl
%_desktopdir/%name-sdl.desktop

%files server
%doc darkplaces.txt
%_bindir/nexuiz-dedicated

%files client-common
%_iconsdir/*/*/apps/*

%changelog
* Mon Oct 29 2012 Igor Zubkov <icesik@altlinux.org> 2.5.2-alt2
- relocate binaries from /usr/games/ to /usr/bin/
- buildreq
- sync patches with nexuiz-2.5.2-5.fc18
- add debuginfo packages

* Sat Apr 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1.2
- NMU: converted menu to desktop file

* Fri Apr 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.2-alt1.1
- Fixed build

* Sat Dec 12 2009 Igor Zubkov <icesik@altlinux.org> 2.5.2-alt1
- 2.4.2 -> 2.5.2

* Sun Oct 25 2009 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt3.1
- friendly repocop NMU: icon name in menu, pixmap locations.

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 2.4.2-alt3
- buildreq

* Sat Nov 15 2008 Igor Zubkov <icesik@altlinux.org> 2.4.2-alt2
- apply patch from repocop

* Sun May 18 2008 Igor Zubkov <icesik@altlinux.org> 2.4.2-alt1
- 2.4 -> 2.4.2

* Wed Apr 16 2008 Igor Zubkov <icesik@altlinux.org> 2.4-alt3
- relax deps

* Thu Apr 10 2008 Igor Zubkov <icesik@altlinux.org> 2.4-alt2
- run %%update_menus & %%cleanup_menus in proper place's

* Sun Mar 02 2008 Igor Zubkov <icesik@altlinux.org> 2.4-alt1
- 2.3 -> 2.4

* Tue Nov 27 2007 Igor Zubkov <icesik@altlinux.org> 2.3-alt1
- 2.2.3 -> 2.3

* Thu Mar 15 2007 Igor Zubkov <icesik@altlinux.org> 2.2.3-alt1
- 2.0 -> 2.2.3

* Wed Aug 23 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.0-alt1
- 2.0 release.
- specfile cleanup.

* Tue Feb 21 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.5-alt1
- 1.5 release.

* Fri Sep 02 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.2-alt1
- Initial build for Sisyphus.

