%def_disable static
Summary:        Utility for computing hash sums and creating magnet links.
Name:           rhash
Version:        1.3.5
Release:        alt3
License:        MIT
Group:          File tools
URL:            http://rhash.sourceforge.net/
Source:         %name-%version.tar
Patch:          %name-%version.patch
BuildRequires:  gcc libssl-devel

%description
RHash is a console utility for calculation and verification of magnet links
and a wide range of hash sums like CRC32, MD4, MD5, SHA1, SHA256, SHA512,
AICH, ED2K, Tiger, DC++ TTH, BitTorrent BTIH, GOST R 34.11-94, RIPEMD-160,
HAS-160, EDON-R, Whirlpool and Snefru.
Hash sums are used to ensure and verify integrity of large volumes of data
for a long-term storing or transferring.

Features:
 * Output in a predefined (SFV, BSD-like) or a user-defined format.
 * Calculation of Magnet links and EDonkey 2000 links.
 * Updating hash files (adding hash sums of files missing in the hash file).
 * Ability to process directories recursively.
 * Portability: the program works the same on Linux, *BSD or Windows.

# LibRHash shared library, contains librhash.so.[major] only
%package -n lib%name
Summary:        LibRHash shared library
Group:          System/Libraries

%description -n lib%name
LibRHash is a professional, portable, thread-safe C library for computing
a wide variety of hash sums, such as CRC32, MD4, MD5, SHA1, SHA256, SHA512,
AICH, ED2K, Tiger, DC++ TTH, BitTorrent BTIH, GOST R 34.11-94, RIPEMD-160
HAS-160, EDON-R, Whirlpool and Snefru.
Hash sums are used to ensure and verify integrity of large volumes of data
for a long-term storing or transferring.

%package -n lib%name-devel
Summary:        Headers and shared library for LibRHash
Group:          Development/C
Requires:       lib%name = %version-%release

%description -n lib%name-devel
LibRHash is a professional, portable, thread-safe C library for computing
a wide variety of hash sums, such as CRC32, MD4, MD5, SHA1, SHA256, SHA512,
AICH, ED2K, Tiger, DC++ TTH, BitTorrent BTIH, GOST R 34.11-94, RIPEMD-160
HAS-160, EDON-R, Whirlpool and Snefru.
Hash sums are used to ensure and verify integrity of large volumes of data
for a long-term storing or transferring.

%package -n lib%name-devel-static
Summary:        Static library for LibRHash
Group:          Development/C
Requires:       lib%name-devel = %version-%release

%description -n lib%name-devel-static
LibRHash is a professional, portable, thread-safe C library for computing
a wide variety of hash sums, such as CRC32, MD4, MD5, SHA1, SHA256, SHA512,
AICH, ED2K, Tiger, DC++ TTH, BitTorrent BTIH, GOST R 34.11-94, RIPEMD-160
HAS-160, EDON-R, Whirlpool and Snefru.
Hash sums are used to ensure and verify integrity of large volumes of data
for a long-term storing or transferring.

%prep
%setup
%patch -p1

%build
make CFLAGS="$RPM_OPT_FLAGS -DNDEBUG -DUSE_OPENSSL -DOPENSSL_RUNTIME -rdynamic" LDFLAGS=-ldl lib-shared build-shared all

%check
make test-shared

%install
make PREFIX=%_prefix DESTDIR="%buildroot" MANDIR="%_mandir" LIBDIR="%_libdir" install install-lib-static install-lib-shared install-shared-binary
make PREFIX=%_prefix DESTDIR="%buildroot" MANDIR="%_mandir" LIBDIR="%_libdir" -C librhash install-so-link install-headers

%if_disabled static
rm -v %buildroot%_libdir/librhash.a
%endif

%files
%_bindir/*
%config %_sysconfdir/rhashrc
%_man1dir/*

%files -n lib%name-devel
%_libdir/librhash.so
%_includedir/*.h

%if_enabled static
%files -n lib%name-devel-static
%_libdir/librhash.a
%endif

%files -n lib%name
%doc COPYING README ChangeLog
%_libdir/librhash.so.*

%changelog
* Thu Sep 30 2021 Vitaly Lipatov <lav@altlinux.ru> 1.3.5-alt3
- NMU: disable build devel-static subpackage

* Mon Sep 11 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.5-alt2
- fix requires for static package

* Mon Sep 11 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.5-alt1
- 1.3.5
- add static library package

* Wed Jul 31 2013 Evgeny Sinelnikov <sin@altlinux.ru> 1.2.10-alt1
- Initial Sisyphus release based on original specfile by Aleksey Kravchenko
  from Novosibirsk, Animegorodok last build for mdk in 14 September 2011
 + Upstream git repository^ git://github.com/rhash/RHash.git
 + Author contact: Aleksey <rhash.admin@gmail.com>

