%define oname django-photologue

%def_with python3

Name: python-module-%oname
Version: 3.1
Release: alt1.dev0.git20140928
Summary: Powerful image management for the Django web framework
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-photologue/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jdriscoll/django-photologue.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel python-module-django-tests
BuildPreReq: python-module-Pillow python-module-django-sortedm2m
BuildPreReq: python-module-dj-queryset-manager python-module-south
BuildPreReq: python-module-django-model-utils
BuildPreReq: python-module-django-dbbackend-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
A powerful image management and gallery application for the Django web
framework. Upload photos, group them into galleries, apply effects such
as watermarks.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A powerful image management and gallery application for the Django web
framework. Upload photos, group them into galleries, apply effects such
as watermarks.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Powerful image management for the Django web framework
Group: Development/Python3

%description -n python3-module-%oname
A powerful image management and gallery application for the Django web
framework. Upload photos, group them into galleries, apply effects such
as watermarks.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A powerful image management and gallery application for the Django web
framework. Upload photos, group them into galleries, apply effects such
as watermarks.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A powerful image management and gallery application for the Django web
framework. Upload photos, group them into galleries, apply effects such
as watermarks.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A powerful image management and gallery application for the Django web
framework. Upload photos, group them into galleries, apply effects such
as watermarks.

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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt1.dev0.git20140928
- Initial build for Sisyphus

