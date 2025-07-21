%define _unpackaged_files_terminate_build 1

Name: pgcat
Version: 1.2.0
Release: alt1
Summary: PostgreSQL pooler with sharding, load balancing and failover support
Group: Networking/WWW
License: MIT
Url: https://github.com/postgresml/pgcat
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
PostgreSQL pooler and proxy (like PgBouncer) with support for sharding,
load balancing, failover and mirroring.

%prep
%setup

%build
%rust_build

%install
%rust_install
mkdir -p %buildroot%_localstatedir/%name
install -pD -m640 %name.toml %buildroot%_sysconfdir/%name/%name.toml
install -pD -m644 %name.service %buildroot%_unitdir/%name.service

%pre
groupadd -r -f _%name > /dev/null 2>&1 ||:
useradd -g _%name -M -d %_localstatedir/%name -s /dev/null -r _%name > /dev/null 2>&1 ||:

%post
%post_systemd %name.service

%preun
%preun_systemd %name.service

%files
%doc *.md
%dir %_sysconfdir/%name/
%config(noreplace) %attr(640, root, _%name) %_sysconfdir/%name/%name.toml
%_unitdir/%name.service
%_bindir/%name
%dir %attr(770, root, _%name) %_localstatedir/%name

%changelog
* Thu May 22 2025 Vladislav Tsarev <tyaplyapych@altlinux.org> 1.2.0-alt1
- initial build for sisyphus
