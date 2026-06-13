# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: dufs
Version: 0.46.0
Release: alt1
Summary: A file server that supports static serving, uploading, searching, accessing control, webdav
License: Apache-2.0 or MIT
Group: System/Servers
Url: https://github.com/sigoden/dufs

Source: %name-%version.tar
BuildRequires: rust-cargo
BuildRequires: pkgconfig(liblzma)

%description
Dufs is a distinctive utility file server that supports static serving,
uploading, searching, accessing control, webdav...

Features
- Serve static files
- Download folder as zip file
- Upload files and folders (Drag & Drop)
- Create/Edit/Search files
- Resumable/partial uploads/downloads
- Access control
- Support https
- Support webdav
- Easy to use with curl

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%build
cargo build %_smp_mflags --offline --release --all-features

%install
install -Dp target/release/%name -t %buildroot%_bindir
mkdir -p %buildroot%_datadir/bash-completion/completions
mkdir -p %buildroot%_datadir/fish/vendor_completions.d
mkdir -p %buildroot%_datadir/zsh/site-functions
target/release/%name --completions bash > %buildroot%_datadir/bash-completion/completions/%name
target/release/%name --completions fish > %buildroot%_datadir/fish/vendor_completions.d/%name.fish
target/release/%name --completions zsh > %buildroot%_datadir/zsh/site-functions/_%name

%check
%buildroot%_bindir/dufs --version | grep -Fx '%name %version'
cargo test --release

%files
%define _customdocdir %_docdir/%name
%doc CHANGELOG.md LICENSE-APACHE LICENSE-MIT README.md SECURITY.md
%_bindir/dufs
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Sat Jun 13 2026 Daniel Zagaynov <kotopesutility@altlinux.org> 0.46.0-alt1
- Update to upstream v0.46.0 (2026-05-07).

* Fri Apr 04 2025 Vitaly Chikunov <vt@altlinux.org> 0.43.0-alt1
- First import v0.43.0-13-g4fbdec2 (2025-03-20).
