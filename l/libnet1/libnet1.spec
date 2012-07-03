%define realname libnet
Name: %{realname}1
Version: 1.0.2a
Release: alt3
Epoch: 1

Summary: A C library for portable packet creation
Group: System/Libraries
License: BSD-style
Url: http://www.packetfactory.net/libnet

Source0: %url/dist/libnet-%version.tar.bz2
Source1: libnet-1.0-manual.tar.bz2
Source2: libnet-config.1

Patch1: libnet-1.0.2-alt-shared.patch
Patch2: libnet-1.0.1b-alt-test.patch
Patch3: libnet-1.0.2a-alt-memory-leaks.patch
Patch4: libnet-1.0.2a-deb-multiline-warning.patch

Provides: %realname = %version-%release
Obsoletes: %realname

%def_disable static

%package devel
Summary: Development Libnet library, header files, documentation and examples
Group: Development/C
Provides: %realname-devel = %version-%release
Obsoletes: %realname-devel
Conflicts: %{realname}2-devel
Requires: %name = %epoch:%version-%release

%package devel-static
Summary: Static Libnet library
Group: Development/C
Provides: %realname-devel-static = %version-%release
Obsoletes: %realname-devel-static
Conflicts: %{realname}2-devel-static
Requires: %name-devel = %epoch:%version-%release

%description
Libnet is an API to help with the construction and handling of network
packets.  It provides a portable framework for low-level network
packet writing and handling (use Libnet in conjunction with libpcap and
you can write some really cool stuff).  Libnet includes packet creation
at the IP layer and at the link layer as well as a host of supplementary
and complementary functionality. Libnet is avery handy with which to
write network tools and network test code.  See the manpage and sample
test code for more detailed information.

%description devel
Libnet is an API to help with the construction and handling of network
packets.  It provides a portable framework for low-level network
packet writing and handling (use Libnet in conjunction with libpcap and
you can write some really cool stuff).  Libnet includes packet creation
at the IP layer and at the link layer as well as a host of supplementary
and complementary functionality. Libnet is avery handy with which to
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
and complementary functionality. Libnet is avery handy with which to
write network tools and network test code.  See the manpage and sample
test code for more detailed information.

This package contains the static library required to develop statically
linked Libnet-based applications.

%prep
%setup -q -n Libnet-%version -a1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

install -pm755 /usr/share/automake/config.* .

find -type d -name CVS -print0 |
	xargs -r0 rm -rf --
find -type f \( -name .cvsignore -o -name .#\* -o -name \*.orig \) -delete -print

%build
export ac_cv_lib_pcap_pcap_open_live=no
export ac_cv_lib_net_libnet_build_ip=no
export ac_libnet_have_pf_packet=yes
%configure %{subst_enable static}

# First build shared,
%make_build lib/%realname.so.%version CFLAGS="%optflags %optflags_shared -I$PWD/include" CPPFLAGS=-D_GNU_SOURCE

%if_enabled static
# then static,
make clean
%make_build CFLAGS="%optflags -I$PWD/include" CPPFLAGS=-D_GNU_SOURCE

sleep 1
touch lib/%realname.so.%version
%endif

# and test.
ADD_CFLAGS="$(./%realname-config --defines)"
make -C test CFLAGS="%optflags -I$PWD/include $ADD_CFLAGS"
make -C test clean

%install
mkdir -p %buildroot%_man1dir
install -pm644 %_sourcedir/libnet-config.1 %buildroot%_man1dir/

%makeinstall_std MAN_PREFIX=%_man3dir
cp -dp lib/*.so* %buildroot%_libdir/
ln -s libnet.so %buildroot%_libdir/libpwrite.so

rm doc/%realname.3

ADD_CFLAGS="$(./%realname-config --defines)"
ADD_LIBS="$(./%realname-config --libs)"

mkdir extra
cp -a test example extra
pushd extra
	find -type f -name Makefile.in -print0 |
		xargs -r0 rm -f --
	find -type f -name Makefile -print0 |
		xargs -r0 perl -pi -e '
s/^(DEFINES\s*\+=\s*).*/$1'"$ADD_CFLAGS"'/;
s/^(LIBS\s*=\s*).*/$1'"$ADD_LIBS"'/
'
popd

%define docdir %_docdir/%realname-%version
mkdir -p %buildroot%docdir
cp -a doc/COPYING doc/CHANGELOG* doc/README doc/TODO* extra/* html \
	%buildroot%docdir/

%files
%_libdir/*.so.*
%dir %docdir
%docdir/COPYING
%docdir/README

%files devel
%_bindir/*
%_libdir/*.so
%_includedir/*
%_mandir/man?/*
%dir %docdir
%docdir/CHANGELOG*
%docdir/TODO*
%docdir/[eht]*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Sat Nov 06 2010 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.2a-alt3
- Rebuilt for soname set-versions.

* Tue Sep 08 2009 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.2a-alt2
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.
- Disabled static library subpackage.

* Tue Jan 24 2006 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.2a-alt1
- Fixed potential build issue on fast CPU and filesystem with
  low timestamp resolution.

* Sun Sep 05 2004 Dmitry V. Levin <ldv@altlinux.org> 1.0.2a-ipl6mdk
- Added libnet-config(1) manpage.

* Tue Nov 11 2003 Dmitry V. Levin <ldv@altlinux.org> 1.0.2a-ipl5mdk
- Build the shared library with -fPIC.

* Thu Aug 21 2003 Alexey Tourbin <at@altlinux.ru> 1.0.2a-ipl4mdk
- memory leaks fixed in libnet_close_link_interface() functions
- _GNU_SOURCE defined to obtain random(3) and srandom(3) prototypes
- compiler warnings fixed (debian #106071)
- reference manual from libnet site added to devel package (debian)

* Sun Nov 24 2002 Dmitry V. Levin <ldv@altlinux.org> 1.0.2a-ipl3mdk
- Renamed to libnet1.
- Really build with packet socket support.

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
