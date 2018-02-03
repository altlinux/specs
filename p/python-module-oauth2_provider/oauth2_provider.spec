%define oname oauth2_provider

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.0
Release: alt1.git20120909.1.1.1
Summary: Python implementation of the server side of OAUTH2 spec
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/oauth2_provider/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eventray/oauth2_provider.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-mock python-module-webtest
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-mock python3-module-webtest
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cssselect python-module-genshi python-module-html5lib python-module-pytest python-module-setuptools python-module-waitress python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python-modules-wsgiref python-tools-2to3 python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-html5lib python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-waitress
BuildRequires: python-module-pbr python-module-setuptools python-module-unittest2 python-module-webtest python3-module-pbr python3-module-setuptools python3-module-unittest2 python3-module-webtest rpm-build-python3 time

%description
Python implementation of the server side of OAUTH2 spec.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Python implementation of the server side of OAUTH2 spec.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Python implementation of the server side of OAUTH2 spec
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Python implementation of the server side of OAUTH2 spec.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Python implementation of the server side of OAUTH2 spec.

This package contains tests for %oname.
%endif

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0-alt1.git20120909.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0-alt1.git20120909.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0-alt1.git20120909.1
- NMU: Use buildreq for BR.

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0-alt1.git20120909
- Initial build for Sisyphus

