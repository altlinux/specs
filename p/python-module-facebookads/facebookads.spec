%define oname facebookads

%def_with python3

Name: python-module-%oname
Version: 2.2.1
Release: alt1.git20141107
Summary: An SDK built to facilitate application development for Facebook Ads API
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/facebookads/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/facebook/facebook-python-ads-sdk.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-requests python-module-six
BuildPreReq: python-module-configparser python-modules-json
BuildPreReq: python-module-backports.ssl_match_hostname
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-requests python3-module-six
BuildPreReq: python3-module-configparser
BuildPreReq: python3-module-backports.ssl_match_hostname
%endif

%py_provides %oname
Requires: python-module-backports.ssl_match_hostname

%description
facebookads provides an interface between your python application and
Facebook's Ads API.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
facebookads provides an interface between your python application and
Facebook's Ads API.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: An SDK built to facilitate application development for Facebook Ads API
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-backports.ssl_match_hostname
%add_python3_req_skip __main__

%description -n python3-module-%oname
facebookads provides an interface between your python application and
Facebook's Ads API.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
facebookads provides an interface between your python application and
Facebook's Ads API.

This package contains tests for %oname.

%prep
%setup
ln -s README.md README.rst

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
%doc *.txt *.md examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.md examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%endif

%changelog
* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1.git20141107
- Version 2.2.1

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.git20141030
- Version 2.2.0

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20141025
- Version 0.2.1

* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20141023
- Initial build for Sisyphus

