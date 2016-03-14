%define oname importmagic

%def_with python3

Name: python-module-%oname
Version: 0.1.2
Release: alt1.git20150126.1.1
Summary: Python Import Magic - automagically add, remove and manage imports
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/importmagic/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/alecthomas/importmagic.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname
%py_requires json

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-pytest python-modules-json python3-module-pytest rpm-build-python3

%description
The goal of this package is to be able to automatically manage imports
in Python. To that end it can:

* Build an index of all known symbols in all packages.
* Find unresolved references in source, and resolve them against the
  index, effectively automating imports.
* Automatically arrange imports according to PEP8.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The goal of this package is to be able to automatically manage imports
in Python. To that end it can:

* Build an index of all known symbols in all packages.
* Find unresolved references in source, and resolve them against the
  index, effectively automating imports.
* Automatically arrange imports according to PEP8.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python Import Magic - automagically add, remove and manage imports
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The goal of this package is to be able to automatically manage imports
in Python. To that end it can:

* Build an index of all known symbols in all packages.
* Find unresolved references in source, and resolve them against the
  index, effectively automating imports.
* Automatically arrange imports according to PEP8.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The goal of this package is to be able to automatically manage imports
in Python. To that end it can:

* Build an index of all known symbols in all packages.
* Find unresolved references in source, and resolve them against the
  index, effectively automating imports.
* Automatically arrange imports according to PEP8.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install
install -p -m644 %oname/*.json %buildroot%python_sitelibdir/%oname/

%if_with python3
pushd ../python3
%python3_install
install -p -m644 %oname/*.json %buildroot%python3_sitelibdir/%oname/
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
%doc CHANGES *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*test*

%files tests
%python_sitelibdir/*/*test*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*test*
%exclude %python3_sitelibdir/*/*/*test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*test*
%python3_sitelibdir/*/*/*test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.git20150126.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1.git20150126.1
- NMU: Use buildreq for BR.

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150126
- Initial build for Sisyphus

