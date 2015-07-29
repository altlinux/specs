%define oname Paginator

%def_with python3

Name: python-module-%oname
Version: 0.2.2
Release: alt1.git20150713
Summary: Paginator for SQLAlchemy query object, list or iterable
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Paginator/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mardix/Paginator.py.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six
%endif

%py_provides paginator
%py_requires six

%description
Paginator for SQLAlchemy query object, list or iterable.

%if_with python3
%package -n python3-module-%oname
Summary: Paginator for SQLAlchemy query object, list or iterable
Group: Development/Python3
%py3_provides paginator
%py3_requires six

%description -n python3-module-%oname
Paginator for SQLAlchemy query object, list or iterable.
%endif

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

%check
python setup.py test -v
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test -v
py.test-%_python3_version -vv
popd
%endif

%files
%doc CHANGELOG *.html *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.html *.md
%python3_sitelibdir/*
%endif

%changelog
* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20150713
- Initial build for Sisyphus

