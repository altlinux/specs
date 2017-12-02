Name:    msd_lite
Version: 1.08
Release: alt1
License: BSD
Group:	 Networking/Other
URL: http://www.netlab.linkpc.net/wiki/ru:software:msd:lite

Source: %name-%version.tar

Summary: msd_lite is a program for organizing streaming IP TV on the network via HTTP.

%description
msd_lite - is a program for organizing streaming IP TV on
the network via HTTP. One server can serve thousands of
clients simultaneously.

The focus is on maximum performance, as well as a variety
of subtle adjustments related to the perceptual quality of
customer service: speed channel switching, fault tolerance transfer.

Implemented proxying one to many: the data received via the
one HTTP connection to be given away to the set of connected clients.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall
install -pDm0644 %name.conf		%buildroot%_sysconfdir/%name.conf
install -pDm0755 %name.init		%buildroot%_initdir/%name
install -pDm0644 %name.sysconfig	%buildroot%_sysconfdir/sysconfig/%name
install -pDm0644 %name.service		%buildroot%_unitdir/%name.service

%post
%post_service %name

%preun
%preun_service %name


%files
%config(noreplace) %_sysconfdir/%name.conf
%_sysconfdir/sysconfig/%name
%_initdir/*
%_unitdir/*
%_bindir/%name
%doc AUTHORS COPYING README

%changelog
* Sat Dec 02 2017 Alexei Takaseev <taf@altlinux.org> 1.08-alt1
- Initial build for ALT Sisyphus
