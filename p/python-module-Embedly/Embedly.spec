%define oname Embedly

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.5.0
Release: alt1.git20141215.1
Summary: Python Library for Embedly
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Embedly/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/embedly/embedly-python.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-httplib2 python-module-mock
#BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-httplib2 python3-module-mock
%endif

%py_provides embedly
%py_requires httplib2 json

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-httplib2 python-module-pbr python-module-pytest python-module-unittest2 python3-module-html5lib python3-module-httplib2 python3-module-pbr python3-module-pytest python3-module-unittest2 rpm-build-python3

%description
Python library for interacting with Embedly's API. To get started sign
up for a key at https://app.embed.ly/signup

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Python library for interacting with Embedly's API. To get started sign
up for a key at https://app.embed.ly/signup

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python Library for Embedly
Group: Development/Python3
%py3_provides embedly
%py3_requires httplib2

%description -n python3-module-%oname
Python library for interacting with Embedly's API. To get started sign
up for a key at https://app.embed.ly/signup

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Python library for interacting with Embedly's API. To get started sign
up for a key at https://app.embed.ly/signup

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
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.git20141215.1
- NMU: Use buildreq for BR.

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20141215
- Initial build for Sisyphus

