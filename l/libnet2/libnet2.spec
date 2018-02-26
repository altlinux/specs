Name: libnet2
Version: 1.1.6
Release: alt1

Summary: C library for portable packet creation and injection
Group: System/Libraries
License: BSD-style
Url: http://www.sourceforge.net/projects/libnet-dev/

# http://git.altlinux.org/gears/l/libnet2.git
Source: libnet-%version-%release.tar
Source1: libnet-config.1

Provides: libnet = %version-%release
Obsoletes: libnet < %version-%release
BuildRequires: doxygen

%def_disable static

%package devel
Summary: Development Libnet library, header files, documentation and examples
Group: Development/C
Provides: libnet-devel = %version-%release
Obsoletes: libnet-devel < %version-%release
Conflicts: libnet1-devel
Requires: %name = %version-%release

%package devel-static
Summary: Static Libnet library
Group: Development/C
Provides: libnet-devel-static = %version-%release
Obsoletes: libnet-devel-static < %version-%release
Conflicts: libnet1-devel-static
Requires: %name-devel = %version-%release

%description
Libnet is an API to help with the construction and handling of network
packets.  It provides a portable framework for low-level network
packet writing and handling (use Libnet in conjunction with libpcap and
you can write some really cool stuff).  Libnet includes packet creation
at the IP layer and at the link layer as well as a host of supplementary
and complementary functionality.  Libnet is avery handy with which to
write network tools and network test code.  See the manpage and sample
test code for more detailed information.

%description devel
Libnet is an API to help with the construction and handling of network
packets.  It provides a portable framework for low-level network
packet writing and handling (use Libnet in conjunction with libpcap and
you can write some really cool stuff).  Libnet includes packet creation
at the IP layer and at the link layer as well as a host of supplementary
and complementary functionality.  Libnet is avery handy with which to
write network tools and network test code.  See the manpage and sample
test code for more detailed information.

This package contains the development library, it's header files,
documentation and examples needed to develop Libnet-based applications.

%description devel-static
Libnet is an API to help with the construction and handling of network
packets.  It provides a portable framework for low-level network
packet writing and handling (use Libnet in conjunction with libpcap and
you can write some really cool stuff).  Libnet includes packet creation
at the IP layer and at the link layer as well as a host of supplementary
and complementary functionality.  Libnet is avery handy with which to
write network tools and network test code.  See the manpage and sample
test code for more detailed information.

This package contains the static library required to develop statically
linked Libnet-based applications.

%prep
%setup -n libnet-%version-%release
bzip2 -9k doc/CHANGELOG

%build
%add_optflags -fno-strict-aliasing
%autoreconf
export ac_cv_libnet_linux_procfs=yes
%configure %{subst_enable static}
make -C doc doc
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_man1dir
install -pm644 %_sourcedir/libnet-config.1 %buildroot%_man1dir/

# Relocate shared libraries from %_libdir/ to /%_lib/
mkdir %buildroot/%_lib
for f in %buildroot%_libdir/lib*.so; do
	t=$(readlink "$f") || continue
	ln -sf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/lib*.so.* %buildroot/%_lib/

%define _customdocdir %_docdir/libnet-%version

%files
/%_lib/*.so.*

%files devel
%_bindir/*
%_libdir/*.so
%_includedir/*
%_mandir/man?/*
%doc doc/{CHANGELOG.bz2,COPYING,DESIGN_NOTES,MIGRATION,PACKET_BUILDING,RAWSOCKET_NON_SEQUITUR,TODO}

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Mon Apr 02 2012 Dmitry V. Levin <ldv@altlinux.org> 1.1.6-alt1
- Updated to libnet-1.1.6.

* Mon Apr 25 2011 Dmitry V. Levin <ldv@altlinux.org> 1.1.5-alt1
- Updated to libnet-1.1.5-42-g4aac7af.

* Sun Nov 07 2010 Dmitry V. Levin <ldv@altlinux.org> 1.1.4-alt1
- Updated to 1.1.4.

* Fri Dec 19 2008 Dmitry V. Levin <ldv@altlinux.org> 1.1.2.1-alt4
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.
- Imported patches from Debian libnet-1.1.2.1-4 package.

* Fri Sep 28 2007 Dmitry V. Levin <ldv@altlinux.org> 1.1.2.1-alt3
- Relocated shared library from /usr/lib to /lib (#12938).

* Sun Apr 08 2007 Dmitry V. Levin <ldv@altlinux.org> 1.1.2.1-alt2
- Backported upstream fix to libnet_in_cksum().
- Disabled gcc optimization based on strict aliasing rules.

* Sun Sep 05 2004 Dmitry V. Levin <ldv@altlinux.org> 1.1.2.1-alt1
- Updated to 1.1.2.1.
- Updated patches.
- Added libnet-config(1) manpage.
- Do not build and package static library by default.

* Tue Dec 09 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt3
- Do not package .la files.

* Sat Sep 27 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt2
- Fixed libnet_init() to work without complete root privileges.

* Sun Nov 24 2002 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt1
- Updated to 1.1.0
- Ported to autoconf >= 2.53, automake >= 1.6.1
- Libtoolized.
- Renamed to libnet2.

* Mon Apr 15 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.0.2a-ipl2mdk
- Moved static libraries to devel-static subpackage.

* Thu Feb 08 2001 Dmitry V. Levin <ldv@fandra.org> 1.0.2a-ipl1mdk
- 1.0.2a

* Mon Feb 05 2001 Dmitry V. Levin <ldv@fandra.org> 1.0.2-ipl1mdk
- 1.0.2

* Sat Sep 02 2000 Dmitry V. Levin <ldv@fandra.org> 1.0.1b-ipl1mdk
- 1.0.1b
- Build and package shared library too.

* Fri Mar 24 2000 Dmitry V. Levin <ldv@fandra.org>
- 1.0.1

* Wed Mar 15 2000 Dmitry V. Levin <ldv@fandra.org>
- removed Makefile.in from examples
- updated to rpm-3.0.4

* Thu Nov 11 1999 Dmitry V. Levin <ldv@fandra.org>
- 1.0

* Tue Sep 16 1999 Dmitry V. Levin <ldv@fandra.org>
- initial revision
