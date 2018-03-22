%def_with python3

Name: picosat
Version: 960
Release: alt2.1.1
Summary: PicoSAT solver
License: MIT
Group: Sciences/Mathematics
Url: http://fmv.jku.at/picosat/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make
BuildPreReq: python-devel swig
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

Requires: lib%name = %EVR

%description
The SAT problem is the classical NP complete problem of searching for a
satisfying assignment of a propositional formula in conjunctive normal
form (CNF). General information on SAT can be found at www.satlive.org
or www.satlib.org.

%package -n lib%name
Summary: Shared library of %name
Group: System/Libraries

%description -n lib%name
The SAT problem is the classical NP complete problem of searching for a
satisfying assignment of a propositional formula in conjunctive normal
form (CNF). General information on SAT can be found at www.satlive.org
or www.satlib.org.

This package contains shared library of %name.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
The SAT problem is the classical NP complete problem of searching for a
satisfying assignment of a propositional formula in conjunctive normal
form (CNF). General information on SAT can be found at www.satlive.org
or www.satlib.org.

This package contains development files of %name.

%package -n python-module-%name
Summary: Python bindings of %name
Group: Development/Python
Requires: lib%name = %EVR
%py_provides _%name

%description -n python-module-%name
The SAT problem is the classical NP complete problem of searching for a
satisfying assignment of a propositional formula in conjunctive normal
form (CNF). General information on SAT can be found at www.satlive.org
or www.satlib.org.

This package contains Python bindings of %name.

%if_with python3
%package -n python3-module-%name
Summary: Python bindings of %name
Group: Development/Python3
Requires: lib%name = %EVR
%py3_provides _%name

%description -n python3-module-%name
The SAT problem is the classical NP complete problem of searching for a
satisfying assignment of a propositional formula in conjunctive normal
form (CNF). General information on SAT can be found at www.satlive.org
or www.satlib.org.

This package contains Python bindings of %name.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags %optflags_shared
./configure \
	--shared
%make_build_ext libpicosat.so
%make_build_ext all

%python_build

%if_with python3
pushd ../python3
export LDFLAGS=-L$PWD/../%name-%version
%python3_build
popd
%endif

%install
%ifarch x86_64
LIB_SUFF=64
%endif
%makeinstall_std LIB_SUFF=$LIB_SUFF

install -d %buildroot%python_sitelibdir
install -m644 build/lib*/*.so %buildroot%python_sitelibdir/

%if_with python3
pushd ../python3
install -d %buildroot%python3_sitelibdir
install -m644 build/lib*/*.so %buildroot%python3_sitelibdir/
popd
%endif

%check
pushd ~
export LD_LIBRARY_PATH=%buildroot%_libdir
export PYTHONPATH=%buildroot%python_sitelibdir
python -c "import _picosat; print (_picosat.picosat_version())"
%if_with python3
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 -c "import _picosat; print (_picosat.picosat_version())"
%endif
popd

%files
%doc NEWS README
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n python-module-%name
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%name
%python3_sitelibdir/*
%endif

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 960-alt2.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 960-alt2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 960-alt2
- Applied patch from https://github.com/pysmt/pysmt/tree/master/patches
  for Python bindings

* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 960-alt1
- Initial build for Sisyphus

