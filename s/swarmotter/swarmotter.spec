%define _unpackaged_files_terminate_build 1
%define binname swarmotterd
%def_with check

Name: swarmotter
Version: 2.0.3
Release: alt1

Summary: BitTorrent daemon with Web UI and network containment
License: Apache-2.0
Group: Networking/File transfer

URL: https://sphildreth.github.io/swarmotter
VCS: https://github.com/sphildreth/swarmotter

Source: %name-%version.tar
Source1: vendor.tar
Source2: swarmotter.sysusers

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%if_with check
BuildRequires: node
%endif

ExcludeArch: i586

%description
SwarmOtter is a performance-first Rust BitTorrent daemon with
a practical Web UI, a complete API, and fail-closed VPN/NIC
traffic containment.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
sed -i \
    -e 's|/data/downloads|/var/lib/swarmotter/downloads|g' \
    -e 's|/data/incomplete|/var/lib/swarmotter/incomplete|g' \
    config/%name.toml.example \
    deploy/%binname.service
install -Dm755 target/release/%binname \
    %buildroot%_bindir/%binname
sed -i 's/^\(User=\|Group=\)swarmotter$/\1_swarmotter/' deploy/%binname.service
install -Dm644 deploy/%binname.service %buildroot%_unitdir/%binname.service
install -Dm644 %SOURCE2 %buildroot%_sysusersdir/%name.conf
install -dm700 %buildroot%_sysconfdir/%name
install -Dm600 config/%name.toml.example %buildroot%_sysconfdir/%name/%name.toml
install -dm750 \
    %buildroot%_localstatedir/%name/downloads \
    %buildroot%_localstatedir/%name/incomplete

%pre
%sysusers_create_package %name %SOURCE2

%post
%post_systemd_postponed %binname.service

%preun
%preun_systemd %binname.service

%check
%rust_test

%files
%doc LICENSE README.md THIRD_PARTY_LICENSES.md
%_bindir/%binname
%_unitdir/%binname.service
%_sysusersdir/%name.conf
%attr(0750,_%name,_%name) %dir %_localstatedir/%name
%attr(0700,_%name,_%name) %dir %_sysconfdir/%name
%attr(0600,_%name,_%name) %config(noreplace) %_sysconfdir/%name/%name.toml
%attr(0750,_%name,_%name) %dir %_localstatedir/%name/downloads
%attr(0750,_%name,_%name) %dir %_localstatedir/%name/incomplete

%changelog
* Thu Aug 13 2026 Vladislav Eliseev <general@altlinux.org> 2.0.3-alt1
- Initial build for ALT.
