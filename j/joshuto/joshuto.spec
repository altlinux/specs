Name:    joshuto
Version: 0.9.8
Release: alt2

Summary: ranger-like terminal file manager written in Rust
License: LGPL-3.0
Group:   Other
Url:     https://github.com/kamiyaa/joshuto

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar

Patch1: joshuto-0.9.8-alt-loongarch64_nix_vendor_fix.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: cargo-vendor-checksum

%description
%summary

%prep
%setup
%patch1 -p1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
# Checksum update for patched files
cargo-vendor-checksum \
    --vendor %_builddir/%name-%version/vendor -f \
	nix-0.26.4/src/sys/ioctl/linux.rs

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%doc *.md
%doc docs
%doc config
%_bindir/*

%changelog
* Fri Jun 21 2024 Aleksei Kalinin <kaa@altlinux.org> 0.9.8-alt2
- NMU: Patched vendor nix for loongarch64 support

* Wed Jun 05 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.9.8-alt1
- Initial build for Sisyphus
