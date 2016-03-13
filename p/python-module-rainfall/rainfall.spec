%define oname rainfall

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.8.3
Release: alt1.git20141217.1
Summary: Micro web framework around asyncio (ex tulip)
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/rainfall/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mind1master/rainfall.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio python-module-jinja2
BuildPreReq: python-module-websockets
%endif
BuildPreReq: python-module-sphinx-devel python3-module-sphinx
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio python3-module-jinja2
BuildPreReq: python3-module-websockets
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires asyncio websockets jinja2

%description
To start off, rainfall is a micro web framework around asyncio (ex
tulip), similiar to the cyclone or tornado. Since it is asyncio based,
rainfall is fully asyncronous.

%package -n python3-module-%oname
Summary: Micro web framework around asyncio (ex tulip)
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio websockets jinja2

%description -n python3-module-%oname
To start off, rainfall is a micro web framework around asyncio (ex
tulip), similiar to the cyclone or tornado. Since it is asyncio based,
rainfall is fully asyncronous.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3/%oname/tests -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

%make -C docs html

rm -f requirements.txt

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
%doc *.txt *.md docs/_build/html
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.md docs/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.3-alt1.git20141217.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20141217
- Initial build for Sisyphus

