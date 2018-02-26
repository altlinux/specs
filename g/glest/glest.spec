Name: glest
Version: 3.1.2
Release: alt3

Summary: Glest is a project for making a free 3d real-time customizable strategy game
Group: Games/Strategy
License: GPL
Packager: Damir Shayhutdinov <damir@altlinux.ru>
Url: http://www.glest.org

Source: %name-source-%version.tar.bz2
Source2: %name.sh
Source3: %name.ini
Source4: %name.png
Source5: %name.desktop

Patch1: glest-2.0.0-logfile.patch
Patch2: glest-3.1.2-debian-gcc-4.3-fixes.patch

# Automatically added by buildreq on Sun Mar 14 2010
BuildRequires: gcc-c++ imake jam libGL-devel libSDL-devel libX11-devel libopenal-devel libvorbis-devel libxerces-c28-devel xorg-cf-files

Requires: %name-data = %version
Requires: fonts-bitmap-terminus

%description
Glest is a project for making a free 3d real-time customizable strategy
game. Current version is fully playable, includes single player game
against CPU controlled players, two factions with their corresponding
tech trees, units, buildings and some maps.

%prep
%setup  -n %name-source-%version
%patch1 -p2
%patch2 -p1

%build
%configure --disable-debug --enable-optimize

jam -j%__nprocs

%install
# let's create directory structure...
mkdir -p %buildroot{%_gamesdatadir/%name,%_gamesbindir,%_docdir/%name-%version,%_iconsdir,%_desktopdir}

# and install what we need where we need it to be...
install -pm755 glest %buildroot%_gamesbindir/glest-bin
install -pm644 %SOURCE3 %buildroot%_gamesdatadir/%name/glest.ini
install -pm755 %SOURCE2 %buildroot%_gamesbindir/glest

install -pm 644 README README.linux license.txt %buildroot%_docdir/%name-%version/
install -pm 644 %SOURCE4 %buildroot%_iconsdir/%name.png
install -pm 644 %SOURCE5 %buildroot%_desktopdir/%name.desktop

%files
%_docdir/%name-%version
%_gamesdatadir/%name
%_gamesbindir/*
%_iconsdir/%name.png
%_desktopdir/%name.desktop

%changelog
* Sun Mar 14 2010 Andrew Clark <andyc@altlinux.org> 3.1.2-alt3
- spec cleanup
- buildreq

* Thu Nov 20 2008 Damir Shayhutdinov <damir@altlinux.ru> 3.1.2-alt2
- Fixed build with gcc4.3 (patch from debian)

* Sun Aug 31 2008 Damir Shayhutdinov <damir@altlinux.ru> 3.1.2-alt1
- New version

* Tue Jan 30 2007 Damir Shayhutdinov <damir@altlinux.ru> 2.0.0-alt3
- Changed default fonts to terminus (#10677)
- Added requires for terminus font

* Sat Dec 02 2006 Damir Shayhutdinov <damir@altlinux.ru> 2.0.0-alt2
- Added desktop file
- Enabled unicode

* Thu Nov 30 2006 Damir Shayhutdinov <damir@altlinux.ru> 2.0.0-alt1
- Resurrected from orphaned.
- 2.0.0 version.

* Mon Sep 19 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.1.0-alt1
- Initial build for Sisyphus.
- Based on custom build by Denis Klykvin (nikon@).

