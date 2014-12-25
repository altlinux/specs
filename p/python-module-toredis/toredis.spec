%define oname toredis

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.2
Release: alt1.git20140515
Summary: Really simple async Redis client for Tornado
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/toredis/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mrjoes/toredis.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tornado python-module-hiredis
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tornado python3-module-hiredis
%endif

%py_provides %oname
%py_requires tornado hiredis

%description
This is minimalistic, but feature rich redis client for Tornado built on
top of hiredis protocol parser.

Supports all redis commands, which are auto-generated from the redis
JSON documentation file.

%package -n python3-module-%oname
Summary: Really simple async Redis client for Tornado
Group: Development/Python3
%py3_provides %oname
%py3_requires tornado hiredis

%description -n python3-module-%oname
This is minimalistic, but feature rich redis client for Tornado built on
top of hiredis protocol parser.

Supports all redis commands, which are auto-generated from the redis
JSON documentation file.

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
%doc AUTHORS *.rst examples
%doc *.json gen_commands.py
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst examples
%doc *.json gen_commands.py
%python3_sitelibdir/*
%endif

%changelog
* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20140515
- Initial build for Sisyphus

