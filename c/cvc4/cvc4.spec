%define pyname CVC4
%def_with python3

Name: cvc4
Version: 1.4
Release: alt1
Summary: Automatic theorem prover for satisfiability modulo theories (SMT) problems
License: BSD
Group: Development/Python
Url: http://cvc4.cs.nyu.edu/web/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-c++ libgmp-devel antlr3-C-devel boost-devel antlr3-tool
BuildPreReq: swig libreadline-devel python-devel doxygen graphviz /proc
BuildPreReq: libglpk-cut-log-devel libgmpxx-devel cxxtest %_bindir/java
BuildPreReq: chrpath
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

Requires: lib%name = %EVR

%description
CVC4 is an efficient open-source automatic theorem prover for
satisfiability modulo theories (SMT) problems. It can be used to prove
the validity (or, dually, the satisfiability) of first-order formulas in
a large number of built-in logical theories and their combination.

CVC4 is the fourth in the Cooperating Validity Checker family of tools
(CVC, CVC Lite, CVC3) but does not directly incorporate code from any
previous version. A joint project of NYU and U Iowa, CVC4 aims to
support the features of CVC3 and SMT-LIBv2 while optimizing the design
of the core system architecture and decision procedures to take
advantage of recent engineering and algorithmic advances.

%package -n lib%name-devel-docs
Summary: Documentation for %name
Group: Development/Documentation
#BuildArch: noarch

%description -n lib%name-devel-docs
CVC4 is an efficient open-source automatic theorem prover for
satisfiability modulo theories (SMT) problems. It can be used to prove
the validity (or, dually, the satisfiability) of first-order formulas in
a large number of built-in logical theories and their combination.

This package contains documentation for %name.

%package -n lib%name
Summary: Shared libraries of %name
Group: System/Libraries

%description -n lib%name
CVC4 is an efficient open-source automatic theorem prover for
satisfiability modulo theories (SMT) problems. It can be used to prove
the validity (or, dually, the satisfiability) of first-order formulas in
a large number of built-in logical theories and their combination.

This package contains shared libraries of %name.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
CVC4 is an efficient open-source automatic theorem prover for
satisfiability modulo theories (SMT) problems. It can be used to prove
the validity (or, dually, the satisfiability) of first-order formulas in
a large number of built-in logical theories and their combination.

This package contains development files of %name.

%package -n python-module-%pyname
Summary: Python bindings of %name
Group: Development/Python
Requires: lib%name = %EVR

%description -n python-module-%pyname
CVC4 is an efficient open-source automatic theorem prover for
satisfiability modulo theories (SMT) problems. It can be used to prove
the validity (or, dually, the satisfiability) of first-order formulas in
a large number of built-in logical theories and their combination.

This package contains Python bindings of %name.

%if_with python3
%package -n python3-module-%pyname
Summary: Python bindings of %name
Group: Development/Python3
Requires: lib%name = %EVR

%description -n python3-module-%pyname
CVC4 is an efficient open-source automatic theorem prover for
satisfiability modulo theories (SMT) problems. It can be used to prove
the validity (or, dually, the satisfiability) of first-order formulas in
a large number of built-in logical theories and their combination.

This package contains Python bindings of %name.
%endif

%prep
%setup

%build
%add_optflags -I%_includedir/glpk-cut-log
%autoreconf
%configure \
	--enable-gpl \
	--enable-optimized \
	--enable-doxygen-dot \
	--enable-doxygen-man \
	--enable-language-bindings=c,c++,python \
	--enable-replay \
	--with-glpk \
	--with-glpk-dir=%prefix \
	--with-boost=%prefix \
	--with-portfolio \
	--with-readline
%make V=1

%make doc

%install
%makeinstall_std
install -d %buildroot%python_sitelibdir
mv %buildroot%_datadir/pyshared/* %buildroot%python_sitelibdir/
ln -s ../../pyshared/CVC4.so %buildroot%python_sitelibdir/_CVC4.so

%if_with python3
rm -fR builds
export PYTHON=python3
%configure \
	--enable-gpl \
	--enable-optimized \
	--enable-doxygen-dot \
	--enable-doxygen-man \
	--enable-language-bindings=c,c++,python \
	--enable-replay \
	--with-glpk \
	--with-glpk-dir=%prefix \
	--with-boost=%prefix \
	--with-portfolio \
	--with-readline
%make_install DESTDIR=$PWD/buildroot install V=1
install -d %buildroot%python3_sitelibdir
mv buildroot%_libdir/pyshared %buildroot%_libdir/pyshared3
mv buildroot%_datadir/pyshared/* %buildroot%python3_sitelibdir/
ln -s ../../pyshared3/CVC4.so %buildroot%python3_sitelibdir/_CVC4.so
%endif

chrpath -d %buildroot%_bindir/pcvc4

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
# don't work after chrpath
#make check V=1
export PYTHONPATH=%buildroot%python_sitelibdir
python -c "from %pyname import *"
%if_with python3
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 -c "from %pyname import *"
%endif

%files
%doc AUTHORS COPYING NEWS README RELEASE-NOTES THANKS
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_man3dir/*
%_man5dir/*

%files -n python-module-%pyname
%python_sitelibdir/*
%_libdir/pyshared

%files -n lib%name-devel-docs
%doc doc/doxygen/html examples

%if_with python3
%files -n python3-module-%pyname
%python3_sitelibdir/*
%_libdir/pyshared3
%endif

%changelog
* Mon Mar 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Initial build for Sisyphus

