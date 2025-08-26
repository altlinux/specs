%define _unpackaged_files_terminate_build 1

%global import_path github.com/bettercap/bettercap

Name: bettercap
Version: 2.41.4
Release: alt1

Summary: Swiss army knife for network attacks and monitoring
License: GPL-3.0-only
Group: Monitoring
Url: https://www.bettercap.org/
Vcs: https://github.com/bettercap/bettercap

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: libusb-devel
BuildRequires: libpcap-devel

%description
bettercap is a powerful, easily extensible and portable framework written in Go
which aims to offer to security researchers, red teamers and reverse engineers
an easy to use, all-in-one solution with all the features they might
possibly need for performing reconnaissance and attacking WiFi networks,
Bluetooth Low Energy devices, CAN-bus, wireless HID devices
and Ethernet networks.

%prep
%setup -a1

sed -i 's/\/local//' caplets/env.go
sed -i 's/\/local//' caplets/env_test.go
sed -i 's/\/local//' bettercap.service
sed -i 's/\/local//' Makefile

%build
export GOROOT="%_libexecdir/golang"
%gobuild -mod=vendor

%install
install -Dpm 755 %name %{buildroot}%{_bindir}/%name
install -Dpm 644 %name.service %{buildroot}%{_unitdir}/%name.service

%files
%doc *.md
%{_bindir}/%name
%{_unitdir}/%name.service

%changelog
* Tue Aug 26 2025 Denis Rastyogin <gerben@altlinux.org> 2.41.4-alt1
- Initial build for Sisyphus.
