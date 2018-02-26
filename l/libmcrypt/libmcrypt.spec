Name: libmcrypt
Version: 2.5.8
Release: alt1

Summary: Encryption/decryption library
License: LGPL
Group: System/Libraries
Url: http://mcrypt.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sf.net/%name/%name-%version.tar.bz2
Patch: libmcrypt-2.5.7-alt-libdl.patch
Patch1: libmcrypt-2.5.1-dlopen.patch
Patch2: libmcrypt-2.5.1-symbols.patch
Patch3: libmcrypt-2.5.1-extra.patch
Patch4: libmcrypt-2.5.7-automake.patch

Source1: mcrypt_symb.c

# Automatically added by buildreq on Sat May 19 2012
# optimized out: libstdc++-devel
BuildRequires: gcc-c++ glibc-devel-static

%package devel
Summary: Development environment for %name
Group: Development/Other
Requires: %name = %version-%release

%package devel-static
Summary: Development environment for %name
Group: Development/Other
Requires: %name-devel = %version-%release

%description
The libmcrypt is a data encryption library. The library is thread safe
and provides encryption and decryption functions. This version of the
library supports many encryption algorithms and encryption modes. Some
algorithms which are supported: SERPENT, RIJNDAEL, 3DES, GOST, SAFER+,
CAST-256, RC2, XTEA, 3WAY, TWOFISH, BLOWFISH, ARCFOUR, WAKE and more.

%description devel
This package contains the header files and libraries needed
to develop programs that use the %name library.

%description devel-static
This package contains static libraries.

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
#patch4

%__subst 's,libmcrypt_la_LIBADD = @EXTRA_OBJECTS@,,' lib/Makefile.am

(cd modules
    find . -type f -name '*.c'|xargs %__subst 's/#define _.*//'
)

# only invalid libtool.m4 inclusion
rm -f acinclude.m4
#rm -rf libltdl/

%build
%autoreconf 
# Since 2.5.4 libmcrypt does not use dynamic loading for the modules by default
%configure --enable-static --disable-ltdl \
           --disable-libtool-lock --disable-dynamic-loading

cp %SOURCE1 lib

%make_build 

%install
%makeinstall_std

mkdir -p %buildroot%_libdir/%name

for i in  modes algorithms
do
    cp modules/$i/.libs/*.so %buildroot%_libdir/%name
    #cp modules/$i/.libs/*.la %buildroot%_libdir/%name
    cp modules/$i/.libs/*.a %buildroot%_libdir/%name
done

%files
%_libdir/*.so.*
%dir %_libdir/%name
%_libdir/%name/*.so

%files devel
%doc AUTHORS NEWS README THANKS TODO doc/{README.*,example.c}
%_bindir/*
%_libdir/*.so
%_includedir/*
%_mandir/man?/*
%_datadir/aclocal/*

%files devel-static
%_libdir/*.a
%_libdir/%name/*.a

# TODO: add test for module working (from example?)
# TODO: remove strange hacking for build & install

%changelog
* Sun May 27 2012 Andrew Clark <andyc@altlinux.ru> 2.5.8-alt1
- version update to 2.5.8

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 2.5.7-alt2.qa2
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.5.7-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libmcrypt
  * postun_ldconfig for libmcrypt
  * postclean-05-filetriggers for spec file

* Mon Nov 20 2006 Vitaly Lipatov <lav@altlinux.ru> 2.5.7-alt2
- change packager
- fix bug #6977
- remove libdir/name from devel packages

* Fri Feb 27 2004 Stanislav Ievlev <inger@altlinux.org> 2.5.7-alt1.2
- fix building with new autotools

* Wed Dec 03 2003 Stanislav Ievlev <inger@altlinux.org> 2.5.7-alt1.1
- remove .la files

* Fri Mar 28 2003 Stanislav Ievlev <inger@altlinux.ru> 2.5.7-alt1
- 2.5.7

* Tue Oct 22 2002 Stanislav Ievlev <inger@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Tue Jun 04 2002 Stanislav Ievlev <inger@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Mon Jan 21 2002 Stanislav Ievlev <inger@altlinux.ru> 2.4.19-alt1
- 2.4.19
- removed -lltdl from libmcrypt.m4
- libtool suxx, but author love it.

* Wed Sep 19 2001 Stanislav Ievlev <inger@altlinux.ru> 2.4.16b-alt1
- 2.4.16b
- backport support for normal libdl instead ltdl.

* Fri Jul 06 2001 Stanislav Ievlev <inger@altlinux.ru> 2.4.15-alt1
- 2.4.15

* Wed May 16 2001 Stanislav Ievlev <inger@altlinux.ru> 2.4.11-alt1
- 2.4.11. Statification

* Fri Mar 30 2001 Stanislav Ievlev <inger@altlinux.ru> 2.4.10-alt2
- Upgrade to current cvs-state. Bugfix memory leak

* Thu Mar 29 2001 Stanislav Ievlev <inger@altlinux.ru> 2.4.10-alt1
- Upgrade to 2.4.10

* Thu Feb 08 2001 Dmitry V. Levin <ldv@fandra.org> 2.4.9-ipl1
- Initial revision.
