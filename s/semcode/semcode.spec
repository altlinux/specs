# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: semcode
Version: 20260211
Release: alt1
Summary: Semantic Code Search
License: Apache-2.0 or MIT
Group: Development/Other
Url: https://github.com/facebookexperimental/semcode
# Unable to build f16 kernels on given target_arch.  Please use x86_64 or aarch64 or remove the fp16kernels feature
ExclusiveArch: x86_64

Source: %name-%version.tar
# libprotobuf and libssl are not linked but build fail if they are absent.
# It can build w/o bzip2-devel and libcurl-devel without noticeable difference,
# they are linked if present.
BuildRequires: gcc-c++
BuildRequires: libprotobuf-devel
BuildRequires: libssl-devel
BuildRequires: rust-cargo
%{?!_without_check:%{?!_disable_check:
BuildRequires: git-core
}}

%description
Semcode is a semantic code search tool for C/C++ codebases that indexes
your codebase and allows you to search for functions, types, and code
patterns using both exact matches and semantic similarity.

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
rustflags = ["-Copt-level=3", "-Cdebuginfo=0"]

[profile.release]
strip = true
EOF

%build
# debuginfo is deliberately disabled, otherwise: error: cpio archive too big - 4240M
cargo build %_smp_mflags --offline --release

%install
install -Dp target/release/semcode{,-index,-lsp,-mcp} -t %buildroot%_bindir
# `test-vectors` requirins Model2Vec model which we don't support, it is not
# easy downloadable reqiring conversion (distillation) with Python script form
# nomic models. The vector search is not required for general usage.

%check
# git repo is required for branch tests.
git init -q
git add README.md
git config user.name name
git config user.email email
git commit -m README.md
cargo test --release

%files
%define _customdocdir %_docdir/%name
%doc LICENSE-APACHE LICENSE-MIT README.md
%doc scripts docs examples plugin
%_bindir/semcode
%_bindir/semcode-*

%changelog
* Thu Mar 26 2026 Vitaly Chikunov <vt@altlinux.org> 20260211-alt1
- Experimental import b4f1282b (2026-02-11).
