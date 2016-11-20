Name: fastnetmon
Version: 1.1.3
Release: alt1.git20161119
Summary: A high performance DoS/DDoS load analyzer.
Group: Networking/Other

Packager: Alexei Takaseev <taf@altlinux.ru>

License: GPLv2
Url: https://github.com/pavel-odintsov/fastnetmon
Source0: %name-%version.tar

# Automatically added by buildreq on Wed Dec 23 2015
# optimized out: boost-devel boost-devel-headers cmake-modules libbson-devel libjson-c libsasl2-3 libstdc++-devel libtinfo-devel
BuildRequires: boost-asio-devel boost-program_options-devel cmake gcc-c++ libhiredis-devel
BuildRequires: libjson-c-devel liblog4cpp-devel libluajit-devel libmongoc-devel libnDPI-devel
BuildRequires: libncurses-devel libpcap-devel

# Temporary, while upstream fix
ExclusiveArch: x86_64

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

%files
%_bindir/*
%_sbindir/*
%config %_initdir/%name
%config(noreplace) %_sysconfdir/fastnetmon.conf
%config(noreplace) %_sysconfdir/networks_list
%config(noreplace) %_sysconfdir/networks_whitelist
%_unitdir/*
%_localstatedir/%name
%doc README.md docs
%_mandir/man1/*


%changelog
* Sun Nov 20 2016 Alexei Takaseev <taf@altlinux.org> 1.1.3-alt1.git20161119
- update to git:a1659df66a8b129784761cb068f5d0f44bf20239

* Sun Sep 18 2016 Alexei Takaseev <taf@altlinux.org> 1.1.3-alt1.git10092016
- update to git:70bbdf94836d32100dc03b8ff8b52c984f0d5d9a

* Tue Jul 05 2016 Alexei Takaseev <taf@altlinux.org> 1.1.3-alt1
- 1.1.3

* Mon Jul 04 2016 Alexei Takaseev <taf@altlinux.org> 1.1.2-alt4
- fix build with luajit-2.1
- update to git:11522e4d905ca2bacb1510a107b7bd654f58016e

* Sun Dec 27 2015 Alexei Takaseev <taf@altlinux.org> 1.1.2-alt3
- update to git:0f2be7279cc47473dab05f4f02daca60576d19e7
- Build only x86_64

* Wed Dec 23 2015 Alexei Takaseev <taf@altlinux.org> 1.1.2-alt2
- update to git:fd3ddc7ca60c530318a735ebf10d731ed3660dc9

* Wed Jun 03 2015 Alexei Takaseev <taf@altlinux.org> 1.1.2-alt1
- 1.1.2

* Tue May 12 2015 Alexei Takaseev <taf@altlinux.org> 1.1.1-alt4
- update to git:3829c685b9425491007e22b8622778f586df4986

* Mon May 11 2015 Alexei Takaseev <taf@altlinux.org> 1.1.1-alt3
- update to git:7170f257cfaf2638d5735d8f165507962c43f139

* Fri May 08 2015 Alexei Takaseev <taf@altlinux.org> 1.1.1-alt2
- update to git:b4e1a9cc7779c33841d7cec41b94232a519299de

* Thu Apr 30 2015 Alexei Takaseev <taf@altlinux.org> 1.1.1-alt1
- Initial build for ALT
