%define oname pyramid-tm

%def_with python3

Name:           python-module-%oname
Version:        2.2
Release:        alt1
Summary:        A package which allows Pyramid requests to join the active transaction
Group:          Development/Python
License:        BSD
URL:            https://pypi.python.org/pypi/pyramid_tm
BuildArch:      noarch

# https://github.com/Pylons/pyramid_tm.git
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools python2.7(pyramid) python2.7(transaction)
BuildRequires: python2.7(nose) python2.7(coverage) python2.7(webtest)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools python3(pyramid) python3(transaction)
BuildRequires: python3(nose) python3(coverage) python3(webtest)
%endif

%description
pyramid_tm is a package which allows Pyramid requests to join the
active transaction as provided by the transaction
http://pypi.python.org/pypi/transaction

See http://docs.pylonsproject.org/projects/pyramid_tm/dev/
or docs/index.rst in this distribution for detailed documentation.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
pyramid_tm is a package which allows Pyramid requests to join the
active transaction as provided by the transaction
http://pypi.python.org/pypi/transaction

See http://docs.pylonsproject.org/projects/pyramid_tm/dev/
or docs/index.rst in this distribution for detailed documentation.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Group:          Development/Python3
Summary:        A package which allows Pyramid requests to join the active transaction

%description -n python3-module-%oname
pyramid_tm is a package which allows Pyramid requests to join the
active transaction as provided by the transaction
http://pypi.python.org/pypi/transaction

See http://docs.pylonsproject.org/projects/pyramid_tm/dev/
or docs/index.rst in this distribution for detailed documentation.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
pyramid_tm is a package which allows Pyramid requests to join the
active transaction as provided by the transaction
http://pypi.python.org/pypi/transaction

See http://docs.pylonsproject.org/projects/pyramid_tm/dev/
or docs/index.rst in this distribution for detailed documentation.

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -a . ../python3
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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

python setup.py test

%files
%doc README.rst LICENSE.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.py*

%files tests
%python_sitelibdir/*/tests.py*

%if_with python3
%files -n python3-module-%oname
%doc README.rst LICENSE.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.py*
%exclude %python3_sitelibdir/*/*/tests*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.py*
%python3_sitelibdir/*/*/tests*
%endif

%changelog
* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2-alt1
- Initial build for ALT.
