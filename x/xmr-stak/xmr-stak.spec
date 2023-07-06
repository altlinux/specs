Name:		xmr-stak
Version:	2.10.8
Release:	alt2
Summary:	XMR-Stak - Cryptonight Mining Software
Url:		https://github.com/fireice-uk/xmr-stak
Group:		Office
License:	GPLv3
Source0:	%name.tar.xz
Patch0:	%name-libmicrohttpd.patch

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
%patch0 -p2

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
* Thu Jul  6 2023 Artyom Bystrov <arbars@altlinux.org> 2.10.8-alt2
- Fix build on GCC13

* Wed Apr 21 2021 Slava Aseev <ptrnine@altlinux.org> 2.10.8-alt1
- 2.10.8
- fix build with libmicrohttpd-0.9.71

* Wed Nov 14 2018 Motsyo Gennadi <drool@altlinux.ru> 2.5.2-alt1
- 2.5.2

* Wed Oct 24 2018 Motsyo Gennadi <drool@altlinux.ru> 2.5.1-alt1
- 2.5.1

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
