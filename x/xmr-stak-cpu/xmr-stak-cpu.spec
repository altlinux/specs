Name:		xmr-stak-cpu
Version:	1.5.0
Release:	alt1
Summary:	Monero mining software (CPU)
Url:		https://github.com/fireice-uk/xmr-stak-cpu
Group:		Office
License:	GPLv3
Source0:	%name.tar.xz

ExclusiveArch:	x86_64

# Automatically added by buildreq on Mon Sep 18 2017 (-bi)
# optimized out: cmake-modules elfutils libcom_err-devel libgpg-error libkrb5-devel libp11-kit libstdc++-devel perl pkg-config python-base python-modules python3 python3-base rpm-build-python3 xz
BuildRequires: cmake gcc-c++ libhwloc-devel libmicrohttpd-devel libssl-devel python3-dev

%description
XMR-Stak is a universal Stratum pool miner. This is the CPU-mining version

%prep
%setup -n %name

%build
subst 's|2.0|0.1|g' donate-level.h
mkdir ./build && cd ./build
cmake		../. \
		-DCMAKE_BUILD_TYPE=STATIC \
		-DCMAKE_CXX_FLAGS:STRING="%optflags" \
		-DCMAKE_C_FLAGS:STRING="%optflags"
%make_build

%install
cd ./build
install -Dp -m 0755 ./bin/%name %buildroot%_bindir/%name
mkdir -p ../examples
cp -a ../config.txt ../examples/

%files
%doc LICENSE README.md ./examples
%_bindir/*

%changelog
* Mon Sep 18 2017 Motsyo Gennadi <drool@altlinux.ru> 1.5.0-alt1
- initial build for ALT Linux
