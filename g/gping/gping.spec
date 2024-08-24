%def_with check

Name: gping
Version: 1.17.3
Release: alt1
Summary: Ping, but with a graph
License: MIT
Group: Networking/Other
Url: https://github.com/orf/gping

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo

%if_with check
BuildRequires: iputils
%endif

%description
%summary.

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

%changelog
* Sat Aug 24 2024 Alexander Makeenkov <amakeenk@altlinux.org> 1.17.3-alt1
- Updated to version 1.17.3.

* Mon May 13 2024 Anastasia Osmolovskaya <lola@altlinux.org> 1.16.1-alt1
- Updated to version 1.16.1

* Sun Dec 10 2023 Alexander Makeenkov <amakeenk@altlinux.org> 1.16.0-alt1
- Updated to version 1.16.0.

* Mon Jan 30 2023 Alexander Makeenkov <amakeenk@altlinux.org> 1.8.0-alt1
- Updated to version 1.8.0

* Sat Dec 17 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.6.1-alt1
- Updated to version 1.6.1

* Fri Oct 07 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.4.0-alt1
- Updated to version 1.4.0

* Mon Jun 27 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.3.2-alt1
- Updated to version 1.3.2

* Mon May 16 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.3.1-alt1
- Updated to version 1.3.1

* Sat Nov 20 2021 Alexander Makeenkov <amakeenk@altlinux.org> 1.2.6-alt1
- Updated to version 1.2.6

* Sun Jun 06 2021 Alexander Makeenkov <amakeenk@altlinux.org> 1.2.1-alt1
 - Initial build for ALT

