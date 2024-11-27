# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: typos
Version: 1.28.1
Release: alt1
Summary: Source code spell checker
License: Apache-2.0 or MIT
Group: Development/Tools
Url: https://github.com/crate-ci/typos
Provides: typos-cli = %EVR

Source: %name-%version.tar
BuildRequires: rust-cargo

%description
Finds and corrects spelling mistakes among source code.

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
rm docs/github-action.md
rm docs/screenshot.png
sed -i '/screenshot.png/d' README.md
sed -i 's/docs\///g' README.md

%build
cargo build %_smp_mflags --offline --release --all-features

%install
install -Dp target/release/%name -t %buildroot%_bindir

%check
cargo test --release
PATH=%buildroot%_bindir:$PATH
typos --version | grep -Fx '%name-cli %version'
echo Millenium  > /tmp/example.txt
! typos /tmp/example.txt || exit 2
  typos -w /tmp/example.txt
  grep -qx Millennium /tmp/example.txt
  rm /tmp/example.txt

%files
%doc CHANGELOG.md CONTRIBUTING.md LICENSE-APACHE LICENSE-MIT README.md
%doc docs/*
%_bindir/typos

%changelog
* Wed Nov 27 2024 Vitaly Chikunov <vt@altlinux.org> 1.28.1-alt1
- First import v1.28.1 (2024-11-26).
