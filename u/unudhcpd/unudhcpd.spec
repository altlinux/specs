%define _unpackaged_files_terminate_build 1
%def_enable check

Name: unudhcpd
Version: 0.5.0
Release: alt1
Summary: extremely basic DHCP server
License: GPL-3.0-only
Group: System/Servers
Url: https://gitlab.postmarketos.org/postmarketOS/unudhcpd
VCS: https://gitlab.postmarketos.org/postmarketOS/unudhcpd.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

%description
This is an extremely basic DHCP server that only issues 1 IP address to any
client that sends a DHCP{OFFER,REQUEST}.
It is meant to be used on an interface that will only ever see 1 client at a
time, but where the client's MAC may change, making it inconvenient to try and
configure leasing, etc on other DHCP servers. With unudhcpd, the client always
gets an IP quickly.

%prep
%setup

%build
%meson
%meson_build -v

%install
%meson_install

%check
%__meson_test

%files
%_bindir/%name
%_unitdir/%name@.service
%exclude %_sysconfdir/init.d/%name

%changelog
* Wed Oct 21 2026 Vasiliy Doylov <neko@altlinux.org> 0.5.0-alt1
- Initial build for ALT.
