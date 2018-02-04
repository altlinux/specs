%define oname passlib

%def_with python3
# very slow:
%def_disable check

Name:		python-module-%oname
Version:	1.7.1
Release:	alt1.1
Summary:	Comprehensive password hashing framework supporting over 20 schemes
Group:		Development/Python
License:	BSD and Beerware and Copyright only
URL:		https://bitbucket.org/ecollins/passlib
Source0:	https://pypi.python.org/packages/source/p/%oname/%oname-%version.tar.gz

BuildArch:	noarch
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-nose
BuildRequires: python-module-sphinx-devel
BuildRequires: python-module-cloud_sptheme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-nose
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx

%description
Passlib is a password hashing library for Python 2 & 3, which provides
cross-platform implementations of over 20 password hashing algorithms,
as well as a framework for managing existing password hashes. It's
designed to be useful for a wide range of tasks, from verifying a hash
found in /etc/shadow, to providing full-strength password hashing for
multi-user application.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Comprehensive password hashing framework supporting over 20 schemes
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Passlib is a password hashing library for Python 2 & 3, which provides
cross-platform implementations of over 20 password hashing algorithms,
as well as a framework for managing existing password hashes. It's
designed to be useful for a wide range of tasks, from verifying a hash
found in /etc/shadow, to providing full-strength password hashing for
multi-user application.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Passlib is a password hashing library for Python 2 & 3, which provides
cross-platform implementations of over 20 password hashing algorithms,
as well as a framework for managing existing password hashes. It's
designed to be useful for a wide range of tasks, from verifying a hash
found in /etc/shadow, to providing full-strength password hashing for
multi-user application.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
Passlib is a password hashing library for Python 2 & 3, which provides
cross-platform implementations of over 20 password hashing algorithms,
as well as a framework for managing existing password hashes. It's
designed to be useful for a wide range of tasks, from verifying a hash
found in /etc/shadow, to providing full-strength password hashing for
multi-user application.

This package contains documentation for %oname.

%prep
%setup -n %oname-%version

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/
sed -i 's|@VERSION@|%version|' docs/conf.py

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

%if 0
export PYTHONPATH=$PWD
pushd docs
sphinx-build -b pickle -d build/doctrees . build/pickle
sphinx-build -b html -d build/doctrees . build/html
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
%doc LICENSE README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.7.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jun 01 2017 Alexey Shabalin <shaba@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7-alt1.dev0.hg20131228.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7-alt1.dev0.hg20131228.1
- NMU: Use buildreq for BR.

* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.dev0.hg20131228
- Version 1.7.dev0
- Added module for Python 3

* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 1.5.3-alt1
- Initial release for Sisyphus (based on Fedora)
