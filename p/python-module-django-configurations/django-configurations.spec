%define oname django-configurations

%def_with python3

Name: python-module-%oname
Version: 0.8
Release: alt1.git20140812
Summary: A helper for organizing Django settings
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-configurations/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jezdez/django-configurations.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-django-tests python-module-mock
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-django-tests python3-module-mock
%endif

%description
django-configurations eases Django project configuration by relying on
the composability of Python classes. It extends the notion of Django's
module based settings loading with well established object oriented
programming patterns.

%package -n python3-module-%oname
Summary: A helper for organizing Django settings
Group: Development/Python3

%description -n python3-module-%oname
django-configurations eases Django project configuration by relying on
the composability of Python classes. It extends the notion of Django's
module based settings loading with well established object oriented
programming patterns.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
django-configurations eases Django project configuration by relying on
the composability of Python classes. It extends the notion of Django's
module based settings loading with well established object oriented
programming patterns.

This package contains tests for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
django-configurations eases Django project configuration by relying on
the composability of Python classes. It extends the notion of Django's
module based settings loading with well established object oriented
programming patterns.

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
%if_with python3
pushd ../python3
python3 setup.py test
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
* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.git20140812
- Initial build for Sisyphus

