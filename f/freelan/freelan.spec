Name: freelan
Version: 2.3
Release: alt1

Summary: Peer-to-peer virtual private network daemon
License: GPLv3+
Group: Networking/Other

Url: http://www.freelan.org
Source0: %name-%version.tar
Source1: freelan.service
Source2: freelan.init

BuildRequires: libssl-devel
BuildRequires: boost-complete
BuildRequires: libcurl-devel
BuildRequires: libminiupnpc-devel
BuildRequires: help2man
BuildRequires: scons
Requires: openssl

%description
Freelan is an application to create secure ethernet tunnels over a
single UDP port. It can be used to create virtual LANs ("Local
Area Network"), hence the name: "freelan".

Freelan may create peer-to-peer tunnel connections or rely on a
more classic client/server layout. The virtual network can be
shaped to fit exactly the bandwidth or topology constraints,
providing an optimal virtual private network.

Freelan is particularly useful for remote sites interconnection and
gaming.

%prep
%setup

%build
scons %_smp_mflags --mode=release apps prefix=/ bin_prefix=%_usr --upnp=yes --mongoose=no

%install
install -pDm755 build/release/bin/freelan %buildroot/%_bindir/%name
install -pDm755 apps/freelan/config/freelan.cfg \
	%buildroot/%_sysconfdir/%name/%name.cfg
install -pDm644 build/release/man/freelan.1 %buildroot/%_man1dir/%name.1
install -pDm644 %SOURCE1 %buildroot/%_unitdir/%name.service
install -pDm755 %SOURCE2 %buildroot/%_initdir/%name

%files
%_bindir/%name
%_man1dir/*
%_sysconfdir/%name/%name.cfg
%_unitdir/%name.service
%_initdir/%name

%preun
%preun_service %name
%changelog
* Thu Dec 17 2020 Nikolay Burykin <bne@altlinux.org> 2.3-alt1
- Initial build for ALT

* Tue May 7 2019  <sebastien.vincent@freelan.org> 2.2-1
- Version 2.2.

* Fri Aug 11 2017  <sebastien.vincent@freelan.org> 2.1-1
- First RPM version.
