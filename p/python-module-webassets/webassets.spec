%define oname webassets

%def_with python3

Name: python-module-%oname
Version: 0.11
Release: alt1.dev.git20150202
Summary: Media asset management for Python, with glue code for various web frameworks
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/webassets/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/miracle2k/webassets.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose python-module-mock
BuildPreReq: python-module-yaml python-module-glob2
BuildPreReq: python-module-jinja2 python-module-cssutils
BuildPreReq: python-module-yuicompressor python-module-closure
BuildPreReq: python-module-closure-soy python-module-slimit
BuildPreReq: python-module-libsass python-module-cssprefixer
BuildPreReq: python-module-Pillow python-module-CleverCSS
BuildPreReq: python-module-pyScss python-module-slimmer
BuildPreReq: python-module-cssmin
BuildPreReq: python-modules-json python-modules-logging
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-mock
BuildPreReq: python3-module-yaml python3-module-glob2
BuildPreReq: python3-module-jinja2 python3-module-cssutils
BuildPreReq: python3-module-yuicompressor python3-module-closure
BuildPreReq: python3-module-closure-soy python3-module-slimit
BuildPreReq: python3-module-libsass python3-module-cssprefixer
BuildPreReq: python3-module-Pillow python3-module-CleverCSS
BuildPreReq: python3-module-pyScss python3-module-slimmer
BuildPreReq: python3-module-cssmin
%endif

%py_provides %oname
%py_requires json logging yaml glob2 jinja2 cssutils yuicompressor PIL
%py_requires closure closure_soy slimit libsass cssprefixer clevercss
%py_requires pyScss slimmer cssmin

%description
Merges, minifies and compresses Javascript and CSS files, supporting a
variety of different filters, including YUI, jsmin, jspacker or CSS
tidy. Also supports URL rewriting in CSS files.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Merges, minifies and compresses Javascript and CSS files, supporting a
variety of different filters, including YUI, jsmin, jspacker or CSS
tidy. Also supports URL rewriting in CSS files.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Media asset management for Python, with glue code for various web frameworks
Group: Development/Python3
%py3_provides %oname
%py3_requires json logging yaml glob2 jinja2 cssutils yuicompressor PIL
%py3_requires closure closure_soy slimit libsass cssprefixer clevercss
%py3_requires pyScss slimmer cssmin

%description -n python3-module-%oname
Merges, minifies and compresses Javascript and CSS files, supporting a
variety of different filters, including YUI, jsmin, jspacker or CSS
tidy. Also supports URL rewriting in CSS files.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Merges, minifies and compresses Javascript and CSS files, supporting a
variety of different filters, including YUI, jsmin, jspacker or CSS
tidy. Also supports URL rewriting in CSS files.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Merges, minifies and compresses Javascript and CSS files, supporting a
variety of different filters, including YUI, jsmin, jspacker or CSS
tidy. Also supports URL rewriting in CSS files.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Merges, minifies and compresses Javascript and CSS files, supporting a
variety of different filters, including YUI, jsmin, jspacker or CSS
tidy. Also supports URL rewriting in CSS files.

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
%doc AUTHORS CHANGES RELEASING TODO *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test.*

%files tests
%python_sitelibdir/*/test.*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html examples

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES RELEASING TODO *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*
%endif

%changelog
* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.dev.git20150202
- Initial build for Sisyphus

