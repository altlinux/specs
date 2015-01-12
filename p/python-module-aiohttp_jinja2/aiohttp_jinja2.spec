%define oname aiohttp_jinja2

%def_without python2
%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 0.0.1
Release: alt1.git20150108
Summary: jinja2 template renderer for aiohttp.web
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/aiohttp_jinja2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aio-libs/aiohttp_jinja2.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio python-module-aiohttp
BuildPreReq: python-module-jinja2 python-module-nose
BuildPreReq: python-module-ipdb python-module-coverage
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio python3-module-aiohttp
BuildPreReq: python3-module-jinja2 python3-module-nose
BuildPreReq: python3-module-ipdb python3-module-coverage
%endif

%py_provides %oname
%py_requires asyncio aiohttp jinja2

%description
jinja2 template renderer for aiohttp.web.

%package -n python3-module-%oname
Summary: jinja2 template renderer for aiohttp.web
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio aiohttp jinja2

%description -n python3-module-%oname
jinja2 template renderer for aiohttp.web.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

rm -f requirements-dev.txt

%check
%if_with python2
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc *.txt *.rst
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.0.1-alt1.git20150108
- Version 0.0.1

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.a.git20141227
- Initial build for Sisyphus

