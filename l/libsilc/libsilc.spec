# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/ar /usr/bin/bison /usr/bin/dot /usr/bin/doxygen /usr/bin/gtkdocize /usr/bin/guile /usr/bin/guile-config /usr/bin/indent /usr/bin/ld /usr/bin/nasm /usr/bin/pkg-config /usr/bin/valgrind /usr/bin/yasm cppunit-devel gcc-c++ gcc-fortran glib2-devel guile18-devel libGL-devel libGLU-devel libSDL-devel libSDL_image-devel libX11-devel libaccounts-glib-devel libexpat-devel libflac-devel libgcrypt-devel libglibmm-devel libgmp-devel libgpgme-devel libifp-devel libmpfr-devel libmutil-devel libncurses-devel liboggz-devel libreadline-devel libsigc++2-devel libsilc-devel libspeex-devel libtinfo-devel libusb-compat-devel libuuid-devel libvorbis-devel libxml2-devel pkgconfig(check) pkgconfig(dbus-1) pkgconfig(freetype2) pkgconfig(glib-2.0) pkgconfig(gnutls-extra) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0) python-module-pygobject-devel pkgconfig(pygtk-2.0) python-devel unzip zlib-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Summary: SILC Client Library
Name:    libsilc
Version: 1.1.10
Release: alt2_6.1
License: GPLv2 or BSD
Group:   System/Libraries
URL:     http://www.silcnet.org/
Source0: http://www.silcnet.org/download/toolkit/sources/silc-toolkit-%{version}.tar.bz2
Patch0:  silc-toolkit-1.1-wordsize.patch
Patch1:  silc-toolkit-1.1.5-docinst.patch
Patch2:  silc-toolkit-1.1.10-libs.patch
BuildRequires: libidn-devel
BuildRequires: libtool autoconf automake
Source44: import.info

%description
SILC Client Library libraries for clients to connect to SILC networks.

SILC (Secure Internet Live Conferencing) is a protocol which provides
secure conferencing services on the Internet over insecure channel.

%package devel
Summary: Headers and shared libraries for %{name}
Group:   Development/C
Requires: libsilc = %{version}-%{release}

%description devel
The SILC Toolkit development libraries and headers. Required for building
SILC clients.

%package doc
Summary: Development documentation for %{name}
Group:   Documentation

%description doc
The SILC Toolkit documentation in HTML format. Useful for writing new SILC
applications.

%prep
%setup -q -n silc-toolkit-%{version}
%patch0 -p1 -b .wordsize
%patch1 -p1 -b .docinst
%patch2 -p1 -b .libs

# filter out libsilc module SONAME Provides (#245323)
cat << \EOF > %{name}-prov
#!/bin/sh
sed -e '\,/silc/modules/,d' |\
%{__find_provides} $*
EOF

%define _use_internal_dependency_generator 0
%define __find_provides %{_builddir}/silc-toolkit-%{version}/%{name}-prov
chmod +x %{__find_provides}

%build
autoreconf -f -i
%configure --libdir=%{_libdir} --enable-shared --without-libtoolfix \
           --includedir=%{_includedir}/silc --with-simdir=%{_libdir}/silc/modules \
           --docdir=%{_docdir}/%{name}-%{version} CFLAGS="$RPM_OPT_FLAGS"

# WARNING! smp flags cause bad binaries!
make

%install
# clear the buildroot

# make install
make DESTDIR=$RPM_BUILD_ROOT install
chmod 0755 ${RPM_BUILD_ROOT}%{_libdir}/lib* ${RPM_BUILD_ROOT}%{_libdir}/silc/modules/*.so

# move doc files that would be deleted by rpm
mkdir docinst
mv $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/{toolkit,tutorial} docinst/
# fix encoding of zlib.html
mv docinst/toolkit/zlib.html docinst/toolkit/zlib.html.orig
iconv -f iso-8859-15 -t utf8 -o docinst/toolkit/zlib.html docinst/toolkit/zlib.html.orig
rm -f docinst/toolkit/zlib.html.orig

# remove files we don't want into the package, but are being installed to buildroot
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/silcalgs.conf $RPM_BUILD_ROOT%{_sysconfdir}/silcd.conf

# remove .a and .la
rm -f $RPM_BUILD_ROOT%{_libdir}/libsilc.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libsilc.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libsilcclient.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libsilcclient.la

# Fix encoding of CREDITS
mv CREDITS CREDITS.orig
iconv -f iso-8859-15 -t utf8 -o CREDITS CREDITS.orig

%check
# If this fails, the filter-provides script needs an update.
[ -d $RPM_BUILD_ROOT%{_libdir}/silc/modules ]

%files
%doc COPYING BSD GPL doc/FAQ CREDITS
%{_libdir}/libsilc-1.1.so.*
%{_libdir}/libsilcclient-1.1.so.*
%dir %_libdir/silc
%dir %_libdir/silc/modules
%{_libdir}/silc/modules/*.so

# sub-package libsilc-devel
%files devel
%{_libdir}/libsilc.so
%{_libdir}/libsilcclient.so
%{_libdir}/pkgconfig/silc.pc
%{_libdir}/pkgconfig/silcclient.pc
%dir %_includedir/silc
%{_includedir}/silc/*.h

%files doc
%doc COPYING BSD GPL
%doc docinst/toolkit
%doc docinst/tutorial


%changelog
* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.10-alt2_6.1
- Fixed build

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt2_6
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt2_5
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt1_5
- initial import by fcimport

