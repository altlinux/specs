%define _unpackaged_files_terminate_build 1

Name: rainfrog
Version: 0.3.6
Release: alt1
Summary: %name a database tool for the terminal
License: MIT
Group: Databases
Url: https://github.com/achristmascarl/rainfrog

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo

%description
%summary

%prep
%setup -a 1
%autopatch -p1

%build
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[profile.release]
strip = false
%ifarch i586
# Use less optimisation otherwise it causes "out of memory" error on 32-bit
lto = "thin"
codegen-units = 16
%endif
EOF
%rust_build

%install
%rust_install

%files
%doc *.md LICENSE
%_bindir/%name

%changelog
* Wed Aug 26 2025 Pavel Shilov <zerospirit@altlinux.org> 0.3.6-alt1
- 0.3.5 -> 0.3.6

* Mon Aug 25 2025 Pavel Shilov <zerospirit@altlinux.org> 0.3.5-alt1
- Initial build for Sisyphus.

