%global _unpackaged_files_terminate_build 1
%def_with check

Name: trusttunnel
Version: 1.0.33
Release: alt1
Summary: Modern, fast and obfuscated VPN protocol
License: Apache-2.0
Group: Security/Networking
URL: https://trusttunnel.org
VCS: https://github.com/TrustTunnel/TrustTunnel

Source: %name-%version.tar
Source1: vendor.tar
Source2: %name.service
Source3: %name.sysusers
Source4: %name.sysconfig
Source5: README_ALT.md

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: cmake
BuildRequires: clang-devel
BuildRequires: clang-libs
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: git-core

%if_with check
BuildRequires: python3
%endif

%description
A modern, open-source VPN protocol originally developed by AdGuard VPN
and now available for anyone to use, audit, and implement. It delivers
fast, secure, and reliable VPN connections without the usual trade-offs.
By design, TrustTunnel traffic is indistinguishable from regular HTTPS
traffic, allowing it to bypass throttling and deep-packet inspection
while maintaining strong privacy protections.

%prep
%setup -a1
cp %SOURCE5 README_ALT.md
%rust_prep

%build
%rust_build

%install
%rust_install setup_wizard trusttunnel_endpoint
install -Dm 0644 %SOURCE2 %buildroot%_unitdir/%name.service
install -Dm 0644 %SOURCE3 %buildroot%_sysusersdir/%name.conf
install -Dm 0600 %SOURCE4 %buildroot%_sysconfdir/sysconfig/%name
mkdir -p %buildroot%_sysconfdir/%name

%check
%rust_test

%pre
%sysusers_create_package %name %SOURCE3

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/setup_wizard
%_bindir/trusttunnel_endpoint
%_unitdir/%name.service
%_sysusersdir/%name.conf
%dir %attr(0750, root, _%name) %_sysconfdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%doc README.md README_ALT.md

%changelog
* Wed Jul 15 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.0.33-alt1
- Initial build for ALT.
