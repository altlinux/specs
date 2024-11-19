%define _unpackaged_files_terminate_build 1

Name: netscanner
Version: 0.5.3
Release: alt1
Summary: Terminal Network scanner & diagnostic tool with modern TUI.
License: MIT 
Group: Networking/Other
Url: https://github.com/Chleba/netscanner

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
* Tue Oct 08 2024 Pavel Shilov <zerospirit@altlinux.org> 0.5.3-alt1
- initial build for Sisyphus

