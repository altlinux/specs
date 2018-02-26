%define oname pyglet

%def_enable docs
%def_with python3

Name: python-module-%oname
Version: 1.2
Release: alt2.dev.hg20120428
Summary: Cross-platform windowing and multimedia library

Group: Development/Python
License: BSD
URL: http://www.pyglet.org/
# hg clone https://pyglet.googlecode.com/hg/ pyglet
Source: %oname-%version.tar.gz
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: python-devel python-modules-ctypes python-module-docutils
BuildPreReq: libGL-devel libX11-devel libXxf86vm-devel inkscape
BuildPreReq: python-module-sphinx-devel python-module-Pygments
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-docutils
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

export PYTHONPATH=$PYTHONPATH:$PWD:$PWD/tools
pushd tools
./gendoc.sh html-api html-tutorial html-guide
popd

%if_enabled docs
%generate_pickles $PWD $PWD/doc/html %oname
install -d %buildroot%python_sitelibdir/%oname
cp -fR pickle %buildroot%python_sitelibdir/%oname/
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
%doc doc/programming_guide doc/html examples
%endif

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG DESIGN LICENSE NOTICE PY3K README
%python3_sitelibdir/*
%endif

%changelog
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

