%def_with check

Name: broot
Version: 1.36.1
Release: alt1
Summary: A new way to see and navigate directory trees
License: MIT
Group: File tools
Url: https://dystroy.org/broot
Source: %name-%version.tar
Source1: vendor.tar
Patch: alt-fix-build-nix-on-loongarch64.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: cargo-vendor-checksum diffstat

%description
%summary.

%prep
%setup -a 1
%patch -p1
diffstat -p1 -l < %PATCH0 | sed -re 's@vendor/@@' | xargs -r cargo-vendor-checksum -f
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%ifarch armh
# build failed with lto
sed -i 's/lto = true/lto = false/' Cargo.toml
%endif
%rust_build

%install
%rust_install
install -Dm 0644 man/page %buildroot%_man1dir/%name.1

%check
%rust_test

%files
%_bindir/%name
%_man1dir/%name.1.*

%changelog
* Fri Apr 26 2024 Alexander Makeenkov <amakeenk@altlinux.org> 1.36.1-alt1
- Updated to version 1.36.1.

* Sun Jan 07 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.32.0-alt2
- NMU: fixed FTBFS on LoongArch.

* Sat Jan 06 2024 Alexander Makeenkov <amakeenk@altlinux.org> 1.32.0-alt1
- Updated to version 1.32.0.

* Sat Dec 17 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.17.1-alt1
- Updated to version 1.17.1

* Sat Nov 19 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.16.2-alt1
- Updated to version 1.16.2

* Sun Oct 30 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.16.1-alt1
- Initial build for ALT

