# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: scx-scheds
Version: 1.0.15
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
BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-systemd
BuildRequires: rust-cargo
BuildRequires: bpftool
BuildRequires: clang-devel
BuildRequires: jq
BuildRequires: libbpf-devel
BuildRequires: libelf-devel
BuildRequires: libprotobuf-devel
BuildRequires: libseccomp-devel
BuildRequires: libsystemd-devel
BuildRequires: llvm-devel
BuildRequires: meson
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
# Not installed in meson-scripts/install_rust_user_scheds
#  [ "$name" = "scx_mitosis" ]
#  [ "$name" = "scx_wd40" ]
sed -i- \
	-e /scx_chaos/d    %dnl "experimental and should not be used in production environments"
	-e /scx_lavd/d     %dnl "under development"
	-e /scx_mitosis/d  %dnl "not ready yet"
	-e /scx_tickless/d %dnl "This scheduler is still experimental"
	-e /scx_wd40/d     %dnl "experimental"
%ifarch aarch64
	-e /scxtop/d	   %dnl FTBFS
%endif
	Cargo.toml
! diff -U0 Cargo.toml- Cargo.toml || exit 2
# Fix debianism.
sed -i 's!/etc/default!/etc/sysconfig!' \
	services/README.md \
	services/systemd/scx.service \
	services/systemd/meson.build

%build
export CC=clang CXX=clang++
cargo build %_smp_mflags --offline --release --all-features
%meson \
	-Dbpftool=/usr/sbin/bpftool \
	-Denable_rust=false \
	-Dlibbpf_a=disabled \
	-Doffline=true \
	-Dopenrc=disabled \
	%nil
%meson_build
for f in scheds/c/README.md scheds/rust/scx_*/README.md; do
	n=${f%%/README.md}
	n=${n##*/}
	cp -np $f README-${n:?}.md
done

%install
pushd target/release
install -Dp -t %buildroot%_bindir -- $(file * | grep executable | cut -d: -f1)
popd
%meson_install
# Temporary compatibility with other distributions.
mkdir -p %buildroot%_sysconfdir/default
ln -sf ../sysconfig/scx %buildroot%_sysconfdir/default
rm \
	%buildroot/usr/lib/systemd/system/scx_loader.service \
	%buildroot/usr/share/dbus-1/system-services/org.scx.Loader.service \
	%buildroot/usr/share/scx_loader/config.toml
rm -rf %buildroot%_includedir/scx

%post
%post_systemd scx.service

%preun
%preun_systemd scx.service

%files
%doc BREAKING_CHANGES.md LICENSE OVERVIEW.md README*.md
%_bindir/scx*
%_bindir/vmlinux_docify
%_sysconfdir/default/scx
%config(noreplace) %_sysconfdir/sysconfig/scx
%_unitdir/scx.service

%changelog
* Thu Aug 28 2025 Vitaly Chikunov <vt@altlinux.org> 1.0.15-alt1
- Experimental import v1.0.15 (2025-08-13).
