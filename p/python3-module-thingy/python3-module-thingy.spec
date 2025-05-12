%define pypi_name thingy

%def_with check

Name:    python3-module-%pypi_name
Version: 0.10.0
Release: alt2

Summary: Dictionaries as objects, that can have different dictionary views
License: MIT
Group:   Development/Python3
URL:     https://github.com/Refty/thingy

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version
sed -i '54s/^/    /' test_thingy.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/%pypi_name.py
%python3_sitelibdir/__pycache__/%{pypi_name}*
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Mon May 12 2025 Alexander Burmatov <thatman@altlinux.org> 0.10.0-alt2
- Fix build.

* Mon Apr 28 2025 Alexander Burmatov <thatman@altlinux.org> 0.10.0-alt1
- Initial build for Sisyphus.
