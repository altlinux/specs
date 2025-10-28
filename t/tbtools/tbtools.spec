%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: tbtools
Version: 0.7.0
Release: alt1
Summary: Thunderbolt/USB4 debugging tools
Group: System/Configuration/Hardware
License: BSD
Url: https://github.com/intel/tbtools
Vcs: https://github.com/intel/tbtools.git

BuildRequires(pre): rpm-macros-rust
BuildRequires: /proc rust rust-cargo libudev-devel

Source0: %name-%version.tar
Source1: %name-vendor.tar

Requires: bash-completion

%description
This is a collection of tools for Linux Thunderbolt/USB4 development,
debugging and validation but may be useful to others as well. This
consists of a library (`tbtools`) that can be used as standalone for a
custom tools, and a basic set of debugging tools built on top of this
library.

%prep
%setup -a1

mkdir -p .cargo
cat > .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[profile.release]
strip = "none"
lto= "thin"
debug = "full"
EOF

%build
%rust_build

%install
mkdir -p %buildroot%_prefix
make install PREFIX=%buildroot%_prefix
rm -f %buildroot%_prefix/.crates*

%files
%_bindir/lstb
%_bindir/tb*
%_datadir/%name
%_datadir/bash-completion/completions/*

%changelog
* Tue Oct 28 2025 L.A. Kostis <lakostis@altlinux.ru> 0.7.0-alt1
- 0.7.0.

* Mon Aug 18 2025 L.A. Kostis <lakostis@altlinux.ru> 0.6.0-alt1
- Initial build for ALTLinux.

