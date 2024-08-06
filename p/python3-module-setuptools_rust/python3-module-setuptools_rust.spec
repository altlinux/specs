%define pypi_name setuptools-rust
%define modname setuptools_rust

Name: python3-module-%modname
Version: 1.10.1
Release: alt1

Summary: Setuptools helpers for rust Python extensions.

License: MIT
Group: Development/Python3
Url: https://github.com/PyO3/setuptools-rust

Packager: Vladimir Didenko <cow@altlinux.org>

Source: %name-%version.tar
BuildArch: noarch
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
Compile and distribute Python extensions written in rust as easily as if they
were written in C.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%modname/
%python3_sitelibdir/%{pyproject_distinfo %modname}

%changelog
* Tue Aug 6 2024 Vladimir Didenko <cow@altlinux.org> 1.10.1-alt1
- new version

* Tue Feb 27 2024 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt1
- new version

* Tue Oct 31 2023 Vladimir Didenko <cow@altlinux.org> 1.8.1-alt1
- new version

* Tue Sep 5 2023 Vladimir Didenko <cow@altlinux.org> 1.7.0-alt1
- new version

* Thu May 25 2023 Vladimir Didenko <cow@altlinux.org> 1.6.0-alt1
- new version

* Fri May 05 2023 Stanislav Levin <slev@altlinux.org> 1.5.2-alt2
- Mapped PyPI name to distro's one.

* Fri Oct 28 2022 Vladimir Didenko <cow@altlinux.org> 1.5.2-alt1
- new version

* Wed Aug 24 2022 Vladimir Didenko <cow@altlinux.org> 1.5.1-alt1
- new version

* Wed May 4 2022 Vladimir Didenko <cow@altlinux.org> 1.3.0-alt1
- new version

* Wed Apr 6 2022 Vladimir Didenko <cow@altlinux.org> 1.2.0-alt1
- new version

* Mon Dec 6 2021 Vladimir Didenko <cow@altlinux.org> 1.1.2-alt1
- new version

* Thu Dec 2 2021 Vladimir Didenko <cow@altlinux.org> 1.1.1-alt1
- new version

* Fri Jul 30 2021 Vladimir Didenko <cow@altlinux.org> 0.12.1-alt1
- initial build for Sisyphus

* Mon Feb 8 2021 Vladimir Didenko <cow@altlinux.org> 0.11.6-alt1
- initial build for Sisyphus
