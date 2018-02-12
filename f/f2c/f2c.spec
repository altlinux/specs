%set_verify_elf_method unresolved=relaxed

%define somver 0
%define sover %somver.0.0
Name: f2c
Version: 20160102
Release: alt1
Summary: F2c converts Fortran 77 source code to C/C++ source code
License: %bsdstyle
Group: Development/C
Url: http://www.netlib.org/f2c/
BuildRequires(pre): unzip rpm-build-licenses
Patch: f2c-ALT-build.patch
Patch1: f2c-ALT-MIPS.patch

Source: http://www.netlib.org/f2c/libf2c.zip
Source2: http://www.netlib.org/f2c/fc
Source4: http://www.netlib.org/f2c/f2c.pdf
Source6: makefile
# http://www.netlib.org/f2c/src/
Source7: src.tgz

Requires: lib%name-ng-devel = %version-%release

%description
F2c converts Fortran 77 source code in files with names ending in `.f' or `.F' to
C (or C++) source files in the current directory, with `.c' substituted for the
final `.f' or `.F'. If no Fortran files are named, f2c reads Fortran from
standard input and writes C on standard output. File names that end with `.p' or
`.P' are taken to be prototype files, as produced by option `-P', and are read
first.

%package -n lib%name-ng
Summary: Shared library of f2c
Group: Development/C

%description -n lib%name-ng
F2c converts Fortran 77 source code in files with names ending in `.f' or `.F' to
C (or C++) source files in the current directory, with `.c' substituted for the
final `.f' or `.F'. If no Fortran files are named, f2c reads Fortran from
standard input and writes C on standard output. File names that end with `.p' or
`.P' are taken to be prototype files, as produced by option `-P', and are read
first.

This package contains shared library of f2c.

%package -n lib%name-ng-devel
Summary: Headers of f2c
Group: Development/C
Requires: lib%name-ng = %version-%release

%description -n lib%name-ng-devel
F2c converts Fortran 77 source code in files with names ending in `.f' or `.F' to
C (or C++) source files in the current directory, with `.c' substituted for the
final `.f' or `.F'. If no Fortran files are named, f2c reads Fortran from
standard input and writes C on standard output. File names that end with `.p' or
`.P' are taken to be prototype files, as produced by option `-P', and are read
first.

This package contains headers of f2c.

%package -n lib%name-ng-devel-static
Summary: Static library of f2c
Group: Development/C
Requires: lib%name-ng-devel = %version-%release

%description -n lib%name-ng-devel-static
F2c converts Fortran 77 source code in files with names ending in `.f' or `.F' to
C (or C++) source files in the current directory, with `.c' substituted for the
final `.f' or `.F'. If no Fortran files are named, f2c reads Fortran from
standard input and writes C on standard output. File names that end with `.p' or
`.P' are taken to be prototype files, as produced by option `-P', and are read
first.

This package contains static library of f2c.

%package -n lib%name-devel-doc
Summary: Documentation for f2c
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
F2c converts Fortran 77 source code in files with names ending in `.f' or `.F' to
C (or C++) source files in the current directory, with `.c' substituted for the
final `.f' or `.F'. If no Fortran files are named, f2c reads Fortran from
standard input and writes C on standard output. File names that end with `.p' or
`.P' are taken to be prototype files, as produced by option `-P', and are read
first.

This package contains development documentation for f2c.

%prep
%setup -c -a7
%patch -p1
%patch1 -p1
install -p -m644 %SOURCE6 ./
sed -i '19s|(LIBDIR)|%buildroot%_libdir|' makefile

%build
%make_build f2c.h hadd
%make_build MALLOC=malloc.o
%make_build libf2c.so SOMVER=%somver SOVER=%sover
%make_build -C src -f makefile.u

%install
mkdir -p %buildroot%_libdir
%makeinstall_std
%makeinstall_std -C src -f makefile.u
mkdir -p %buildroot%_docdir/%name
install -p -m755 %SOURCE2 %buildroot%_bindir/f2cc
install -p -m644 %SOURCE4 %buildroot%_docdir/%name
bzip2 src/changes

%files
%doc src/README src/Notice
%_bindir/*
%_man1dir/*

%files -n lib%name-ng
%doc README Notice src/changes.bz2
%_libdir/*.so.*

%files -n lib%name-ng-devel
%_includedir/*
%_libdir/*.so

%files -n lib%name-ng-devel-static
%_libdir/*.a

%files -n lib%name-devel-doc
%_docdir/%name

%changelog
* Mon Feb 12 2018 Fr. Br. George <george@altlinux.ru> 20160102-alt1
- Version 20160102
- MIPS build

* Thu May 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20130926-alt1
- Version 20130926

* Fri Sep 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20110108-alt1
- Version 20110108

* Wed Apr 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100903-alt1
- Version 20100903

* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090102-alt7
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090102-alt6
- Rebuilt for debuginfo

* Tue Oct 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090102-alt5
- Rebuilt for soname set-versions

* Wed Feb 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090102-alt4
- Removed conflicts/obsoletes on old package

* Thu Nov 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090102-alt3
- Renamed library packages for avoid conflict with old gcc (ALT #22139)
- Added executable files

* Thu Mar 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090102-alt2
- Add shared library

* Tue Mar 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090102-alt1
- Initial build for Sisyphus
