%define _unpackaged_files_terminate_build 1

Name: cbindgen
Version: 0.29.2
Release: alt1

Summary: A project for generating C bindings from Rust code.
License: MPL-2.0
Group: Development/Tools
Url: https://crates.io/crates/cbindgen
Vcs: https://github.com/mozilla/cbindgen

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

%description
cbindgen creates C/C++11 headers for Rust libraries which expose a public C API.

%prep
%setup -a1

mkdir -p .cargo
cat >> .cargo/config <<EOF
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
%rust_install

%files
%doc README.md
%_bindir/cbindgen

%changelog
* Fri Oct 24 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.29.2-alt1
- New version.

* Sat May 24 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.29.0-alt1
- New version.

* Mon May 05 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.28.0-alt1
- New version.
- Change group tag from File tools to Development/Tools.
- Update VCS, URL and summary.

* Fri Aug 30 2024 L.A. Kostis <lakostis@altlinux.ru> 0.27.0-alt1
- 0.27.0.

* Tue Jun 11 2024 L.A. Kostis <lakostis@altlinux.ru> 0.26.0-alt2
- build with debuginfo.

* Fri Jun 07 2024 L.A. Kostis <lakostis@altlinux.ru> 0.26.0-alt1
- 0.26.0.

* Fri Jan 28 2022 Alexey Shabalin <shaba@altlinux.org> 0.20.0-alt1
- Initial build.
