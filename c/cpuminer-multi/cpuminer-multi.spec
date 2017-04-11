Name:		cpuminer-multi
Version:	1.3.1
Release:	alt1
Summary:	Multi-threaded CPU miner
Url:		https://github.com/tpruvot/cpuminer-multi
Group:		Office
License:	GPLv2
Source0:	%name-linux.tar.xz
Source1:	README.txt
Source2:	cpuminer-conf.json.axiom
Source3:	cpuminer-conf.json.lyra2re
Source4:	cpuminer-conf.json.scryptjanenf16

# Automatically added by buildreq on Tue Apr 11 2017 (-bi)
# optimized out: elfutils gnu-config libstdc++-devel python-base python-modules xz
BuildRequires: gcc-c++ libcurl-devel libssl-devel zlib-devel

%description
This is a multi-threaded CPU miner,
fork of [pooler](//github.com/pooler)'s cpuminer (see AUTHORS for list of contributors).

For more informations visit:
https://www.nicehash.com/index.jsp?p=software#cpu

%prep
%setup -n %name-linux

%build
./autogen.sh
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
* Tue Apr 11 2017 Motsyo Gennadi <drool@altlinux.ru> 1.3.1-alt1
- initial build for ALT Linux
