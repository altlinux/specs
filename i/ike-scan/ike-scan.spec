Name:           ike-scan
Version:        1.9
Release:        alt2
Summary:        IKE protocol tool to discover, fingerprint and test IPsec VPN servers

Group:          Networking/Other
License:        GPLv2+
URL:            http://www.nta-monitor.com/tools/ike-scan/
Source0:        %{name}-%{version}.tar

BuildRequires:  openssl-devel

%description
ike-scan is a command-line tool that uses the IKE protocol to discover,
fingerprint and test IPsec VPN servers.

%prep
%setup

%build
%configure --with-openssl
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/*
%{_mandir}/man?/*
%{_datadir}/ike-scan

%changelog
* Wed Nov 12 2014 Lenar Shakirov <snejok@altlinux.ru> 1.9-alt2
- Fake version up for Autoimports

* Fri Oct 31 2014 Lenar Shakirov <snejok@altlinux.ru> 1.9-alt1
- Initial build for ALT (based on Fedora 1.9-16.fc21)

