%define cargo_prep %nil
%define cargo_build %rust_build
%define cargo_install %rust_install

Name: matrix-conduit
Version: 0.10.12
Release: alt1

Summary: A simple, fast and reliable Matrix homeserver written in Rust

License: Apache-2.0
Group: Networking/Other
URL: https://conduit.rs
# Source-url: https://gitlab.com/famedly/conduit/-/archive/v%version/conduit-v%version.tar.gz
Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: %name.service
Source3: %name.sysusers
Source4: %name.tmpfiles
Source5: conduit.toml

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust /proc
BuildRequires: gcc-c++ clang-devel

%description
Conduit is a lightweight open-source server implementation of the Matrix
Specification with a focus on easy setup and low system requirements.
That means you can make your own Conduit setup in just a few minutes.

Conduit keeps things simple, it's a single binary with an embedded database
and can be much faster than other server implementations.

%prep
%setup -a1
%cargo_prep
cat <<EOF >> .cargo/config.toml
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/ruma/ruma.git"]
git = "https://github.com/ruma/ruma.git"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%cargo_build

%install
install -Dm 755 target/release/conduit %buildroot%_bindir/%name
install -Dm 644 %SOURCE2 %buildroot%_unitdir/%name.service
install -Dm 644 %SOURCE3 %buildroot%_sysusersdir/%name.conf
install -Dm 644 %SOURCE4 %buildroot%_tmpfilesdir/%name.conf
install -Dm 644 %SOURCE5 %buildroot%_sysconfdir/%name/conduit.toml

%pre
%sysusers_create_package %name %SOURCE3

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/%name
%_unitdir/%name.service
%_sysusersdir/%name.conf
%_tmpfilesdir/%name.conf
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/conduit.toml
%doc README.md
%doc LICENSE

%changelog
* Fri Apr 10 2026 Vitaly Lipatov <lav@altlinux.ru> 0.10.12-alt1
- initial build for ALT Sisyphus

