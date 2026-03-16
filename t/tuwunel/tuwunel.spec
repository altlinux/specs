Name:    tuwunel
Version: 1.5.1
Release: alt1
Summary: High Performance Matrix Homeserver in Rust!
License: Apache-2.0
Group:   System/Servers
URL:     https://github.com/matrix-construct/tuwunel
VCS:     https://github.com/matrix-construct/tuwunel.git

ExcludeArch: %ix86

Source:  %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml
Source3: %name.sysusers

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: liburing-devel
BuildRequires: unzip
BuildRequires: glibc-devel
BuildRequires: clang21.1 libclang21
BuildRequires: gcc-c++

%description
Tuwunel is a featureful Matrix homeserver you can use instead of Synapse with
your favorite client, bridge or bot. It is written entirely in Rust
to be a scalable, low-cost, enterprise-ready, community-driven alternative,
fully implementing the Matrix Specification for all but the most niche uses.

%prep
%setup -a1
cat %SOURCE2 >> .cargo/config.toml
sed 's/PrivateUsers/#PrivateUsers/' -i rpm/%name.service

%build
%rust_build

%pre
%sysusers_create_package %name %SOURCE3

%install
install -Dm 755 target/release/%name %buildroot/%_sbindir/%name
install -Dm 644 rpm/tuwunel.service %buildroot/%_unitdir/%name.service
install -Dm 644 %SOURCE3 %buildroot/%_sysusersdir/%name.conf
install -Dm 644 %name-example.toml %buildroot/%_sysconfdir/%name/%name.toml
mkdir -p %buildroot/%_localstatedir/%name

%files
%_sbindir/%name
%_unitdir/%name.service
%_sysusersdir/%name.conf
%attr(644,%name,%name) %config(noreplace) %_sysconfdir/%name/%name.toml
%attr(755,%name,%name) %dir %_localstatedir/%name/
%attr(755,%name,%name) %dir %_sysconfdir/%name/
%doc LICENSE README.md

%changelog
* Mon Mar 16 2026 Alexey Shabalin <shaba@altlinux.org> 1.5.1-alt1
- Updated from 1.5.0 to 1.5.1 with security fixes.

* Wed Feb 18 2026 Arseniy Romenskiy <romenskiy@altlinux.org> 1.5.0-alt1
- Initial build.
