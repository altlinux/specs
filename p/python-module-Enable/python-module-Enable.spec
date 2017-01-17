%define _unpackaged_files_terminate_build 1
%define oname Enable
Name: python-module-%oname
Version: 4.6.1
Release: alt1
Summary: Drawing and interaction packages

Group: Development/Python
License: BSD and GPLv2
URL: http://code.enthought.com/projects/enable/
# https://github.com/enthought/enable.git
Source0: https://pypi.python.org/packages/08/3d/d57626e77a6fdc16feab3b5df615507193ad5c1ec163d960f1f54e729e70/enable-%{version}.tar.bz2
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires: python-devel, python-module-setuptools
BuildPreReq: libnumpy-devel gcc-c++ swig python-module-Pyrex
BuildPreReq: python-module-sphinx-devel python-module-Pygments
BuildPreReq: libGL-devel libX11-devel python-module-Cython
BuildPreReq: libGLU-devel python-module-traits fonts-ttf-PT

%add_python_req_skip macport mac_context hypothesis

%description
The Enable project provides two related multi-platform packages for
drawing GUI objects. The Enable package is a multi-platform object
drawing library built on top of Kiva. The core of Enable is a
container/component model for drawing and event notification. Kiva is a
multi-platform DisplayPDF vector drawing engine that supports multiple
output backends, including Windows, GTK, and Macintosh native windowing
systems, a variety of raster image formats, PDF, and Postscript.

%package pickles
Summary: Pickles for Enable project
Group: Development/Python

%description pickles
The Enable project provides two related multi-platform packages for
drawing GUI objects. The Enable package is a multi-platform object
drawing library built on top of Kiva. The core of Enable is a
container/component model for drawing and event notification. Kiva is a
multi-platform DisplayPDF vector drawing engine that supports multiple
output backends, including Windows, GTK, and Macintosh native windowing
systems, a variety of raster image formats, PDF, and Postscript.

This package contains pickles for Enable project.

%package tests
Summary: Tests for Enable project
Group: Development/Python
Requires: %name = %version-%release
%add_python_req_skip hypothesis

%description tests
The Enable project provides two related multi-platform packages for
drawing GUI objects. The Enable package is a multi-platform object
drawing library built on top of Kiva. The core of Enable is a
container/component model for drawing and event notification. Kiva is a
multi-platform DisplayPDF vector drawing engine that supports multiple
output backends, including Windows, GTK, and Macintosh native windowing
systems, a variety of raster image formats, PDF, and Postscript.

This package contains tests for Enable project.

%package doc
Summary: Documentation for Enable project
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description doc
The Enable project provides two related multi-platform packages for
drawing GUI objects. The Enable package is a multi-platform object
drawing library built on top of Kiva. The core of Enable is a
container/component model for drawing and event notification. Kiva is a
multi-platform DisplayPDF vector drawing engine that supports multiple
output backends, including Windows, GTK, and Macintosh native windowing
systems, a variety of raster image formats, PDF, and Postscript.

This package contains development documentation for Enable project.

%prep
%setup -q -n enable-%{version}

%prepare_sphinx .

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%generate_pickles docs/source docs/source %oname
sphinx-build -E -a -b html -c docs/source -d doctrees docs/source html

%install
%python_install

find %buildroot%python_sitelibdir -type f -name '*.py' -exec \
	sed -i 's|// |#|' '{}' +

rm -fR %buildroot%python_sitelibdir/enthought/kiva/mac
rm -f $(find %buildroot%python_sitelibdir -name '*mac*.py*')

install -d %buildroot%python_sitelibdir/enable
cp -fR pickle %buildroot%python_sitelibdir/enable/

%files
%doc *.rst PKG-INFO docs examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/example*
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests
%exclude %python_sitelibdir/enable/pickle

%files pickles
%dir %python_sitelibdir/enable
%python_sitelibdir/enable/pickle

%files tests
%python_sitelibdir/*/test*
%python_sitelibdir/*/example*
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests

%files doc
%doc docs/kiva examples

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 4.6.1-alt1
- automated PyPI update

* Tue Feb 09 2016 Sergey Alembekov <rt@altlinux.ru> 4.6.0-alt3.git20151207
- skip hypothesys requirement for -tests subpackage

* Mon Dec 07 2015 Sergey Alembekov <rt@altlinux.ru> 4.6.0-alt2.git20151207
- update to current upstream branch

* Sun May 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.0-alt1.git20150423
- Version 4.6.0

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1.git20141003
- New snapshot

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1.git20140501
- Version 4.5.0

* Sun Oct 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2.git20131017
- New snapshot

* Mon Jun 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2.git20130328
- Rebuilt with updated NumPy

* Mon May 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.git20130328
- Version 4.3.0

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20130108
- New snapshot

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20120920
- Version 4.2.1

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120504
- New snapshot

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.1-alt1.git20120117.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120117
- Version 4.1.1

* Wed Nov 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.git20111114
- Version 4.0.1

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.1-alt1.svn20110127.2
- Rebuild with Python-2.7

* Mon Oct 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.svn20110127.1
- Rebuilt with updated NumPy

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.svn20110127
- Version 3.4.1

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.3-alt1.svn20101113.2
- Rebuilt with python-module-sphinx-devel

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.3-alt1.svn20101113.1
- Rebuilt for debuginfo

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.3-alt1.svn20101113
- Version 3.3.3

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.2-alt1.svn20100722
- Version 3.3.2

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1.svn20100225
- Version 3.3.1
- Extracted tests into separate package
- Added pickles package

* Sat Feb 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090901.5
- Extracted tests into separated package
- Rebuilt with reformed NumPy

* Sat Feb 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090901.4
- Rebuilt with reformed NumPy

* Sat Jan 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090901.3
- Rebuilt without python-module-Numeric

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090901.2
- Rebuilt with python 2.6

* Mon Oct 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090901.1
- Extracted documentation into separate package

* Wed Oct 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090901
- Initial build for Sisyphus

