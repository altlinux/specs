%define oname	cryptopp
Name: libcryptopp
Version: 5.6.0
Release: alt3.qa1

# convert 5.6.0 -> 560 format
%define orig_version	%(echo %version | sed -e "s/\\.//g")

Summary: Cryptopp Library - a free C++ class library of cryptographic schemes

License: GPL
Url: http://www.cryptopp.com/
Group: System/Libraries

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.cryptopp.com/%oname%orig_version.tar.bz2
Patch: %oname-5.6.1-autotools.patch

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
%setup -c
%patch -p1
rm -f GNUmakefile
#touch NEWS README AUTHORS ChangeLog

%build
%autoreconf
%configure
%ifnarch x86_64
# Does not build with PIC by default on x86, see
# http://groups.google.com/group/cryptopp-users/browse_thread/thread/d639907b0b1816b9
%__subst '1 i #define CRYPTOPP_DISABLE_SSE2' config.h
%endif

%make_build

# too long
#%check
#./cryptest v 2>&1 | tee cryptest.log
#grep -qs '^FAILED' cryptest.log && exit 1 || :

%install
%makeinstall_std

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
#%_datadir/cryptopp/

%changelog
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

