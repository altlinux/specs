%define oname linkedin

%def_with python3

Name: python-module-%oname
Version: 4.2
Release: alt1.git20150625
Summary: Python Interface to the LinkedIn API
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/python-linkedin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ozgur/python-linkedin.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-requests python-module-requests-oauthlib
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-requests python3-module-requests-oauthlib
%endif

%py_provides %oname
%py_requires requests requests_oauthlib json

%description
This library provides a pure Python interface to the LinkedIn Profile,
Group, Company, Jobs, Search, Share, Network and Invitation REST APIs.

%if_with python3
%package -n python3-module-%oname
Summary: Python Interface to the LinkedIn API
Group: Development/Python3
%py3_provides %oname
%py3_requires requests requests_oauthlib json

%description -n python3-module-%oname
This library provides a pure Python interface to the LinkedIn Profile,
Group, Company, Jobs, Search, Share, Network and Invitation REST APIs.
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
%doc *.md *.rst examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md *.rst ../python3/examples
%python3_sitelibdir/*
%endif

%changelog
* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt1.git20150625
- New snapshot

* Thu Apr 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt1.git20150214
- Initial build for Sisyphus

