%define _unpackaged_files_terminate_build 1

Name: oha
Version: 1.14.0
Release: alt1
Summary: Ohayou, HTTP load generator with tui animation
License: MIT
Group: Networking/Remote access
Url: https://github.com/hatoo/oha

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: pkgconfig(openssl)

%ifarch loongarch64 riscv64
# need to recompile aws-lc-sys
BuildRequires: cmake rust-bindgen clang-devel
%endif

%description
Oha is a tiny program that sends some load to a web application and show
realtime tui inspired by rakyll/hey.

%prep
%setup -a 1
%patch -p1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF

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
%doc README.md CHANGELOG.md
%_bindir/%name

%changelog
* Fri May 08 2026 Pavel Shilov <zerospirit@altlinux.org> 1.14.0-alt1
- 1.12.1 -> 1.14.0

* Tue Dec 23 2025 Pavel Shilov <zerospirit@altlinux.org> 1.12.1-alt1
- 1.10.0 -> 1.12.1

* Mon Sep 15 2025 Pavel Shilov <zerospirit@altlinux.org> 1.10.0-alt1
- 1.9.0 -> 1.10.0

* Fri Sep 12 2025 Ivan A. Melnikov <iv@altlinux.org> 1.9.0-alt2
- NMU: fix FTBFS on loongarch64

* Fri Jul 11 2025 Pavel Shilov <zerospirit@altlinux.org>  1.9.0-alt1
- Initial build for Sisyphus.
