%define _unpackaged_files_terminate_build 1

Name: cargo-about
Version: 0.6.2
Release: alt1

Summary: Cargo plugin to generate list of all licenses for a crate
License: Apache-2.0 or MIT
Group: Development/Tools
Url: https://crates.io/crates/cargo-about
Vcs: https://github.com/EmbarkStudios/cargo-about

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: rust
BuildRequires: rust-cargo

%description
%summary.

%prep
%setup -a1
%autopatch -p1

mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%build
%rust_build

%install
%rust_install

%files
# LICENSE-MIT has copyright
%doc LICENSE-MIT
%_bindir/cargo-about

%changelog
* Mon Jul 15 2024 Anton Zhukharev <ancieg@altlinux.org> 0.6.2-alt1
- Built for ALT Sisyphus.

