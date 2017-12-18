%define oname babelfish

%def_with python3

Name: python-module-%oname
Version: 0.5.5
Release: alt3
Summary: A module to work with countries and languages
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/babelfish/

# https://github.com/Diaoul/babelfish.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
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

%if_with python3
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
%endif

%prep
%setup
%patch1 -p1

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
* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.5-alt3
- Updated to upstream release version 0.5.5.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.5-alt2.dev.git20150124.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 03 2016 Sergey Alembekov <rt@altlinux.ru> 0.5.5-alt2.dev.git20150124
- Delete unnecessary dependens

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5-alt1.dev.git20150124
- Version 0.5.5-dev

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.4-alt1.dev.git20140622
- Initial build for Sisyphus

