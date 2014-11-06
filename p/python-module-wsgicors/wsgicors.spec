%define oname wsgicors

%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt1.git20140821
Summary: WSGI for Cross Origin Resource Sharing (CORS)
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/wsgicors/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/may-day/wsgicors.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests pandoc
BuildPreReq: python-module-nose python-module-nose-testconfig
BuildPreReq: python-module-webob
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-nose-testconfig
BuildPreReq: python3-module-webob python-tools-2to3
%endif

%py_provides %oname

%description
This is a WSGI middleware that answers CORS preflight requests and adds
the needed header to the response. For CORS see:
http://www.w3.org/TR/cors/

%package -n python3-module-%oname
Summary: WSGI for Cross Origin Resource Sharing (CORS)
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This is a WSGI middleware that answers CORS preflight requests and adds
the needed header to the response. For CORS see:
http://www.w3.org/TR/cors/

%prep
%setup

./preprelease.sh

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
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20140821
- Initial build for Sisyphus

