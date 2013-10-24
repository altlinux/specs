%define oname patsy

%def_with python3

Name: python-module-%oname
Version: 0.2.1
Release: alt1

Summary: A Python package for describing statistical models and for building design matrices
License: BSD
Group: Development/Python
Url: http://patsy.readthedocs.org/en/latest/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel
BuildPreReq: libnumpy-devel python-module-matplotlib ipython
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
A Python package for describing statistical models and for building
design matrices. It is closely inspired by and compatible with the
'formula' mini-language used in R and S.

%package tests
Summary: Tests for patsy
Group: Development/Python
Requires: %name = %EVR

%description tests
A Python package for describing statistical models and for building
design matrices. It is closely inspired by and compatible with the
'formula' mini-language used in R and S.

This package contains tests for patsy.

%package pickles
Summary: Pickles for patsy
Group: Development/Python

%description pickles
A Python package for describing statistical models and for building
design matrices. It is closely inspired by and compatible with the
'formula' mini-language used in R and S.

This package contains pickles for patsy.

%package docs
Summary: Documentation for patsy
Group: Development/Documentation

%description docs
A Python package for describing statistical models and for building
design matrices. It is closely inspired by and compatible with the
'formula' mini-language used in R and S.

This package contains documentation for patsy.

%if_with python3
%package -n python3-module-%oname
Summary: A Python package for describing statistical models and for building design matrices
Group: Development/Python3

%description -n python3-module-%oname
A Python package for describing statistical models and for building
design matrices. It is closely inspired by and compatible with the
'formula' mini-language used in R and S.

%package -n python3-module-%oname-tests
Summary: Tests for patsy
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A Python package for describing statistical models and for building
design matrices. It is closely inspired by and compatible with the
'formula' mini-language used in R and S.

This package contains tests for patsy.
%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
pushd ../python3
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +
#find -type f -exec sed -i 's|%_bindir/python|%_bindir/python3|' -- '{}' +
#find -type f -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%make -C doc pickle
%make -C doc html

%install
%python_build_install

%if_with python3
pushd ../python3
%python3_build_install
popd
%endif

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc README TODO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test_*

%files tests
%python_sitelibdir/*/test_*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc README TODO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test_*
%exclude %python3_sitelibdir/*/__pycache__/test_*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test_*
%python3_sitelibdir/*/__pycache__/test_*
%endif

%changelog
* Thu Oct 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

