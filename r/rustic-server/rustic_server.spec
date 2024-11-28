# SPDX-License-Identifier: CC0
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: rustic-server
Version: 0.4.3
Release: alt1
Summary: A REST server built in rust for use with rustic/restic
License: AGPL-3.0-or-later
Group: System/Servers
Url: https://rustic.cli.rs/ecosystem/rustic-server/
Vcs: https://github.com/rustic-rs/rustic_server
Obsoletes: rustic_server < %EVR
Provides: rustic_server = %EVR

Source: %name-%version.tar
BuildRequires: rust-cargo

%description
A REST server built in rust for use with rustic and restic.
Works pretty similar to rest-server. Most features are already implemented.

%prep
%setup
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[build]
rustdocflags = ["--document-private-items"]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%build
cargo build %_smp_mflags --offline --release --all-features

%install
install -Dp target/release/rustic-server -t %buildroot%_bindir

%check
%buildroot%_bindir/rustic-server --version |& grep -Fx '%name %version'
cargo test --release

%files
%define _customdocdir %_docdir/%name
%doc CHANGELOG.md LICENSE README.md
%_bindir/rustic-server

%changelog
* Thu Nov 28 2024 Vitaly Chikunov <vt@altlinux.org> 0.4.3-alt1
- Update to v0.4.3 (2024-11-27).
- Package renamed from rustic_server to rustic-server to have the same name as
  the tool.

* Sun Nov 10 2024 Vitaly Chikunov <vt@altlinux.org> 0.1.1-alt1
- First import v0.1.1 (2024-11-09).
