# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: scx-scheds
Version: 1.0.19
Release: alt1
Summary: sched_ext schedulers and tools
License: GPL-2.0-only
Group: System/Kernel and hardware
Url: https://github.com/sched-ext/scx
ExcludeArch: %ix86
# Temporary provide names for compatibility with other distros. Do not use them.
Provides: scx
Provides: scx_c_schedulers
Provides: scx_layered
Provides: scx_rustland
Provides: scx_rusty

Source: %name-%version.tar
BuildRequires(pre): rpm-macros-systemd
BuildRequires: bpftool
BuildRequires: clang-devel
BuildRequires: jq
BuildRequires: libbpf-devel
BuildRequires: libelf-devel
BuildRequires: libprotobuf-devel
BuildRequires: libseccomp-devel
BuildRequires: libsystemd-devel
BuildRequires: libzstd-devel
BuildRequires: llvm-devel
BuildRequires: rust-cargo
BuildRequires: zlib-devel

%description
Experimental %summary.

sched_ext is a Linux kernel feature which enables implementing kernel thread
schedulers in BPF and dynamically loading them. This repository contains
various scheduler implementations and support utilities.

sched_ext enables safe and rapid iterations of scheduler implementations, thus
radically widening the scope of scheduling strategies that can be experimented
with and deployed; even in massive and complex production environments.

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
rustflags = ["-Copt-level=3", "-Cdebuginfo=1", "--cfg=rustix_use_libc"]

[profile.release]
strip = false
EOF
# Non-ready C schedulers
sed -Ei "/C_SCHEDS/s/scx_(userland|qmap|pair|central)//" Makefile

%build
export CC=clang CXX=clang++
cargo build %_smp_mflags --offline --release --all-features \
	--workspace \
	--exclude scx_arena_selftests \
	--exclude scxcash \
	--exclude scx_rlfifo \
	--exclude scx_wd40 \
	--exclude vmlinux_docify \
	--exclude xtask \
	%nil
%make_build BPFTOOL=/usr/sbin/bpftool
for f in scheds/c/README.md scheds/rust/scx_*/README.md; do
	n=${f%%/README.md}
	n=${n##*/}
	cp -np $f README-${n:?}.md
done

%install
pushd target/release
install -Dp -t %buildroot%_bindir -- $(file * | grep executable | cut -d: -f1)
popd
%makeinstall_std INSTALL_DIR=%buildroot%_bindir

%files
%doc BREAKING_CHANGES.md LICENSE OVERVIEW.md README*.md
%_bindir/scx*

%changelog
* Tue Dec 23 2025 Vitaly Chikunov <vt@altlinux.org> 1.0.19-alt1
- Experimental update to v1.0.19 (2025-12-02).

* Thu Aug 28 2025 Vitaly Chikunov <vt@altlinux.org> 1.0.15-alt1
- Experimental import v1.0.15 (2025-08-13).
