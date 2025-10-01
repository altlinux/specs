%global _unpackaged_files_terminate_build 1

Name: traefik-crowdsec-bouncer
Version: 0.6.1
Release: alt1
Summary: A service to verify request and bounce them according to decisions made by CrowdSec
License: MIT
Group: System/Servers
Url: https://github.com/freifunkMUC/traefik-crowdsec-bouncer

Source: %name-%version.tar
Source1: vendor.tar
Source2: %name.service
Source3: %name.sysconfig

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
This repository aims to implement a CrowdSec bouncer for the router
Traefik to block malicious IPs from accessing your services.

%prep
# go mod vendor
# git add vendor -f && git commit -m "Updated go vendor modules."
%setup -a 1

%build
go build -o %name

%install
mkdir -p %buildroot%_bindir \
         %buildroot%_unitdir \
         %buildroot%_sysconfdir/sysconfig
install -m 0755 %name %buildroot%_bindir/%name
install -m 0644 %SOURCE2 %buildroot%_unitdir/%name.service
install -m 0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/%name
%_unitdir/%name.service
%_sysconfdir/sysconfig/%name
%doc LICENSE

%changelog
* Wed Oct 01 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.6.1-alt1
- Initial build for ALT.
