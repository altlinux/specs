%define  modulename cairocffi

Name:    python3-module-%modulename
Version: 1.0.2
Release: alt2

Summary: CFFI-based cairo bindings for Python.
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/Kozea/cairocffi

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-cffi
BuildRequires: python3-module-pytest-runner

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%package tests
Summary: %summary
Group: Development/Python3
Requires: %name = %EVR

%description tests
%summary

This package contains tests for Python-3.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%exclude %python3_sitelibdir/%modulename/test_*.py
%exclude %python3_sitelibdir/%modulename/__pycache__/test_*
%python3_sitelibdir/*.egg-info
%doc *.rst

%files tests
%python3_sitelibdir/%modulename/test_*.py
%python3_sitelibdir/%modulename/__pycache__/test_*

%changelog
* Wed Jun 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.2-alt2
- Moved tests into separate package.

* Sat Jun 29 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
