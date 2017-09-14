Name:           bfgminer
Version:        5.4.2
Release:        alt1
Summary:        A multi-threaded BitCoin miner
Url:            http://bfgminer.org
Group:          Office
License:        GPLv3
Source0:        %name-%version.txz

BuildPreReq:	udev-rules

# Automatically added by buildreq on Thu Sep 14 2017 (-bi)
# optimized out: elfutils gnu-config libgpg-error libncurses-devel libp11-kit libtinfo-devel perl pkg-config python-base python-modules python3 python3-base rpm-build-python3 xz zlib-devel
BuildRequires: libcurl-devel libevent-devel libhidapi-devel libjansson-devel libmicrohttpd-devel libsensors3-devel libusb-devel libuthash-devel python3-dev yasm

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

%build
NOAUTOCONF=1 ./autogen.sh
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
* Thu Sep 14 2017 Motsyo Gennadi <drool@altlinux.ru> 5.4.2-alt1
- initial build for ALT Linux
