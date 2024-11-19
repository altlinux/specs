%define _unpackaged_files_terminate_build 1

Name: systeroid
Version: 0.4.4
Release: alt1
Summary: A more powerful alternative to sysctl(8) with a terminal user interface.
License: Apache-2.0 and MIT 
Group: System/Configuration/Boot and Init
Url: https://github.com/orhun/systeroid

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: libX11-devel
BuildRequires: rust-cargo

%description
%summary

%prep
%setup
%patch -p1
tar -xf %SOURCE1
mkdir -p .cargo
cat > .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install
install -Dm 755 target/release/%name-tui %buildroot%_bindir/%name-tui

%files
%doc README.md
%_bindir/*

%changelog
* Wed Oct 16 2024 Pavel Shilov <zerospirit@altlinux.org> 0.4.4-alt1
- initial build for Sisyphus
