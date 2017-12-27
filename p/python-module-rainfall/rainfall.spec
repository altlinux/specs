%define oname rainfall

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.8.3
Release: alt2.git20141217
Summary: Micro web framework around asyncio (ex tulip)
License: ASLv2.0
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/rainfall/

# https://github.com/mind1master/rainfall.git
Source: %name-%version.tar

%if_with python2
BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python2.7(asyncio) python-module-jinja2
BuildRequires: python-module-websockets
%endif
BuildRequires: python-module-sphinx-devel python3-module-sphinx
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3(asyncio) python3-module-jinja2
BuildRequires: python3-module-websockets
BuildRequires: python-tools-2to3
%endif

%py_provides %oname
%py_requires asyncio websockets jinja2

%description
To start off, rainfall is a micro web framework around asyncio (ex
tulip), similiar to the cyclone or tornado. Since it is asyncio based,
rainfall is fully asyncronous.

%if_with python3
%package -n python3-module-%oname
Summary: Micro web framework around asyncio (ex tulip)
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio websockets jinja2

%description -n python3-module-%oname
To start off, rainfall is a micro web framework around asyncio (ex
tulip), similiar to the cyclone or tornado. Since it is asyncio based,
rainfall is fully asyncronous.
%endif

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
* Wed Dec 27 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.3-alt2.git20141217
- Updated build dependencies.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.3-alt1.git20141217.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20141217
- Initial build for Sisyphus

