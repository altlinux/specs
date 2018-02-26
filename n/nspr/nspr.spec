Summary:	Netscape Portable Runtime (NSPR)
Name:		nspr
Version:	4.9.0
Release:	alt1
Epoch:		1
License:	MPL/GPL/LGPL
Group:		System/Libraries
Url:		http://www.mozilla.org/projects/nspr/
Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	%name-%version.tar
Source1:	%name.pc.in

# Automatically added by buildreq on Wed Feb 13 2008 (-bi)
BuildRequires: gcc-c++

%description
Netscape Portable Runtime (NSPR) provides a platform-neutral API for system level and libc like functions. 
The API is used in the Mozilla client, many of Netscape/AOL/iPlanet's and other software offerings.

%package -n lib%name
Summary:        Netscape Portable Runtime (NSPR)
Group:          System/Libraries
Provides:	%name = %version-%release

%description -n lib%name
Netscape Portable Runtime (NSPR) provides a platform-neutral API for system level and libc like functions. 
The API is used in the Mozilla client, many of Netscape/AOL/iPlanet's and other software offerings.

%package -n lib%name-devel
Summary: NSPR development kit
Group: Development/C
Requires: lib%name = %epoch:%version-%release
Provides: %name-devel = %version-%release

%description -n lib%name-devel
NSPR development kit

%package -n lib%name-devel-static
Summary: NSPR static libraries
Group: Development/C
Requires: lib%name-devel = %epoch:%version-%release
Provides: %name-devel-static = %version-%release

%description -n lib%name-devel-static
NSPR development kit (static libs)

%prep
%setup -q

sed -i \
	-e 's@AC_CONFIG_AUX_DIR(\${srcdir}/build/autoconf)@AC_CONFIG_AUX_DIR(build/autoconf)@' \
	mozilla/nsprpub/configure.in

%build
cd mozilla/nsprpub
%add_optflags %optflags_shared
%configure \
	--includedir=%_includedir/%name \
	--with-mozilla \
%ifarch x86_64
	--enable-64bit \
%endif
	--enable-optimize="$RPM_OPT_FLAGS" \
	--enable-mdupdate \
	--with-pthreads \
	--disable-cplus \
	#

%make_build

%install
cd mozilla/nsprpub
%makeinstall install export \
	  includedir=%buildroot/%_includedir/%name

find %buildroot/%_includedir/nspr -type f -name '*.h' -print0 |
    xargs -r0 sed -i -e 's@^\([[:space:]]*#include[[:space:]]\+\)"\([^"]\+\)"@\1<nspr/\2>@g'

%__mkdir_p %buildroot/%_datadir/%name-%version
mv -f %buildroot/%_bindir/prerr.properties %buildroot/%_datadir/%name-%version/

NSPR_LIBS=`%buildroot/%_bindir/nspr-config --libs`
NSPR_CFLAGS=`%buildroot/%_bindir/nspr-config --cflags`
NSPR_VERSION=`%buildroot/%_bindir/nspr-config --version`
%__mkdir_p %buildroot/%_libdir/pkgconfig
sed -e "s,@libdir@,%_libdir,g" \
    -e "s,@prefix@,%_prefix,g" \
    -e "s,@exec_prefix@,%_prefix,g" \
    -e "s,@includedir@,%_includedir/nspr,g" \
    -e "s,@NSPR_VERSION@,$NSPR_VERSION,g" \
    -e "s,@FULL_NSPR_LIBS@,$NSPR_LIBS,g" \
    -e "s,@FULL_NSPR_CFLAGS@,$NSPR_CFLAGS,g" \
	%SOURCE1 > %buildroot/%_libdir/pkgconfig/nspr.pc

%files -n lib%name
%_libdir/*.so*

%files -n lib%name-devel
%_bindir/%name-config
%_includedir/nspr
%_libdir/pkgconfig/*
%_datadir/%name-%version
%_datadir/aclocal/*

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Wed Apr 18 2012 Alexey Gladkov <legion@altlinux.ru> 1:4.9.0-alt1
- New stable release 4.9.

* Wed Aug 17 2011 Alexey Gladkov <legion@altlinux.ru> 1:4.8.9-alt1
- New stable release 4.8.9.

* Tue Mar 08 2011 Dmitry V. Levin <ldv@altlinux.org> 1:4.8.7-alt2
- Renamed Serial to Epoch, fixed interpackage dependencies.
- Built without --enable-strip to enable debuginfo.

* Fri Feb 25 2011 Alexey Gladkov <legion@altlinux.ru> 1:4.8.7-alt1
- New stable release 4.8.7.

* Sun Oct 24 2010 Alexey Gladkov <legion@altlinux.ru> 1:4.8.6-alt1
- New stable release 4.8.6.

* Mon May 31 2010 Alexey Gladkov <legion@altlinux.ru> 1:4.8.5-alt0.20100531
- New cvs snapshot 4.8.5 20100531.

* Sun Mar 28 2010 Alexey Gladkov <legion@altlinux.ru> 1:4.8.4-alt1
- New stable release 4.8.4.

* Mon Nov 09 2009 Alexey Gladkov <legion@altlinux.ru> 1:4.8.2-alt1
- New stable release 4.8.2.
- Fix CVE-2009-1563, CVE-2009-2463 (ALT#22207).

* Mon Jun 01 2009 Alexey Gladkov <legion@altlinux.ru> 1:4.8.0-alt1
- new stable release 4.8.0.

* Tue Nov 18 2008 Alexey Gladkov <legion@altlinux.ru> 1:4.7.3-alt1
- new stable release 4.7.3.

* Sat Jun 28 2008 Alexey Gladkov <legion@altlinux.ru> 1:4.7.2-alt1.20080628
- new cvs snapshot 4.7.2 20080628.

* Wed Jun 25 2008 Alexey Gladkov <legion@altlinux.ru> 1:4.7.2-alt1.20080625
- new cvs snapshot 4.7.2 20080625.

* Fri May 30 2008 Alexey Gladkov <legion@altlinux.ru> 1:4.7.2-alt1.20080530
- new cvs snapshot 4.7.1 20080530.
- Add libnspr-devel-static package.

* Tue May 13 2008 Alexey Gladkov <legion@altlinux.ru> 1:4.7.2-alt1.20080512
- new cvs snapshot 4.7.1 20080512.
* Fri Mar 21 2008 Alexey Gladkov <legion@altlinux.ru> 1:4.7.1-alt1.20080321
- new cvs snapshot 4.7.1 20080321.

* Fri Feb 29 2008 Alexey Gladkov <legion@altlinux.ru> 1:4.7.1-alt1.20080229
- new cvs snapshot 4.7.1 20080229.

* Sat Feb 02 2008 Alexey Gladkov <legion@altlinux.ru> 1:4.7-alt1.20080202
- new cvs snapshot 20080202.

* Thu Jan 10 2008 Alexey Gladkov <legion@altlinux.ru> 1:4.7-alt1.20071127
- new cvs snapshot 20071127.

* Thu Sep 27 2007 Alexey Gladkov <legion@altlinux.ru> 1:4.6.7-alt1
- new stable release 4.6.7.

* Fri Feb 23 2007 Alexey Gladkov <legion@altlinux.ru> 1:4.6.5-alt1
- new stable release 4.6.5.

* Sun Oct 29 2006 Alexey Gladkov <legion@altlinux.ru> 1:4.6.3-alt1
- new stable release 4.6.3.

* Sun Feb 19 2006 Alexey Gladkov <legion@altlinux.ru> 4.7.0.cvs20060807-alt1
- new cvs snapshot 20060807.

* Wed Dec 21 2005 Alexey Gladkov <legion@altlinux.ru> 4.7.0.cvs20051124-alt2
- nspr.pc was added.

* Thu Nov 24 2005 Alexey Gladkov <legion@altlinux.ru> 4.7.0-alt1.cvs20051124
- new cvs snapshot.
- build with --disable-cplus.

* Mon Oct 17 2005 Alexey Gladkov <legion@altlinux.ru> 4.7.0-alt1.cvs
- initial build for ALT Linux.

