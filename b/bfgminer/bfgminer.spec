Name:           bfgminer
Version:        5.5.0
Release:        alt2
Summary:        A multi-threaded BitCoin miner
Url:            http://bfgminer.org
Group:          Office
License:        GPLv3
Source:         %name-%version.tar
Patch0:         %name-%version-fno-common.patch
Patch1:         %name-%version-altivec.patch

BuildPreReq:	udev-rules

# Automatically added by buildreq on Thu Sep 14 2017 (-bi)
# optimized out: elfutils gnu-config libgpg-error libncurses-devel libp11-kit libtinfo-devel perl pkg-config python-base python-modules python3 python3-base rpm-build-python3 xz zlib-devel
BuildRequires: libcurl-devel libevent-devel libhidapi-devel libjansson-devel libmicrohttpd-devel libsensors3-devel libusb-devel libuthash-devel python3-dev yasm zlib-devel

%description
This is a multi-threaded multi-pool FPGA, GPU and CPU miner with ATI GPU
monitoring, (over)clocking and fanspeed support for bitcoin and derivative
coins.

%package devel
Summary: Development files for %name
Group: Development/C
PreReq: %name = %version-%release

%description devel
This package contains the header files and documentation needed
to develop applications with %name

%prep
%setup
%patch0 -p2
%patch1 -p2

%build
cat > version.h << EOF
# add version.h
#define BFG_GIT_DESCRIBE "%name-%version"
#ifdef VERSION
#  undef VERSION
#endif
#define VERSION "%version"
EOF
%add_optflags -no-pie
%autoreconf
%configure	--prefix=%prefix \
		--enable-keccak \
		--enable-scrypt \
		--enable-minergate \
		--enable-alchemist \
		--enable-bfsb \
		--enable-cpumining \
		--enable-bitmain \
		--enable-titan \
		--enable-minion \
		--enable-metabank \
		--enable-kncasic \
		--enable-jingtian \
		--enable-opencl \
		--enable-bfsb
%make_build

%install
make DESTDIR=%buildroot install

%files
%_docdir/%name
%_docdir/libbase58
%_bindir/*
%_sbindir/*
%_libdir/*.so.*
%_udevrulesdir/*.rules
%_datadir/%name

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%changelog
* Mon Apr 19 2021 Slava Aseev <ptrnine@altlinux.org> 5.5.0-alt2
- fix build due to:
  + -fno-common in gcc-10 (adapted gentoo patch)
  + -enable-default-pie (-no-pie added)
  + altivec related errors on ppc64le

* Tue Sep 18 2018 Alexey Shabalin <shaba@altlinux.org> 5.5.0-alt1
- 5.5.0
- build with libmicrohttpd-0.9.59

* Thu Sep 14 2017 Motsyo Gennadi <drool@altlinux.ru> 5.4.2-alt1
- initial build for ALT Linux
