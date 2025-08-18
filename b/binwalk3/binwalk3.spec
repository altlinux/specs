# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: binwalk3
Version: 3.1.0
Release: alt1
Summary: Firmware Analysis Tool
License: MIT
Group: File tools
Url: https://github.com/ReFirmLabs/binwalk
Conflicts: binwalk < %EVR

# "compilation is only allowed for 64-bit targets"
ExcludeArch: %ix86 armh

Source: %name-%version.tar
BuildRequires: rust-cargo
BuildRequires: help2man
# BuildRequires: pkgconfig(bzip2) %dnl extractors::common::Chroot::make_executable (line 513) ... FAILED
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(liblzma)
%{?!_without_check:%{?!_disable_check:
BuildRequires: man-pages
}}

%description
This is an updated version of the Binwalk firmware analysis tool,
re-written in Rust for speed and accuracy.

Binwalk can identify, and optionally extract, files and data that have
been embedded inside of other files.

While its primary focus is firmware analysis, it supports a wide variety
of file and data types.

Through entropy analysis, it can even help to identify unknown compression
or encryption.

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

[install]
root = "%buildroot%_prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF
# For analyze & extract tests.
sed -i "s/accept.2.gz/$(basename /usr/share/man/man2/accept.2*)/g" src/binwalk.rs
ls -la /usr/share/man/man2/accept.2*
grep accept.2 src/binwalk.rs

%build
cargo build %_smp_mflags --offline --release
help2man -n "%summary" --no-info --version-string=%version target/release/binwalk > binwalk.1

%install
install -Dp target/release/binwalk -t %buildroot%_bindir
install -Dp binwalk.1 -t %buildroot%_man2dir

%check
%buildroot%_bindir/binwalk --version | grep -Fx 'binwalk %version'
%buildroot%_bindir/binwalk --list
RUST_BACKTRACE=full cargo test --release

%files
%doc LICENSE README.md
%doc scripts/binwalk-ui
%_bindir/binwalk
%_man2dir/binwalk.1*

%changelog
* Mon Aug 18 2025 Vitaly Chikunov <vt@altlinux.org> 3.1.0-alt1
- First import v3.1.0 (2024-10-31).
