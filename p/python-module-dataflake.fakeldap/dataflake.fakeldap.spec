%define oname dataflake.fakeldap

%def_with python3

Name: python-module-%oname
Version: 2.1
Release: alt2
Summary: LDAP connection library
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/dataflake.fakeldap/

# https://github.com/dataflake/dataflake.fakeldap.git
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires: python-devel python-module-ldap
BuildRequires: python-module-setuptools python-module-dataflake
BuildRequires: python-module-nose python-module-coverage
BuildRequires: python-module-sphinx-devel python-module-pkginfo
BuildRequires: python-module-six python-module-pyldap
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-ldap
BuildRequires: python3-module-setuptools python3-module-dataflake
BuildRequires: python3-module-nose python3-module-coverage
BuildRequires: python3-module-six python3-module-pyldap
%endif

%py_provides %oname
%py_requires dataflake

%description
This package offers a mock python-ldap library that can be used for
testing code relying on python-ldap without having to configure and
populate a real directory server.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package offers a mock python-ldap library that can be used for
testing code relying on python-ldap without having to configure and
populate a real directory server.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This package offers a mock python-ldap library that can be used for
testing code relying on python-ldap without having to configure and
populate a real directory server.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This package offers a mock python-ldap library that can be used for
testing code relying on python-ldap without having to configure and
populate a real directory server.

This package contains documentation for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: LDAP connection library
Group: Development/Python3
%py3_provides %oname
%py3_requires dataflake

%description -n python3-module-%oname
This package offers a mock python-ldap library that can be used for
testing code relying on python-ldap without having to configure and
populate a real directory server.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package offers a mock python-ldap library that can be used for
testing code relying on python-ldap without having to configure and
populate a real directory server.

This package contains tests for %oname.
%endif

%prep
%setup
%patch1 -p1

sed -i 's:../bin/sphinx-build:sphinx-build:g' \
	docs/Makefile

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

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
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
export PYTHONPATH=$PWD
python3 setup.py test
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Tue Jan 29 2019 Ivan A. Melnikov <iv@altlinux.org> 2.1-alt2
- Enable python3.

* Mon Mar 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1-alt1
- Updated to upstream version 2.1.

* Fri Aug 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0-alt1
- Updated to upstream version 2.0

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2-alt2.dev.git20121018.1
- (AUTO) subst_x86_64.

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.dev.git20121018
- Fixed build

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.dev.git20121018
- Initial build for Sisyphus

