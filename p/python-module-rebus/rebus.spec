%define oname rebus

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt1.git20140314.1.1
Summary: Generate base64-encoded strings consisting of alphanumeric symbols only
License: GPLv2.0/LGPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/rebus/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/barseghyanartur/rebus.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-six
%endif

%py_provides %oname
%py_requires six

%description
Generate base64-encoded strings consisting of alphanumeric symbols only.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Generate base64-encoded strings consisting of alphanumeric symbols only.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Generate base64-encoded strings consisting of alphanumeric symbols only
Group: Development/Python3
%py3_provides %oname
%py3_requires six

%description -n python3-module-%oname
Generate base64-encoded strings consisting of alphanumeric symbols only.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Generate base64-encoded strings consisting of alphanumeric symbols only.

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
export PYTHONPATH=$PWD/src
python setup.py test
python src/rebus/tests.py -v
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD/src
python3 setup.py test
python3 src/rebus/tests.py -v
popd
%endif

%files
%doc *.rst docs/*.rst*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2-alt1.git20140314.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1.git20140314.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20140314
- Initial build for Sisyphus

