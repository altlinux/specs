# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: rosenpass
Version: 0.1.1
Release: alt1
Summary: Post-quantum secure VPN with WireGuard
License: MIT or Apache-2.0
Group: Security/Networking
Url: https://rosenpass.eu/
Vcs: https://github.com/rosenpass/rosenpass

Source: %name-%version.tar
BuildRequires: rust-cargo
BuildRequires: libsodium-devel
BuildRequires: clang-devel
BuildRequires: cmake

%description
Rosenpass is a formally verified, post-quantum secure VPN that uses
WireGuard to transport the actual data.

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config <<EOF
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

%ifarch armh
# Add armh to the list of supported arm32 arches.
sed -i '/CMAKE_SYSTEM_PROCESSOR.*armhf/s/")/|armv8l&/'	vendor/oqs-sys/liboqs/CMakeLists.txt
sed -i 's!,"liboqs/CMakeLists.txt":"[^"]\+",!,!'	vendor/oqs-sys/.cargo-checksum.json
%endif

%build
cargo build %_smp_mflags --offline --release

%install
cargo install %_smp_mflags --offline --no-track --path .
install -Dp rp -t %buildroot%_bindir

%define _customdocdir %_docdir/%name

%check
cargo test %_smp_mflags --release --no-fail-fast --locked

# Also manual test for rosenpass.
PATH=%buildroot%_bindir:$PATH
rosenpass keygen private-key r1 public-key p1
rosenpass keygen private-key r2 public-key p2
rosenpass exchange private-key r1 public-key p1 verbose listen 0:2345 peer public-key p2 outfile o1 &
rosenpass exchange private-key r2 public-key p2 verbose peer public-key p1 endpoint 127.1:2345 outfile o2 &
sleep 1
diff -u o1 o2
kill %%1 %%2

%files
%doc LICENSE* readme*
%_bindir/rosenpass
%_bindir/rp

%changelog
* Fri Mar 03 2023 Vitaly Chikunov <vt@altlinux.org> 0.1.1-alt1
- First import v0.1.1-7-gbecc8c05 (2023-02-28).
