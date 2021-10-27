Name:           ike-scan
Version:        1.9.5
Release:        alt1
Summary:        IKE protocol tool to discover, fingerprint and test IPsec VPN servers

Group:          Networking/Other
License:        GPLv3+
URL:            https://github.com/royhills/ike-scan
Source0:        %{name}-%{version}.tar

BuildRequires:  openssl-devel

Patch1: ike-scan-memleak.patch

%description
ike-scan is a command-line tool that uses the IKE protocol to discover,
fingerprint and test IPsec VPN servers.

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure --with-openssl
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog COPYING README.md TODO
%{_bindir}/*
%{_mandir}/man?/*
%{_datadir}/ike-scan

%changelog
* Wed Oct 27 2021 Pavel Nakonechnyi <zorg@altlinux.org> 1.9.5-alt1
- Updated to 1.9.5.
- memleak patch from Fedora was added.
- Minor spec update.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.9-alt2.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Nov 12 2014 Lenar Shakirov <snejok@altlinux.ru> 1.9-alt2
- Fake version up for Autoimports

* Fri Oct 31 2014 Lenar Shakirov <snejok@altlinux.ru> 1.9-alt1
- Initial build for ALT (based on Fedora 1.9-16.fc21)

