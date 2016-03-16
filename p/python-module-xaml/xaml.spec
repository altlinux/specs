%define oname xaml

%def_with python3

Name: python-module-%oname
Version: 0.3.05
Release: alt1.1.1
Summary: XML Abstract Markup Language
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/xaml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-antipathy python-module-scription
#BuildPreReq: python-module-enum34
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-antipathy python3-module-scription
#BuildPreReq: python3-module-enum34
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
Requires: python-module-enum34
%py_requires antipathy scription

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python3 python3-base
BuildRequires: python-devel python-module-enum34 python-modules-unittest python-tools-2to3 python3-module-enum34 rpm-build-python3 time

%description
An easier way for humans to write xml.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
An easier way for humans to write xml.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: XML Abstract Markup Language
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-enum34
%py3_requires antipathy scription

%description -n python3-module-%oname
An easier way for humans to write xml.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
An easier way for humans to write xml.

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
export PYTHONPATH=$PWD
python %oname/test.py -v
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
python3 %oname/test.py -v
popd
%endif

%files
%doc README CHANGES
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test.*

%files tests
%python_sitelibdir/*/test.*

%if_with python3
%files -n python3-module-%oname
%doc README CHANGES
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.05-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.05-alt1.1
- NMU: Use buildreq for BR.

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.05-alt1
- Version 0.3.05

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.08-alt1
- Initial build for Sisyphus

