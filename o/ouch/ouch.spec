%def_with check

Name: ouch
Version: 0.5.1
Release: alt1
Summary: Painless compression and decompression for your terminal
License: MIT
Group: Archiving/Compression
Url: https://github.com/ouch-org/ouch
Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: gcc-c++
BuildRequires: rust-cargo

%description
ouch stands for Obvious Unified Compression Helper and is a CLI tool
to help you compress and decompress files of several formats.

%prep
%setup -a 1
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

%check
%rust_test

%files
%_bindir/%name
%doc README.md

%changelog
* Wed Dec 20 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.5.1-alt1
- Updated to version 0.5.1.

* Mon Jan 30 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.4.1-alt1
- Updated to version 0.4.1

* Sat Dec 17 2022 Alexander Makeenkov <amakeenk@altlinux.org> 0.4.0-alt1
- Updated to version 0.4.0

* Thu Jun 02 2022 Alexander Makeenkov <amakeenk@altlinux.org> 0.3.1-alt1
- Initial build for ALT
