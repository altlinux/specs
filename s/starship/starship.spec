%ifarch i586 armh ppc64le
%def_without check
%else
%def_with check
%endif

Name: starship
Version: 1.20.1
Release: alt1
Summary: The minimal, blazing-fast, and infinitely customizable prompt for any shell
License: ISC
Group: Shells
Url: https://github.com/starship/starship

Source: %name-%version.tar
Source1: vendor.tar
Patch: starship-1.17.1-libz-ng-sys-loongarch64.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: cargo-vendor-checksum
BuildRequires: rust-cargo
BuildRequires: cmake

%if_with check
BuildRequires: git
%endif

%description
%summary.

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
%ifarch armh i586
# build failed with lto
sed -i 's/lto = true/lto = false/' Cargo.toml
%endif
cargo-vendor-checksum --all
%rust_build

%install
%rust_install

%check
%buildroot%_bindir/%name print-config > %name.toml
export STARSHIP_CONFIG=%name.toml
export TERM=xterm
# skip randomly failing test
cargo test -- --skip expiration_date_set

%files
%_bindir/%name

%changelog
* Tue Aug 27 2024 Alexander Makeenkov <amakeenk@altlinux.org> 1.20.1-alt1
- Updated to version 1.20.1.

* Sun Jan 07 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.17.1-alt2
- NMU: fixed FTBFS on LoongArch

* Fri Jan 05 2024 Alexander Makeenkov <amakeenk@altlinux.org> 1.17.1-alt1
- Updated to version 1.17.1.

* Wed Sep 13 2023 Alexander Makeenkov <amakeenk@altlinux.org> 1.16.0-alt1
- Updated to version 1.16.0.

* Thu Apr 06 2023 Alexander Makeenkov <amakeenk@altlinux.org> 1.13.1-alt1
- Updated to version 1.13.1

* Sun Dec 18 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.12.0-alt1
- Updated to version 1.12.0
- Enabled check

* Sun Nov 20 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.11.0-alt1
- Initial build for ALT

