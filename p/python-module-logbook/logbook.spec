%define oname logbook

%def_with python3

Name: python-module-%oname
Version: 1.1.0
Release: alt1.1
Summary: A logging replacement for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Logbook/

# https://github.com/mitsuhiko/logbook.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-Cython python-module-alabaster python-module-html5lib python-module-notebook python-module-objects.inv python-module-setuptools time
BuildRequires: python-module-mock python-module-pip
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Cython python3-module-html5lib python3-module-notebook python3-module-setuptools
BuildRequires: python3-module-mock python3-module-pip
%endif

%description
An awesome logging implementation that is fun to use.

%package -n python3-module-%oname
Summary: A logging replacement for Python
Group: Development/Python3

%description -n python3-module-%oname
An awesome logging implementation that is fun to use.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
An awesome logging implementation that is fun to use.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
An awesome logging implementation that is fun to use.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%add_optflags -fno-strict-aliasing
export USE_CYTHON=1
CFLAGS="%optflags" python scripts/travis_build.py
%python_build_debug

%if_with python3
pushd ../python3
CFLAGS="%optflags" python3 scripts/travis_build.py
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

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
py.test
%if_with python3
pushd ../python3
py.test3
popd
%endif

%files
%doc AUTHORS CHANGES *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt1
- Updated to upstream release 1.1.0.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.1-alt1.dev.git20141012.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1.dev.git20141012.1
- NMU: Use buildreq for BR.

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.dev.git20141012
- Initial build for Sisyphus

