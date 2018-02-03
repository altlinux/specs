%define oname hypothesis

%def_with python3

Name: python-module-%oname
Version: 3.18.1
Release: alt1.1
Summary: A library for property based testing
License: MPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/hypothesis
BuildArch: noarch

# https://github.com/HypothesisWorks/hypothesis-python.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-tests.patch

BuildRequires(pre): rpm-build-python
BuildRequires: python-module-setuptools
BuildRequires: python-module-enum34 python-module-numpy python-module-flaky python-module-pytz python-module-django
BuildRequires: python-module-django-tests python-module-fake-factory python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-enum34 python3-module-numpy python3-module-flaky python3-module-pytz python3-module-django
BuildRequires: python3-module-django-tests python3-module-fake-factory python3-modules-sqlite3
%endif

%description
Hypothesis is an advanced testing library for Python. It lets you write tests
which are parametrized by a source of examples, and then generates simple and
comprehensible examples that make your tests fail. This lets you find more bugs
in your code with less work.

%package -n python3-module-%oname
Summary: A library for property based testing for Python 3
Group: Development/Python3

%description -n python3-module-%oname
Hypothesis is an advanced testing library for Python. It lets you write tests
which are parametrized by a source of examples, and then generates simple and
comprehensible examples that make your tests fail. This lets you find more bugs
in your code with less work.

%prep
%setup
%patch1 -p1

%if_with python3
cp -a . ../python3
%endif

%if_with docs
%prepare_sphinx doc
ln -s ../objects.inv doc/en/
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%check
rm -rf tests/py3 tests/django/toystore
PYTHONPATH=%buildroot%python_sitelibdir py.test

%if_with python3
pushd ../python3
rm -rf tests/py2 tests/django/toystore
PYTHONPATH=%buildroot%python3_sitelibdir py.test3
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.18.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.18.1-alt1
- Updated to upstream version 3.18.1.

* Thu Jan 19 2017 Anton Midyukov <antohami@altlinux.org> 3.6.1-alt1
- Initial build for ALT Linux Sisyphus.
