%define oname pyglet

%def_disable docs
%def_with python3

Name: python-module-%oname
Version: 1.3.0
Release: alt4.a1.hg20150730.1
Summary: Cross-platform windowing and multimedia library

Group: Development/Python
License: BSD
URL: http://www.pyglet.org/
# hg clone https://bitbucket.org/pyglet/pyglet
Source: %oname-%version.tar.gz
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

#BuildPreReq: python-devel python-modules-ctypes python-module-docutils
#BuildPreReq: libGL-devel libX11-devel libXxf86vm-devel inkscape
#BuildPreReq: python-module-sphinx-devel python-module-Pygments
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-bsddb python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-2to3 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-jinja2 python3-module-pytz python3-module-setuptools python3-module-snowballstemmer
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python3-module-html5lib python3-module-sphinx rpm-build-python3 time

#BuildRequires: python3-devel python3-module-docutils
%endif

%add_python_req_skip Cocoa CoreFoundation LaunchServices Quartz

%description
pyglet provides an object-oriented programming interface for developing
games and other visually-rich applications for Windows, Mac OS X and
Linux.

%if_with python3
%package -n python3-module-%oname
Summary: Cross-platform windowing and multimedia library (Python 3)
Group: Development/Python3
%add_python3_req_skip Cocoa CoreFoundation LaunchServices Quartz

%description -n python3-module-%oname
pyglet provides an object-oriented programming interface for developing
games and other visually-rich applications for Windows, Mac OS X and
Linux.
%endif

%if_enabled docs

%package pickles
Summary: Pickles for cross-platform windowing and multimedia library
Group: Development/Python

%description pickles
pyglet provides an object-oriented programming interface for developing
games and other visually-rich applications for Windows, Mac OS X and
Linux.

This package contains pickles for pyglet.

%package docs
Summary: Documentation for cross-platform windowing and multimedia library
Group: Development/Documentation
BuildArch: noarch

%description docs
pyglet provides an object-oriented programming interface for developing
games and other visually-rich applications for Windows, Mac OS X and
Linux.

This package contains development documentation for pyglet.

%endif

%prep
%setup

touch tools/__init__.py

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%if_enabled docs
%prepare_sphinx .
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
pushd %buildroot%python_sitelibdir/%oname
rm -fR */win32* libs/darwin input/*win* */*carbon.* \
	image/codecs/quicktime.* image/codecs/gdiplus.*
popd

%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%python3_sitelibdir/%oname
rm -fR */win32* libs/darwin input/*win* */*carbon.* \
	image/codecs/quicktime.* image/codecs/gdiplus.*
popd
%endif

./make.py clean
mkdir -p doc/_build/html
./make.py docs

%if_enabled docs
#generate_pickles $PWD $PWD/doc/_build/html %oname
%make -C doc pickle
install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%files
%doc CHANGELOG DESIGN LICENSE NOTICE PY3K README
%python_sitelibdir/*
%if_enabled docs
%exclude %python_sitelibdir/%oname/pickle
%endif

%if_enabled docs
%files pickles
%dir %python_sitelibdir/%oname
%python_sitelibdir/%oname/pickle

%files docs
%doc doc/programming_guide doc/_build/html examples
%endif

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG DESIGN LICENSE NOTICE PY3K README
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt4.a1.hg20150730.1
- NMU: Use buildreq for BR.

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt4.a1.hg20150730
- Version 1.3.0a1

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt4.alpha1.hg20140614
- New snapshot

* Tue Jan 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt4.alpha1.hg20131128
- Fixed build

* Tue Dec 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt3.alpha1.hg20131128
- New snapshot

* Thu Feb 21 2013 Aleksey Avdeev <solo@altlinux.ru> 1.2-alt3.alpha1
- New version 1.2alpha1

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.dev.hg20120428
- New snapshot
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.dev.hg20111121
- New snapshot

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt2.dev.hg20110508.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.dev.hg20110508
- New snapshot

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.dev.hg20101021.1
- Rebuilt with python-module-sphinx-devel

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.dev.hg20101021
- New snapshot

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.dev.hg20100427
- New snapshot (svn -> hg)

* Mon Mar 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20100124
- New snapshot
- Extracted docs into separate package

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20090906.2
- Rebuilt with python 2.6

* Thu Oct 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20090906.1
- Fixed OpenGL configuration error

* Wed Oct 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20090906
- Initial build for Sisyphus

