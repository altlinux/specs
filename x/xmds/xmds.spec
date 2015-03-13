Name: xmds
Version: 1.6.6
Release: alt1

Summary: xmds - an extensible multi-dimensional simulator for PDEs (Partial Differential Equations) and ODEs

License: GPL
Group: Sciences/Mathematics
Url: http://www.xmds.org
Packager: Denis Medvedev <nbr@altlinux.org>

Source: xmds-%version.tar.bz2
Requires: libfftw-devel,libfftw3-devel,lam-devel,lam,gcc4.1-c++

BuildPreReq: libfftw-devel,libfftw3-devel,lam,lam-devel,gcc4.1-c++
%description
     An open-source XML based simulation package
   Solves  From Ordinary Differential Equations (ODEs) up to stochastic Partial Differential Equations (PDEs)
 Many applications:
 physics
 mathematics
 engineering
 finance
 economics
 chemistry
 theoretical biology
 Generates fast, C++ compiled code
 Documentation and source are free!
 Runs on Linux, Unix, MacOS X and Cygwin (Windows)
 XMDS is a code generator that integrates equations. You write them down in human readable form in an XML file, and it goes away and writes and compiles a C++ program that integrates those equations as fast as it can possibly be done in your architecture.

%prep
%setup

%build
%remove_optflags -Wtrampolines
%add_optflags %optflags_shared
%configure --enable-fftw3 --disable-mpi --enable-threads
%make_build

%install
%makeinstall_std
mkdir -p %buildroot/%_docdir/xmds-%version-%release
cp AUTHORS ChangeLog NEWS README TODO \
	%buildroot/%_docdir/xmds-%version-%release/
mkdir -p %buildroot/%_docdir/xmds-%version-%release/examples
cp examples/* %buildroot/%_docdir/xmds-%version-%release/examples
install -p -m755 source/loadxsil.m %buildroot%_bindir/

SRCDIR=$PWD
pushd %buildroot%_libdir
g++ -shared -Wl,--whole-archive lib%name.a -Wl,--no-whole-archive \
	$SRCDIR/source/xsil2graphics.o -o lib%name.so
popd

%files
%_docdir/xmds-%version-%release
%_bindir/xmds
%_bindir/xsil2graphics
%_bindir/loadxsil.m
/usr/include/*
/usr/share/man/man1/*
%_libdir/lib*.*

%changelog
* Fri Mar 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.6-alt1
- Version 1.6.6

* Tue May 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6-alt4
- fix build

* Fri Dec 14 2007 Denis Medvedev <nbr@altlinux.ru> 1.6-alt3
- Added description about PAE

* Fri Aug 31 2007 Denis Medvedev <nbr@altlinux.ru> 1.6-alt2
- Recompiled without mpi, who really needs mpi should recompile fftw with mpi too

* Tue Aug 28 2007 Denis Medvedev <nbr@altlinux.ru> 1.6-alt1
- Initial ALT release

