%define oname ultra_rest_client

%def_with python3

Name: python-module-%oname
Version: 0.1.4
Release: alt1.git20150515.1.1
Summary: A sample Python client for communicating with the UltraDNS REST API
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/ultra_rest_client
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ultradns/python_rest_api_client.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-requests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-requests
%endif

%py_provides %oname
%py_requires requests

%description
The sample code does not attempt to implement a client for all available
UltraDNS REST API functionality. It provides access to basic
functionality. Adding additional functionality should be relatively
straightforward, and any contributions from the UltraDNS community would
be greatly appreciated. See sample.py for an example of how to use this
library in your own code.

%if_with python3
%package -n python3-module-%oname
Summary: A sample Python client for communicating with the UltraDNS REST API
Group: Development/Python3
%py3_provides %oname
%py3_requires requests

%description -n python3-module-%oname
The sample code does not attempt to implement a client for all available
UltraDNS REST API functionality. It provides access to basic
functionality. Adding additional functionality should be relatively
straightforward, and any contributions from the UltraDNS community would
be greatly appreciated. See sample.py for an example of how to use this
library in your own code.
%endif

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
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.md *.txt sample.py
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md *.txt ../python3/sample.py
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.4-alt1.git20150515.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.git20150515.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150515
- Initial build for Sisyphus

