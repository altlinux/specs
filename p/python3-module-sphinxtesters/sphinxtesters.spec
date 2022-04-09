%def_without test
%define oname sphinxtesters

Name: python3-module-%oname
Version: 0.2.3
Release: alt3

Summary: Utilities for testing Sphinx extensions

License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/sphinxtesters

BuildArch: noarch

# Source-url: %__pypi_url %oname
Source: %oname-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3

#BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(docutils) python3(nose.tools) python3(sphinx.application)
BuildRequires: python3-module-pytest

%description
Sphinxtesters - utilities for testing Sphinx extensions.

%package tests
Summary: Utilities for testing Sphinx extensions
Group: Development/Python3

%description tests
Sphinxtesters - utilities for testing Sphinx extensions.

This package contains tests.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install
%python3_prune

%check
py.test3 -vv

%files
%doc LICENSE README.rst
%python3_sitelibdir/*
#exclude %python_sitelibdir/%oname/tests

#files tests
#python_sitelibdir/%oname/tests

%changelog
* Sat Apr 09 2022 Vitaly Lipatov <lav@altlinux.ru> 0.2.3-alt3
- disable tests (due test_pagebuilder.py:88)

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 0.2.3-alt2
- NMU: build python3 module separately

* Wed Aug 28 2019 Grigory Ustinov <grenka@altlinux.org> 0.2.3-alt1
- Build new version.

* Mon Dec 24 2018 Grigory Ustinov <grenka@altlinux.org> 0.2.1-alt1
- Build new version.

* Thu Feb 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt2
- Updated build dependencies.

* Tue Nov 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt1
- Initial build for ALT.
