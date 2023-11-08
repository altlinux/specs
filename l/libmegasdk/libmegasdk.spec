Name: libmegasdk
Version: 4.28.3
Release: alt1

Summary: MEGA SDK - Client Access Engine Coverity Scan Build Status

License: BSD 2-clause Simplified License
Group: System/Libraries
Url: https://github.com/meganz/sdk

# Source-url: https://github.com/meganz/sdk/archive/v%version.tar.gz
Source: v%version.tar.gz

#Source1: #name
#Source2: #name.service
#Source3: #name.conf
#Source4: #name-serv

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildRequires: doxygen
BuildRequires: gcc-c++
# devel-static due libstdc++fs.a
BuildRequires: libstdc++-devel-static
BuildRequires: libcares-devel libcryptopp-devel libcurl-devel libfreeimage-devel libfuse-devel libpcrecpp-devel
BuildRequires: libreadline-devel libsodium-devel libsqlite3-devel libssl-devel libuv-devel zlib-devel libicu-devel
BuildRequires: libavformat-devel libgomp-devel libraw-devel libswscale-devel libzen-devel libmediainfo-devel libcryptopp-devel
# FIXME: suddenly required for libcryptopp checking
BuildRequires: libudev-devel

%description
MEGA SDK - Client Access Engine Coverity Scan Build Status.

MEGA --- The Privacy Company --- is a Secure Cloud Storage provider
that protects your data thanks to end-to-end encryption.
We call it User Controlled Encryption, or UCE, and all our clients automatically manage it.

All files stored on MEGA are encrypted. All data transfers from and to MEGA are encrypted.
And while most cloud storage providers can and do claim the same,
MEGA is different - unlike the industry norm where the cloud storage provider holds the decryption key,
with MEGA, you control the encryption, you hold the keys, and you decide who you grant or deny access to your files.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: libmegasdk = %EVR

%description devel
This package contains the header and object files necessary for developing with
%name.

%package devel-qt5
Summary: Qt5 development binding files for %name
Group: Development/C
Requires: libmegasdk-devel = %EVR

%description devel-qt5
This package contains Qt5 development binding files for %name.

%package tools
Summary: Tools from MEGA SDK
Group: File tools
Requires: libmegasdk = %EVR

Conflicts: megafuse
Provides: megasymplesync = %EVR
Obsoletes: megasymplesync

%description tools
Example tools from MEGA SDK - Client Access Engine
* megacli (a powerful command line tool that allows to use all SDK features)
* megasimplesync (a command line tool that allows to use the synchronization engine)

%prep
%setup
# hack against missed --tag=CXX during linking
sed -i 's|ANDROID|TRUE|' Makefile.am

sed -i 's/#define CAP_TRUNCATED CODEC_CAP_TRUNCATED/#define CAP_TRUNCATED 0/' src/gfx/freeimage.cpp

sed -i 's|with_pcre/include|with_pcre|' configure.ac
sed -i 's|with_db/include|with_db|' configure.ac

%build
%autoreconf
#add_optflags -std=gnu++17
%configure --disable-static \
           --disable-java \
           --disable-php \
           --disable-python \
           --disable-curl-checks \
           --disable-gcc-hardening \
           --enable-drive-notifications \
           --enable-chat \
           --with-cares --with-curl --with-sodium --with-openssl --with-sqlite --with-zlib \
           --with-freeimage --with-pcre=%_includedir/pcre --with-fuse --with-libuv \
           --with-libzen --with-libmediainfo --with-ffmpeg --with-cryptopp \
           %nil

# only sqlite or db4
#           --with-db=%_includedir/db4

%make_build

%install
%makeinstall_std

# just copy, no qt build here
mkdir -p %buildroot/%_datadir/%name/qt5/
cp -a bindings/qt/* %buildroot/%_datadir/%name/qt5/

mkdir -p %buildroot/%_datadir/%name/m4/
cp -a m4/ax*.m4 %buildroot/%_datadir/%name/m4/

#mkdir -p %buildroot%_initdir/ %buildroot/lib/systemd/system/ %buildroot/etc/
#cp #SOURCE1 %buildroot%_initdir/
#cp #SOURCE2 %buildroot/lib/systemd/system/
#cp #SOURCE3 %buildroot/etc/
#cp #SOURCE4 %buildroot%_bindir/

# missed headers
cp include/mega/{mega_glob.h,mega_http_parser.h,textchat.h,nodemanager.h,setandelement.h,heartbeats.h} %buildroot/%_includedir/mega/
cp include/mega/posix/drivenotifyposix.h %buildroot/%_includedir/mega/posix/

%files
%_libdir/libmega.so.*

%files devel
%_includedir/mega/
%_includedir/*.h
%_libdir/pkgconfig/libmega.pc
%_libdir/libmega.so
%dir %_datadir/%name/
%_datadir/%name/m4/

%files devel-qt5
%_datadir/%name/qt5/

%files tools
%_bindir/megacli
#_bindir/megafuse
%_bindir/megasimplesync

%changelog
* Tue Nov 07 2023 Vitaly Lipatov <lav@altlinux.ru> 4.28.3-alt1
- new version 4.28.3 (with rpmrb script)

* Tue Sep 15 2020 Vitaly Lipatov <lav@altlinux.ru> 3.7.3b-alt1
- new version 3.7.3b (with rpmrb script)

* Sun Mar 08 2020 Vitaly Lipatov <lav@altlinux.ru> 3.6.8-alt1
- new version 3.6.8

* Wed Apr 10 2019 Fr. Br. George <george@altlinux.ru> 3.4.9-alt1
- Autobuild version bump to 3.4.9

* Sun Nov 25 2018 Vitaly Lipatov <lav@altlinux.ru> 3.4.3-alt1
- new version 3.4.3 (with rpmrb script)

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 3.4.0-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Aug 15 2018 Fr. Br. George <george@altlinux.ru> 3.4.0-alt1
- Autobuild version bump to 3.4.0

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 3.3.8-alt1
- new version 3.3.8 (with rpmrb script)
- rebuild with libcryptopp-6.1.0

* Mon Feb 12 2018 Vitaly Lipatov <lav@altlinux.ru> 3.2.8-alt3.1
- NMU: autorebuild with libsodium-1.0.16

* Sat Dec 23 2017 Vitaly Lipatov <lav@altlinux.ru> 3.2.8-alt3
- pack m4 subdir
- pack missed mega_glob.h, mega_http_parser.h

* Sat Dec 23 2017 Vitaly Lipatov <lav@altlinux.ru> 3.2.8-alt2
- build devel-qt5 subpackage with qt binding
- build with all possible libs

* Fri Dec 22 2017 Vitaly Lipatov <lav@altlinux.ru> 3.2.8-alt1
- rename source package, cleanup spec
- new version (3.2.8), change packager

* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt1.3
- NMU: autorebuild with libcryptopp-5.6.5

* Wed Jul 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5.0-alt1.2
- Updated build dependencies

* Tue Aug 18 2015 Danil Mikhailov <danil@altlinux.org> 2.5.0-alt3
- added two new packages libmegasdk and libmegasdk-devel

* Thu Aug 13 2015 Danil Mikhailov <danil@altlinux.org> 2.5.0-alt2
- fix bugs with /bin/sh in mss-serv, added $ to CONFIG var
- remove megafuse, use megafuse package

* Sat Jul 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.1
- Rebuilt with gcc5

* Mon May 25 2015 Danil Mikhailov <danil@altlinux.org> 2.5.0-alt1
- initial build for ALT Linux Sisyphus
