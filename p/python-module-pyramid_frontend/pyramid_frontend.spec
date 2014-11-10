%define oname pyramid_frontend

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.4
Release: alt1.git20141108
Summary: Theme handling, image filtering, and asset optimization for Pyramid
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_frontend/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/cartlogic/pyramid_frontend.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: pngcrush optipng jpegoptim ImageMagick-tools
BuildPreReq: lessjs python-module-webtest
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-Pillow
BuildPreReq: python-module-mako python-module-WebHelpers2
BuildPreReq: python-module-six python-module-lockfile
BuildPreReq: python-module-nose python-module-nose-cover3
BuildPreReq: python-module-sphinx-devel python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-Pillow
BuildPreReq: python3-module-mako python3-module-WebHelpers2
BuildPreReq: python3-module-six python3-module-lockfile
BuildPreReq: python3-module-nose python3-module-nose-cover3
BuildPreReq: python3-module-mock python-module-webtest
%endif

%py_provides %oname
Requires: %_bindir/convert pngcrush optipng jpegoptim lessjs

%description
Provides:

* Theme / template handling.
* Theme configuration.
* Theme stacking (one theme can inherit from another).
* Image filtering / serving.
* Asset handling and compilation.
* Uses Mako, PIL, require.js, and LESS.

Command line tools:

* Compile assets (in addition to a programmatic method for integrating
  with other build steps)

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires pyramid.testing

%description tests
%oname is theme handling, image filtering, and asset optimization for
Pyramid.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Theme handling, image filtering, and asset optimization for Pyramid
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Provides:

* Theme / template handling.
* Theme configuration.
* Theme stacking (one theme can inherit from another).
* Image filtering / serving.
* Asset handling and compilation.
* Uses Mako, PIL, require.js, and LESS.

Command line tools:

* Compile assets (in addition to a programmatic method for integrating
  with other build steps)

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires pyramid.testing

%description -n python3-module-%oname-tests
%oname is theme handling, image filtering, and asset optimization for
Pyramid.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
%oname is theme handling, image filtering, and asset optimization for
Pyramid.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
%oname is theme handling, image filtering, and asset optimization for
Pyramid.

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

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc CHANGES *.rst
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
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20141108
- Initial build for Sisyphus

