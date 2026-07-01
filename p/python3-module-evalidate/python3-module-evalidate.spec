%define pypi_name evalidate

%def_without check

Name:    python3-module-%pypi_name
Version: 2.1.4
Release: alt1

Summary: Safe and fast evaluation of untrusted user-supplied python expressions
License: MIT
Group:   Development/Python3
URL:     https://github.com/yaroslaff/evalidate

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-hatchling

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Evalidate is simple python module for safe and very fast eval()'uating
user-supplied (possible malicious) python expressions.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jul 01 2026 Egor Ignatov <egori@altlinux.org> 2.1.4-alt1
- New version 2.1.4.

* Thu Jul 24 2025 Egor Ignatov <egori@altlinux.org> 2.0.5-alt1
- New version 2.0.5.

* Fri Oct 25 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.0.2-alt1
- Initial build for Sisyphus
