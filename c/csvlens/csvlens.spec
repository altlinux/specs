%def_without check

Name:    csvlens
Version: 0.14.0
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

# XXX: check fails
# error: 1 target failed:
#     `--lib`
%if_with check
%check
%rust_test --workspace
%endif

%files
%doc *.md LICENSE
%_bindir/%name
%_man1dir/%name.1.*

%changelog
* Wed Nov 05 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.14.0-alt1
- New version.

* Mon Aug 04 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.13.0-alt2
- Fixed FTBFS: removed --no-fail-fast cause macro already contains.

* Mon Jun 16 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.13.0-alt1
- New version.

* Mon Feb 24 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.12.0-alt1
- New version.

* Tue Feb 04 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.11.0-alt1
- New version.

* Thu Sep 19 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.10.1-alt1
- New version

* Tue Aug 06 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.9.1-alt1
- Initial build for Sisyphus (Closes: #50194)
