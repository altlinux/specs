Name: xdelta1
Version: 1.1.4
Release: alt4

%define _includedir %_usr/include/%name
%define srcname xdelta-%version
%define	lib_name libxdelta
%define lib_major 2

Summary: A binary delta generator
License: GPL
Group: File tools
Url: http://www.xdelta.org/
Packager: Dmitry V. Levin <ldv@altlinux.org>

# ttp://xdelta.googlecode.com/files/xdelta-1.1.4.tar.gz
Source: %srcname.tar
Patch1: xdelta-1.1.4-alt-configure.patch
Patch2: xdelta-1.1.4-alt-makefile.patch
Patch3: xdelta-1.1.3-rh-aclocal.patch
Patch4: xdelta-1.1.4-rh-glib2.patch
Patch5: xdelta-1.1.3-rh-alt-pkgconfig.patch
Patch6: xdelta-1.1.4-alt-oom.patch

Requires: %lib_name%lib_major = %version-%release
Provides: xdelta = %version
Obsoletes: xdelta

BuildRequires: glib2-devel zlib-devel

%def_disable static
%{?_enable_static:BuildPreReq: glibc-devel-static}

%description
XDelta is a library interface and application program designed to
compute changes between files.  These changes (deltas) are similar to
the output of the "diff" program in that they may be used to store and
transmit only the changes between files.  However, unlike diff, the
output of XDelta is not expressed in a human-readable format--XDelta
can also also apply these deltas to a copy of the original file(s).
XDelta uses a fast, linear algorithm and performs well on both binary
and text files.  XDelta typically outperforms GNU diff in both time
and generated-delta-size, even for plain text files.  XDelta also
includes a simple implementation of the Rsync algorithm and several
advanced features for implementing RCS-like file-archival with.

%package -n %lib_name%lib_major
Summary: Shared libraries for XDelta
Group: System/Libraries

%package -n %lib_name%lib_major-devel
Summary: Development libraries and include files for development with XDelta
Group: Development/C
Requires: %lib_name%lib_major = %version-%release
Provides: xdelta-devel = %version-%release
Obsoletes: xdelta-devel

%package -n %lib_name%lib_major-devel-static
Summary: Static libraries and header files for development with XDelta
Group: Development/C
Requires: %lib_name%lib_major-devel = %version-%release

%description -n %lib_name%lib_major
This package contains shared libraries required by Xdelta applications.

%description -n %lib_name%lib_major-devel
This package contains the development libraries and include files required
to develop applications using Xdelta.

%description -n %lib_name%lib_major-devel-static
This package contains static libraries required to develop statically linked
applications using Xdelta.

%prep
%setup -q -n %srcname
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%add_optflags -fno-strict-aliasing
autoreconf -fisv
%configure %{subst_enable static}
%make_build all

%install
%makeinstall

%files
%_bindir/xdelta
%_mandir/man?/*
%doc AUTHORS NEWS README

%files -n %lib_name%lib_major
%_libdir/*.so.*

%files -n %lib_name%lib_major-devel
%_bindir/*-config
%_libdir/*.so
%_includedir
%_pkgconfigdir/*
%_datadir/aclocal/*.m4

%if_enabled static
%files -n %lib_name%lib_major-devel-static
%_libdir/*.a
%endif

%changelog
* Mon May 21 2012 Dmitry V. Levin <ldv@altlinux.org> 1.1.4-alt4
- Fixed build with ld --no-copy-dt-needed-entries.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 1.1.4-alt3
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Sun Apr 08 2007 Dmitry V. Levin <ldv@altlinux.org> 1.1.4-alt2
- Fixed OOM handling.

* Thu Feb 15 2007 Dmitry V. Levin <ldv@altlinux.org> 1.1.4-alt1
- Updated to 1.1.4.
- Enabled LFS support.
- Imported FC patch to provide pkgconfig file.
- Imported FC patch to link with glib2 instead of glib.

* Sun Jan 15 2006 Dmitry V. Levin <ldv@altlinux.org> 1.1.3-alt4
- Link libxdelta with libedsio.
- Use getopt from glibc.
- Dropped emacs cruft.

* Tue Dec 09 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.3-alt3
- Do not package .la files.
- Do not build static library by default.

* Mon Nov 18 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1.3-alt2
- rebuild

* Tue Oct 09 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.1.3-alt1
- 1.1.3
- Libification.

* Mon Dec 04 2000 Dmitry V. Levin <ldv@fandra.org> 1.1.1-ipl7mdk
- Fixed texinfo documentation.
- RE adaptions.

* Wed Jul 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1.1-7mdk
- fix bad script

* Tue Jul 25 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1.1-6mdk
- BM

* Mon Apr  3 2000 Adam Lebsack <adam@mandrakesoft.com> 1.1.1-5mdk
- Release build.

* Wed Jan 12 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.1.1-4mdk
- Regnerate libtoolize.

* Thu Nov 11 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- rebuilt for Oxygen

* Fri Aug 20 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- fixed edsio-comp script.

* Tue Aug 19 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- First spec file for Mandrake distribution.
