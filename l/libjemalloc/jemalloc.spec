%define title jemalloc
Name: libjemalloc
Version: 3.0.0
Release: alt1
Summary: A general-purpose scalable concurrent malloc(3) implementation
Group: System/Libraries
License: BSD
Source: jemalloc-%version.tar.bz2
Url: http://www.canonware.com/jemalloc/

# Automatically added by buildreq on Thu Jan 12 2012
# optimized out: libgpg-error xml-common
BuildRequires: docbook-dtds docbook-style-xsl xsltproc

%description
jemalloc is a general-purpose scalable concurrent malloc(3)
implementation. There are several divergent versions of jemalloc in
active use, including:

 * FreeBSD's default system allocator (malloc.c, manual page). This was
    the first public use of jemalloc, and it is still author-maintained.
 * NetBSD's default system allocator (jemalloc.c).
 * Mozilla Firefox's allocator (source code), specifically for
   Microsoft Windows-related platforms, Solaris, and Linux. There is
   Apple Mac OS X support code as well, but it has never been used in a
   release.
 * The stand-alone jemalloc, which currently targets only Linux.
   Thus far I have had no driving need to integrate support for other
   operating systems into this version of jemalloc, but it is probable
   that the stand-alone jemalloc library's platform support will
    broaden over time.

%package devel
Summary: Development files, debugging and profiling version of %title
Group: System/Libraries
License: BSD
Requires: google-perftools

%description devel
Development files, debugging and profiling version of %title

%prep
%setup -n %title-%version

%build
CONF="--enable-swap --enable-xmalloc --enable-dss --enable-sysv --enable-prof --with-xslroot=/usr/share/xml/docbook/xsl-stylesheets"
%configure $CONF --enable-debug
%make_build
%make doc
mkdir -p debug
cp -p lib/lib* debug
%configure $CONF --enable-prof --enable-stats
%make_build
mkdir -p prof
cp -p lib/lib* prof
%configure $CONF
%make_build

%install
%makeinstall DESTDIR=%buildroot
mkdir -p %buildroot%_libdir/debug %buildroot%_libdir/prof
install debug/* %buildroot%_libdir/debug
( cd prof; for N in *; do
  install $N %buildroot%_libdir/${N%%.*}_profiler.${N##*.}
done )
mv %buildroot%_bindir/pprof %buildroot%_bindir/pprof.%title

%files
%doc %_defaultdocdir/jemalloc
%doc COPYING README INSTALL VERSION
%_libdir/%name.so.*
%_bindir/pprof.%title

%files devel
%_includedir/*
%_man3dir/*
%exclude %_libdir/%name.so.*
%_libdir/lib*.so*
%_libdir/lib*.a
%_libdir/debug/lib*

%changelog
* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 3.0.0-alt1
- Autobuild version bump to 3.0.0

* Tue Jan 10 2012 Fr. Br. George <george@altlinux.ru> 2.2.5-alt1
- Autobuild version bump to 2.2.5
- Documentation rebuilding added

* Wed Sep 07 2011 Fr. Br. George <george@altlinux.ru> 2.2.3-alt1
- Autobuild version bump to 2.2.3

* Tue Aug 16 2011 Fr. Br. George <george@altlinux.ru> 2.2.2-alt1
- Autobuild version bump to 2.2.2

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 2.2.1-alt1
- Autobuild version bump to 2.2.1

* Thu Mar 31 2011 Fr. Br. George <george@altlinux.ru> 2.2.0-alt1
- Autobuild version bump to 2.2.0

* Thu Mar 10 2011 Fr. Br. George <george@altlinux.ru> 2.1.2-alt1
- Autobuild version bump to 2.1.2

* Tue Feb 22 2011 Fr. Br. George <george@altlinux.ru> 2.1.1-alt1
- Autobuild version bump to 2.1.1

* Mon Dec 20 2010 Fr. Br. George <george@altlinux.ru> 2.1.0-alt1
- Autobuild version bump to 2.1.0

* Sun Nov 14 2010 Fr. Br. George <george@altlinux.ru> 2.0.1-alt1
- Autobuild version bump to 2.0.1

* Thu Oct 28 2010 Fr. Br. George <george@altlinux.ru> 2.0.0-alt1
- Autobuild version bump to 2.0.0

* Wed Aug 18 2010 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Version up

* Wed May 19 2010 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Version up

* Wed Apr 21 2010 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Version up

* Wed Apr 14 2010 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- Initial build from scratch

