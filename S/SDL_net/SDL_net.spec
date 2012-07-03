%define lib_name lib%name

Name: SDL_net
Version: 1.2.8
Release: alt1

Summary: Simple DirectMedia Layer - network
License: zlib
Group: System/Libraries
Url: http://www.libsdl.org/projects/SDL_net/

Source0: %name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Sat Apr 07 2012
# optimized out: libstdc++-devel
BuildRequires: gcc-c++ glibc-devel-static libSDL-devel

%description
This is an example portable network library for use with SDL. Note that this
isn't necessarily how you would want to write a chat program, but it
demonstrates how to use the basic features of the network and GUI libraries.

%package -n %lib_name
Summary: Main library for %name
Group: System/Libraries

%description -n %lib_name
This package contains the library needed to run programs dynamically
linked with %name.

%package -n %lib_name-devel
Summary: Headers for developing programs that will use %name
Group: Development/C
Requires: %lib_name = %version-%release

%description -n %lib_name-devel
This package contains the headers that programmers will need to develop
applications which will use %name.

%package -n %lib_name-devel-static
Summary: Static libraries for developing programs that will use %name
Group: Development/C
Requires: %lib_name-devel = %version-%release

%description -n %lib_name-devel-static
This package contains the static libraries that programmers will need to develop
applications which will use %name.

%prep
%setup -q

%build
touch NEWS AUTHORS ChangeLog
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files -n %lib_name
%doc CHANGES COPYING README
%_libdir/*.so.*

%files -n %lib_name-devel
%_includedir/SDL/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files -n %lib_name-devel-static
%_libdir/*.a

%changelog
* Sat Apr 07 2012 Igor Zubkov <icesik@altlinux.org> 1.2.8-alt1
- 1.2.7 -> 1.2.8
- New license: zlib

* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7-alt5
- Rebuilt for debuginfo

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7-alt4
- Rebuilt for soname set-versions

* Mon Nov 02 2009 Igor Zubkov <icesik@altlinux.org> 1.2.7-alt3
- update License
- fix repocop warning

* Fri Mar 06 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.2.7-alt2
- Get rid of post/postun ldconfig.

* Wed Aug 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.2.7-alt1
- 1.2.7 release.

* Tue Jul 17 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.2.6-alt3
- Macroize %%post and %%postun.

* Sun Feb 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.2.6-alt2
- 1.2.6 release.
- Fixed buildrequires.

* Sun Dec 14 2003 Rider <rider@altlinux.ru> 1.2.5-alt2
- removed .la files

* Thu May 08 2003 Rider <rider@altlinux.ru> 1.2.5-alt1
- new version

* Thu Jan 23 2003 Rider <rider@altlinux.ru> 1.2.4-alt4
- fix rebuild in new invironment (automake)

* Tue Oct 01 2002 Rider <rider@altlinux.ru> 1.2.4-alt3
- includedir fix
- added BuildRequires (auto)

* Mon Sep 23 2002 Rider <rider@altlinux.ru> 1.2.4-alt2
- rebuild (gcc 3.2)

* Fri Jun 07 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.2.4-alt1
- 1.2.4
- Some spec cleanup

* Sat Feb 09 2002 Rider <rider@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Tue Oct 09 2001 Rider <rider@altlinux.ru 1.2.2-alt1
- 1.2.2

* Wed Apr 11 2001 Kostya Timoshenko <kt@altlinux.ru> 1.1.1-ipl4mdk
- Rebuild with SDL-1.2.0
- Moved static libraries to devel-static subpackage.

* Wed Mar 14 2001 Kostya Timoshenko <kt@petr.kz> 1.1.1-ipl3mdk
- Libification.

* Wed Dec 27 2000 Kostya Timoshenko <kt@petr.kz> 1.1.1-ipl2mdk
- Rebuild for RE

* Fri Dec  1 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.1.1-2mdk
- new lib policy

* Fri Sep 01 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.1.1-1mdk
- updated to version 1.1.1
- use of macros like %_libdir et al.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.0.2-2mdk
- automatically added BuildRequires

* Fri Jun 23 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.0.2-1mdk
- v1.0.2

* Tue Jun 20 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.1-5mdk
- Use makeinstall macros.

* Tue May 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.1-4mdk
- Fix m4 macros with new libtoolize.
- Use configure macro.

* Tue Apr 11 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-2mdk
- added url
- fixed group
- some minor package build fixes
- built against stable SDL version, previous was using 1.1.x devel

* Fri Feb 11 2000 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
- used srpm provided by Hakan Tandogan <hakan@iconsult.com>

* Sun Jan 16 2000 Hakan Tandogan <hakan@iconsult.com>
- initial spec file

