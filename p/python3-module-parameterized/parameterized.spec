%define  modulename parameterized

# not adapted for modern pytest
%def_without check

Name:    python3-module-%modulename
Version: 0.9.0
Release: alt1

Summary: Parameterized testing with any Python test framework

License: BSD
Group:   Development/Python3
URL:     https://pypi.org/project/parameterized/
# https://github.com/wolever/parameterized

Source:  %name-%version.tar
Patch: remove_nose.patch

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

%description
%summary

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -v parameterized/test.py

%files
%doc *.rst
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Wed Jun 14 2023 Grigory Ustinov <grenka@altlinux.org> 0.9.0-alt1
- Automatically updated to 0.9.0.

* Mon May 30 2022 Grigory Ustinov <grenka@altlinux.org> 0.8.1-alt1
- Build new version.
- Build without nose.

* Sat Mar 16 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus
