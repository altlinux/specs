%define _unpackaged_files_terminate_build 1

Name: systemctl-tui
Version: 0.3.8
Release: alt1.1
Summary: A fast, simple TUI for interacting with systemd services and their logs.
License: MIT 
Group: System/Configuration/Other
Url: https://github.com/rgwood/systemctl-tui
ExclusiveArch: aarch64 loongarch64 riscv64 x86_64

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch
Patch1: vendored-nix-loongarch64-support.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo

%description
%summary

%prep
%setup
tar -xf %SOURCE1

%patch -p1
%patch1 -p1

mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

# allow patching vendored rust code
sed -i -e 's/"files":{[^}]*}/"files":{}/' \
  ./vendor/nix-0.24.3/.cargo-checksum.json

%build
%rust_build

%install
%rust_install

%files
%doc README.md
%_bindir/%name

%changelog
* Wed Nov 20 2024 Ivan A. Melnikov <iv@altlinux.org> 0.3.8-alt1.1
- build on loongarch64 and riscv64

* Mon Oct 07 2024 Pavel Shilov <zerospirit@altlinux.org> 0.3.8-alt1
- initial build for Sisyphus

