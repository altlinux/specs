%define oname mailinglogger

%def_without python3

Name: python-module-%oname
Version: 4.0.0
Release: alt1.dev.git20140127
Summary: Enhanced emailing handlers for the python logging package
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/mailinglogger/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Simplistix/mailinglogger.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-nose python-module-nose_fixes
BuildPreReq: python-module-testfixtures python-module-manuel-tests
BuildPreReq: python-module-nose-cov python-module-pkginfo
BuildPreReq: python-module-cov-core
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-nose_fixes
BuildPreReq: python3-module-testfixtures python3-module-manuel-tests
BuildPreReq: python3-module-nose-cov python3-module-cov-core
%endif

%py_provides %oname

%description
This package contains two handlers for the python logging framework that
enable important log entries to be sent by email.

This can either be as the entries are logged or as a summary at the end
of the running process.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires manuel.testing

%description tests
This package contains two handlers for the python logging framework that
enable important log entries to be sent by email.

This can either be as the entries are logged or as a summary at the end
of the running process.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Enhanced emailing handlers for the python logging package
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This package contains two handlers for the python logging framework that
enable important log entries to be sent by email.

This can either be as the entries are logged or as a summary at the end
of the running process.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires manuel.testing

%description -n python3-module-%oname-tests
This package contains two handlers for the python logging framework that
enable important log entries to be sent by email.

This can either be as the entries are logged or as a summary at the end
of the running process.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This package contains two handlers for the python logging framework that
enable important log entries to be sent by email.

This can either be as the entries are logged or as a summary at the end
of the running process.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This package contains two handlers for the python logging framework that
enable important log entries to be sent by email.

This can either be as the entries are logged or as a summary at the end
of the running process.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.dev.git20140127
- Initial build for Sisyphus

