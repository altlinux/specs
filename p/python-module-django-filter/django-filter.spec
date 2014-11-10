%define oname django-filter

%def_with python3

Name: python-module-%oname
Version: 0.7
Release: alt1.git20140929
Summary: A generic system for filtering Django QuerySets based on user selections
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-filter/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/alex/django-filter.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-django python-module-django-discover-runner
BuildPreReq: python-module-mock python-module-coverage
BuildPreReq: python-module-django-dbbackend-sqlite3
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-django python3-module-django-discover-runner
BuildPreReq: python3-module-mock python3-module-coverage
BuildPreReq: python3-module-django-dbbackend-sqlite3
%endif

%py_provides django_filters

%description
Django-filter is a reusable Django application for allowing users to
filter querysets dynamically.

%package -n python3-module-%oname
Summary: A generic system for filtering Django QuerySets based on user selections
Group: Development/Python3
%py3_provides django_filters

%description -n python3-module-%oname
Django-filter is a reusable Django application for allowing users to
filter querysets dynamically.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Django-filter is a reusable Django application for allowing users to
filter querysets dynamically.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Django-filter is a reusable Django application for allowing users to
filter querysets dynamically.

This package contains documentation for %oname.

%prep
%setup

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

%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
python runtests.py
%if_with python3
pushd ../python3
python3 setup.py test
python3 runtests.py
popd
%endif

%files
%doc AUTHORS *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20140929
- Initial build for Sisyphus

