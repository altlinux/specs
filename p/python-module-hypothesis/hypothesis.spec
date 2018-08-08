%define _unpackaged_files_terminate_build 1

%define oname hypothesis

%def_with python3

%ifnarch %ix86 x86_64
%def_disable check
%endif

Name: python-module-%oname
Version: 3.66.30
Release: alt1
Summary: A library for property based testing
License: MPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/hypothesis

BuildArch: noarch

# https://github.com/HypothesisWorks/hypothesis-python.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python
BuildRequires: python-module-setuptools
BuildRequires: python-module-enum34 python-module-numpy python-module-flaky python-module-pytz python-module-django
BuildRequires: python-module-django-tests python-module-fake-factory python-modules-sqlite3
BuildRequires: python2.7(mock) python2.7(coverage) python2.7(pandas) python2.7(dateutil)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-numpy python3-module-flaky python3-module-pytz python3-module-django
BuildRequires: python3-module-django-tests python3-module-fake-factory python3-modules-sqlite3
BuildRequires: python3(mock) python3(coverage) python3(pandas) python3(dateutil)
%endif

%py_requires coverage

%description
Hypothesis is an advanced testing library for Python. It lets you write tests
which are parametrized by a source of examples, and then generates simple and
comprehensible examples that make your tests fail. This lets you find more bugs
in your code with less work.

%package -n python3-module-%oname
Summary: A library for property based testing for Python 3
Group: Development/Python3
%py3_requires coverage

%description -n python3-module-%oname
Hypothesis is an advanced testing library for Python. It lets you write tests
which are parametrized by a source of examples, and then generates simple and
comprehensible examples that make your tests fail. This lets you find more bugs
in your code with less work.

%prep
%setup

%if_with python3
cp -a . ../python3
%endif

%build
pushd hypothesis-python
%python_build
popd

%if_with python3
pushd ../python3/hypothesis-python
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3/hypothesis-python
%python3_install
popd
%endif

pushd hypothesis-python
%python_install
popd

%check
pushd hypothesis-python
rm -rf tests/py3 tests/django/toystore
PYTHONPATH=%buildroot%python_sitelibdir py.test
popd

%if_with python3
pushd ../python3/hypothesis-python
rm -rf tests/py2 tests/django/toystore
PYTHONPATH=%buildroot%python3_sitelibdir py.test3
popd
%endif

%files
%doc CONTRIBUTING.rst LICENSE.txt hypothesis-python/README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CONTRIBUTING.rst LICENSE.txt hypothesis-python/README.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Aug 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.66.30-alt1
- Updated to upstream version 3.66.30.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.18.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.18.1-alt1
- Updated to upstream version 3.18.1.

* Thu Jan 19 2017 Anton Midyukov <antohami@altlinux.org> 3.6.1-alt1
- Initial build for ALT Linux Sisyphus.
