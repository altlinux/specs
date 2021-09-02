%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: smpeg
Summary: summary SDL MPEG Library
Version: 0.4.5
Release: alt4.svn20120121
License: LGPL
Group: Video
URL: http://icculus.org/smpeg/

# svn://svn.icculus.org/smpeg/trunk
Source: %name-%version.tar
Source10: gtv_16x16.xpm
Source11: gtv_32x32.xpm
Source12: gtv_48x48.xpm

Patch1: %name-%version-debian-gcc-6.patch

# Automatically added by buildreq on Mon Feb 13 2006
BuildRequires: gcc-c++ gtk+2-devel imake libICE-devel libSDL-devel libX11-devel libXt-devel libstdc++-devel xorg-cf-files
BuildRequires: libGL-devel libGLU-devel

%description
SMPEG is based on UC Berkeley's mpeg_play software MPEG decoder and SPLAY,
an mpeg audio decoder created by Woo-jae Jung. We have completed the
initial work to wed these two projects in order to create a general
purpose MPEG video/audio player for the Linux OS.

%package -n lib%name
Summary: Main library for %name
Group: System/Libraries

%description -n lib%name
This package contains the library needed to run programs dynamically
linked with %name.

%package -n lib%name-devel
Summary: Headers for developing programs that will use %name
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
This package contains the headers that programmers will need to develop
applications which will use %name.

%package player
Summary: Simple MPEG player baed on %name library
Group: Video

%description player
This package contains a MPEG player based on %name.

%prep
%setup
%patch1 -p1

%build
%add_optflags -D_FILE_OFFSET_BITS=64

# Needed for snapshot releases.
if [ ! -f configure ]; then
  CFLAGS="%optflags" ./autogen.sh --prefix=%_prefix
fi
%configure \
	--disable-opengl-player \
	--disable-static \
	%nil

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall

mkdir -p %buildroot%_miconsdir
mkdir -p %buildroot%_liconsdir
mkdir -p %buildroot%_niconsdir
cat %SOURCE10 > %buildroot%_miconsdir/gtv.xpm
cat %SOURCE11 > %buildroot%_niconsdir/gtv.xpm
cat %SOURCE12 > %buildroot%_liconsdir/gtv.xpm

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}-player.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Gtv Mpeg player
Comment=Gtv Mpeg video player
Icon=gtv
Exec=gtv
Terminal=false
Categories=AudioVideo;Video;Player;
EOF

%files player
%doc CHANGES COPYING README
%_bindir/plaympeg
%_bindir/gtv
%_mandir/*/*
%_desktopdir/%{name}-player.desktop
%_niconsdir/gtv.xpm
%_miconsdir/gtv.xpm
%_liconsdir/gtv.xpm

%files -n lib%name
%doc CHANGES COPYING README
%_libdir/lib*.so.*

%files -n lib%name-devel
%doc CHANGES COPYING README
%_bindir/smpeg-config
%_includedir/*
%_libdir/*.so
%_datadir/aclocal/*.m4

%changelog
* Thu Sep 02 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.5-alt4.svn20120121
- Disabled static libraries.

* Mon Mar 11 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.5-alt3.svn20120121
- Updated build dependencies (Closes: #36254)

* Thu Nov 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.5-alt2.svn20120121
- Fixed build with gcc-6.

* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.5-alt1.svn20120121
- Version 0.4.5

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt11
- Removed RPATH

* Sat Apr 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt10.qa1
- NMU: converted menu to desktop file

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt10
- BuildRequires:
  + replaced libmesa-devel by libGL-devel and libGLU-devel
  + removed xorg-x11-proto-devel and automake_1.4

* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt9
- Rebuilt for debuginfo

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt8
- Rebuilt for soname set-versions

* Sat Nov 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.4.4-alt7.1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for smpeg
  * post_ldconfig for libsmpeg
  * postun_ldconfig for libsmpeg
  * update_menus for smpeg-player

* Tue May 16 2006 Anton Farygin <rider@altlinux.ru> 0.4.4-alt7
- include some patches from Gentoo
- fixed compilation errors with gcc-4.1

* Mon Feb 13 2006 Anton Farygin <rider@altlinux.ru> 0.4.4-alt6
- fixed xorg-7.0 requires

* Sun Dec 14 2003 Rider <rider@altlinux.ru> 0.4.4-alt5
- removed .la files

* Fri Oct 17 2003 Rider <rider@altlinux.ru> 0.4.4-alt4
- fix build

* Wed Oct 23 2002 Grigory Milev <week@altlinux.ru> 0.4.4-alt3
- rebuild with new directfb

* Tue Oct 01 2002 Rider <rider@altlinux.ru> 0.4.4-alt2
- BuildRequires fix
- gcc 3.2 rebuild
- specfile cleanup

* Wed Jul 18 2001 Sergie Pugachev <fd_rag@altlinux.ru> 0.4.4-alt1
- new version

* Mon Apr 16 2001 Kostya Timoshenko <kt@altlinux.ru> 0.4.3-alt2
- fix section Multimedia/Video

* Wed Apr 10 2001 Rider <rider@altlinux.ru> 0.4.3-alt1
- 0.4.3

* Wed Apr  4 2001 Kostya Timoshenko <kt@altlinux.ru> 0.4.2-ipl6mdk
- Rebuild with SDL-1.2.0
- Moved static libraries to devel-static subpackage.

* Tue Mar 13 2001 Kostya Timoshenko <kt@petr.kz> 0.4.2-ipl5mdk
- build for RE

* Thu Mar  8 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.2-4mdk
- rename player subpackage to "smpeg-player"

* Mon Mar  5 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.2-3mdk
- fix smpeg-config to not provide rpath
- fix provides
- bzip icons

* Tue Jan 23 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.4.2-2mdk
- corrected doc file list for libsmpeg package

* Fri Jan  5 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.2-1mdk
- 0.4.2

* Fri Dec  1 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.1-4mdk
- better new lib policy, do not generate anymore an ambiguous package
  containing binaries but with the old lib name

* Wed Nov 29 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.1-3mdk
- follow new lib policy, split packages with binaries

* Wed Oct 25 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.1-2mdk
- rebuild to ensure that icons are not executables

* Tue Oct 24 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.1-1mdk
- 0.4.1

* Fri Sep 15 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.0-10mdk
- rebuild against fixed XFree4 by fredl

* Thu Sep 14 2000 Florin Grad <florin@mandrakesoft.com> 0.4.0-9mdk
- now we have transparent icons

* Thu Sep 07 2000 Florin Grad <florin@mandrakesoft.com> 0.4.0-8mdk
- removed the explicit icon path

* Thu Aug 31 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.0-7mdk
- explicit name for menu entry :-)

* Wed Aug 30 2000 Florin Grad <florin@mandrakesoft.com> 0.4.0-6mdk

* Mon Aug 28 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 0.4.0-5mdk
- make coherent menu name. Thanks Fred.

* Mon Aug 28 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 0.4.0-4mdk
- rebuilt for latest SDL 1.1.4.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.4.0-3mdk
- automatically added BuildRequires.

* Wed Aug 02 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 0.4.0-2mdk
- macroszifications.
- BM.

* Fri Jun 23 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.4.0-1mdk
- v0.4.0.

* Tue Apr 11 2000 Denis Havlik <denis@mandrakesoft.com> 0.3.5-2mdk
- fixed "Requires",

* Tue Apr 11 2000 Denis Havlik <denis@mandrakesoft.com> 0.3.5-1mdk
- new version,
- merged with loki's original rpm (add devel rpm!).
- menu entry and icon (by Hélène Durosini) for gtv.

* Tue Feb 07 2000 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- mandrake adations.
- added BuildPreReq.
- updated to version 0.3.3.

* Wed Jan 19 2000 Sam Lantinga <hercules@lokigames.com>
- initial release.

