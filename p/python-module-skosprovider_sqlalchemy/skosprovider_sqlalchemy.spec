%define oname skosprovider_sqlalchemy

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.4.1
Release: alt1.git20141218
Summary: A SQLAlchemy implementation of the skosprovider interface
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/skosprovider_sqlalchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/koenedaele/skosprovider_sqlalchemy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-skosprovider python-module-SQLAlchemy
BuildPreReq: python-module-nose python-module-pytest-cov
BuildPreReq: python-module-coveralls
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-skosprovider python3-module-SQLAlchemy
BuildPreReq: python3-module-nose python3-module-pytest-cov
BuildPreReq: python3-module-coveralls
%endif

%py_provides %oname
%py_requires skosprovider sqlalchemy

%description
An implementation of the skosprovider interface against SQLAlchemy.

%package -n python3-module-%oname
Summary: A SQLAlchemy implementation of the skosprovider interface
Group: Development/Python3
%py3_provides %oname
%py3_requires skosprovider sqlalchemy

%description -n python3-module-%oname
An implementation of the skosprovider interface against SQLAlchemy.

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst docs/*.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20141218
- Initial build for Sisyphus

