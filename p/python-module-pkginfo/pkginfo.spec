%define oname pkginfo

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.2
Release: alt2.b1
Summary: Query metadatdata from sdists / bdists / installed packages
License: Python
Group: Development/Python
Url: https://pypi.python.org/pypi/pkginfo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-module-alabaster python-module-coverage python-module-docutils python-module-html5lib python-module-nose python-module-objects.inv python-module-pytest python-modules-wsgiref 
BuildRequires: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-coverage python3-module-nose python3-module-pytest
BuildPreReq: python-tools-2to3
%endif

%description
This package provides an API for querying the distutils metadata written
in the PKG-INFO file inside a source distriubtion (an sdist) or a binary
distribution (e.g., created by running bdist_egg). It can also query the
EGG-INFO directory of an installed distribution, and the *.egg-info
stored in a "development checkout" (e.g, created by running setup.py
develop).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package provides an API for querying the distutils metadata written
in the PKG-INFO file inside a source distriubtion (an sdist) or a binary
distribution (e.g., created by running bdist_egg). It can also query the
EGG-INFO directory of an installed distribution, and the *.egg-info
stored in a "development checkout" (e.g, created by running setup.py
develop).

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Query metadatdata from sdists / bdists / installed packages
Group: Development/Python3

%description -n python3-module-%oname
This package provides an API for querying the distutils metadata written
in the PKG-INFO file inside a source distriubtion (an sdist) or a binary
distribution (e.g., created by running bdist_egg). It can also query the
EGG-INFO directory of an installed distribution, and the *.egg-info
stored in a "development checkout" (e.g, created by running setup.py
develop).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package provides an API for querying the distutils metadata written
in the PKG-INFO file inside a source distriubtion (an sdist) or a binary
distribution (e.g., created by running bdist_egg). It can also query the
EGG-INFO directory of an installed distribution, and the *.egg-info
stored in a "development checkout" (e.g, created by running setup.py
develop).

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This package provides an API for querying the distutils metadata written
in the PKG-INFO file inside a source distriubtion (an sdist) or a binary
distribution (e.g., created by running bdist_egg). It can also query the
EGG-INFO directory of an installed distribution, and the *.egg-info
stored in a "development checkout" (e.g, created by running setup.py
develop).

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This package provides an API for querying the distutils metadata written
in the PKG-INFO file inside a source distriubtion (an sdist) or a binary
distribution (e.g., created by running bdist_egg). It can also query the
EGG-INFO directory of an installed distribution, and the *.egg-info
stored in a "development checkout" (e.g, created by running setup.py
develop).

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/.build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/.build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Feb 03 2016 Sergey Alembekov <rt@altlinux.ru> 1.2-alt2.b1
- cleanup buildreq

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.b1
- Initial build for Sisyphus

