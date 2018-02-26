%define somver 1
%define sover %somver.4.0
Name: chasm
Version: 1.4.0
Release: alt4.cvs20090407
Summary: Tool to improve C++ and Fortran 90 interoperability
License: LANL
Group: Development/Tools
Url: http://chasm-interop.sourceforge.net
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: openpdt libopenpdt-devel java-devel-default saxon8
BuildPreReq: gcc-c++ gcc-fortran
BuildPreReq: doxygen texlive-latex-base

Source: http://www.cca-forum.org/download/cca-tools/cca-tools-0.7.0/chasm-1.4.tar.gz

%description
Chasm is a tool to improve C++ and Fortran 90 interoperability.  Chasm
parses Fortran 90 source code and automatically generates C++ bridging
code that can be used in C++ programs to make calls to Fortran
routines.  It also automatically generates C structs that provide
a bridge to Fortran derived types.  Chasm supplies a C++ array
descriptor class which provides an interface between C and F90
arrays.  This allows arrays to be created in one language and then
passed to and used by the other language.

Chasm works by parsing C++ and Fortran source files and generating an
XML file.  The XML file describes C++ classes, Fortran modules,
user-defined types, functions, and function parameters.  XSLT
stylesheets are used to transform the XML file into bridging code
that is used to call C++ and Fortran routines.

Chasm (version 1.1.0 and later) contains the Fortran, array descriptor
library.  This is a low-level C library used to manipulate Fortran array
descriptors (dope vectors).  It is the only way one can pass F90
assumed-shape arrays and array sections between C and Fortran.  This
library is primarily aimed at interoperability tool developers, rather
than end users.

%package -n lib%name
Summary: Shared library of Chasm
Group: System/Libraries

%description -n lib%name
This package contains shared library of Chasm. If You need XSLT
transformation, in addition install package chasm-xml.

%package -n lib%name-devel
Summary: Development files of Chasm
Group: Development/Other
Requires: %name = %version-%release
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
This package contains libraries and headers of Chasm. If You need XSLT
transformation, in addition install package chasm-xml.

%package -n lib%name-devel-static
Summary: Static library of Chasm
Group: Development/Other
Requires: %name = %version-%release
Requires: lib%name-devel = %version-%release
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-static
This package contains static library of Chasm.

%package xml
Summary: XSLT and DTD files for developing with Chasm
Group: Development/Other
BuildArch: noarch
Requires: lib%name-devel = %version-%release

%description xml
XSLT and DTD files for developing with Chasm.

%package devel-doc
Summary: Development documentation for Chasm
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
Development documentation for Chasm.

%package -n cca-tutorial-engine
Summary: Master CCA tutorial engine package
Group: Development/Other
BuildArch: noarch

%description -n cca-tutorial-engine
Master CCA tutorial engine package.

%package -n cca-tutorial-%name-examples
Summary: Chasm examples for CCA tutorial engine
Group: Development/Other
BuildArch: noarch
Requires: lib%name-devel = %version-%release
Requires: cca-tutorial-engine = %version-%release
Obsoletes: cca-tutorial-%name-sidl
Obsoletes: cca-tutorial-components-f90

%description -n cca-tutorial-%name-examples
Chasm examples for CCA tutorial engine.

%package example-particle
Summary: Example of generating code for calling Fortran from C++
Group: Development/Other
BuildArch: noarch
Requires: lib%name-devel = %version-%release
Requires: saxon8 gcc-c++ gcc-fortran openpdt

%description example-particle
The array descriptor library is completely tested and is considered
production-level quality.  Currently, other Chasm tools for generating code
for language interoperability are under development and are not tested, nor
are they complete.  The most mature are the tools for generating code for
calling Fortran from C++.  See this package for an example
of how to use these tools.

%prep
%setup

%build
%add_optflags %optflags_shared
%autoreconf
%configure \
%ifarch x86_64
	--with-arch=linux64 \
%endif
	--enable-pdt \
	--enable-shared \
	--with-xalan-root=%_javadir \
	--with-F90-vendor=GNU
%make_build
pushd doc
doxygen
popd
pushd example/cca-tutorial
%make_build
popd

%install
%makeinstall_std
pushd %buildroot%_bindir
mv xmlgen chasm_xmlgen
popd

%ifarch x86_64
install -d %buildroot%_libdir
mv %buildroot%_libexecdir/* %buildroot%_libdir/
%endif

install -d %buildroot%_man3dir
install -d %buildroot%_docdir/%name/html
install -d %buildroot%_datadir/%name/xml
install -d %buildroot%_datadir/cca-tutorial
install -d %buildroot%_datadir/%name-example-particle

mv %buildroot%_datadir/mapping.dtd %buildroot%_datadir/%name/xml
mv %buildroot%_datadir/xform %buildroot%_datadir/%name/xml

install -m644 doc/man/man3/* %buildroot%_man3dir
install -m644 doc/html/* %buildroot%_docdir/%name/html
install -m644 doc/CCA_Tutorial_Chasm.ppt %buildroot%_docdir/%name
rm -f example/particle/Makefile.in
install -m644 example/particle/* %buildroot%_datadir/%name-example-particle
rm -f $(find example/cca-tutorial/ -name 'Makefile*')
cp -fR example/cca-tutorial/* %buildroot%_datadir/cca-tutorial/
cp -fR xml/* %buildroot%_datadir/%name/xml/

srcdir=$PWD
pushd %buildroot%_datadir
find ./cca-tutorial -type d|sed 's|^\./|%%dir %_datadir/|' > \
	$srcdir/cca-dirs.list
find ./cca-tutorial -type f|sed 's|^\./|%_datadir/|' > $srcdir/cca-files.list
popd

# shared library, mod's

pushd %buildroot%_libdir
for i in $(ls *.mod); do
ln -s %_libdir/$i %buildroot%_includedir
done

mkdir tmp
pushd tmp
ar x ../lib%name.a
f77 -shared * \
	-Wl,-soname,lib%name.so.%somver -o ../lib%name.so.%sover
rm -f *
popd
rmdir tmp
ln -s lib%name.so.%sover lib%name.so.%somver
ln -s lib%name.so.%somver lib%name.so
popd

%files
%doc LICENSE
%_bindir/*
%dir %_datadir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_libdir/*.mod
%_includedir/*
%_man3dir/*

%files -n lib%name-devel-static
%_libdir/*.a

%files xml
%_datadir/%name

%files devel-doc
%_docdir/%name

%files -n cca-tutorial-engine -f cca-dirs.list

%files -n cca-tutorial-%name-examples -f cca-files.list

%files example-particle
%_datadir/%name-example-particle

%changelog
* Sat Mar 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt4.cvs20090407
- Rebuilt with OpenPDT

* Tue Mar 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt3.cvs20090407
- Rebuilt without pdtoolkit

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.cvs20090407.5
- Rebuilt for debuginfo

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.cvs20090407.4
- Rebuilt for soname set-versions

* Sun Jan 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.cvs20090407.3
- Fixed for autoconf 2.6

* Wed Jan 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.cvs20090407.2
- Fixed:
  + autoreconf by using autoconf 2.5
  + working with XSLT transformer: xalan -> saxon8

* Sun Aug 30 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.cvs20090407.1
- Added links to *.mod files into include directory
- Added shared library

* Sun Apr 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.cvs20090407
- Add files into cca-tutorial packages and example of using the array descriptor library

* Tue Apr 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.cvs20090407
- Initial build for Sisyphus

