%define oname psycopg2cffi

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.6.1
Release: alt1.git20150208
Summary: An implementation of the psycopg2 module using cffi
License: LGPLv3+
Group: Development/Python
Url: https://pypi.python.org/pypi/psycopg2cffi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/chtd/psycopg2cffi.git
Source: %name-%version.tar

BuildPreReq: postgresql-devel libpq-devel
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six python-module-cffi
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six python3-module-cffi
%endif

%py_provides %oname
%py_requires six cffi json

%description
An implementation of the psycopg2 module using cffi. The module is
currently compatible with Psycopg 2.5.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
An implementation of the psycopg2 module using cffi. The module is
currently compatible with Psycopg 2.5.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: An implementation of the psycopg2 module using cffi
Group: Development/Python3
%py3_provides %oname
%py3_requires six cffi

%description -n python3-module-%oname
An implementation of the psycopg2 module using cffi. The module is
currently compatible with Psycopg 2.5.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
An implementation of the psycopg2 module using cffi. The module is
currently compatible with Psycopg 2.5.

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

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

python setup.py test ||:
install -d %buildroot%python_sitelibdir/%oname/_impl/__pycache__
install -m644 %oname/_impl/__pycache__/*.so \
	%buildroot%python_sitelibdir/%oname/_impl/__pycache__/
%if_with python3
pushd ../python3
python3 setup.py test ||:
install -d %buildroot%python3_sitelibdir/%oname/_impl/__pycache__
install -m644 %oname/_impl/__pycache__/*.so \
	%buildroot%python3_sitelibdir/%oname/_impl/__pycache__/
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
%doc AUTHORS *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.1-alt1.git20150208
- Initial build for Sisyphus

