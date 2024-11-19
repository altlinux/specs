%define _unpackaged_files_terminate_build 1

Name: systemctl-tui
Version: 0.3.8
Release: alt1
Summary: A fast, simple TUI for interacting with systemd services and their logs.
License: MIT 
Group: System/Configuration/Other
Url: https://github.com/rgwood/systemctl-tui
ExclusiveArch: aarch64 x86_64 

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo

%description
%summary

%prep
%setup
%patch -p1
tar -xf %SOURCE1
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install

%files
%doc README.md
%_bindir/%name

%changelog
* Mon Oct 07 2024 Pavel Shilov <zerospirit@altlinux.org> 0.3.8-alt1
- initial build for Sisyphus

