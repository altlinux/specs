# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: rosenpass
Version: 0.2.2
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

This is experimental and all (non-packaging) bug reports should go to
upstream tracker:

  https://github.com/rosenpass/rosenpass/issues

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
install -Dp target/release/rosenpass -t %buildroot%_bindir
install -Dp rp -t %buildroot%_bindir
install -Dpm644 doc/rosenpass.1 -t %buildroot%_man1dir
install -Dpm644 doc/rp.1 -t %buildroot%_man1dir

%define _customdocdir %_docdir/%name

%check
cargo test %_smp_mflags --release --no-fail-fast --locked

# Also manual test for rosenpass.
PATH=%buildroot%_bindir:$PATH
rosenpass gen-keys --secret-key r1 --public-key p1
rosenpass gen-keys --secret-key r2 --public-key p2
rosenpass exchange private-key r1 public-key p1 verbose listen 0:2345 peer public-key p2 outfile o1 &
rosenpass exchange private-key r2 public-key p2 verbose peer public-key p1 endpoint 127.1:2345 outfile o2 &
sleep 1
diff -u o1 o2
kill %%1 %%2

%files
%doc LICENSE* readme*
%_bindir/rosenpass
%_bindir/rp
%_man1dir/rosenpass.1*
%_man1dir/rp.1*

%changelog
* Sat Jul 06 2024 Vitaly Chikunov <vt@altlinux.org> 0.2.2-alt1
- Security update to v0.2.2 (2024-06-05).

* Sun Nov 26 2023 Vitaly Chikunov <vt@altlinux.org> 0.2.1-alt1
- Update to v0.2.1 (2023-11-18) (ALT#48591).

* Fri Mar 03 2023 Vitaly Chikunov <vt@altlinux.org> 0.1.1-alt1
- First import v0.1.1-7-gbecc8c05 (2023-02-28).
