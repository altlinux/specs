Name: fortranposix
Version: 0.1
Release: alt1
Summary: Makes system calls on Linux and Unix like systems available to Fortran programs
License: LGPLv2.1+
Group: Development/Tools
Url: http://sourceforge.net/projects/fortranposix/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-fortran

%description
This is an implementation of some POSIX functions in Fortran 90/95.

%package -n lib%name
Summary: Shared library of fortranposix
Group: System/Libraries

%description -n lib%name
This is an implementation of some POSIX functions in Fortran 90/95.

%prep
%setup

%build
%make_build

%install
install -d %buildroot%_libdir
install -m644 *.so %buildroot%_libdir

%files -n lib%name
%doc CHANGES CREDITS README TODO
%doc Makefile *.f90 *.c
%_libdir/*.so

%changelog
* Wed Mar 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

