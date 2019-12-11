%define modname dateparser

%def_enable python2
%def_disable check

Name: python-module-%modname
Version: 0.7.2
Release: alt1

Summary: Python parser for human readable dates 
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/dateparser

#VCS: https://github.com/scrapinghub/dateparser.git
Source: https://github.com/scrapinghub/dateparser/archive/v%version/%modname-%version.tar.gz
BuildArch: noarch

# https://pypi.org/project/umalqurra/
%filter_from_requires /umalqurra/d

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-nose python3-module-mock
BuildRequires: python3-module-nose-parameterized python3-module-wheel
BuildRequires: python3-module-dateutil python3-module-tzlocal python3-module-regex
BuildRequires: python3-module-sphinx-devel

%if_enabled python2
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-nose python-module-mock
BuildRequires: python-module-nose-parameterized python-module-wheel
BuildRequires: python-module-dateutil python-module-tzlocal python-module-regex
%py_provides %modname
%endif

%description
Date parsing library designed to parse dates from HTML pages.

%package -n python3-module-%modname
Summary: Python parser for human readable dates
Group: Development/Python3
%py3_provides %modname

%description -n python3-module-%modname
Date parsing library designed to parse dates from HTML pages.

%package -n python3-module-%modname-pickles
Summary: Pickles for %modname
Group: Development/Python3

%description -n python3-module-%modname-pickles
Date parsing library designed to parse dates from HTML pages.

This package contains pickles for %modname.

%package -n python3-module-%modname-docs
Summary: Documentation for %modname
Group: Development/Documentation
BuildArch: noarch

%description -n python3-module-%modname-docs
Date parsing library designed to parse dates from HTML pages.

This package contains documentation for %modname.

%prep
%setup -n %modname-%version %{?_enable_python2:-a0
mv %modname-%version python2}

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%python3_build_debug

%if_enabled python2
pushd python2
%python_build_debug
popd
%endif

%install
%python3_install

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%modname/

%if_enabled python2
pushd python2
%python_install
popd
%endif

%check
python3 setup.py test
%if_enabled python2
pushd python2
python setup.py test
popd
%endif

%if_enabled python2
%files
%doc *.rst
%python_sitelibdir/*
%endif

%files -n python3-module-%modname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files -n python3-module-%modname-pickles
%python3_sitelibdir/*/pickle

%files -n python3-module-%modname-docs
%doc docs/_build/html/*


%changelog
* Wed Dec 11 2019 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- 0.7.2
- made python2 build optional

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.0-alt1.git20141125.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20141125.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20141125
- Initial build for Sisyphus

