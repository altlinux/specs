
Name: cbindgen
Version: 0.26.0
Release: alt1
Summary: cbindgen creates C/C++11 headers for Rust libraries which expose a public C API
License: MPL-2.0
Group: File tools
Url: https://github.com/eqrion/cbindgen
Vcs: https://github.com/eqrion/cbindgen.git
Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

%description
%summary.

%prep
%setup
%patch -p1

mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF


%build
%rust_build

%install
%rust_install

%files
%doc README.md
%_bindir/%name

%changelog
* Fri Jun 07 2024 L.A. Kostis <lakostis@altlinux.ru> 0.26.0-alt1
- 0.26.0.

* Fri Jan 28 2022 Alexey Shabalin <shaba@altlinux.org> 0.20.0-alt1
- Initial build.
