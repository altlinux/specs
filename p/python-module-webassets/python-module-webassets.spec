%define oname webassets

%def_without docs
%def_with python3
%def_without tests

Name: python-module-%oname
Version: 0.12.1
Release: alt1.1

Summary: Media asset management for Python, with glue code for various web frameworks

License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/webassets/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/miracle2k/webassets.git
# Source-url: https://pypi.io/packages/source/w/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose python-module-mock
BuildPreReq: python-module-yaml python-module-glob2
BuildPreReq: python-module-jinja2 python-module-cssutils
BuildPreReq: python-module-yuicompressor python-module-closure
BuildPreReq: python-module-closure-soy python-module-slimit
#BuildPreReq: python-module-libsass
BuildPreReq: python-module-Pillow python-module-CleverCSS
BuildPreReq: python-module-pyScss
BuildPreReq: python-module-psutil
#BuildPreReq: python-module-slimmer
#BuildPreReq: python-module-cssmin python-module-cssprefixer
BuildPreReq: python-modules-json python-modules-logging
%if_with docs
BuildPreReq: python-module-sphinx-devel
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose python3-module-mock
BuildPreReq: python3-module-yaml python3-module-glob2
BuildPreReq: python3-module-jinja2 python3-module-cssutils
BuildPreReq: python3-module-yuicompressor python3-module-closure
BuildPreReq: python3-module-closure-soy python3-module-slimit
#BuildPreReq: python3-module-libsass
BuildPreReq: python3-module-psutil
BuildPreReq: python3-module-Pillow python3-module-CleverCSS
#BuildPreReq: python3-module-pyScss python3-module-slimmer
#BuildPreReq: python3-module-cssmin python3-module-cssprefixer
%endif

%py_provides %oname
#py_requires json logging yaml glob2 jinja2 cssutils yuicompressor PIL
#py_requires closure closure_soy slimit libsass cssprefixer clevercss
#py_requires pyScss slimmer cssmin

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
#py3_requires json logging yaml glob2 jinja2 cssutils yuicompressor PIL
#py3_requires closure closure_soy slimit libsass cssprefixer clevercss
#py3_requires pyScss slimmer cssmin

# FIXME
%add_python3_req_skip webassets.six.moves

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

%if_with docs
%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Merges, minifies and compresses Javascript and CSS files, supporting a
variety of different filters, including YUI, jsmin, jspacker or CSS
tidy. Also supports URL rewriting in CSS files.

This package contains documentation for %oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%if_with docs
%prepare_sphinx .
ln -s ../objects.inv docs/
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

%if_with docs
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%if_with tests
%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif
%endif

%files
%doc AUTHORS CHANGES *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
#exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test.*

%files tests
%python_sitelibdir/*/test.*

#%files pickles
#python_sitelibdir/*/pickle

%if_with docs
%files docs
%doc docs/_build/html examples
%endif

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.12.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Oct 04 2017 Vitaly Lipatov <lav@altlinux.ru> 0.12.1-alt1
- switch to build from tarball
- new version (0.12.1) with rpmgs script

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.dev.git20150202
- Initial build for Sisyphus

