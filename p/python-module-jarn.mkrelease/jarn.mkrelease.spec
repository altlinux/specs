%define mname jarn
%define oname %mname.mkrelease

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 3.9
Release: alt1.git20131125.1.1
Summary: Python egg releaser
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jarn.mkrelease/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Jarn/jarn.mkrelease.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-lazy
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-lazy
%endif

%py_provides %oname
Requires: python-module-%mname = %EVR

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-pytest python3-module-pytest rpm-build-python3

%description
mkrelease is a no-frills Python egg releaser. It is designed to take the
cumber out of building and distributing Python eggs.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
mkrelease is a no-frills Python egg releaser. It is designed to take the
cumber out of building and distributing Python eggs.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python

%description -n python-module-%mname
Core files of %mname.

%package -n python3-module-%oname
Summary: Python egg releaser
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-%mname = %EVR

%description -n python3-module-%oname
mkrelease is a no-frills Python egg releaser. It is designed to take the
cumber out of building and distributing Python eggs.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
mkrelease is a no-frills Python egg releaser. It is designed to take the
cumber out of building and distributing Python eggs.

This package contains tests for %oname.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3

%description -n python3-module-%mname
Core files of %mname.

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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/
%if_with python3
pushd ../python3
install -p -m644 %mname/__init__.py \
	%buildroot%python3_sitelibdir/%mname/
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
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*
%exclude %python_sitelibdir/%mname/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/%mname/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/*/test*
%exclude %python3_sitelibdir/%mname/*/*/test*
%exclude %python3_sitelibdir/%mname/__init__.*
%exclude %python3_sitelibdir/%mname/__pycache__/__init__.*

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%dir %python3_sitelibdir/%mname/__pycache__
%python3_sitelibdir/%mname/__init__.*
%python3_sitelibdir/%mname/__pycache__/__init__.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/%mname/*/test*
%python3_sitelibdir/%mname/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.9-alt1.git20131125.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.9-alt1.git20131125.1
- NMU: Use buildreq for BR.

* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9-alt1.git20131125
- Initial build for Sisyphus

