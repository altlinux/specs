Name:		xmr-stak
Version:	2.4.7
Release:	alt2
Summary:	XMR-Stak - Cryptonight Mining Software
Url:		https://github.com/fireice-uk/xmr-stak
Group:		Office
License:	GPLv3
Source0:	%name.tar.xz

ExclusiveArch:	x86_64

BuildRequires: cmake gcc-c++ libhwloc-devel libmicrohttpd-devel libssl-devel-static

Provides:	%name-cpu
Obsoletes:	%name-cpu

%description
XMR-Stak is a universal Stratum pool miner. This miner supports CPUs, AMD and NVIDIA gpus
(GPU not supported in ALT Linux) and can be used to mine the crypto currencys Monero, Aeon
and many more Cryptonight coins.

%prep
%setup -n %name

%build
subst 's|2.0|0.1|g' ./xmrstak/donate-level.hpp
mkdir ./build && cd ./build
cmake		../. \
		-DCMAKE_BUILD_TYPE=STATIC \
		-DCMAKE_CXX_FLAGS:STRING="%optflags" \
		-DCMAKE_C_FLAGS:STRING="%optflags" \
		-DCUDA_ENABLE=OFF \
		-DOpenCL_ENABLE=OFF
%make_build

%install
cd ./build
install -Dp -m 0755 ./bin/%name %buildroot%_bindir/%name

%files
%doc doc/{FAQ.md,pgp_keys.md,tuning.md,usage.md}
%_bindir/*

%changelog
* Sun Sep 23 2018 Motsyo Gennadi <drool@altlinux.ru> 2.4.7-alt2
- fix build tag

* Sun Sep 23 2018 Motsyo Gennadi <drool@altlinux.ru> 2.4.7-alt1
- build new all-in-one version (without cuda and openCL)

* Sat Sep 22 2018 Alexey Shabalin <shaba@altlinux.org> 1.5.0-alt2
- rebuild with libmicrohttpd-0.9.59

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.5.0-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Mon Sep 18 2017 Motsyo Gennadi <drool@altlinux.ru> 1.5.0-alt1
- initial build for ALT Linux
