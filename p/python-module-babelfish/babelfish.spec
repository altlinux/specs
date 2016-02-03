%define oname babelfish

%def_with python3

Name: python-module-%oname
Version: 0.5.5
Release: alt2.dev.git20150124
Summary: A module to work with countries and languages
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/babelfish/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Diaoul/babelfish.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
BabelFish is a Python library to work with countries and languages.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
BabelFish is a Python library to work with countries and languages.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A module to work with countries and languages
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
BabelFish is a Python library to work with countries and languages.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
BabelFish is a Python library to work with countries and languages.

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*


%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Wed Feb 03 2016 Sergey Alembekov <rt@altlinux.ru> 0.5.5-alt2.dev.git20150124
- Delete unnecessary dependens

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5-alt1.dev.git20150124
- Version 0.5.5-dev

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.4-alt1.dev.git20140622
- Initial build for Sisyphus

