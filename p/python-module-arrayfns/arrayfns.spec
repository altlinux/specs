%define oname arrayfns

Summary: arrayfns from Numerical Extension to Python
Name: python-module-%oname
Version: 24.2
Release: alt6.1.1
Source0: Numeric-%version.tar.gz
License: Python License
Group: Development/Python
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%py_provides %oname
Url: http://www.pfdubois.com/numpy/

%setup_python_module %oname
# Automatically added by buildreq on Tue Jul 18 2006
BuildRequires: liblapack-goto-devel python-devel python-modules 
BuildRequires: python-modules-compiler python-modules-encodings
BuildPreReq: libnumpy-devel

%description
NumPy is a collection of extension modules to provide high-performance
multidimensional numeric arrays to the Python programming language.
Numerical Extension to Python with subpackages.

This package contains %oname module from Numeric Extension.

%prep
%setup -n Numeric-%version 

%build
%add_optflags -I%_includedir/gotoblas -DXDOUBLE
%python_build_debug

%install
%python_build_install --optimize=2

%files
%python_sitelibdir/arrayfns.so
%exclude %python_sitelibdir/*.py*
%exclude %python_sitelibdir/arrayfns-*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 24.2-alt6.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 24.2-alt6.1
- Rebuild with Python-2.7

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 24.2-alt6
- Built with GotoBLAS2 instead of ATLAS

* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 24.2-alt5
- Rebuilt for debuginfo

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 24.2-alt4
- Rebuilt for soname set-versions

* Fri Mar 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 24.2-alt3
- Rebuilt with reformed NumPy

* Fri Jan 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 24.2-alt2
- Extracted arrayfns module into separate package from
  python-module-Numeric

* Wed Dec 16 2009 Igor Vlasenko <viy@altlinux.ru> 24.2-alt1.1.1.qa1
- NMU (by repocop): the following fixes applied:
  * vendor-tag for python-module-Numeric-devel
  * vendor-tag for python-module-Numeric-demo
  * vendor-tag for python-module-Numeric
  * postclean-05-filetriggers for spec file

* Fri Nov 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 24.2-alt1.1.1
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 24.2-alt1.1
- Rebuilt with python-2.5.

* Thu Jul 18 2006 Andrey Khavryuchenko <akhavr@altlinux.ru> 24.2-alt1
- Updated to new release

* Fri Jan 14 2005 Andrey Orlov <cray@altlinux.ru> 23.7-alt1
- New version

* Sat Jun 26 2004 Andrey Orlov <cray@altlinux.ru> 23.3-alt2
- Demonstration and testing utilites added

* Fri Jun 25 2004 Andrey Orlov <cray@altlinux.ru> 23.3-alt1
- New version

* Fri Jun 25 2004 Andrey Orlov <cray@altlinux.ru> 22.0-alt2
- Rebuild for python 23
- Path from Numeric.pth added for AutoReqProv;
- Some duplicated files excluded;

* Wed Oct 30 2002 Yuri N. Sedunov <aris@altlinux.ru> 22.0-alt1
- new version.

* Tue Feb 12 2002 Stanislav Ievlev <inger@altlinux.ru> 20.3-alt2
- Added buildreq filter

* Mon Jan 28 2002 Stanislav Ievlev <inger@altlinux.ru> 20.3-alt1
- 20.3 

* Fri Aug 10 2001 Stanislav Ievlev <inger@altlinux.ru> 20.1.0-alt1
- 20.1.0

* Wed Jun 27 2001 Stanislav Ievlev <inger@altlinux.ru> 17.3.0-alt1
- 17.3.0 . Cleanup spec. Rebuilt with python-2.1

* Sat Jan 20 2001 AEN <aen@logic.ru>
- RE adaptation
- build for python-2.0 only
* Mon Jan 15 2001 Lenny Cartier <lenny@mandrakesoft.com> 17.0-1mdk
- new in contribs

