%define somver 1
%define sover %somver.7.3
Name: cint
Summary: An interpreter for C and C++ code
Version: 7.3.00
Release: alt1.svn20091016.2
Group: Development/Tools
License: MIT
URL: http://root.cern.ch/drupal/content/cint
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn co http://root.cern.ch/svn/root/trunk/cint cint
Source: %name-%version-source.tar.gz

Requires: lib%name-devel = %version-%release

BuildPreReq: libreadline-devel gcc-c++ libtinfo-devel libncurses-devel
BuildPreReq: python-devel

%description
CINT is an interpreter for C and C++ code. It is useful e.g. for situations
where rapid development is more important than execution time. Using an
interpreter the compile and link cycle is dramatically reduced facilitating
rapid development. CINT makes C/C++ programming enjoyable even for part-time
programmers.

CINT covers most of ANSI C and ISO C++. A CINT script can call compiled
classes/functions and compiled code can make callbacks to CINT interpreted
functions. Utilities like makecint and rootcint automate the process of
embedding compiled C/C++ library code as shared objects (as Dynamic Link
Library, DLL, or shared library, .so). Source files and shared objects can be
dynamically loaded/unloaded without stopping the CINT process. CINT offers a gdb
like debugging environment for interpreted programs.

%package -n lib%name
Summary: Shared libraries of CINT interpreter
Group: System/Libraries

%description -n lib%name
CINT is an interpreter for C and C++ code. It is useful e.g. for situations
where rapid development is more important than execution time. Using an
interpreter the compile and link cycle is dramatically reduced facilitating
rapid development. CINT makes C/C++ programming enjoyable even for part-time
programmers.

This package contains shared libraries of CINT.

%package -n lib%name-devel
Summary: Development files of CINT interpreter
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
CINT is an interpreter for C and C++ code. It is useful e.g. for situations
where rapid development is more important than execution time. Using an
interpreter the compile and link cycle is dramatically reduced facilitating
rapid development. CINT makes C/C++ programming enjoyable even for part-time
programmers.

This package contains development files of CINT.

%package -n lib%name-devel-static
Summary: Static libraries of CINT interpreter
Group: Development/C++
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
CINT is an interpreter for C and C++ code. It is useful e.g. for situations
where rapid development is more important than execution time. Using an
interpreter the compile and link cycle is dramatically reduced facilitating
rapid development. CINT makes C/C++ programming enjoyable even for part-time
programmers.

This package contains static libraries of CINT.

%package doc
Summary: Documentation for CINT interpreter
Group: Development/Documentation
BuildArch: noarch

%description doc
CINT is an interpreter for C and C++ code. It is useful e.g. for situations
where rapid development is more important than execution time. Using an
interpreter the compile and link cycle is dramatically reduced facilitating
rapid development. CINT makes C/C++ programming enjoyable even for part-time
programmers.

This package contains documentation for CINT.

%package examples
Summary: Examples for CINT interpreter
Group: Development/Documentation
BuildArch: noarch

%description examples
CINT is an interpreter for C and C++ code. It is useful e.g. for situations
where rapid development is more important than execution time. Using an
interpreter the compile and link cycle is dramatically reduced facilitating
rapid development. CINT makes C/C++ programming enjoyable even for part-time
programmers.

This package contains examples for CINT.

%prep
%setup
sed -i 's|@SOMVER@|%somver|g' build/*.mk
sed -i 's|@SOVER@|%sover|g' build/*.mk

%build
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"
./configure \
	--prefix=%prefix \
	--libdir=%_libdir \
	--datadir=%_libdir \
	--with-prefix=$PWD \
	--coreversion=new \
	--checkstack \
	--inputmode=C++ \
	--readlinelib=%_libdir/libreadline.so
%make_build

%install
%makeinstall_std

install -d %buildroot%_docdir/%name
pushd doc
cp -fR man2 man3 %buildroot%_mandir/
cp -fR *.txt *.html v* ../demo %buildroot%_docdir/%name/
popd

# avoid conflict with man-pages
mv %buildroot%_man2dir/security.2 %buildroot%_man2dir/%name-security.2

%files
%doc COPYING FAQ.txt README.txt RELNOTE.txt
%_bindir/cint
%_bindir/makecint
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_libdir/%name
%_includedir/*
%_bindir/cint-config
%_man2dir/*
%_man3dir/*

%files -n lib%name-devel-static
%_libdir/*.a

%files doc
%doc %dir %_docdir/%name
%doc %_docdir/%name/*
%exclude %_docdir/%name/demo

%files examples
%doc %dir %_docdir/%name
%doc %_docdir/%name/demo

%changelog
* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.3.00-alt1.svn20091016.2
- Rebuilt for debuginfo

* Tue Oct 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.3.00-alt1.svn20091016.1
- Rebuilt for soname set-versions

* Mon Oct 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.3.00-alt1.svn20091016
- New snapshot
- Avoided conflict with man-pages

* Tue Jul 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.3.00-alt1.svn20090707
- Initial build for Sisyphus

