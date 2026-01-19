%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: texlab
Version: 5.25.1
Release: alt1

Summary: An implementation of the Language Server Protocol for LaTeX
License: GPL-3.0-or-later
Group: Publishing
Url: https://github.com/latex-lsp/texlab
VCS: https://github.com/latex-lsp/texlab

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires: rust-cargo

%description
A cross-platform implementation of the Language Server Protocol
providing rich cross-editing support for the LaTeX typesetting system.

%prep
%setup -a1
%autopatch -p1
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[profile.release]
strip = false
EOF

%build
cargo build %_smp_mflags --offline --release

%install
install -pD -m0755 target/release/texlab %buildroot%_bindir/texlab

%files
%_bindir/texlab

%changelog
* Mon Jan 19 2025 Alexey Volkov <qualimock@altlinux.org> 5.25.1-alt1
- initial build for ALT
