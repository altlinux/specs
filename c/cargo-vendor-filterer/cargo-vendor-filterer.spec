
# The integration tests require full access to crates.io.
# which is not available in hasher. You can stil l run e.g.
#   gear-rpm -ba --commit --with=integration_tests
# to make sure everything's ok.
%def_without integration_tests

Name:    cargo-vendor-filterer
Version: 0.5.14
Release: alt1

Summary: Tool to `cargo vendor` with filtering
License: Apache-2.0
Group:   Other
Url:     https://github.com/coreos/cargo-vendor-filterer

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:  %name-%version.tar
Source1: vendor.tar
Source2: cargo-vendor-alt
Patch:   %name-%version-%release.patch

BuildRequires: libssl-devel
BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

%description
The core cargo vendor tool is useful to save all dependencies. However, it
doesn't offer any filtering; today cargo includes all platforms, but some
projects only care about Linux for example.

%prep
%setup
tar -xf %SOURCE1
%autopatch -p1


# The test actually remove the `vendor` directory, and then
# fail miserably. As a workaround for that we use non-standard
# name for the vendored sources directory
mv vendor vendor-alt
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor-alt"
EOF

%build
%rust_build

%install
%rust_install
install -pDm 0755 %SOURCE2 %buildroot%_bindir

%check
export RUST_BACKTRACE=full
%if_with integration_tests
rm -rf .cargo
%rust_test
%else
%rust_test --lib --bins
%endif

%files
%doc *.md
%_bindir/*

%changelog
* Sun Oct 20 2024 Ivan A. Melnikov <iv@altlinux.org> 0.5.14-alt1
- 0.5.14
- build from gear tag
- add riscv64 platform to cargo-vendor-alt
- disable integration tests by default, as they require
  internet access

* Thu Mar 07 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.5.9-alt3
- cargo-vendor-alt: added LoongArch platform
- updated rustix, libc, linux-raw-sys so the package builds on LoongArch

* Fri Apr 21 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.5.9-alt2
- Vendor all features in cargo-vendor-alt

* Wed Apr 19 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.5.9-alt1
- Initial build for Sisyphus
