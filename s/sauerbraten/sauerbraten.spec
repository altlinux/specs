%define rev svn3956
%define origname sauerbraten_2010_07_21_justice_edition_linux
Name: sauerbraten
Version: 20100721
Release: alt1.%rev
Summary: Sauerbraten is a free multiplayer/singleplayer FPS

Group: Games/Arcade
License: Zlib
Packager: Andrew Clark <andyc@altlinux.org>
Url: http://sauerbraten.org/
Source: http://downloads.sourceforge.net/sauerbraten/%origname.tar.bz2
Source1: sauerbraten_client.sh
Source2: sauerbraten_server.sh
Source3: %name.desktop
Source4: %name.png

# Automatically added by buildreq on Sun Oct 10 2010
BuildRequires: gcc-c++ libGL-devel libSDL_image-devel libSDL_mixer-devel libX11-devel zlib-devel

Requires: %name-data = %version

%description
Cube 2: Sauerbraten is a free multiplayer/singleplayer first person
shooter, built as a major redesign of the Cube FPS.

%prep
%setup -q -n %name

%build
%make_build -C src/ CFLAGS="%optflags" CXXOPTFLAGS="%optflags"

%install
mkdir -p %buildroot%_bindir
install -pD -m 755 %SOURCE1 %buildroot%_bindir/sauerbraten_client
install -pD -m 755 %SOURCE2 %buildroot%_bindir/sauerbraten_server

mkdir -p %buildroot%_desktopdir
install -pD -m 644 %SOURCE3 %buildroot%_desktopdir/%name.desktop

mkdir -p %buildroot%_liconsdir
install -pD -m 644 %SOURCE4 %buildroot%_liconsdir/%name.png

mkdir -p %buildroot%_docdir/%name/
mkdir -p %buildroot%_gamesdatadir/%name/
mv %_builddir/%name/src/sauer_client %buildroot%_bindir/
mv %_builddir/%name/src/sauer_server %buildroot%_bindir/
mv %_builddir/%name/docs %buildroot/%_docdir/%name/
mv %_builddir/%name/README.html %buildroot/%_docdir/%name/
mv %_builddir/%name/server-init.cfg %buildroot/%_gamesdatadir/%name/

%files
%_bindir/*
%_docdir/%name
%_desktopdir/*
%_liconsdir/*.png
%_gamesdatadir/%name/server-init.cfg

%changelog
* Fri Jan 6 2012 Andrew Clark <andyc@altlinux.org> 20100721-alt1.svn3956
- version update to 20100721-alt1.svn3956

* Sun Sep 25 2011 Andrew Clark <andyc@altlinux.org> 20100721-alt1.svn3711
- version update to 20100721-alt1.svn3711

* Sat Jun 4 2011 Andrew Clark <andyc@altlinux.org> 20100721-alt1.svn3603
- version update to 20100721-alt1.svn3603

* Sun Feb 13 2011 Andrew Clark <andyc@altlinux.org> 20100721-alt1.svn3443
- version update to 20100721-alt1.svn3443

* Sun Oct 10 2010 Andrew Clark <andyc@altlinux.org> 20100721-alt1.svn3299
- version update to 20100721-alt1.svn3299

* Sat Jul 24 2010 Andrew Clark <andyc@altlinux.org> 20100721-alt1.svn3213
- version update to 20100721-alt1.svn3213

* Wed May 26 2010 Andrew Clark <andyc@altlinux.org> 20090619-alt3.svn2875
- version update to 20090619-alt3.svn2875

* Fri Mar 12 2010 Andrew Clark <andyc@altlinux.org> 20090619-alt3.svn2372
- version update to 20090619-alt3.svn2372

* Wed Dec 30 2009 Andrew Clark <andyc@altlinux.org> 20090619-alt3.svn2077
- version update to 20090619-alt3.svn2077

* Thu Oct 15 2009 Andrew Clark <andyc@altlinux.org> 20090619-alt3.svn1928
- version update to 20090619-alt3.svn1928
- data files are separeted into data package

* Mon Aug 31 2009 Andrew Clark <andyc@altlinux.org> 20090619-alt2
- Added CFLAGS and CXXOPTFLAGS. desktop file correction.

* Wed Aug  5 2009 Andrew Clark <andyc@altlinux.org> 20090619-alt1
- new version

* Mon Jun  8 2009 Andrew Clark <andyc@altlinux.org> 20090504-alt1
- initial build for ALT.

