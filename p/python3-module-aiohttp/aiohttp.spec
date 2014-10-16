%define oname aiohttp
Name: python3-module-%oname
Version: 0.9.2
Release: alt1.dev.git20141015
Summary: http client/server for asyncio
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/aiohttp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/KeepSafe/aiohttp.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools-tests python3-module-nose
BuildPreReq: python3-module-asyncio python3-module-gunicorn
BuildPreReq: python3-module-chardet
BuildPreReq: python-module-sphinx-devel

%py3_provides %oname

%description
http client/server for asyncio.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
http client/server for asyncio.

This package contains tests for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
http client/server for asyncio.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python3_build_debug

%install
%python3_install

%make -C docs html

%check
python3 setup.py test
nosetests3

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*

%files docs
%doc examples docs/_build/html

%changelog
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.dev.git20141015
- Initial build for Sisyphus

