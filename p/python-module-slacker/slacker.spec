%define oname slacker

%def_with python3

Name: python-module-%oname
Version: 0.6.8
Release: alt1.git20150717.1.1
Summary: Slack API client
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/slacker
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/os/slacker.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-requests python-module-mock
BuildPreReq: python-module-tox
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-requests python3-module-mock
BuildPreReq: python3-module-tox
%endif

%py_provides %oname
%py_requires requests

%description
Slacker is a full-featured Python interface for the Slack API.

%if_with python3
%package -n python3-module-%oname
Summary: Slack API client
Group: Development/Python3
%py3_provides %oname
%py3_requires requests

%description -n python3-module-%oname
Slacker is a full-featured Python interface for the Slack API.
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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.8-alt1.git20150717.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.8-alt1.git20150717.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.8-alt1.git20150717
- Initial build for Sisyphus

