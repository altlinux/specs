%define _unpackaged_files_terminate_build 1
%define oname nazca
Name: python-module-%oname
Version: 0.7.2
Release: alt2.1
Summary: Python library for data alignment
License: LGPL
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/nazca/

Source: %{oname}-%{version}.tar.gz

BuildRequires: python-module-setuptools python-module-lxml
BuildRequires: python-module-scipy python-module-scikit-learn
BuildRequires: python-module-dateutil python2.7(SPARQLWrapper) python2.7(nltk)

%py_provides %oname
%py_requires scipy sklearn lxml dateutil SPARQLWrapper nltk

%description
Python library for data alignment.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Python library for data alignment.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test
%exclude %python_sitelibdir/*/examples

%files tests
%python_sitelibdir/*/test
%python_sitelibdir/*/examples

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.2-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.2-alt2
- Updated dependencies.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.2-alt1
- automated PyPI update

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus

