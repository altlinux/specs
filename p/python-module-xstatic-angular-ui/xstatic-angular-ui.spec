%define mname xstatic
%define oname %mname-angular-ui

%def_with python3

Name: python-module-%oname
Version: 0.4.0.1
Release: alt1.1
Summary: angular-ui 0.4.0 (XStatic packaging standard)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/XStatic-angular-ui/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-%mname
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-%mname
%endif

%py_provides %mname.pkg.angular_ui
%py_requires %mname.pkg

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools-tests python-module-xstatic python3-module-setuptools-tests python3-module-xstatic rpm-build-python3

%description
angular-ui javascript library packaged for setuptools (easy_install) /
pip.

This package is intended to be used by any project that needs these
files.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
angular-ui javascript library packaged for setuptools (easy_install) /
pip.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: angular-ui 0.4.0 (XStatic packaging standard)
Group: Development/Python3
%py3_provides %mname.pkg.angular_ui
%py3_requires %mname.pkg

%description -n python3-module-%oname
angular-ui javascript library packaged for setuptools (easy_install) /
pip.

This package is intended to be used by any project that needs these
files.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
angular-ui javascript library packaged for setuptools (easy_install) /
pip.

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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt
%python_sitelibdir/%mname/pkg/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/pkg/*/*/test
%exclude %python_sitelibdir/%mname/pkg/*/*/*/test
%exclude %python_sitelibdir/%mname/pkg/*/*/*/*/*/test

%files tests
%python_sitelibdir/%mname/pkg/*/*/test
%python_sitelibdir/%mname/pkg/*/*/*/test
%python_sitelibdir/%mname/pkg/*/*/*/*/*/test

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/%mname/pkg/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/pkg/*/*/test
%exclude %python3_sitelibdir/%mname/pkg/*/*/*/test
%exclude %python3_sitelibdir/%mname/pkg/*/*/*/*/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/%mname/pkg/*/*/test
%python3_sitelibdir/%mname/pkg/*/*/*/test
%python3_sitelibdir/%mname/pkg/*/*/*/*/*/test
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.0.1-alt1.1
- NMU: Use buildreq for BR.

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0.1-alt1
- Initial build for Sisyphus

