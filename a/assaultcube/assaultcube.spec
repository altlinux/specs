%define origname AssaultCube_v1.2.0.2
%define rev 779627cb
Name: assaultcube
Version: 1.2.0.2
Release: alt4.%rev
Summary: Free first-person-shooter based on the game Cube
Group: Games/Arcade
License: Creative Commons
Packager: Andrew Clark <andyc@altlinux.org>
Url: http://assault.cubers.net/
Source: http://assault.cubers.net/download.html/%origname.tar.bz2
Source1: assaultcube_client.sh
Source2: assaultcube_server.sh
Source3: %name.desktop
Source4: %name.png
Patch1: %name-%version-alt-gcc6.patch

# Automatically added by buildreq on Sun Mar 23 2014
# optimized out: libGL-devel libGLU-devel libSDL-devel libX11-devel libcloog-isl4 libogg-devel llvm xorg-xproto-devel
BuildRequires: clang libSDL_image-devel libcurl-devel libopenal-devel libstdc++-devel libvorbis-devel zlib-devel

Requires: %name-data = %version

%description
AssaultCube,formerly ActionCube, is a free first-person-shooter based on
the game Cube. Set in a realistic looking environment, as far as that's
possible with this engine, while gameplay stays fast and arcade. This
game is all about team oriented multiplayer fun.

%prep
%setup -q -n %origname
%patch1 -p2

%build
%add_optflags -D__STRICT_ANSI__
%remove_optflags -frecord-gcc-switches
%make_build -C source/src CFLAGS="%optflags" CXXOPTFLAGS="%optflags" CXXFLAGS="%optflags"

%install
mkdir -p %buildroot%_bindir
install -pD -m 755 %SOURCE1 %buildroot%_bindir/assaultcube_client
install -pD -m 755 %SOURCE2 %buildroot%_bindir/assaultcube_server

mkdir -p %buildroot%_desktopdir
install -pD -m 644 %SOURCE3 %buildroot%_desktopdir/%name.desktop

mkdir -p %buildroot%_liconsdir
install -pD -m 644 %SOURCE4 %buildroot%_liconsdir/%name.png

mkdir -p %buildroot%_docdir/%name/
mkdir -p %buildroot%_gamesdatadir/%name/

mv %_builddir/%origname/source/src/ac_client %buildroot%_bindir/
mv %_builddir/%origname/source/src/ac_server %buildroot%_bindir/
mv %_builddir/%origname/docs %buildroot/%_docdir/%name/
mv %_builddir/%origname/mods %buildroot/%_docdir/%name/
mv %_builddir/%origname/README.html %buildroot/%_docdir/%name/

%files
%_bindir/*
%_docdir/%name
%_desktopdir/%name.desktop
%_liconsdir/*.png

%changelog
* Wed Feb 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.0.2-alt4.779627cb
- Fixed build with new toolchain.

* Mon Jul 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.0.2-alt3.779627cb
- Updated build with gcc-6

* Fri Jan 2 2015 Andrew Clark <andyc@altlinux.org> 1.2.0.2-alt2.779627cb
- version update to 1.2.0.2-alt2.779627cb

* Sun Mar 23 2014 Andrew Clark <andyc@altlinux.org> 1.2.0.2-alt1.svn7688
- version update to 1.2.0.2-alt1.svn7688

* Thu Oct 4 2012 Andrew Clark <andyc@altlinux.org> 1.1.0.4-alt1.svn6897
- version update to 1.1.0.4-alt1.svn6897

* Sun Mar 25 2012 Andrew Clark <andyc@altlinux.org> 1.1.0.4-alt1.svn6772
- version update to 1.1.0.4-alt1.svn6772

* Fri Jan 6 2012 Andrew Clark <andyc@altlinux.org> 1.1.0.4-alt1.svn6746
- version update to 1.1.0.4-alt1.svn6746

* Sat Sep 24 2011 Andrew Clark <andyc@altlinux.org> 1.1.0.4-alt1.svn6656
- version update to 1.1.0.4-alt1.svn6656

* Sat Jun 4 2011 Andrew Clark <andyc@altlinux.org> 1.1.0.4-alt1.svn6490
- version update to 1.1.0.4-alt1.svn6490

* Fri Jan 7 2011 Andrew Clark <andyc@altlinux.org> 1.1.0.4-alt1.svn5994
- version update to 1.1.0.4-alt1.svn5994

* Sun Oct 10 2010 Andrew Clark <andyc@altlinux.org> 1.1.0.2-alt1.svn5740
- version update to 1.1.0.2-alt1.svn5740

* Sat Aug 14 2010 Andrew Clark <andyc@altlinux.org> 1.1.0.1-alt1.svn5613
- version update to 1.1.0.1-alt1.svn5613

* Wed May 26 2010 Andrew Clark <andyc@altlinux.org> 1.0.4-alt3.svn5057
- version update to 1.0.4-alt3.svn5057

* Mon Apr 5 2010 Andrew Clark <andyc@altlinux.org> 1.0.4-alt3.svn4799
- version update to 1.0.4-alt3.svn4799

* Fri Mar 12 2010 Andrew Clark <andyc@altlinux.org> 1.0.4-alt3.svn4788
- version update to 1.0.4-alt3.svn4788

* Wed Dec 30 2009 Andrew Clark <andyc@altlinux.org> 1.0.4-alt3.svn4746
- version update to 1.0.4-alt3.svn4746

* Sun Oct 18 2009 Andrew Clark <andyc@altlinux.org> 1.0.4-alt3.svn4660
- version update to 1.0.4-alt3.svn4660
- data files are separeted into data package

* Mon Aug 31 2009 Andrew Clark <andyc@altlinux.org> 1.0.4-alt2
- Added CFLAGS and CXXOPTFLAGS. desktop file correction.

* Sun Aug  2 2009 Andrew Clark <andyc@altlinux.org> 1.0.4-alt1
- new version.

* Mon Jun  9 2009 Andrew Clark <andyc@altlinux.org> 1.0.2-alt1
- initial build for ALT.

