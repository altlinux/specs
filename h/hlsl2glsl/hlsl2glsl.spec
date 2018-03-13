Name: hlsl2glsl
Version: 2016.11
Release: alt2.git20161116
Summary: HLSL to GLSL shader language translator
License: BSD
Group: Development/Tools
Url: https://github.com/aras-p/hlsl2glslfork

# https://github.com/aras-p/hlsl2glslfork.git
Source: %name-%version.tar

BuildPreReq: cmake gcc-c++ libglsl-optimizer-devel flex libGLEW-devel
BuildPreReq: libGLUT-devel

%description
HLSL2GLSL is a library and tool that converts HLSL shaders to GLSL.

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
	.
%make_build VERBOSE=1

%install
install -d %buildroot%_bindir
install -m644 hlsl2glsltest %buildroot%_bindir/

for i in $(find ./ -name '*.h*'); do
	j=$(echo $i |sed 's|\(.*\)/[^/]*|\1|')
	install -d %buildroot%_includedir/%name/$j
	install -p -m644 $i %buildroot%_includedir/%name/$j/
done

install -d %buildroot%_libdir
install -m644 *.a %buildroot%_libdir/

%files
%doc *.md LICENSE.txt TODO.txt
%_bindir/*
%_includedir/*
%_libdir/*.a

%changelog
* Tue Mar 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2016.11-alt2.git20161116
- Rebuilt with libGLEW 2.1.0.

* Tue Jul 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2016.11-alt1.git20161116
- Updated to latest upstream version

* Thu Sep 18 2014 Nazarov Denis <nenderus@altlinux.org> 2014.09-alt2.git20140912
- Rebuilt with libGLEW 1.11.0

* Wed Sep 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.09-alt1.git20140912
- Initial build for Sisyphus

