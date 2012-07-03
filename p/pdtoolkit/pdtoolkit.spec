%ifarch %ix86
%define destdir linux
%endif
%ifarch x86_64
%define destdir x86_64
%endif
%define _perl_lib_path %buildroot%perl_vendor_privlib/pdbSql

%define somver 3
%define sover %somver.14.1
Name: pdtoolkit
Version: 3.17
Release: alt2
Summary: The Program Database Toolkit
License: BSD-like
Group: Development/Tools
Url: http://www.cs.uoregon.edu/research/pdt/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# originally extension of source archive was .tgz
Source: http://www.cs.uoregon.edu/research/paracomp/pdtoolkit/Download/pdt_latest.tar.gz

Conflicts: tau < 2.18.1p1-alt4

BuildPreReq: gcc-fortran gcc-c++ rpm-build-perl

%description
The Program Database Toolkit (PDT) is a tool infrastructure that provides
access to the high-level interface of source code for analysis tools and
applications.  Currently, the toolkit consists of the C/C++ and Fortran 77/90/95
IL (Intermediate Language) Analyzers, and DUCTAPE (C++ program Database 
Utilities and Conversion Tools APplication Environment) library and applica-
tions.  The EDG C++ (or Mutek Fortran 90) Front End first parses a source 
file, and produces an intermediate language file.  The appropriate IL 
Analyzer processes this IL file, and creates a "program database" (PDB) file 
consisting of the high-level interface of the original source.  Use of the 
DUCTAPE library then makes the contents of the PDB file accessible to 
applications. This release also includes the Flint F95 parser from Cleanscape 
Inc.

%package doc
Summary: Documentation for PDT
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation for PDT.

%package -n lib%name
Summary: Shared library of PDT
Group: System/Libraries

%description -n lib%name
Shared library of PDT.

%package -n lib%name-devel
Summary: Development files of PDT
Group: Development/Other
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
Development files of PDT.

%package -n lib%name-devel-static
Summary: Static library of PDT
Group: Development/Other
Requires: lib%name-devel = %version-%release
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-static
Static library of PDT.

#package -n pdbsql
#Summary: PDB files as a relational database
#Group: Development/Databases
#BuildArch: noarch
#Requires: %name = %version-%release
#Requires: sqlite3

#description -n pdbsql
#The pdbsql package includes two important pieces:
#
# - An SQLite schema that represents PDB files as a relational database.
# - A Perl script for converting PDB 3.0 files to the SQLite form.
#
#The goal of this package is to allow users to write code that consumes
#data contained within PDB files in a wider set of languages than
#currently provided by the C++ Ductape API alone.  Any language that
#has a binding to SQLite can use this method of accessing PDB data.
#Furthermore, the use of SQL to construct queries on the data removes
#the need for the user to explicitly code up the query by combining STL
#data structures, iterators, and query-specific logic.  This also means
#that general purpose user interface tools for accessing the data in
#the database can traverse the PDB data using the standard SQL language.

%prep
%setup

%build
TARGET=$PWD/built
./configure \
	-useropt='%optflags %optflags_shared' \
	-GNU \
	-prefix=$TARGET
%make_build

%install
TARGET=$PWD/built
%make install
pushd ductape/inc
PATH=$PATH:$TARGET/%destdir/bin ./MakeHtmlDocu
popd

rm contrib/pdbsql/sqlite-3.5.6.tar.gz -f
pushd $TARGET/%destdir/bin
sed -i -e '4,5d' f95parse gfparse
sed -i 's|${BINDIR}/pdt_gfortran|%_libexecdir/%name/bin|' gfparse
for i in $(ls *parse); do
	sed -i '4s|^\(BINDIR\)\=.*|\1=%_bindir|' $i
	sed -i '5s|^\(PDTDIR\)\=.*|\1=%prefix|' $i
done
popd

install -d %buildroot%_bindir
install -d %buildroot%_libdir
install -d %buildroot%_libexecdir/%name/bin
install -d %buildroot%_sysconfdir
install -d %buildroot%_includedir
install -d %buildroot%_docdir/%name
install -d %buildroot%_datadir/pdbsql
install -d %buildroot%perl_vendor_privlib/pdbSql
cp -fR $TARGET/include/* %buildroot%_includedir
cp -fR ductape/html/* %buildroot%_docdir/%name
install -m755 $TARGET/%destdir/bin/pdt_gfortran/* %buildroot%_libexecdir/%name/bin
rm -fR $TARGET/%destdir/bin/pdt_gfortran
install -m755 $TARGET/%destdir/bin/* %buildroot%_bindir
install -m644 $TARGET/%destdir/lib/* %buildroot%_libdir
install -m644 $TARGET/etc/* %buildroot%_sysconfdir
mv contrib/pdbsql/pdbSql.pm %buildroot%perl_vendor_privlib/pdbSql
install -p -m644 contrib/pdbsql/* %buildroot%_datadir/pdbsql
mv %buildroot%_bindir/tau_instrumentor %buildroot%_bindir/tau_instrumentor_pdt

# shared library

pushd %buildroot%_libdir
mkdir tmp
pushd tmp
ar x ../libpdb.a
g++ -shared * -lstdc++ \
	-Wl,-soname,libpdb.so.%somver -o ../libpdb.so.%sover
rm -f *
popd
rmdir tmp
ln -s libpdb.so.%sover libpdb.so.%somver
ln -s libpdb.so.%somver libpdb.so
popd

sed -i '1s|/sh|/bash|' %buildroot%_bindir/gfparse

# install true edgcpfe
#rm -f %buildroot%_bindir/edgcpfe
#%ifarch x86_64
#install -m755 x86_64/bin/edgcpfe %buildroot%_bindir
#%else
#install -m755 linux/bin/edgcpfe %buildroot%_bindir
#%endif

%brp_strip_debug %_bindir/edgcpfe

%files
%doc README CREDITS LICENSE doc
%_bindir/*
%_libexecdir/%name
%_sysconfdir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-static
%_libdir/*.a

#files -n pdbsql
#_datadir/pdbsql
#perl_vendor_privlib/pdbSql

%files doc
%doc html
%_docdir/%name

%changelog
* Sat Mar 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.17-alt2
- Disabled pdbsql

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.17-alt1
- Version 3.17

* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.16-alt4
- Rebuilt for debuginfo

* Fri Oct 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.16-alt3
- Fixed edgcpfe by disabling strip

* Tue Aug 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.16-alt2
- Fixed for checkbashisms

* Fri Jul 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.16-alt1
- Version 3.16

* Sun Aug 30 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.14.1-alt5
- Added shared library

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.14.1-alt4
- Rebuild with PIC

* Tue Jun 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.14.1-alt3
- Rename tau_instrumentor -> tau_instrumentor_pdt

* Wed May 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.14.1-alt2
- Rebuild with gcc 4.4

* Mon Apr 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.14.1-alt1
- Initial build for Sisyphus

