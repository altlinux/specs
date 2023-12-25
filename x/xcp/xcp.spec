%def_without check

Name: xcp
Version: 0.16.0
Release: alt2
Summary: An extended cp
License: GPL-3.0
Group: File tools
Url: https://github.com/tarka/xcp
Source: %name-%version.tar
Source1: vendor.tar
Patch1: alt-fix-i586-armh-build.patch
Patch3500: alt-loongarch64-fiemap.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: cargo-vendor-checksum diffstat

%description
xcp is a (partial) clone of the Unix cp command. It is not intended
as a full replacement, but as a companion utility with some more
user-friendly feedback and some optimisations that make sense under
certain tasks.

%prep
%setup -a 1
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
%ifarch i586 armh
%patch1 -p1
%endif

%patch3500 -p1
diffstat -p1 -l < %PATCH3500 | sed -re 's@vendor/@@' | xargs cargo-vendor-checksum -f

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/%name

%changelog
* Mon Dec 25 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.16.0-alt2
- NMU: fixed FTBFS on LoongArch.

* Sun Dec 24 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.16.0-alt1
- Updated to version 0.16.0.

* Sun Sep 17 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.12.0-alt1
- Updated to version 0.12.0.

* Sun Jun 25 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.10.0-alt1
- Initial build for ALT.
