%define _unpackaged_files_terminate_build 1

Name: rainfrog
Version: 0.3.18
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
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel

%description
%summary

%prep
%setup -a 1
%autopatch -p1

%build
export CC=gcc
export CXX=g++
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
lto = false
codegen-units = 1
opt-level = 2
panic = "abort"
%endif
EOF
%rust_build

%install
%rust_install

%files
%doc *.md LICENSE
%_bindir/%name

%changelog
* Tue May 12 2026 Pavel Shilov <zerospirit@altlinux.org> 0.3.18-alt1
- Update to new version 0.3.18.

* Thu Feb 26 2026 Pavel Shilov <zerospirit@altlinux.org> 0.3.17-alt1
- Update to new version 0.3.17.

* Wed Feb 04 2026 Pavel Shilov <zerospirit@altlinux.org> 0.3.14-alt1
- Update to new version 0.3.14.

* Tue Dec 23 2025 Pavel Shilov <zerospirit@altlinux.org> 0.3.12-alt1
- 0.3.8 -> 0.3.12

* Wed Oct 22 2025 Pavel Shilov <zerospirit@altlinux.org> 0.3.8-alt1
- 0.3.7 -> 0.3.8

* Wed Sep 03 2025 Pavel Shilov <zerospirit@altlinux.org> 0.3.7-alt1
- 0.3.6 -> 0.3.7

* Wed Aug 27 2025 Pavel Shilov <zerospirit@altlinux.org> 0.3.6-alt1
- 0.3.5 -> 0.3.6

* Mon Aug 25 2025 Pavel Shilov <zerospirit@altlinux.org> 0.3.5-alt1
- Initial build for Sisyphus.

