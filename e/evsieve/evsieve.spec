Name: evsieve
Version: 1.4.0
Release: alt1
Summary: A utility for mapping events from Linux event devices
Group: Other
Source0: %name-%version.tar
License: GPL-2.0-or-later AND MIT AND GPL-2.0-only WITH Linux-syscall-note

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
* Thu Oct 17 2024 Artyom Bystrov <arbars@altlinux.org> 1.4.0-alt1
- Initial build