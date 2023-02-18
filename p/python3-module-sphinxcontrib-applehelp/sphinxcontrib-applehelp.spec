%define  oname sphinxcontrib-applehelp

%def_with check

Name:    python3-module-%oname
Version: 1.0.4
Release: alt1

Summary: A sphinx extension which outputs Apple help books

License: BSD-2-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/sphinxcontrib-applehelp

# https://github.com/sphinx-doc/sphinxcontrib-applehelp
Source:  %oname-%version.tar

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-sphinx-tests
%endif

BuildArch: noarch

%description
%summary

%prep
%setup -n %oname-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc README.rst
%python3_sitelibdir/sphinxcontrib
%python3_sitelibdir/%{pyproject_distinfo sphinxcontrib_applehelp}

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 1.0.4-alt1
- Automatically updated to 1.0.4.

* Mon Mar 02 2020 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt1
- Build new version.
- Build with check.
- Fix license.

* Thu Apr 25 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
