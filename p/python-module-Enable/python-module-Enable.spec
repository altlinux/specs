%define oname Enable
Name: python-module-%oname
Version: 4.1.1
Release: alt1.git20120504
Summary: Drawing and interaction packages

Group: Development/Python
License: BSD and GPLv2
URL: http://code.enthought.com/projects/enable/
# https://github.com/enthought/enable.git
Source: %oname-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires: python-devel, python-module-setuptools
BuildPreReq: libnumpy-devel gcc-c++ swig python-module-Pyrex
BuildPreReq: python-module-sphinx-devel python-module-Pygments
BuildPreReq: libGL-devel libX11-devel python-module-Cython
BuildPreReq: libGLU-devel

%add_python_req_skip macport

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
%setup

%prepare_sphinx .

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%generate_pickles docs/source docs/source %oname
sphinx-build -E -a -b html -c docs/source -d doctrees docs/source html

%install
%python_install

rm -fR %buildroot%python_sitelibdir/enthought/kiva/mac
rm -f $(find %buildroot%python_sitelibdir -name '*mac*.py*')

install -d %buildroot%python_sitelibdir/enable
cp -fR pickle %buildroot%python_sitelibdir/enable/

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests
%exclude %python_sitelibdir/enable/pickle

%files pickles
%dir %python_sitelibdir/enable
%python_sitelibdir/enable/pickle

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests

%files doc
%doc docs/kiva docs/*.txt examples html

%changelog
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

