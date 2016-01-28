%define oname antipathy

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.81.04
Release: alt1.1
Summary: oo view of file paths and names, subclassed from bytes/str/unicode
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/antipathy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel rpm-build-python3

%description
oo view of file paths and names, subclassed from bytes/str/unicode.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
oo view of file paths and names, subclassed from bytes/str/unicode.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: oo view of file paths and names, subclassed from bytes/str/unicode
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
oo view of file paths and names, subclassed from bytes/str/unicode.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
oo view of file paths and names, subclassed from bytes/str/unicode.

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
%doc CHANGES README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test.*

%files tests
%python_sitelibdir/*/test.*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.81.04-alt1.1
- NMU: Use buildreq for BR.

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.81.04-alt1
- Version 0.81.04

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.81.03-alt1
- Initial build for Sisyphus

