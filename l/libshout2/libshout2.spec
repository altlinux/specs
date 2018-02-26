Name: libshout2
Version: 2.2.2
Release: alt3

Summary: libshout - icecast source streaming library
Group: System/Libraries
License: LGPLv2+
Url: http://www.icecast.org/
# http://downloads.us.xiph.org/releases/libshout/libshout-%version.tar.gz
Source: libshout-%version.tar
# http://git.altlinux.org/gears/l/libshout2.git
Patch: libshout-%version-%release.patch

%def_disable static

%if_enabled static
BuildRequires: glibc-devel-static
%endif
BuildRequires: libogg-devel libvorbis-devel libtheora-devel libspeex-devel

%description
Libshout is a library for communicating with and sending data to an
icecast server. It handles the socket connection, the timing of the
data, and prevents most bad data from getting to the icecast server.

%package devel
Summary: icecast2 source streaming library development package
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development library and header files needed for
developing applications that send data to an icecast2 server.

%package devel-static
Summary: icecast2 static library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package contains static version of libshout2 library.

%prep
%setup -n libshout-%version
%patch -p1

%build
%autoreconf
%configure \
	--includedir=%_includedir/shout2 \
	--oldincludedir=%_includedir/shout2 \
	%{subst_enable static}

%make_build docdir=%_docdir/libshout-%version

%install
%makeinstall_std docdir=%_docdir/libshout-%version

%files
%_libdir/*.so.*
%_docdir/libshout-%version

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/aclocal/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Thu Apr 21 2011 Dmitry V. Levin <ldv@altlinux.org> 2.2.2-alt3
- Cleaned up packaging.
- Rebuilt for soname set-versions and debuginfo.

* Sun Nov 15 2009 Nikolay A. Fetisov <naf@altlinux.ru> 2.2.2-alt2
- Removed obsolete %%post_ldconfig calls.

* Sun Jan 14 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.2.2-alt1
- 2.2.2 release.
- Merged into git.
- Some buildrequires cleanup.
- Disable static build by default.
- Added a patch fixing problem build with speex enabled.

* Sat Jan 21 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.2-alt1
- 2.2 release.
- reworked patch.

* Mon Mar 14 2005 Pavlov Konstantin <thresh@altlinux.ru> 2.1-alt1.1
- fixed wrong patch.

* Fri Mar 04 2005 Pavlov Konstantin <thresh@altlinux.ru> 2.1-alt1
- 2.1 release.

* Mon Nov 22 2004 Pavlov Konstantin <thresh@altlinux.ru> 2.0-alt2
- Fixed bug #5544.
- so name changed to libshout2.
- spec cleanup.

* Wed Oct 20 2004 Pavlov Konstantin <thresh@altlinux.ru> 2.0-alt1
- Initial build for Sisyphus.
