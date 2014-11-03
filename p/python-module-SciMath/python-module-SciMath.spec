%define oname SciMath
Name: python-module-%oname
Version: 4.1.2
Release: alt2.git20140829
Summary:  Scientific and Mathematical calculations

Group: Development/Python
License: BSD and GPLv2
URL: http://www.enthought.com/
# https://github.com/enthought/scimath.git
Source: %oname-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires: python-devel, python-module-setuptools gcc-c++
BuildPreReq: python-module-setupdocs libnumpy-devel
BuildPreReq: python-module-sphinx-devel python-module-Pygments

%description
The SciMath project includes packages to support scientific and
mathematical calculations, beyond the capabilities offered by SciPy.

  * enthought.interpolate
  * enthought.mathematics
  * enthought.units

%package tests
Summary: Tests for Scientific and Mathematical calculations
Group: Development/Python
Requires: %name = %version-%release

%description tests
The SciMath project includes packages to support scientific and
mathematical calculations, beyond the capabilities offered by SciPy.

This package contains tests for SciMath.

%package pickles
Summary: Pickles for Scientific and Mathematical calculations
Group: Development/Python

%description pickles
The SciMath project includes packages to support scientific and
mathematical calculations, beyond the capabilities offered by SciPy.

This package contains pickles for SciMath.

%package docs
Summary: Documentation for Scientific and Mathematical calculations
Group: Development/Documentation
BuildArch: noarch

%description docs
The SciMath project includes packages to support scientific and
mathematical calculations, beyond the capabilities offered by SciPy.

This package contains documentation for SciMath.

%prep
%setup

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build_debug

%install
%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt2.git20140829
- New snapshot
- Added docs

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt2.git20140415
- New snapshot

* Mon Jun 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt2.git20130329
- Rebuilt with updated NumPy

* Mon May 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt1.git20130329
- Version 4.1.2

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120516
- Version 4.1.1

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1.git20120508
- New snapshot

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.2-alt1.git20120116.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1.git20120116
- Version 4.0.2

* Wed Nov 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.git20110622
- Version 4.0.1

* Sat Oct 29 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.8-alt1.svn20110127.2
- Rebuild with Python-2.7

* Fri Oct 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.8-alt1.svn20110127.1
- Rebuilt with updated NumPy

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.8-alt1.svn20110127
- Version 3.0.8

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.7-alt1.svn20101101.1
- Rebuilt for debuginfo

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.7-alt1.svn20101101
- Version 3.0.7

* Sun Mar 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.6-alt1.svn20100225.1
- Extracted tests into separate package

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.6-alt1.svn20100225
- Version 3.0.6
- Rebuilt with reformed NumPy

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.5-alt1.svn20090721.1
- Rebuilt with python 2.6

* Thu Oct 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.5-alt1.svn20090721
- Initial build for Sisyphus

