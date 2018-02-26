%define rhome %_libdir/R
%define oname rpy

%def_enable docs

Name: python-module-%oname
Version: 1.0.3
Release: alt3.svn20101101.1
Summary: Python interface to the R Programming Language
License: MPL/GPL/LGPL
Group: Development/Python
Url: http://rpy.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://rpy.svn.sourceforge.net/svnroot/rpy/trunk
Source: %oname-%version.tar.gz
Source1: http://rpy.sourceforge.net/faithful.py

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel R-devel python-module-sphinx-devel
BuildPreReq: python-module-Pygments
%setup_python_module %oname

%description
RPy is a very simple, yet robust, Python interface to the R Programming
Language. It can manage all kinds of R objects and can execute arbitrary
R functions (including the graphic functions). All errors from the R
language are converted to Python exceptions. Any module installed for
the R system can be used from within Python.

This code is inspired by RSPython from the Omegahat project. The main
goals of RPy are:

  * to have a very robust interface for using R from Python

  * the interface should be as transparent and easy to use as possible

  * it should be usable for real scientific and statistical computations

%if_enabled docs

%package pickles
Summary: Pickles for RPy
Group: Development/Python

%description pickles
RPy is a very simple, yet robust, Python interface to the R Programming
Language. It can manage all kinds of R objects and can execute arbitrary
R functions (including the graphic functions). All errors from the R
language are converted to Python exceptions. Any module installed for
the R system can be used from within Python.

This package contains pickles for RPy.

%package doc
Summary: Documentation and examples for RPy
Group: Development/Documentation
BuildArch: noarch

%description doc
RPy is a very simple, yet robust, Python interface to the R Programming
Language. It can manage all kinds of R objects and can execute arbitrary
R functions (including the graphic functions). All errors from the R
language are converted to Python exceptions. Any module installed for
the R system can be used from within Python.

This package contains development documentation and examples for RPy.

%endif

%prep
%setup
cp -f %SOURCE1 examples/

%if_enabled docs
%prepare_sphinx .
%endif

%build
find -type f -print0 |
	xargs -r0 grep -FlZ runtime_library_dirs -- |
	xargs -r0 sed -i /runtime_library_dirs/d --
export RHOME=%rhome
%python_build_debug

%if_enabled docs
pushd doc
%make_build info html
popd

%generate_pickles $PWD $PWD/doc/rpy_html %oname
%endif

%install
export RHOME=%_libdir/R
%python_install

install -d %buildroot%_docdir/%oname
install -d %buildroot%_infodir

%if_enabled docs
install -m644 doc/rpy_html/* %buildroot%_docdir/%oname
cp -fR examples %buildroot%_docdir/%oname/
install -m644 doc/*.info %buildroot%_infodir

install -d %buildroot%python_sitelibdir/%oname
cp -fR pickle %buildroot%python_sitelibdir/%oname/
%endif

%files
%doc NEWS README TODO GPL_LICENSE LGPL_LICENSE MPL_LICENSE
%python_sitelibdir/*
%if_enabled docs
%exclude %python_sitelibdir/%oname/pickle
%endif
%exclude %python_sitelibdir/rpy_wintools*

%if_enabled docs
%files pickles
%dir %python_sitelibdir/%oname
%python_sitelibdir/%oname/pickle

%files doc
%_docdir/%oname
%_infodir/*
%endif

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.3-alt3.svn20101101.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Dec 14 2011 Dmitry V. Levin <ldv@altlinux.org> 1.0.3-alt3.svn20101101
- Eliminated RPATH.

* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt2.svn20101101
- Enabled docs

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.3-alt1.svn20101101.3.1
- Rebuild with Python-2.7

* Thu Apr 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.svn20101101.3
- Built with GotoBLAS2 instead of ATLAS

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.svn20101101.2
- Rebuilt with python-module-sphinx-devel

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.svn20101101.1
- Rebuilt for debuginfo

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.svn20101101
- New snapshot

* Fri Jun 11 2010 Alexey Tourbin <at@altlinux.ru> 1.0.3-alt1.svn20100211.1
- Rebuilt with libR-2.11.so

* Mon Mar 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.svn20100211
- New snapshot
- Added pickles package

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.svn20090914.1
- Rebuilt with python 2.6

* Mon Sep 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.svn20090914
- Initial build for Sisyphus

