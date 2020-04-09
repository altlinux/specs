Name: ocproxy
Version: 1.60
Release: alt1

Summary: OpenConnect Proxy

License: BSD
Group: Networking/Other
Url: https://github.com/cernekee/ocproxy

Packager: Maxim Knyazev <mattaku@altlinux.org>

Source: %name-%version.tar

BuildRequires: libevent-devel
Requires: openconnect

%description
OCProxy is a user-level SOCKS and port forwarding proxy for OpenConnect based
on lwIP. When using ocproxy, OpenConnect only handles network activity that
the user specifically asks to proxy, so the VPN interface no longer "hijacks"
all network traffic on the host.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc %_docdir/%name/
%doc LICENSE
%_bindir/%name
%_bindir/vpnns
%_mandir/man1/%name.1*
%_mandir/man1/vpnns.1*

%changelog
* Mon Apr 06 2020 Maxim Knyazev <mattaku@altlinux.org> 1.60-alt1
- Initial build to Sisyphus

