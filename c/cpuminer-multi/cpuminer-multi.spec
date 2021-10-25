Name:		cpuminer-multi
Version:	1.3.5
Release:	alt4
Summary:	Multi-threaded CPU miner
Url:		https://github.com/tpruvot/cpuminer-multi
Group:		Office
License:	GPLv2
ExclusiveArch:	%ix86 x86_64
Source0:	%name-linux.tar.xz
Source1:	README.txt
Source2:	cpuminer-conf.json.axiom
Source3:	cpuminer-conf.json.lyra2re
Source4:	cpuminer-conf.json.scryptjanenf16
Patch:		%name-%version-gcc-11.patch

# Automatically added by buildreq on Tue Apr 11 2017 (-bi)
# optimized out: elfutils gnu-config libstdc++-devel python-base python-modules xz
BuildRequires: gcc-c++ libcurl-devel libssl-devel zlib-devel /usr/bin/xz

%description
This is a multi-threaded CPU miner,
fork of [pooler](//github.com/pooler)'s cpuminer (see AUTHORS for list of contributors).

For more informations visit:
https://www.nicehash.com/index.jsp?p=software#cpu

%prep
%setup -n %name-linux
%patch -p1

%build
./autogen.sh
%ifarch %ix86
%add_optflags -no-pie
%endif
%configure CFLAGS="%optflags" CXXFLAGS="%optflags" --with-crypto --with-curl
%make_build

%install
make DESTDIR=%buildroot install
mkdir -p ./examples
install -Dp -m 644 {%SOURCE1,%SOURCE2,%SOURCE3,%SOURCE4} ./examples/

%files
%doc AUTHORS COPYING LICENSE NEWS README.md ./examples
%_bindir/*
%_man1dir/*

%changelog
* Mon Oct 25 2021 Slava Aseev <ptrnine@altlinux.org> 1.3.5-alt4
- Fix FTBFS with gcc-11

* Thu Apr 22 2021 Slava Aseev <ptrnine@altlinux.org> 1.3.5-alt3
- Use -no-pie on ix86 only

* Thu Apr 22 2021 Slava Aseev <ptrnine@altlinux.org> 1.3.5-alt2
- Fix FTBFS due to --enable-default-pie

* Wed Oct 24 2018 Motsyo Gennadi <drool@altlinux.ru> 1.3.5-alt1
- 1.3.5

* Thu Sep 27 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.3.4-alt1.qa1
- Added ExclusiveArch: %%ix86 x86_64.

* Tue Apr 10 2018 Motsyo Gennadi <drool@altlinux.ru> 1.3.4-alt1
- 1.3.4

* Wed Jun 21 2017 Motsyo Gennadi <drool@altlinux.ru> 1.3.3-alt1
- 1.3.3 (handle a new tribus algo)

* Thu May 11 2017 Motsyo Gennadi <drool@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Tue Apr 11 2017 Motsyo Gennadi <drool@altlinux.ru> 1.3.1-alt1
- initial build for ALT Linux
