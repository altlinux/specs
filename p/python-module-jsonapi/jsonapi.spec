%define oname jsonapi

%def_with python3

Name: python-module-%oname
Version: 0.6.5
Release: alt1.git20150211
Summary: JSON API realisation
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/jsonapi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pavlov99/jsonapi.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-django-tests python-module-mixer
BuildPreReq: python-module-django-command-extensions
BuildPreReq: python-module-django-debug-toolbar
BuildPreReq: python-module-django-nose python-module-coverage
BuildPreReq: python-module-mock ipython python-module-ipdb
BuildPreReq: python-module-django-dbbackend-sqlite3
BuildPreReq: python-modules-sqlite3
BuildPreReq: python-modules-multiprocessing
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-django-tests python3-module-mixer
BuildPreReq: python3-module-django-command-extensions
BuildPreReq: python3-module-django-debug-toolbar
BuildPreReq: python3-module-django-nose python3-module-coverage
BuildPreReq: python3-module-mock ipython3 python3-module-ipdb
BuildPreReq: python3-module-django-dbbackend-sqlite3
BuildPreReq: python3-modules-sqlite3
%endif

%py_provides %oname
%py_requires django

%description
jsonapi protocol implementation for Django.

%package -n python3-module-%oname
Summary: JSON API realisation
Group: Development/Python3
%py3_provides %oname
%py3_requires django

%description -n python3-module-%oname
jsonapi protocol implementation for Django.

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
python setup.py test
%make test
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|django-admin.py|django-admin.py3|' Makefile
%make test
popd
%endif

%files
%doc *.rst docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.5-alt1.git20150211
- Version 0.6.5

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.9-alt1.git20150114
- Initial build for Sisyphus

