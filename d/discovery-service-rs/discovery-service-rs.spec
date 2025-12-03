%define _unpackaged_files_terminate_build 1

Name: discovery-service-rs
Version: 0.1.2
Release: alt1

Summary: The alternative to original Talos Discovery Service
License: AGPL-3.0
Group: System/Configuration/Other
Url: https://altlinux.space/alt-orchestra/discovery-service-rs.git
Vcs: %url
Packager: Artyom Sinyugin <writers@altlinux.org>

Source: %name-%version.tar

Requires: libssl3

BuildRequires(pre): rpm-build-rust
BuildRequires: protobuf-compiler libprotobuf-devel

%description
discovery-service-rs is a lightweight service that enables automatic node
discovery for Talos Linux clusters during initial bootstrap. It serves as an
alternative to the official discovery.talos.dev, allowing nodes to find each
other without hardcoded IP addresses.

%prep
%setup
%rust_prep

%build
%rust_build

%install
%rust_install -- discovery-service-rs snapshot_reader

mkdir -p %buildroot{%_unitdir,{%_sysconfdir,%_localstatedir,%_datadir}/%name}

install -m0644 config/%name.service.example %buildroot%_unitdir/%name.service
install -m0644 config/%name.ini %buildroot%_sysconfdir/%name/%name.ini
cp -r templates %buildroot%_datadir/%name/

%check
%rust_test

%pre
groupadd -r -f %name > /dev/null 2>&1 ||:
useradd -r -g %name -d %_localstatedir/%name -M -s /dev/null -c "discovery-service-rs service" %name > /dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name
%files
%doc *.md
%_bindir/*
%_datadir/%name/*
%_unitdir/%name.service
%config(noreplace) %_sysconfdir/%name/*
%dir %attr(775, root, %name) %_localstatedir/%name

%changelog
* Tue Dec 03 2025 Artyom Sinyugin <writers@altlinux.org> 0.1.2-alt1
- Fix bug with missing html templates for systemd service.

* Tue Oct 06 2025 Artyom Sinyugin <writers@altlinux.org> 0.1.1-alt1
- Initial build.
