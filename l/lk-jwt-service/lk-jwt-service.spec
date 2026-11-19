%global _unpackaged_files_terminate_build 1

Name:           lk-jwt-service
Version:        0.10.0
Release:        alt1
Summary:        Minimal service to issue LiveKit JWTs for MatrixRTC
License:        AGPL-3.0
Group:          System/Servers
Url:            https://github.com/element-hq/lk-jwt-service
ExcludeArch:    %ix86
Vcs:            https://github.com/element-hq/lk-jwt-service.git

Source:         %name-%version.tar
Source1:        %name-development-%version.tar
Source2:        %name.service
Source3:        %name.env
Source4:        %name.sysusers
Patch:          %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: cmake gcc-c++

Requires: ca-certificates

%description
This service is part of the MatrixRTC stack and is primarily used
when the LiveKit RTC backend (MSC4195) is in use.

%prep
%setup -a1
%patch -p1
%rust_prep

%build
%rust_build

%install
%rust_install
install -p -Dm 644 %SOURCE2 %buildroot%_unitdir/%name.service
install -p -Dm 644 %SOURCE3 %buildroot%_sysconfdir/%name/%name.env
install -p -Dm 644 %SOURCE4 %buildroot%_sysusersdir/%name.conf
mkdir -p %buildroot%_localstatedir/%name

%pre
%sysusers_create_package %name %SOURCE4

%post
%post_systemd %name.service

%preun
%preun_systemd %name.service

%files
%doc README.md LICENSE
%_bindir/%name
%_unitdir/%name.service
%_sysusersdir/%name.conf
%dir %_sysconfdir/%name
%config(noreplace) %attr(0640,root,_%name) %_sysconfdir/%name/%name.env
%dir %attr(0750,_%name,_%name) %_localstatedir/%name

%changelog
* Thu Nov 19 2026 Alexey Shabalin <shaba@altlinux.org> 0.10.0-alt1
- updated from 0.6.0 to 0.10.0
- upstream rewrote the service in Rust; switch to rpm-build-rust

* Wed Aug 19 2026 Alexey Shabalin <shaba@altlinux.org> 0.6.0-alt1
- updated from 0.4.4 to 0.6.0

* Wed May 06 2026 Alexey Shabalin <shaba@altlinux.org> 0.4.4-alt1
- updated from 0.4.1 to 0.4.4

* Mon Mar 23 2026 Alexey Shabalin <shaba@altlinux.org> 0.4.1-alt1
- Initial build.
