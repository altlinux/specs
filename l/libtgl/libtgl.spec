Name: libtgl
Version: 2.0.3.0.ffb04caca71
Release: alt1

Summary: library that handles telegram api and protocol

Group: Networking/Instant messaging
License: GPLv2

Url: https://github.com/vysheng/tgl
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Note: pack submodules to .gear/@name@-postsubmodules (as in .gear/rules)

# Source-git: https://github.com/vysheng/tgl.git
Source: %name-%version.tar

Patch: %name-soname.patch

# Automatically added by buildreq on Tue Mar 14 2017
# optimized out: i586-glibc-devel i586-libcrypto10 i586-libssl10 i586-zlib libcom_err-devel libkrb5-devel libssl-devel pkg-config python-base python-modules python3 python3-base zlib-devel
BuildRequires: libevent-devel zlib-devel libssl-devel

%description
This is library that handles telegram api and protocol.

Current versions:

scheme.tl: Layer 38
encrypted_scheme.tl: Layer 23

Documentation for Telegram API is available here: https://core.telegram.org/api

Documentation for MTproto protocol is available here: https://core.telegram.org/mtproto

%package devel
Group: Development/Other
Summary: Development files for %name

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.


%prep
%setup
%patch -p3

%build
%configure --enable-libevent
%make_build

%install
install -m644 -D libs/libtgl.so %buildroot%_libdir/libtgl.so.0
ln -s libtgl.so.0 %buildroot%_libdir/libtgl.so
mkdir -p %buildroot%_includedir/tgl/auto/
mkdir -p %buildroot%_includedir/tgl/crypto/
cp -a *.h %buildroot%_includedir/tgl/
cp -a auto/*.h %buildroot%_includedir/tgl/auto/
cp -a crypto/*.h %buildroot%_includedir/tgl/crypto/

%files
%_libdir/libtgl.so.0

%files devel
%_libdir/libtgl.so
%_includedir/tgl/*.h
%dir %_includedir/tgl/auto/
%_includedir/tgl/auto/*.h
%dir %_includedir/tgl/crypto/
%_includedir/tgl/crypto/*.h

%changelog
* Tue Mar 14 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.3.0.ffb04caca71-alt1
- new build with ffb04caca71de0cddf28cd33a4575922900a59ed

* Tue Jan 03 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1.cec82849cb4
- initial build for ALT Linux Sisyphus
