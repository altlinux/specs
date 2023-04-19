Name:    cargo-vendor-filterer
Version: 0.5.9
Release: alt1

Summary: Tool to `cargo vendor` with filtering
License: Apache-2.0
Group:   Other
Url:     https://github.com/coreos/cargo-vendor-filterer

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar

BuildRequires: libssl-devel
BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

%description
The core cargo vendor tool is useful to save all dependencies. However, it
doesn't offer any filtering; today cargo includes all platforms, but some
projects only care about Linux for example.

%prep
%setup
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
install -pDm 0755 cargo-vendor-alt %buildroot%_bindir

%check
%rust_test

%files
%doc *.md
%_bindir/*

%changelog
* Wed Apr 19 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.5.9-alt1
- Initial build for Sisyphus
