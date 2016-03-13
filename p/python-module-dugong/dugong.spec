%define oname dugong

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 3.4
Release: alt1.1
Summary: Provides an API for communicating with HTTP 1.1 servers
License: PSFLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/dugong/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-docutils python-module-asyncio
%endif
BuildPreReq: python-module-sphinx-devel python3-module-sphinx
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-docutils python3-module-asyncio
%endif

%py_provides %oname
%py_requires asyncio

%description
The Python Dugong module provides an API for communicating with HTTP 1.1
servers. It is an alternative to the standard library's http.client
(formerly httplib) module.

%package -n python3-module-%oname
Summary: Provides an API for communicating with HTTP 1.1 servers
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
The Python Dugong module provides an API for communicating with HTTP 1.1
servers. It is an alternative to the standard library's http.client
(formerly httplib) module.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv rst/

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
mv doc/html docs
%endif

%if_with python3
pushd ../python3
%python3_install
mv doc/html docs
popd
%endif

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
%doc *.rst examples docs
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples ../python3/docs
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt1
- Initial build for Sisyphus

