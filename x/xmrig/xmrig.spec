Name:		xmrig
Version:	2.4.3
Release:	alt1
Summary:	Monero (XMR) CPU miner
Url:		https://github.com/xmrig/xmrig
Group:		Office
License:	GPLv3
Source0:	%name.tar.xz

BuildRequires: cmake gcc-c++ libmicrohttpd-devel libstdc++-devel-static libuv-devel

%description
XMRig is high performance Monero (XMR) CPU miner, with the official full Windows support.
Originally based on cpuminer-multi with heavy optimizations/rewrites and removing a lot
of legacy code, since version 1.0.0 complete rewritten from scratch on C++.

%prep
%setup -n %name

%build
mkdir ./build && cd ./build
cmake		../. \
		-DCMAKE_BUILD_TYPE=Release \
		-DCMAKE_CXX_FLAGS:STRING="%optflags" \
		-DCMAKE_C_FLAGS:STRING="%optflags"
%make_build

%install
cd ./build
install -Dp -m 0755 ./%name %buildroot%_bindir/%name

%files
%doc LICENSE README.md CHANGELOG.md
%_bindir/*

%changelog
* Mon Nov 06 2017 Motsyo Gennadi <drool@altlinux.ru> 2.4.3-alt1
- initial build for ALT Linux
