# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: gitui
Version: 0.26.2
Release: alt1
Summary: Blazing fast terminal-ui for git written in rust
License: MIT
Group: Development/Other
Url: https://github.com/extrawurst/gitui

Source: %name-%version.tar
BuildRequires: /proc
BuildRequires: rust-cargo
BuildRequires: openssl-devel

%description
%summary.

%prep
%setup
mkdir -p .cargo
# Overwriting due to 'linker' settings.
cat > .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1", "--cfg=rustix_use_libc"]

[profile.release]
strip = false

# Incorrect linker specs causing failure on aarch64/armh:
#   error: linker 'aarch64-linux-gnu-gcc' not found
[target.'cfg(all())']
linker = "gcc"
EOF
# Use openssl-devel.
sed -i '/^default =/s/"vendor-openssl"//' Cargo.toml
# There should not be non-source precompiled files.
find vendor \( -name '*.a' -o -name '*.lib' -o -name '*.dll' -o -name '*.obj' \) | grep . && exit 1
mkdir -p $HOME/bin
echo -e '#!/bin/sh\ntest $1 = rev-parse && echo %release' > $HOME/bin/git
chmod a+rx $HOME/bin/git

%build
export RUST_BACKTRACE=full
export GITUI_RELEASE=1
cargo build %_smp_mflags --offline --release
cargo tree --no-dedupe --target all --prefix none --format '{l}' | sort -u > LICENSE.dependencies

%install
install -Dp target/release/%name -t %buildroot%_bindir

%check
%buildroot%_bindir/gitui --version | grep -Px '%name \Q%version\E \S+ \(%release\)'
# This recompiles.
cargo test  %_smp_mflags --release

%files
%define _customdocdir %_docdir/%name
%doc CHANGELOG.md FAQ.md KEY_CONFIG.md LICENSE* README.md THEMES.md
%_bindir/gitui

%changelog
* Wed May 29 2024 Vitaly Chikunov <vt@altlinux.org> 0.26.2-alt1
- Update to v0.26.2 (2024-05-18).

* Wed Apr 03 2024 Vitaly Chikunov <vt@altlinux.org> 0.25.2-alt1
- Update to v0.25.2 (2024-03-22).

* Sat Feb 24 2024 Vitaly Chikunov <vt@altlinux.org> 0.25.1-alt1
- Update to v0.25.1 (2024-02-23).

* Fri Feb 23 2024 Vitaly Chikunov <vt@altlinux.org> 0.25.0-alt1
- Update to v0.25.0 (2024-02-21).

* Mon Jan 29 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.24.3-alt2
- NMU: fixed FTBFS on LoongArch (updated vendored tempfiles to 3.5.0,
  is-terminal -> 0.4.10).

* Sat Jan 27 2024 Vitaly Chikunov <vt@altlinux.org> 0.24.3-alt1
- First import v0.24.3-63-gc30eb7c (2024-01-26).
