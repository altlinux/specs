%define oname freetype

%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt1.git20150409.1.1
Summary: Freetype python bindings
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/freetype-py/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rougier/freetype-py.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: lib%oname xvfb-run
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-numpy python-module-matplotlib
#BuildPreReq: python-module-OpenGL python-module-pygobject3
#BuildPreReq: python-module-Pillow python-module-pycairo
#BuildPreReq: python-module-sphinx-devel python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-numpy python3-module-matplotlib
#BuildPreReq: python3-module-OpenGL python3-module-pygobject3
#BuildPreReq: python3-module-Pillow python3-module-pycairo
%endif

%py_provides %oname
Requires: lib%oname
%py_requires ctypes

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: at-spi2-atk at-spi2-core colord dbus dbus-tools-gui fakeroot fontconfig fonts-bitmap-misc glib-networking gobject-introspection gobject-introspection-x11 libat-spi2-core libatk-gir libcairo-gobject libcap-ng libgdk-pixbuf libgdk-pixbuf-gir libgpg-error libgtk+3-gir libpango-gir libwayland-client libwayland-cursor libwayland-egl libwayland-server python-base python-devel python-module-OpenGL_accelerate python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cssselect python-module-cycler python-module-dateutil python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-matplotlib-gtk3 python-module-numpy python-module-pluggy python-module-py python-module-pyparsing python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-2to3 python3 python3-base python3-module-numpy python3-module-pluggy python3-module-py python3-module-pycparser python3-module-pyparsing python3-module-pytest python3-module-setuptools xauth xkbcomp xkeyboard-config xorg-server-common xorg-xvfb xz
BuildRequires: python-module-OpenGL python-module-Pillow python-module-alabaster python-module-docutils python-module-html5lib python-module-matplotlib python-module-numpy-testing python-module-objects.inv python-module-pycairo python-module-pygobject3 python-module-setuptools-tests python3-module-cffi python3-module-matplotlib python3-module-pycairo python3-module-pygobject3 python3-module-setuptools-tests rpm-build-python3 time xvfb-run

%description
Freetype python provides bindings for the FreeType library. Only the
high-level API is bound.

%if_with python3
%package -n python3-module-%oname
Summary: Freetype python bindings
Group: Development/Python3
%py3_provides %oname
Requires: lib%oname
%py3_requires ctypes

%description -n python3-module-%oname
Freetype python provides bindings for the FreeType library. Only the
high-level API is bound.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Freetype python provides bindings for the FreeType library. Only the
high-level API is bound.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Freetype python provides bindings for the FreeType library. Only the
high-level API is bound.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3/examples -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

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

%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
export PYTHONPATH=$PWD
xvfb-run py.test -vv $(find %oname/ -name '*.py')
xvfb-run py.test -vv $(find examples/ -name '*.py')
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
xvfb-run py.test-%_python3_version -vv $(find %oname/ -name '*.py')
#xvfb-run py.test-%_python3_version -vv $(find examples/ -name '*.py')
popd
%endif

%files
%doc *.rst *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc examples doc/_build/html

%if_with python3
%files -n python3-module-%oname
%doc *.rst *.txt
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.git20150409.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1.git20150409.1
- NMU: Use buildreq for BR.

* Wed Apr 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20150409
- Initial build for Sisyphus

