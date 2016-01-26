%define oname rainbow_logging_handler

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.2.2
Release: alt2.git20140807
Summary: Ultimate Python colorized logger
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/rainbow_logging_handler/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/laysakura/rainbow_logging_handler.git
Source: %name-%version.tar
BuildArch: noarch
BuildRequires: python-module-coverage python-module-logutils python-module-nose-cov python-module-pytest
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-logutils python-module-colorama
#BuildPreReq: python-module-nose python-module-coverage
#BuildPreReq: python-module-nose-cov python-module-cov-core
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-logutils python3-module-colorama
#BuildPreReq: python3-module-nose python3-module-coverage
#BuildPreReq: python3-module-nose-cov python3-module-cov-core
BuildRequires: python3-module-coverage python3-module-logutils python3-module-nose-cov python3-module-pytest
%endif

%py_provides %oname
#%py_requires logutils colorama

%description
Ultimate Python colorized logger with user-custom color.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Ultimate Python colorized logger with user-custom color.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Ultimate Python colorized logger
Group: Development/Python3
%py3_provides %oname
#%py3_requires logutils colorama

%description -n python3-module-%oname
Ultimate Python colorized logger with user-custom color.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Ultimate Python colorized logger with user-custom color.

This package contains tests for %oname.

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
python setup.py test
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -v
popd
%endif

%files
%doc *.rst *.txt doc/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%if_with python3
%files -n python3-module-%oname
%doc *.rst *.txt doc/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%endif

%changelog
* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 2.2.2-alt2.git20140807
- Rebuild with "def_disable check"
- Cleanup buildreq

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt1.git20140807
- Initial build for Sisyphus

