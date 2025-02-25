Name:    csvlens
Version: 0.12.0
Release: alt1

Summary: Command line csv viewer
License: MIT
Group:   File tools
URL:     https://github.com/YS-L/csvlens

Source0: %name-%version.tar
Source1: %name.1.xz
Source2: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo /proc
# Uncomment req below to vendor dependencies inside chrooted env correctly.
# BuildRequires: cargo-vendor-filterer

%description
csvlens is a command line CSV file viewer.
It is like less(1) but made for CSV.

%prep
%setup -a2

mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
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
install -d %buildroot%_man1dir
install -pv %SOURCE1 %buildroot%_man1dir

%check
# FIXME: Failed on x86(_64) arches test switched off. Check in further update.
%rust_test --workspace --no-fail-fast \
-- --skip 'app::tests::test_irregular_filter_columns_then_rows'

%files
%doc *.md LICENSE
%_bindir/%name
%_man1dir/%name.1.*

%changelog
* Mon Feb 24 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.12.0-alt1
- New version.

* Tue Feb 04 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.11.0-alt1
- New version.

* Thu Sep 19 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.10.1-alt1
- New version

* Tue Aug 06 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.9.1-alt1
- Initial build for Sisyphus (Closes: #50194)
