Name: rust-bindgen
Version: 0.68.1
Release: alt1

Summary: Automatically generates Rust FFI bindings to C (and some C++) libraries
License: BSD-3-Clause
Group: Development/Other
Url: https://github.com/rust-lang/rust-bindgen

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

%description
%summary

%prep
%setup
%ifdef bootstrap
cargo vendor
tar cf %SOURCE1 vendor
%else
tar xf %SOURCE1
%endif

%build
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
%rust_build

%install
mkdir -p %buildroot%_bindir
install -Dm0755 target/release/bindgen %buildroot%_bindir/

%files
%doc LICENSE README.md CHANGELOG.md CONTRIBUTING.md
%_bindir/bindgen

%changelog
* Wed Oct 04 2023 L.A. Kostis <lakostis@altlinux.ru> 0.68.1-alt1
- 0.68.1.

* Mon Jul 17 2023 L.A. Kostis <lakostis@altlinux.ru> 0.66.1-alt1
- 0.66.1.

* Fri Jun 16 2023 L.A. Kostis <lakostis@altlinux.ru> 0.66.0-alt1
- 0.66.0.

* Mon Jun 12 2023 L.A. Kostis <lakostis@altlinux.ru> 0.65.1-alt1.1
- Fix Url.

* Fri Jun 09 2023 L.A. Kostis <lakostis@altlinux.ru> 0.65.1-alt1
- Initial build for ALTLinux.
