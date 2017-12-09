%def_without autotools

%define oname	cryptopp
Name: libcryptopp
Version: 5.6.5
Release: alt1

# convert 5.6.2 -> 562 format
%define orig_version	%(echo %version | sed -e "s/\\.//g")

Summary: Cryptopp Library - a free C++ class library of cryptographic schemes

License: Boost Software License
Url: http://www.cryptopp.com/
Group: System/Libraries

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://www.cryptopp.com/%oname%orig_version.zip
Source: %name-%version.tar

Patch: %oname-autotools.patch

Provides: libcrypto++ = %version-%release
Obsoletes: libcrypto++

# Automatically added by buildreq on Sun Jan 27 2008
BuildRequires: gcc-c++

%description
Cryptopp Library is a free C++ class library of cryptographic schemes.

Small intro in russian: http://andreyvit.livejournal.com/37576.html

%package devel
Summary: Files for development of applications which will use Cryptopp
Group: Development/C++
Requires: %name = %version-%release

Provides: libcrypto++-devel = %version-%release
Obsoletes: libcrypto++-devel

%description devel
Files for development of applications which will use Cryptopp.

%package devel-static
Summary: Static Cryptopp library
Group: Development/C++
Requires: %name-devel = %version-%release
Provides: %name-static
Obsoletes: %name-static

%description devel-static
Static Cryptopp library.

%package progs
Summary: Cryptopp programs
Group: File tools
Requires: %name = %version-%release

%description progs
Cryptopp programs.

%prep
%setup
%if_with autotools
%patch -p1
rm -f GNUmakefile
%endif
#touch NEWS README AUTHORS ChangeLog

%build
%add_optflags -fpermissive
%if_with autotools
%autoreconf
%configure
%ifnarch x86_64
# Does not build with PIC by default on x86, see
# http://groups.google.com/group/cryptopp-users/browse_thread/thread/d639907b0b1816b9
%__subst '1 i #define CRYPTOPP_DISABLE_SSE2' config.h
%endif
 %make_build
%else
 %make_build CXXFLAGS="%optflags %optflags_shared" PREFIX=%prefix static dynamic cryptest.exe
%endif


# too long
#%check
#./cryptest v 2>&1 | tee cryptest.log
#grep -qs '^FAILED' cryptest.log && exit 1 || :

%check
make test

%install
%if_with autotools
%makeinstall_std
%else
make install DESTDIR=%buildroot PREFIX=%_prefix LIBDIR=%_libdir
mv %buildroot%_bindir/cryptest.exe %buildroot%_bindir/cryptest
%endif

mkdir -p %buildroot%_pkgconfigdir/
cat >%buildroot%_pkgconfigdir/libcrypto++.pc <<EOF
Name: libcrypto++
Description: General purpose cryptographic shared library
URL: http://www.cryptopp.com
Version: %version
Requires:
Libs: -lcryptopp
Cflags:
EOF

%files
%doc License.txt Readme.txt
%_libdir/libcryptopp.so.*

%files devel
%_libdir/libcryptopp.so
%_includedir/cryptopp/
%_pkgconfigdir/*

%files devel-static
%_libdir/libcryptopp.a

%files progs
%_bindir/cryptest
#_bindir/cryptestcwd
%_datadir/cryptopp/

%changelog
* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 5.6.5-alt1
- new version 5.6.5 (with rpmrb script)
- return to native build
- enable check during build

* Sat Jan 30 2016 Vitaly Lipatov <lav@altlinux.ru> 5.6.3-alt1
- new version 5.6.3 (with rpmrb script)

* Sat Jul 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.2-alt1.1
- Rebuilt with gcc5

* Wed Jul 17 2013 Evgeny Sinelnikov <sin@altlinux.ru> 5.6.2-alt1
- Update to last stable release with multiple fixes and SHA-3 implemetation
- Change license from GPL to Boost Software License 1.0

* Tue Nov 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt3.qa3
- Fixed build with gcc 4.7

* Thu Aug 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt3.qa2
- Rebuilt for debuginfo

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt3.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Sun Dec 13 2009 Vitaly Lipatov <lav@altlinux.ru> 5.6.0-alt3
- really pack 5.6.0 (fix bug #22515)

* Wed Jul 22 2009 Vitaly Lipatov <lav@altlinux.ru> 5.6.0-alt2
- fix pkgconfig file

* Mon Jul 20 2009 Vitaly Lipatov <lav@altlinux.ru> 5.6.0-alt1
- new version 5.6.0 (with rpmrb script)
- add pkgconfig file (ALT #20826)

* Sat Mar 29 2008 Vitaly Lipatov <lav@altlinux.ru> 5.5.2-alt2
- fix devel-static package name

* Fri Jan 25 2008 Vitaly Lipatov <lav@altlinux.ru> 5.5.2-alt1
- new version (5.5.2), update autoconf/automake files
- disable asm code

* Fri Jan 25 2008 Vitaly Lipatov <lav@altlinux.ru> 5.2.1-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)

