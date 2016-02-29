%define name numeric
%define version 24.2
%define release alt6
%setup_python_module Numeric

Summary: Numerical Extension to Python
Name: %packagename
Version: %version
Release: %release
Source0: Numeric-%version.tar.gz
Source1: numpy.pdf.bz2
License: Python License
Group: Development/Python
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Prefix: _prefix
Provides: python-module-Numeric 
Obsoletes: python-Numeric
Requires(pre): python-module-arrayfns
Requires: python-module-arrayfns
%py_requires arrayfns
Url: http://www.pfdubois.com/numpy/

Patch0: Numeric-system-lapack.patch

Requires: python

# Automatically added by buildreq on Tue Jul 18 2006
BuildRequires: liblapack-devel python-devel python-modules 
BuildRequires: python-modules-compiler python-modules-encodings


%description

NumPy is a collection of extension modules to provide high-performance
multidimensional numeric arrays to the Python programming language.
Numerical Extension to Python with subpackages.

The authors and maintainers of the subpackages are: 

FFTPACK-3.1
        maintainer = "Numerical Python Developers"
        maintainer_email = "numpy-discussion@lists.sourceforge.net"
        description = "Fast Fourier Transforms"
        url = "http://numpy.sourceforge.net"

MA-12.2.0
        author = "Paul F. Dubois"
        description = "Masked Array facility"
        maintainer = "Paul F. Dubois"
        maintainer_email = "dubois@users.sf.net"
        url = "http://sourceforge.net/projects/numpy"

RNG-3.1
        author = "Lee Busby, Paul F. Dubois, Fred Fritsch"
        maintainer = "Paul F. Dubois"
        maintainer_email = "dubois@users.sf.net"
        description = "Cray-like Random number package."

%package devel
Group: Development/Python
Summary: Python numerical facilities
Requires: %name = %version-%release

Provides: python-numeric-devel python-Numeric-devel
Provides: python-numpy-devel

Obsoletes: python-numpy-devel python-numeric-devel

%description devel
A collection of extension modules to provide high-performance multidimensional
numeric arrays to the Python programming language.
Development files.

%package demo
Group: Development/Python
Summary: Python numerical facilities - demo 

%description demo
A collection of extension modules to provide high-performance multidimensional
numeric arrays to the Python programming language.

Demonstration and testing utilites

%define python_libdir %_libdir/python%_python_version
%define python_site_packages_dir %python_libdir/site-packages
%define python_includedir %_includedir/python%_python_version

%prep
%setup -q -n Numeric-%version 
bzcat %SOURCE1 >numpy.pdf

%patch0 -p 1

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
%python_install --optimize=2 --record=INSTALLED_FILES

sed -i 's|.*arrayfns\.so$||' INSTALLED_FILES

#find $RPM_BUILD_ROOT -type f | sed -e "s|$RPM_BUILD_ROOT||g" >>INSTALLED_FILES

mkdir -p %buildroot%_sysconfdir/buildreqs/files/ignore.d
cat > %buildroot%_sysconfdir/buildreqs/files/ignore.d/%name << EOF
^/usr/lib/python[^/]*/site-packages/Numeric$
EOF

install -d $RPM_BUILD_ROOT/%python_sitelibdir/Numeric/tools/numeric
install -d $RPM_BUILD_ROOT/%python_sitelibdir/Numeric/tools/numeric/NumTut
install -D -m 755 Demo/*py $RPM_BUILD_ROOT/%python_sitelibdir/Numeric/tools/numeric
install -D -m 644 Demo/NumTut/* $RPM_BUILD_ROOT/%python_sitelibdir/Numeric/tools/numeric/NumTut 
install -D -m 755 Test/*test.py $RPM_BUILD_ROOT/%python_sitelibdir/Numeric/tools/numeric

%add_python_lib_path  %_libdir/python%_python_version/site-packages/Numeric

%files -f INSTALLED_FILES
%config %_sysconfdir/buildreqs/files/ignore.d/%name
%doc MANIFEST *README PKG-INFO
%dir %python_sitelibdir/Numeric
%dir %python_sitelibdir/Numeric/FFT
%dir %python_sitelibdir/Numeric/MA
%dir %python_sitelibdir/Numeric/Numeric_headers
%dir %python_sitelibdir/Numeric/RNG
%exclude %python_includedir/Numeric

%files devel
%dir %python_includedir/Numeric
%python_includedir/Numeric/*
%doc numpy.pdf

%files demo
%python_sitelibdir/Numeric/tools/numeric

%changelog
* Mon Feb 29 2016 Denis Medvedev <nbr@altlinux.org> 24.2-alt6
- Moved demo stuff to python_sitelibdir.

* Fri Oct 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 24.2-alt5
- Restored in Sisyphus

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 24.2-alt4
- Owned directory %python_sitelibdir/Numeric (ALT #13391)

* Wed Jan 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 24.2-alt3
- Moved arrayfns into independent package

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

