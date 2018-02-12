Name: sauerbraten
Version: 20130404
Release: alt1
Summary: Sauerbraten is a free multiplayer/singleplayer FPS

Group: Games/Arcade
License: Zlib
Url: http://sauerbraten.org/

# http://downloads.sourceforge.net/sauerbraten/sauerbraten_2013_04_04_collect_edition_linux.tar.bz2
Source: sauerbraten-%version.tar
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
%setup

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
mv src/sauer_client %buildroot%_bindir/
mv src/sauer_server %buildroot%_bindir/
mv docs %buildroot/%_docdir/%name/
mv README.html %buildroot/%_docdir/%name/
mv server-init.cfg %buildroot/%_gamesdatadir/%name/

%files
%_bindir/*
%_docdir/%name
%_desktopdir/*
%_liconsdir/*.png
%_gamesdatadir/%name/server-init.cfg

%changelog
* Fri Feb 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 20130404-alt1
- Updated to upstream version 2013.04.04.

* Fri Jan 2 2015 Andrew Clark <andyc@altlinux.org> 20130203-alt1.svn5065
- version update to 20130203-alt1.svn5065

* Sun Feb 3 2013 Andrew Clark <andyc@altlinux.org> 20130126-alt1.svn4781
- version update to 20130126-alt1.svn4781

* Sat Feb 2 2013 Andrew Clark <andyc@altlinux.org> 20130126-alt1.svn4776
- version update to 20130126-alt1.svn4776

* Thu Oct 4 2012 Andrew Clark <andyc@altlinux.org> 20100721-alt1.svn4252
- version update to 20100721-alt1.svn4252

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

