%define _unpackaged_files_terminate_build 1

%define sover 0

Name: glsl-optimizer
Version: 2016.10
Release: alt1.git21b98a9854
Summary: GLSL optimizer based on Mesa's GLSL compiler
License: MIT
Group: System/X11
Url: https://github.com/aras-p/glsl-optimizer/

# https://github.com/aras-p/glsl-optimizer.git
Source: %name-%version.tar

BuildRequires: gcc-c++ cmake libGL-devel libGLES-devel

%description
A C++ library that takes GLSL shaders, does some GPU-independent
optimizations on them and outputs GLSL back. Optimizations are function
inlining, dead code removal, copy propagation, constant folding,
constant propagation, arithmetic optimizations and so on.

%package -n lib%name
Summary: Libraries of GLSL optimizer
Group: System/Libraries

%description -n lib%name
A C++ library that takes GLSL shaders, does some GPU-independent
optimizations on them and outputs GLSL back. Optimizations are function
inlining, dead code removal, copy propagation, constant folding,
constant propagation, arithmetic optimizations and so on.

This package contains libraries of GLSL optimizer.

%package -n lib%name-devel
Summary: Development files of GLSL optimizer
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
A C++ library that takes GLSL shaders, does some GPU-independent
optimizations on them and outputs GLSL back. Optimizations are function
inlining, dead code removal, copy propagation, constant folding,
constant propagation, arithmetic optimizations and so on.

This package contains development files of GLSL optimizer.

%prep
%setup

%build
%cmake \
	-DSOVERSION=%sover \
	%nil

%cmake_build VERBOSE=1

%install
%cmakeinstall_std

%ifarch x86_64 aarch64
# on other architectures tests may fail due to precision of floating point
%check
LD_LIBRARY_PATH=BUILD ./BUILD/glsl_test ./tests
%endif

%files
%doc license.txt
%doc *.md
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Wed Feb 13 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2016.10-alt1.git21b98a9854
- Updated to current upstream version.

* Wed Sep 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20140820
- Initial build for Sisyphus

