%define oname BlockCanvas
Name: python-module-%oname
Version: 4.0.2
Release: alt1.git20120221
Summary: Enthought Numerical Modeling

Group: Development/Python
License: BSD and GPLv2
URL: http://www.enthought.com/
# https://github.com/enthought/blockcanvas.git
Source: %oname-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires: python-devel, python-module-setuptools
BuildPreReq: python-module-setupdocs
BuildPreReq: python-module-sphinx python-module-Pygments

%description
The BlockCanvas project provides a visual environment for creating simulation
experiments, where function and data are separated. Thus, you can define your
simulation algorithm by visually connecting function blocks into a data flow
network, and then run it with various data sets (known as "contexts");
likewise, you can use the same context in a different functional simulation.

The project provides support for plotting, function searching and inspection,
and optimization. It includes a stand-alone application that demonstrates the
block-canvas environment, but the same functionality can be incorporated into
other applications.

The BlockCanvas project relies on included libraries that allow multiple data
sets using Numeric arrays to be incorporated in a Traits-based model in a way
that is simple, fast, efficient, and consistent.

%package tests
Summary: Tests for Enthought Numerical Modeling
Group: Development/Documentation
Requires: %name = %version-%release

%description tests
The BlockCanvas project provides a visual environment for creating simulation
experiments, where function and data are separated. Thus, you can define your
simulation algorithm by visually connecting function blocks into a data flow
network, and then run it with various data sets (known as "contexts");
likewise, you can use the same context in a different functional simulation.

This package contains tests for BlockCanvas.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc *.txt docs/*.txt docs/model/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests
%exclude %python_sitelibdir/*/*/*/*/tests
%exclude %python_sitelibdir/*/*/*/*/*/tests

%files tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests
%python_sitelibdir/*/*/*/*/tests
%python_sitelibdir/*/*/*/*/*/tests

%changelog
* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1.git20120221
- New snapshot

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.2-alt1.git20111221.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1.git20111221
- Version 4.0.2

* Wed Nov 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.git20111111
- Version 4.0.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.2-alt1.svn20110127.1
- Rebuild with Python-2.7

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.2-alt1.svn20110127
- Version 3.2.2

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20101101.2
- Rebuilt for debuginfo

* Thu Nov 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20101101.1
- Fixed linking

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20101101
- Version 3.2.1

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt1.svn20100225
- Version 3.1.2
- Exctracted tests into separate package

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1.svn20090901.1
- Rebuilt with python 2.6

* Tue Oct 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1.svn20090901
- Initial build for Sisyphus

