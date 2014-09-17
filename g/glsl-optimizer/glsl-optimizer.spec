%define sover 0

Name: glsl-optimizer
Version: 0.1.0
Release: alt1.git20140820
Summary: GLSL optimizer based on Mesa's GLSL compiler
License: MIT
Group: System/X11
Url: https://github.com/aras-p/glsl-optimizer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aras-p/glsl-optimizer.git
Source: %name-%version.tar

BuildPreReq: gcc-c++ cmake libGL-devel libGLES-devel

%description
A C++ library that takes GLSL shaders, does some GPU-independent
optimizations on them and outputs GLSL back. Optimizations are function
inlining, dead code removal, copy propagation, constant folding,
constant propagation, arithmetic optimizations and so on.

%package -n lib%name-devel
Summary: Development files of GLSL optimizer
Group: Development/C++
Requires: %name = %EVR

%description -n lib%name-devel
A C++ library that takes GLSL shaders, does some GPU-independent
optimizations on them and outputs GLSL back. Optimizations are function
inlining, dead code removal, copy propagation, constant folding,
constant propagation, arithmetic optimizations and so on.

This package contains developemnt files of GLSL optimizer.

%prep
%setup

%build
cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_Fortran_FLAGS:STRING="%optflags" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DSOVERSION=%sover \
	.
%make_build VERBOSE=1

%install
install -d %buildroot%_bindir
install -m755 glsl_* glslopt %buildroot%_bindir/

for i in $(find ./ -name '*.h*'); do
	j=$(echo $i |sed 's|\(.*\)/[^/]*|\1|')
	install -d %buildroot%_includedir/%name/$j
	install -p -m644 $i %buildroot%_includedir/%name/$j/
done

install -d %buildroot%_libdir
install -m644 lib*.a %buildroot%_libdir/

%files
%doc *.md
%_bindir/*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.a

%changelog
* Wed Sep 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20140820
- Initial build for Sisyphus

