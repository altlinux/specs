%define oname nspr

Name: mingw32-libnspr

Version: 4.8.7
Release: alt1

Summary: Netscape Portable Runtime (NSPR)

License: MPL/GPL/LGPL
Group: System/Libraries
Url: http://www.mozilla.org/projects/nspr/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: https://ftp.mozilla.org/pub/mozilla.org/nspr/releases/v%version/src/%oname-%version.tar

Patch1: nspr-pkgconfig.patch
Patch2: nspr-threads.patch

BuildArch: noarch

# MinGW-specific build patch.
Patch1000: nspr-4.8.6-build.patch

BuildRequires: rpm-build-mingw32
BuildRequires: mingw32-runtime >= 3.15.1
BuildRequires: mingw32-gcc
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-binutils

%description
Netscape Portable Runtime (NSPR) provides a platform-neutral API for system level and libc like functions.
The API is used in the Mozilla client, many of Netscape/AOL/iPlanet's and other software offerings.

%package devel
Summary: NSPR development kit
Group: Development/Other
# do not required
#Requires: %name = %version-%release

%description devel
NSPR development kit

%prep
%setup -n %oname-%version

%patch1 -p1

pushd mozilla/nsprpub
%patch2 -p0 -b .threads
%patch1000 -p0 -b .build
popd

%__subst \
	's@AC_CONFIG_AUX_DIR(\${srcdir}/build/autoconf)@AC_CONFIG_AUX_DIR(build/autoconf)@' \
	mozilla/nsprpub/configure.in

# Hack again incorrect behaviour
%__subst 's|NSINSTALL=nsinstall||g' mozilla/nsprpub/configure*

# _InterlockedIncrement provided only MSVC compiler
%__subst "s|_WIN32|_WIN32_ONLY_WINDOWS|g" mozilla/nsprpub/pr/include/pratom.h

%build
cd mozilla/nsprpub
%add_optflags %optflags_shared
HOST_CFLAGS=-D_WIN32 %_mingw32_configure \
	--includedir=%_mingw32_includedir/%oname \
	--with-mozilla \
%ifarch x86_64
	--enable-64bit \
%endif
	--enable-optimize="%_mingw32_cflags" \
	--enable-win32-target=WINNT \
	--enable-shared --enable-static \
	--enable-debug --disable-strip \
	--enable-64bit=no \
	--enable-mdupdate \
	--with-pthreads \
	--disable-cplus \
	#

# NSPR comes with its own "special" install program called nsinstall.
# This must be built as a native program.
%make -C config CC=gcc CFLAGS="-DXP_UNIX=1"

%make_build

%install
cd mozilla/nsprpub
#makeinstall install export \
#	RANLIB=%_mingw32_ranlib \
#	RC=%_mingw32_windres \
#	includedir=%buildroot/%_includedir/%name

# 'make install' doesn't appear to work, so do it by hand.
mkdir -p %buildroot%_mingw32_bindir
mkdir -p %buildroot%_mingw32_libdir/pkgconfig
install dist/bin/*.dll %buildroot%_mingw32_bindir/
install dist/lib/nspr4_s.a %buildroot%_mingw32_libdir/libnspr4.a
install dist/lib/plc4_s.a %buildroot%_mingw32_libdir/libplc4.a
install dist/lib/plds4_s.a %buildroot%_mingw32_libdir/libplds4.a
install dist/lib/nspr4.dll.a %buildroot%_mingw32_libdir/libnspr4.dll.a
install dist/lib/plc4.dll.a %buildroot%_mingw32_libdir/libplc4.dll.a
install dist/lib/plds4.dll.a %buildroot%_mingw32_libdir/libplds4.dll.a
install config/nspr-config %buildroot%_mingw32_bindir
install -m644 config/nspr.pc %buildroot%_mingw32_libdir/pkgconfig/
#install dist/lib/*.dll.a %buildroot%_mingw32_libdir/

mkdir -p %buildroot%_mingw32_includedir/nspr
cp -rL dist/include/nspr/* %buildroot%_mingw32_includedir/nspr/
# #include "file.h" -> #include <nspr/file.h>
find %buildroot/%_includedir/nspr -type f -name '*.h' -print0 |
    xargs -r0 sed -i -e 's@^\([[:space:]]*#include[[:space:]]\+\)"\([^"]\+\)"@\1<nspr/\2>@g'


%files
%_mingw32_bindir/nspr4.dll
%_mingw32_bindir/plc4.dll
%_mingw32_bindir/plds4.dll

%files devel
%_mingw32_bindir/nspr-config
%_mingw32_libdir/libnspr4.a
%_mingw32_libdir/libplc4.a
%_mingw32_libdir/libplds4.a
%_mingw32_libdir/libnspr4.dll.a
%_mingw32_libdir/libplc4.dll.a
%_mingw32_libdir/libplds4.dll.a
%_mingw32_libdir/pkgconfig/nspr.pc
%_mingw32_includedir/nspr/

#_datadir/%name-%version
#_datadir/aclocal/*

#%files -n lib%name-devel-static
#%_libdir/*.a

%changelog
* Fri Mar 25 2011 Vitaly Lipatov <lav@altlinux.ru> 4.8.7-alt1
- initial build for mingw

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

