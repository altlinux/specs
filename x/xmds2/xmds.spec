%def_disable check

Name: xmds2
Version: 2.2.2
Release: alt1

Summary: xmds - an extensible multi-dimensional simulator for PDEs (Partial Differential Equations) and ODEs

License: GPL
Group: Sciences/Mathematics
Url: http://www.xmds.org

Source: xmds-%version.tar
BuildArch: noarch

BuildPreReq: libfftw-devel libfftw3-devel openmpi-devel gcc-c++
BuildPreReq: python-devel python-module-setuptools-tests libhdf5-devel
BuildPreReq: libgsl-devel libnumpy-devel python-module-lxml hdf5-tools
BuildPreReq: python-module-h5py python-module-cheetah xmds
BuildPreReq: python-module-pyparsing python-module-mpmath
BuildPreReq: python-modules-xml

Requires: libfftw-devel libfftw3-devel libhdf5 libgsl-devel hdf5-tools
Requires: xmds libnumpy-devel
%py_requires numpy lxml h5py Cheetah pyparsing mpmath xml

%description
     An open-source XML based simulation package
   Solves From Ordinary Differential Equations (ODEs) up to stochastic
   Partial Differential Equations (PDEs)
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
 XMDS is a code generator that integrates equations. You write them down
   in human readable form in an XML file, and it goes away and writes
   and compiles a C++ program that integrates those equations as fast as
   it can possibly be done in your architecture.

%prep
%setup

%build
source %_libdir/openmpi/bin/mpivars.sh
export PYTHONPATH=$PWD
python bin/xmds2 --reconfigure
%make_build

%install
source %_libdir/openmpi/bin/mpivars.sh
%python_build_install

mkdir -p %buildroot/%_docdir/%name-%version-%release
cp -fR documentation %buildroot/%_docdir/%name-%version-%release/
mkdir -p %buildroot/%_docdir/%name-%version-%release/examples
cp examples/* %buildroot/%_docdir/%name-%version-%release/examples
install -d %buildroot%_man1dir
install -p -m644 man/* %buildroot%_man1dir/

%check
source %_libdir/openmpi/bin/mpivars.sh
export PATH=$PATH:%buildroot%_bindir
export PYTHONPATH=$PWD
./run_tests.py -v

%files
%_docdir/%name-%version-%release
%_bindir/*
%_man1dir/*
%python_sitelibdir/*

%changelog
* Sat Mar 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt1
- Version 2.2.2

* Tue May 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6-alt4
- fix build

* Fri Dec 14 2007 Denis Medvedev <nbr@altlinux.ru> 1.6-alt3
- Added description about PAE

* Fri Aug 31 2007 Denis Medvedev <nbr@altlinux.ru> 1.6-alt2
- Recompiled without mpi, who really needs mpi should recompile fftw with mpi too

* Tue Aug 28 2007 Denis Medvedev <nbr@altlinux.ru> 1.6-alt1
- Initial ALT release

