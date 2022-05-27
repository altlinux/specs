%define _unpackaged_files_terminate_build 1

Name: tayga
Version: 0.9.2
Release: alt1

Summary: Simple, no-fuss NAT64
Group: Other
License: GPLv2+
Url: http://www.litech.org/tayga/

Source: %name-%version.tar

Requires: iproute2

%description
TAYGA is an out-of-kernel stateless NAT64 implementation for Linux that uses
the TUN driver to exchange IPv4 and IPv6 packets with the kernel. It is
intended to provide production-quality NAT64 service for networks where
dedicated NAT64 hardware would be overkill.

%prep
%setup %name-%version

%build
%configure
%make_build

%install
%makeinstall_std
install -d %buildroot%_sysconfdir/%name/
install -d %buildroot%_localstatedir/%name
install -p -D -m 0644 .gear/%name.conf %buildroot%_sysconfdir/%name/default.conf
install -p -D -m 0644 .gear/%name.service %buildroot%_unitdir/%name@.service
install -p -D -m 0644 .gear/%name.tmpfiles.d.conf %buildroot%_tmpfilesdir/%name.conf

%files
%doc README .gear/README.alt
%config(noreplace) %_sysconfdir/%name
%dir %_localstatedir/%name
%dir %_tmpfilesdir/%name.conf
%_unitdir/%name@.service
%_sbindir/%name
%_man5dir/%{name}*
%_man8dir/%{name}*

%changelog
* Wed Mar 02 2022 Andrey Limachko <liannnix@altlinux.org> 0.9.2-alt1
- Initial build

