%define oname sphinxcontrib-serializinghtml

%def_with check

Name:    python3-module-%oname
Version: 1.1.10
Release: alt1

Summary: Sphinx extension for serialized HTML

Group:   Development/Python3
License: BSD-2-Clause
URL:     https://pypi.org/project/sphinxcontrib-serializinghtml

# https://files.pythonhosted.org/packages/54/13/8dd7a7ed9c58e16e20c7f4ce8e4cb6943eb580955236d0c0d00079a73c49/sphinxcontrib_serializinghtml-1.1.10.tar.gz
Source0: %oname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: gettext python3-module-flit-core

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-sphinx-tests
%endif

%description
sphinxcontrib-serializinghtml is a sphinx extension which outputs "serialized"
HTML files (json and pickle).

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
%python3_sitelibdir/%{pyproject_distinfo %oname}/

%changelog
* Sat Jan 20 2024 L.A. Kostis <lakostis@altlinux.ru> 1.1.10-alt1
- 1.1.10.
- .spec:
  + BR: add flit-core
  + modernise python macros.

* Sat Apr 16 2022 Fr. Br. George <george@altlinux.ru> 1.1.5-alt2
- Fix old version

* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.5-alt1
- Automatically updated to 1.1.5.

* Mon Mar 02 2020 Grigory Ustinov <grenka@altlinux.org> 1.1.4-alt1
- Build new version.
- Build with check.
- Fix license.

* Thu Apr 25 2019 Grigory Ustinov <grenka@altlinux.org> 1.1.3-alt1
- Initial build for Sisyphus.
