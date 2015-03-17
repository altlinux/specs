Name: picosat
Version: 960
Release: alt1
Summary: PicoSAT solver
License: MIT
Group: Sciences/Mathematics
Url: http://fmv.jku.at/picosat/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make

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

%prep
%setup

%build
%add_optflags %optflags_shared
./configure \
	--shared
%make_build_ext libpicosat.so
%make_build_ext all

%install
%ifarch x86_64
LIB_SUFF=64
%endif
%makeinstall_std LIB_SUFF=$LIB_SUFF

%files
%doc NEWS README
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 960-alt1
- Initial build for Sisyphus

