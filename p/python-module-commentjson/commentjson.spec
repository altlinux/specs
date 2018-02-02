%define oname commentjson

%def_with python3

Name: python-module-%oname
Version: 0.4
Release: alt1.git20150110.1.1.1
Summary: Add Python and JavaScript style comments in your JSON files
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/commentjson/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/vaidik/commentjson.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires json

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-setuptools
BuildRequires: python-module-setuptools python-modules-json python3-module-pytest rpm-build-python3 time

%description
commentjson (Comment JSON) is a Python package that helps you create
JSON files with Python and JavaScript style inline comments. Its API is
very similar to the Python standard library's json module.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
commentjson (Comment JSON) is a Python package that helps you create
JSON files with Python and JavaScript style inline comments. Its API is
very similar to the Python standard library's json module.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Add Python and JavaScript style comments in your JSON files
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
commentjson (Comment JSON) is a Python package that helps you create
JSON files with Python and JavaScript style inline comments. Its API is
very similar to the Python standard library's json module.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
commentjson (Comment JSON) is a Python package that helps you create
JSON files with Python and JavaScript style inline comments. Its API is
very similar to the Python standard library's json module.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst docs/source/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/source/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4-alt1.git20150110.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.git20150110.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20150110.1
- NMU: Use buildreq for BR.

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20150110
- Initial build for Sisyphus

