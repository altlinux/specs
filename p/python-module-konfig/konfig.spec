%define oname konfig

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt1.git20140428
Summary: Yet Another Config Parser
License: MPLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/konfig/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mozilla-services/konfig.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-configparser python-module-argparse
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-configparser python3-module-argparse
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
Yet another configuration object. Compatible with the updated
configparser.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Yet another configuration object. Compatible with the updated
configparser.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Yet Another Config Parser
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Yet another configuration object. Compatible with the updated
configparser.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Yet another configuration object. Compatible with the updated
configparser.

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
rm -fR build
py.test
%if_with python3
pushd ../python3
python3 setup.py test
rm -fR build
py.test-%_python3_version
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20140428
- Initial build for Sisyphus

