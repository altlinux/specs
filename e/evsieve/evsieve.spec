Name: evsieve
Version: 1.4.0
Release: alt2
Summary: A utility for mapping events from Linux event devices
Group: Other
License: GPL-2.0-or-later AND MIT AND GPL-2.0-only WITH Linux-syscall-note
URL: https://github.com/KarsMulder/evsieve

Source0: %name-%version.tar
Patch0: evsieve-1.4.0-libc-crate-loongarch64.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: gcc gcc-c++ libevdev-devel build-essential glibc-devel
BuildRequires: rust
BuildRequires: rust-cargo
BuildRequires: cargo-about

%description
A utility for mapping events from Linux event devices
Evsieve (from "event sieve") is a low-level utility that can read events from Linux event devices (evdev) and write them to virtual event devices (uinput), performing simple manipulations on the events along the way. 

%prep
%setup

%ifarch loongarch64
%patch0 -p1
sed -i -e 's/"files":{[^}]*}/"files":{}/' \
     ./vendor/libc/.cargo-checksum.json
%endif

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

%build
%rust_build

%install
%rust_install

%files
%_bindir/evsieve

%changelog
* Wed Dec 25 2024 Ilya Sorochan <k0tran@altlinux.org> 1.4.0-alt2
- Add patch for loongarch64 for libc crate.
- Spec cleanup

* Thu Oct 17 2024 Artyom Bystrov <arbars@altlinux.org> 1.4.0-alt1
- Initial build
