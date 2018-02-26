%define flacdocs %_docdir/%name-%version
%define soversion 8
%define cppsoversion 6

%set_verify_elf_method textrel=relaxed

Name: flac
Version: 1.2.1
Release: alt9

Summary: Free Lossless Audio Codec
License: GPLv2+
Group: Sound
Url: http://flac.sourceforge.net/
Packager: Pavlov Konstantin <thresh@altlinux.ru>
# http://download.sourceforge.net/%name/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: lib%name%soversion = %version-%release

%def_disable static
%{?_enable_static:BuildRequires: glibc-devel-static}

%ifarch %ix86 x86_64
BuildRequires: nasm
%endif

# Automatically added by buildreq on Fri Mar 25 2011
BuildRequires: docbook-utils doxygen gcc-c++ libogg-devel libxmms-devel

%description
FLAC (%url) is an Open Source lossless audio codec.

%package -n lib%name%soversion
Summary: FLAC shared library
Group: System/Libraries
License: BSD-like
Provides: lib%name = %version

%description -n lib%name%soversion
The lib%name package contains a shared library of
functions for manipulating FLAC format audio files.

%package -n lib%name-devel
Summary: Development files for FLAC
Group: Development/C
License: BSD-like
Requires: lib%name%soversion = %version-%release
Provides: liboggflac-devel = %version
Obsoletes: liboggflac-devel < %version

%description -n lib%name-devel
This package contains development files required for packaging
FLAC-based software.

%package -n lib%name-devel-static
Summary: Static libraries for FLAC
Group: Development/C
License: BSD-like
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains development libraries required for packaging
statically linked FLAC-based software.

%package -n lib%name++%cppsoversion
Summary: Object shared library FLAC++
Group: System/Libraries
License: BSD-like
Requires: lib%name%soversion = %version-%release
Provides: lib%name++ = %version

%description -n lib%name++%cppsoversion
The lib%name++%cppsoversion package contains a object wrapper library
of functions for manipulating FLAC format audio files.

%package -n lib%name++-devel
Summary: Development files for FLAC++ library
Group: Development/C
License: BSD-like
Requires: lib%name++%cppsoversion = %version-%release
Provides: liboggflac++-devel = %version
Obsoletes: liboggflac++-devel < %version

%description -n lib%name++-devel
This package contains development files required for packaging
FLAC++-based software.

%package -n lib%name++-devel-static
Summary: Static libraries for FLAC++ library
Group: Development/C
License: BSD-like
Requires: lib%name++-devel = %version-%release

%description -n lib%name++-devel-static
This package contains development libraries required for packaging
statically linked FLAC++-based software.

%package -n xmms-in-%name
Summary: Plugin for XMMS
Group: Sound
License: GPLv2+
Provides: xmms-%name
Obsoletes: xmms-%name
Requires: lib%name%soversion = %version-%release

%description -n xmms-in-%name
Xmms plugin for playing FLAC files.

%prep
%setup -q
%patch -p1

%build
# due to libtool mess
%autoreconf
%configure --enable-exhaustive-tests %{subst_enable static}
%make_build

%install
%makeinstall xmmsinputplugindir=%buildroot%xmms_inputdir
install -pm644 COPYING.Xiph AUTHORS README %buildroot%flacdocs/

%check
%make_build -k check

%files
%_bindir/*
%_mandir/man?/*
%flacdocs/html/*.html
%flacdocs/html/*.ico
%flacdocs/html/*.css
%flacdocs/html/ru
%flacdocs/html/images

%files -n lib%name%soversion
%_libdir/libFLAC.so.*
%dir %flacdocs
%dir %flacdocs/html
%flacdocs/AUTHORS
%flacdocs/README
%flacdocs/COPYING.Xiph

%files -n lib%name-devel
%_datadir/aclocal/libFLAC.m4
%_libdir/libFLAC.so
%_includedir/FLAC
%flacdocs/html/api
%flacdocs/FLAC.tag
%_pkgconfigdir/flac.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/libFLAC.a
%endif

%files -n lib%name++%cppsoversion
%_libdir/libFLAC++.so.*

%files -n lib%name++-devel
%_datadir/aclocal/libFLAC++.m4
%_libdir/libFLAC++.so
%_includedir/FLAC++
%_pkgconfigdir/flac++.pc

%if_enabled static
%files -n lib%name++-devel-static
%_libdir/libFLAC++.a
%endif

%files -n xmms-in-%name
%_libdir/xmms/Input/*

%changelog
* Fri Mar 25 2011 Alexey Tourbin <at@altlinux.ru> 1.2.1-alt9
- libflac-devel: removed dependency on libogg-devel

* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt7
- Rebuilt for debuginfo

* Sat Oct 23 2010 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt6
- xmms-in-flac: Fixed underlinkage in libxmms-flac.so.
- Cleaned up specfile, enabled test suite.

* Wed May 13 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.2.1-alt5
- Fix build with new libtool.

* Fri Mar 06 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.2.1-alt4
- Remove unneeded post/postun ldconfig calls.

* Tue Oct 28 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.2.1-alt3
- fix build with gcc 4.3.

* Thu Oct 11 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.2.1-alt2
- Merged kas@ arm changes.
- Fix #13056: licensing.

* Sun Sep 30 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.2.1-alt1
- 1.2.1 release.

* Fri Sep 14 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.2.0-alt1
- 1.2.0 release.

* Mon Feb 26 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.1.4-alt2
- Pack pkg-config files.
- Added needed provides/obsoletes/requires to devel packages.

* Thu Feb 15 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.1.4-alt1
- 1.1.4 release.

* Thu Feb 01 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.1.3-alt3
- Introduced lib%%name%%soversion for libflac library.
- Introduced lib%%name++%cppsoversion for libflac++ library.
- Removed Requires for xmms-in-flac package.
- Added autoreconf macro.
- Removed liboggflac* packages.
- Fixed Provides/Obsoletes for libflac8/libflac++6.
- Removed Prereqs for flac package.

* Sun Jun 04 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.1.2-alt3
- Added patch2 to fix -as-needed problem with linkage.

* Sat Feb 26 2005 Andrey Astafiev <andrei@altlinux.ru> 1.1.2-alt2
- Fixed problem with xmms plugin startup.

* Mon Feb 14 2005 Andrey Astafiev <andrei@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Fri Jun 25 2004 Andrey Astafiev <andrei@altlinux.ru> 1.1.0-alt8
- Fixed bug #4289: libFLAC is now linked with -lm.

* Thu Apr 29 2004 Andrey Astafiev <andrei@altlinux.ru> 1.1.0-alt7
- Updated to current CVS.

* Thu Feb 05 2004 Alexey Tourbin <at@altlinux.ru> 1.1.0-alt6.1
- better fix for non-pic code (convenience libtool libraries)

* Mon Dec 15 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1.0-alt6
- Package with input plugin for xmms renamed.

* Sun Dec 07 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1.0-alt5
- *.la files removed.

* Fri Nov 14 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1.0-alt4
- Set textrel=relaxed for now.

* Fri Mar 07 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1.0-alt3
- Rebuilt with id3lib 3.8.3

* Wed Mar 05 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1.0-alt2
- fixed: documentation added.
- fixed: bug #0002303.

* Wed Jan 29 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Fri Jan 17 2003 Andrey Astafiev <andrei@altlinux.ru> 1.0.5-alt0.9
- Package flac now depends on liboggflac.
- Real fix for xmms plugin.
- Rebuilt with id3lib 3.8.2.

* Mon Nov 04 2002 Andrey Astafiev <andrei@altlinux.ru> 1.0.4-alt3
- Temprorary fix in xmms plugin (id3v2 tags disabled).

* Mon Nov 04 2002 Andrey Astafiev <andrei@altlinux.ru> 1.0.4-alt2
- Rebuilt with gcc3.2.

* Wed Sep 11 2002 Andrey Astafiev <andrei@altlinux.ru> 1.0.4-alt1
- 1.0.4
- Added new packages with OggFLAC and OggFLAC++ liraries.

* Thu Jul 11 2002 Andrey Astafiev <andrei@altlinux.ru> 1.0.3-alt1
- 1.0.3
- Corrected dependencies to xmms library.
- Added new packages with object liraries.

* Tue Dec 04 2001 Andrey Astafiev <andrei@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Mon Nov 26 2001 Andrey Astafiev <andrei@altlinux.ru> 1.0.1-alt1
- 1.0.1
- Some changes in spec.

* Wed Aug 8 2001 Andrey Astafiev <andrei@altlinux.ru> 1.0-alt1
- First version of RPM package.

* Wed Jul 20 2001 Josh Coalson
- FLAC 1.0 is out!
