Name: fastnetmon
Version: 1.1.1
Release: alt3
Summary: A high performance DoS/DDoS load analyzer.
Group: Networking/Other

Packager: Alexei Takaseev <taf@altlinux.ru>

License: GPLv2
Url: https://github.com/FastVPSEestiOu/fastnetmon
Source0: %name-%version.tar

#BuildPreReq: rpm-macros-cmake
# Automatically added by buildreq on Tue May 05 2015
# optimized out: boost-devel-headers cmake-modules libcloog-isl4 libstdc++-devel libtinfo-devel
BuildRequires: boost-devel cmake gcc-c++ liblog4cpp-devel libncurses-devel libpcap-devel

BuildRequires: liblog4cpp-devel libpfring-devel gcc-c++ boost-devel cmake

%description
A high performance DoS/DDoS load analyzer built on top of multiple packet capture
engines (NetFlow, IPFIX, sFLOW, netmap, PF_RING, PCAP).

%prep
%setup

%build
cd src
%cmake -DDISABLE_PF_RING_SUPPORT=YES

%cmake_build

%install
make install/fast DESTDIR=%buildroot -C src/BUILD

mkdir -p %buildroot%_sysconfdir
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_unitdir
mkdir -p %buildroot%_localstatedir/%name
install -m644 src/%name.service %buildroot%_unitdir/%name.service
install -m644 src/%name.conf %buildroot%_sysconfdir/%name.conf
install -m755 %name.init %buildroot%_initdir/%name

mv docs/THANKS.md ./

%files
%_bindir/*
%config %_initdir/%name
%config(noreplace) %_sysconfdir/%name.conf
%_unitdir/*
%_localstatedir/%name
%doc README.md THANKS.md


%changelog
* Mon May 11 2015 Alexei Takaseev <taf@altlinux.org> 1.1.1-alt3
- update to git:7170f257cfaf2638d5735d8f165507962c43f139

* Fri May 08 2015 Alexei Takaseev <taf@altlinux.org> 1.1.1-alt2
- update to git:b4e1a9cc7779c33841d7cec41b94232a519299de

* Thu Apr 30 2015 Alexei Takaseev <taf@altlinux.org> 1.1.1-alt1
- Initial build for ALT
