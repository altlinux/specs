%define _unpackaged_files_terminate_build 1
%define oname moneyed

%def_with python3

Name: python-module-%oname
Version: 0.7
Release: alt1
Summary: Provides Currency and Money classes for use in your Python code
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/py-moneyed/

# https://github.com/limist/py-moneyed.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-tox
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-tox
%endif

%py_provides %oname

%description
The need to represent instances of money frequently arises in software
development, particularly any financial/economics software. To address
that need, the py-moneyed package provides the classes of Money and
Currency, at a level more useful than just using Python's Decimal class,
or ($DEITY forbid) the float primitive. The package is meant to be
stand-alone and easy to either use directly, or subclass further.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The need to represent instances of money frequently arises in software
development, particularly any financial/economics software. To address
that need, the py-moneyed package provides the classes of Money and
Currency, at a level more useful than just using Python's Decimal class,
or ($DEITY forbid) the float primitive. The package is meant to be
stand-alone and easy to either use directly, or subclass further.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Provides Currency and Money classes for use in your Python code
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The need to represent instances of money frequently arises in software
development, particularly any financial/economics software. To address
that need, the py-moneyed package provides the classes of Money and
Currency, at a level more useful than just using Python's Decimal class,
or ($DEITY forbid) the float primitive. The package is meant to be
stand-alone and easy to either use directly, or subclass further.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The need to represent instances of money frequently arises in software
development, particularly any financial/economics software. To address
that need, the py-moneyed package provides the classes of Money and
Currency, at a level more useful than just using Python's Decimal class,
or ($DEITY forbid) the float primitive. The package is meant to be
stand-alone and easy to either use directly, or subclass further.

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
rm -fR build
py.test -vv
%if_with python3
pushd ../python3
rm -fR build
py.test3 -vv
popd
%endif

%files
%doc CONTRIBUTORS *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc CONTRIBUTORS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Wed Dec 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7-alt1
- Updated to upstream version 0.7.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.git20150212.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20150212
- Initial build for Sisyphus

