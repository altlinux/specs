%define oname pyglet

%def_disable docs

Name: python3-module-%oname
Version: 1.5.21
Release: alt1
Summary: Cross-platform windowing and multimedia library

Group: Development/Python3
License: BSD
URL: http://www.pyglet.org/
# hg clone https://bitbucket.org/pyglet/pyglet
Source: %oname-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-html5lib python3-module-sphinx

%add_python3_req_skip Cocoa CoreFoundation LaunchServices Quartz
%filter_from_requires /darwin/d
%filter_from_requires /carbon/d
%filter_from_requires /win32/d

%description
pyglet provides an object-oriented programming interface for developing
games and other visually-rich applications for Windows, Mac OS X and
Linux.

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

%if_enabled docs
%prepare_sphinx .
%endif

%build
%python3_build

%install
%python3_install
pushd %buildroot%python3_sitelibdir/%oname
rm -fR */win32* libs/darwin input/*win* */*carbon.* \
	image/codecs/quicktime.* image/codecs/gdiplus.*
popd

%if_enabled docs
./make.py clean
mkdir -p doc/_build/html
./make.py docs

#generate_pickles $PWD $PWD/doc/_build/html %oname
%make -C doc pickle
install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%files
%doc DESIGN LICENSE NOTICE README.md
%python3_sitelibdir/*
%if_enabled docs
%exclude %python3_sitelibdir/%oname/pickle
%endif

%if_enabled docs
%files pickles
%dir %python3_sitelibdir/%oname
%python3_sitelibdir/%oname/pickle

%files docs
%doc doc/programming_guide doc/_build/html examples
%endif

%changelog
* Thu Jan 13 2022 Grigory Ustinov <grenka@altlinux.org> 1.5.21-alt1
- Automatically updated to 1.5.21.

* Thu Jun 03 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt5.a1.hg20150730
- Drop python2 support.

* Fri Nov 20 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.3.0-alt4.a1.hg20150730.1.1.2
- mac and win32 requires supressed

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0-alt4.a1.hg20150730.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0-alt4.a1.hg20150730.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

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

