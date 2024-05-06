Name:    msd
Version: 3.2.0
Release: alt1
Summary: Program for organizing IP TV streaming on the network via HTTP.

Group: Networking/Other

License: BSD
Url: https://github.com/rozhuk-im/msd.git
Source0: %name-%version.tar
Source1: liblcb.tar
Source2: msd.init
Source3: msd.service
Source4: msd.sysconfig

BuildRequires(pre): cmake
BuildRequires: glibc-kernheaders-generic

%description
Features
* support for IPv4 and IPv6
* Zero Copy on Send (ZCoS) - reduces the overhead of service connected clients, all the work of sending the data to the client assumes the OS kernel
* support half closed http clients
* receiving udp-multicast, including rtp, simultaneously with different interfaces
* the use of various TCP Congestion Control algorithms depending on the port to which the client came and the URL the client's request
* instantaneous sending new client data from the ring buffer in order to minimize waiting times start playback
* sending any additional http headers in requests and responses
* detailed statistics for each TCP connection, to help you find problems at the network level

%prep
%setup
tar -xf %SOURCE1 -C src/liblcb

%build
%cmake \
	-DENABLE_STATIC=FALSE \
	-DCMAKE_INSTALL_PREFIX=%_prefix \
	-DRUNDIR=/run \
	-DCONFDIR=%_sysconfdir/%name
%cmake_build

%install
install -pDm0755 %_target_platform/src/%name %buildroot%_bindir/%name
install -pDm0644 conf/msd.conf               %buildroot%_sysconfdir/%name/msd.conf
install -pDm0644 conf/msd_channels.conf      %buildroot%_sysconfdir/%name/msd_channels.conf
install -pDm0644 conf/msd_channels2.conf     %buildroot%_sysconfdir/%name/msd_channels2.conf
install -pDm0644 conf/msd_minimal.conf       %buildroot%_sysconfdir/%name/msd_minimal.conf

install -pDm0755 %SOURCE2		%buildroot%_initdir/%name
install -pDm0644 %SOURCE3		%buildroot%_unitdir/%name.service
install -pDm0644 %SOURCE4		%buildroot%_sysconfdir/sysconfig/%name


%files
%doc LICENSE readme.md
%config(noreplace) %_sysconfdir/%name
%_initdir/*
%_sysconfdir/sysconfig/%name
%_bindir/*
%_unitdir/*

%changelog
* Mon May 06 2024 Alexei Takaseev <taf@altlinux.org> 3.2.0-alt1
- 3.2.0

* Fri Feb 19 2021 Alexei Takaseev <taf@altlinux.org> 3.1.0-alt1
- Initial build for ALT Sisyphus
