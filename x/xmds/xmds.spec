Name: xmds
Version: 1.6
Release: alt4

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
%setup -q
%build
%configure --enable-fftw3 --disable-mpi   
make
%install
%make_install install DESTDIR=%buildroot
mkdir -p %buildroot/%_docdir/xmds-%version-%release
cp *.pdf %buildroot/%_docdir/xmds-%version-%release/
mkdir -p %buildroot/%_docdir/xmds-%version-%release/examples
cp examples/* %buildroot/%_docdir/xmds-%version-%release/examples

%files
%_docdir/xmds-%version-%release/*
%_docdir/xmds-%version-%release/examples/*
%_bindir/xmds
%_bindir/xsil2graphics
%_bindir/loadxsil.m
/usr/include/getopt_xmds.h
/usr/include/xmdscomplex.h
/usr/include/xmdsconfig.h
/usr/share/man/man1/*
%_libdir/lib*.*

%changelog
* Tue May 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6-alt4
- fix build

* Fri Dec 14 2007 Denis Medvedev <nbr@altlinux.ru> 1.6-alt3
- Added description about PAE

* Fri Aug 31 2007 Denis Medvedev <nbr@altlinux.ru> 1.6-alt2
- Recompiled without mpi, who really needs mpi should recompile fftw with mpi too

* Tue Aug 28 2007 Denis Medvedev <nbr@altlinux.ru> 1.6-alt1
- Initial ALT release

