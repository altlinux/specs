Name: libllvm
Version: 6.0.0
Release: alt1%ubt
Summary: The Low Level Virtual Machine
Group: Development/C
License: NCSA
Url: http://llvm.org

Source0: http://releases.llvm.org/%version/llvm-%version.src.tar.xz
Patch3: llvm-alt-fix-linking.patch
Patch4: llvm-alt-triple.patch
Patch6: RH-0001-CMake-Split-static-library-exports-into-their-own-ex.patch
Patch7: 0001-DebugInfo-Discard-invalid-DBG_VALUE-instructions-in-.patch
Patch8: 0001-Fixup-for-rL326769-RegState-Debug-is-being-truncated.patch

BuildPreReq: /proc
BuildRequires(pre): cmake >= 3.4.3 rpm-build-ubt
BuildRequires: chrpath binutils-devel gcc-c++ libffi-devel libtinfo-devel ninja-build python-modules-compiler

%description
LLVM is a compiler infrastructure designed for compile-time, link-time,
runtime, and idle-time optimization of programs from arbitrary
programming languages. The compiler infrastructure includes mirror sets
of programming tools as well as libraries with equivalent functionality.

%package devel-static
Summary: Static libraries and header files for LLVM
Group: Development/C
Conflicts: llvm-devel llvm-devel-static llvm4.0-devel llvm4.0-devel-static llvm6.0-devel llvm6.0-devel-static

%description devel-static
This package contains static library and header files needed to develop new
native programs that use the LLVM infrastructure.

%prep
%setup -n llvm-%version.src
%patch3 -p1
%patch4 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
%cmake -G Ninja \
	-DCMAKE_BUILD_TYPE=Release \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DLLVM_TARGETS_TO_BUILD="host;AMDGPU;BPF;" \
	-DLLVM_EXPERIMENTAL_TARGETS_TO_BUILD='AVR' \
	-DLLVM_ENABLE_LIBCXX:BOOL=OFF \
	-DLLVM_ENABLE_ZLIB:BOOL=ON \
	-DLLVM_ENABLE_FFI:BOOL=ON \
	-DLLVM_ENABLE_RTTI:BOOL=ON \
	-DLLVM_OPTIMIZED_TABLEGEN:BOOL=ON \
	-DLLVM_BINUTILS_INCDIR="%_includedir/bfd" \
	-DLLVM_BUILD_RUNTIME:BOOL=ON \
	-DLLVM_INCLUDE_TOOLS:BOOL=ON \
	-DLLVM_BUILD_TOOLS:BOOL=ON \
	-DLLVM_INCLUDE_EXAMPLES:BOOL=OFF \
	-DLLVM_BUILD_EXAMPLES:BOOL=OFF \
	-DLLVM_INCLUDE_UTILS:BOOL=ON \
	-DLLVM_INSTALL_UTILS:BOOL=OFF \
	-DLLVM_INCLUDE_DOCS:BOOL=OFF \
	-DLLVM_BUILD_DOCS:BOOL=OFF \
	-DLLVM_ENABLE_SPHINX:BOOL=ON \
	-DSPHINX_WARNINGS_AS_ERRORS:BOOL=OFF \
	-DLLVM_ENABLE_DOXYGEN:BOOL=OFF \
	-DLLVM_BUILD_LLVM_DYLIB:BOOL=OFF \
	-DLLVM_INSTALL_TOOLCHAIN_ONLY:BOOL=OFF \
	%if "%_lib" == "lib64"
	-DLLVM_LIBDIR_SUFFIX="64" \
	%else
	-DLLVM_LIBDIR_SUFFIX=""
	%endif

ninja -j 1 -vvv -C BUILD

%install
pushd BUILD
cmake -DCMAKE_INSTALL_PREFIX=%buildroot%prefix ../
popd
ninja -C BUILD install

mv %buildroot%_bindir/llvm-config %buildroot/
rm -f %buildroot%_bindir/*
mv %buildroot/llvm-config %buildroot%_bindir/
file %buildroot%_bindir/* | awk -F: '$2~/ELF/{print $1}' | xargs -r chrpath -d
rm -f %buildroot%_libdir/lib*.so*

%files devel-static
%_includedir/*
%_bindir/llvm-config
%_libdir/*.a

%changelog
* Wed May 23 2018 Valery Inozemtsev <shrek@altlinux.ru> 6.0.0-alt1.S1
- 6.0.0
