%define oname pycairo
Name: python-module-%oname
Version: 1.10.1
Release: alt2.git20110619

Summary: Pycairo is a set of Python bindings for the vector graphics library cairo

License: GPL
Group: Development/Python
Url: http://www.cairographics.org/pycairo

Packager: Vitaly Lipatov <lav@altlinux.ru>

# git://git.cairographics.org/git/py2cairo
Source: pycairo-%version.tar.gz

%setup_python_module cairo

# Automatically added by buildreq on Wed Jul 01 2009
BuildRequires: gcc-c++ libcairo-devel python-devel
BuildPreReq: python-module-sphinx-devel python-module-Pygments
BuildPreReq: texlive-latex-base

BuildRequires: libcairo-devel >= 1.8.6

%description
James Henstridge has created cairo bindings for Python.
Cairo is a library for drawing vector graphics.
Vector graphics are interesting because when they appear on screen,
they don't lose clarity when resized or transformed.

%package devel
Summary: Development files for pycairo
Group: Development/Python
Requires: %name = %version-%release
#Requires: %name-pickles = %version-%release

%description devel
Development files for pycairo.

%package docs
Summary: Documentation for pycairo
Group: Development/Documentation
BuildArch: noarch

%description docs
Documentation for pycairo.

%package tests
Summary: Tests for pycairo
Group: Development/Python
Requires: %name = %version-%release

%description tests
Documentation for pycairo.

%package examples
Summary: Examples for pycairo
Group: Development/Python
Requires: %name = %version-%release

%description examples
Examples for pycairo.

%package pickles
Summary: Pickles for pycairo
Group: Development/Python

%description pickles
Pickles for pycairo.

%prep
%setup

sed -i 's|@PYVER@|%_python_version|g' doc/Makefile.am

%prepare_sphinx doc

%build
#rm -r aclocal.m4 ltmain.sh
#autoreconf
./autogen.sh
%configure
%make_build
# FIXME: run with built pycairo
#echo "import cairo" >test-cairo.py
#%_bindir/env python test-cairo.py

pushd doc
%make_build html
popd

%install
%makeinstall_std

# docs

install -d %buildroot%_docdir/%name-%version
install -p -m644 AUTHORS COPYING-* NEWS README \
	%buildroot%_docdir/%name-%version

cp -fR doc/.build/html %buildroot%_docdir/%name-%version/
#cp -fR doc/.build/latex/*.pdf %buildroot%_docdir/%name-%version/pdf

# pickles

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

# tests and examples

cp -fR examples test %buildroot%python_sitelibdir/%modulename/
for i in $(find %buildroot%python_sitelibdir/%modulename/examples -type d)
do
	touch $i/__init__.py
done

%pre pickles
rm -fR %python_sitelibdir/%oname/pickle

%files
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/AUTHORS
%doc %_docdir/%name-%version/COPYING-*
%doc %_docdir/%name-%version/NEWS
%doc %_docdir/%name-%version/README
%python_sitelibdir/%modulename
%exclude %python_sitelibdir/%modulename/test
%exclude %python_sitelibdir/%modulename/examples

%files devel
%_includedir/%oname
%_pkgconfigdir/%oname.pc

%files docs
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version
%exclude %_docdir/%name-%version/AUTHORS
%exclude %_docdir/%name-%version/COPYING-*
%exclude %_docdir/%name-%version/NEWS
%exclude %_docdir/%name-%version/README

%files tests
%python_sitelibdir/%modulename/test

%files examples
%python_sitelibdir/%modulename/examples

%files pickles
%dir %python_sitelibdir/%oname
%python_sitelibdir/%oname/pickle

%changelog
* Mon Nov 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt2.git20110619
- Enabled docs (except pdf) and pickles

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.10.1-alt1.git20110619.1
- Rebuild with Python-2.7
- bootstrap without docs and pickles

* Sat Aug 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt1.git20110619
- New snapshot
- Fixed updating (ALT #26118)

* Mon May 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt1.git20110502
- Version 1.10.1

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.11-alt1.git20110328.1
- Rebuilt with python-module-sphinx-devel

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.11-alt1.git20110328
- Some fixes from upstream

* Sun Mar 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.11-alt1.git20110123
- Version 1.8.11
- Rebuilt for debuginfo

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.10-alt1.git20100922.1
- Rebuilt for soname set-versions

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.10-alt1.git20100922
- Version 1.8.10 (ALT #24355)

* Fri Feb 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.9-alt1.git20100114
- Version 1.8.9
- Added docs, tests, examples and pickles packages

* Tue Nov 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.6-alt1.1
- Rebuilt with python 2.6

* Wed Jul 01 2009 Alexey Shabalin <shaba@altlinux.ru> 1.8.6-alt1
- new version 1.8.6 (with rpmrb script)
- update buildreq
- add patch for build with python-2.5 (upstream requires 2.6)

* Tue Sep 30 2008 Alexey Shabalin <shaba@altlinux.ru> 1.4.12-alt1
- new version 1.4.12 (with rpmrb script)

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.4.0-alt1.1
- Rebuilt with python-2.5.

* Sun Jun 24 2007 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0 (with rpmrb script)

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.6-alt1
- new version 1.2.6 (with rpmrb script)

* Sat Sep 02 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt0.1
- new version 1.2.2 (with rpmrb script)

* Sun Apr 30 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt3
- rebuild with new cairo

* Thu Feb 09 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt2
- update build requires

* Tue Nov 22 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- fix build/install sections (#7930)
- split devel package

* Tue Oct 04 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt0.1
- new version
- add pycairo.pc to install

* Mon Sep 12 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- enable build cairo.gtk

* Fri Sep 02 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- new version

* Sun Aug 28 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt0.1
- first build for ALT Linux Sisyphus
