%define oname filedepot

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.5.0
Release: alt1.1
Summary: Toolkit for storing files and attachments in web applications
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/filedepot/

# https://github.com/amol-/depot.git
Source: %name-%version.tar
Patch1: %oname-%version-alt.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-pytest python-module-unittest2
BuildRequires: python-module-Pillow
BuildRequires: python-module-TurboGears2
BuildRequires: python-module-webtest
BuildRequires: python-module-boto python-module-repoze.lru
BuildRequires: python-module-alabaster
BuildRequires: python-module-docutils python-module-objects.inv python-module-pbr
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest python3-module-unittest2
BuildRequires: python3-module-TurboGears2
BuildRequires: python3-module-webtest
BuildRequires: python3-module-repoze.lru python3-module-yaml python3(requests)
BuildRequires: python3-module-ecdsa python3-module-pbr
%endif

%py_provides %oname depot
%py_requires pymongo sqlalchemy PIL ming boto

%description
DEPOT is a framework for easily storing and serving files in web
applications on Python2.6+ and Python3.2+.

%if_with python3
%package -n python3-module-%oname
Summary: Toolkit for storing files and attachments in web applications
Group: Development/Python3
%py3_provides %oname depot
%py3_requires pymongo sqlalchemy PIL ming boto

%description -n python3-module-%oname
DEPOT is a framework for easily storing and serving files in web
applications on Python2.6+ and Python3.2+.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
DEPOT is a framework for easily storing and serving files in web
applications on Python2.6+ and Python3.2+.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
DEPOT is a framework for easily storing and serving files in web
applications on Python2.6+ and Python3.2+.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif
exit 1

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html examples

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.0-alt1
- Updated to upstream version 0.5.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.3-alt1.git20150209.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.3-alt1.git20150209.1
- NMU: Use buildreq for BR.

* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20150209
- Initial build for Sisyphus

