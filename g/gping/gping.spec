%def_with check

Name: gping
Version: 1.20.4
Release: alt1
Summary: Ping, but with a graph
License: MIT
Group: Networking/Other
Url: https://crates.io/crates/gping
VCS: https://github.com/orf/gping

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%if_with check
BuildRequires: iputils
%endif

%description
%summary.

%prep
%setup -a 1
%rust_prep

%build
%rust_build

%install
%rust_install

%check
# ping: operation not permitted
%rust_test -- \
    --skip test_integration_any \
    --skip test_integration_ip6 \
    --skip test_integration_ipv4

%files
%_bindir/%name
%doc LICENSE

%changelog
* Sun Jul 05 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.20.4-alt1
- Updated to version 1.20.4.

* Fri Jun 19 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.20.2-alt1
- Updated to version 1.20.2.

* Sat Nov 08 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.20.1-alt1
- Updated to version 1.20.1.

* Mon Jan 06 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.19.0-alt1
- Updated to version 1.19.0.

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

