%global maj_ver 19.1
%global libcxx_version %maj_ver.5
#global rc_ver 4
%global libcxx_srcdir libcxx-%libcxx_version%{?rc_ver:-rc%rc_ver}.src
%global libcxxabi_srcdir libcxxabi-%libcxx_version%{?rc_ver:-rc%rc_ver}.src
%global libunwind_srcdir libunwind-%libcxx_version%{?rc_ver:-rc%rc_ver}.src

Name: libcxx
Version: %libcxx_version%{?rc_ver:~rc%rc_ver}
Release: alt1
Summary: C++ standard library targeting C++11
Group: System/Libraries
License: Apache-2.0 WITH LLVM-exception OR MIT OR NCSA
Url: http://libcxx.llvm.org/
Source0: https://github.com/llvm/llvm-project/releases/download/llvmorg-%libcxx_version%{?rc_ver:-rc%rc_ver}/%libcxx_srcdir.tar.xz
Source2: https://github.com/llvm/llvm-project/releases/download/llvmorg-%libcxx_version%{?rc_ver:-rc%rc_ver}/%libcxxabi_srcdir.tar.xz
Source4: https://github.com/llvm/llvm-project/releases/download/llvmorg-%libcxx_version%{?rc_ver:-rc%rc_ver}/%libunwind_srcdir.tar.xz
Source7: CMakeLists.txt
Source8: https://github.com/llvm/llvm-project/raw/llvmorg-%libcxx_version%{?rc_ver:-rc%rc_ver}/runtimes/cmake/Modules/HandleFlags.cmake
Source9: https://github.com/llvm/llvm-project/raw/llvmorg-%libcxx_version%{?rc_ver:-rc%rc_ver}/runtimes/cmake/Modules/WarningFlags.cmake

Patch0: standalone.patch
# The cmake dependencies for this target are somehow broken upstream.
# However, the libcxx.imp file is only needed for running include-what-you-use.
Patch1: do-not-install-libcxx.imp.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires: clang%{maj_ver} llvm%{maj_ver}-devel llvm%{maj_ver}-cmake-common-modules libstdc++-devel ninja-build
# We need python3-devel for shebang fix
BuildRequires: rpm-build-python3

# For documentation
BuildRequires: python3-module-sphinx

Requires: libcxxabi = %EVR

%description
libc++ is a new implementation of the C++ standard library, targeting C++11.

%package devel
Group: Development/C++
Summary: Headers and libraries for libcxx devel
Requires: %name = %EVR
Requires: libcxxabi-devel

%description devel
%summary.

%package static
Group: System/Libraries
Summary: Static libraries for libcxx

%description static
%summary.

%package -n libcxxabi
Group: System/Libraries
Summary: Low level support for a standard C++ library

%description -n libcxxabi
libcxxabi provides low level support for a standard C++ library.

%package -n libcxxabi-devel
Summary: Headers and libraries for libcxxabi devel
Group: Development/C++
Requires: libcxxabi = %EVR

%description -n libcxxabi-devel
%summary.

%package -n libcxxabi-static
Group: System/Libraries
Summary: Static libraries for libcxxabi

%description -n libcxxabi-static
%summary.

%package -n llvm-libunwind
Group: System/Libraries
Summary: LLVM libunwind

%description -n llvm-libunwind
LLVM libunwind is an implementation of the interface defined by the HP libunwind
project. It was contributed Apple as a way to enable clang++ to port to
platforms that do not have a system unwinder. It is intended to be a small and
fast implementation of the ABI, leaving off some features of HP's libunwind
that never materialized (e.g. remote unwinding).

%package -n llvm-libunwind-devel
Group: Development/Tools
Summary: LLVM libunwind development files
Provides: libunwind(major) = %maj_ver
Requires: llvm-libunwind = %EVR

%description -n llvm-libunwind-devel
Unversioned shared library for LLVM libunwind

%package -n llvm-libunwind-static
Group: System/Libraries
Summary: Static library for LLVM libunwind

%description -n llvm-libunwind-static
%summary.

%package -n llvm-libunwind-doc
Group: Documentation
Summary: libunwind documentation
# doctools.js, searchtools.js and language_data.js are used in the HTML doc
# generated from sphinx-doc under BSD 2-Clause License.
# Source: https://github.com/sphinx-doc/sphinx
License: BSD-2-Clause AND (Apache-2.0 WITH LLVM-exception OR NCSA OR MIT)
BuildArch: noarch

%description -n llvm-libunwind-doc
Documentation for LLVM libunwind

%prep
%setup -T -b 0 -n %libcxx_srcdir
%setup -T -b 2 -n %libcxxabi_srcdir
%setup -T -b 4 -n %libunwind_srcdir
%setup -T -c -n build

cp %SOURCE7 .
mv ../%libcxx_srcdir libcxx
mv ../%libcxxabi_srcdir libcxxabi
mv ../%libunwind_srcdir libunwind
mkdir -p runtimes/cmake/Modules
cp %SOURCE8 %SOURCE9 runtimes/cmake/Modules/
%autopatch -p1

pushd libcxx/utils
subst '/^#!.*python$/s|python$|python3|' $(grep -Rl '#!.*python$' *)
popd

%build
# Copy CFLAGS into ASMFLAGS, so -fcf-protection is used when compiling assembly files.
export ASMFLAGS=$CFLAGS
export ALTWRAP_LLVM_VERSION=%maj_ver
%cmake -GNinja \
	-DCMAKE_C_COMPILER=clang \
	-DCMAKE_CXX_COMPILER=clang++ \
	-DCMAKE_RANLIB:PATH=%_bindir/llvm-ranlib \
	-DCMAKE_AR:PATH=%_bindir/llvm-ar \
	-DCMAKE_NM:PATH=%_bindir/llvm-nm \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_MODULE_PATH="%prefix/lib/llvm-%maj_ver/%_lib/cmake/llvm;%prefix/lib/llvm-%maj_ver/share/cmake/Modules" \
	-DCMAKE_POSITION_INDEPENDENT_CODE=ON \
%if 0%{?_libsuff} == 64
	-DLIBCXX_LIBDIR_SUFFIX:STRING=64 \
	-DLIBCXXABI_LIBDIR_SUFFIX:STRING=64 \
	-DLIBUNWIND_LIBDIR_SUFFIX:STRING=64 \
%endif
	-DLIBCXX_INCLUDE_BENCHMARKS=OFF \
	-DLIBCXX_STATICALLY_LINK_ABI_IN_STATIC_LIBRARY=ON \
	-DLIBCXX_ENABLE_ABI_LINKER_SCRIPT=ON \
	-DLIBCXXABI_USE_LLVM_UNWINDER=OFF \
	-DLLVM_BUILD_DOCS=ON \
	-DLLVM_ENABLE_SPHINX=ON \
	-DLIBUNWIND_INCLUDE_DOCS=ON \
	-DLIBUNWIND_INSTALL_INCLUDE_DIR=%_includedir/llvm-libunwind \
	-DLIBUNWIND_INSTALL_SPHINX_HTML_DIR=%_docdir/html/libunwind

%cmake_build

%install
%cmake_install

# We can't install the unversionned path on default location because that would conflict with
# https://packages.altlinux.org/en/sisyphus/srpms/libunwind/
#
# The versionned path has a different soname (libunwind.so.1 compared to
# libunwind.so.8) so they can live together in %%{_libdir}
#
# ABI wise, even though llvm-libunwind's library is named libunwind, it doesn't
# have the exact same ABI as gcc's libunwind (it actually provides a subset).
rm %buildroot%_libdir/libunwind.so
mkdir -p %buildroot/%_libdir/llvm-unwind/

pushd %buildroot/%_libdir/llvm-unwind
ln -s ../libunwind.so.1.0 libunwind.so
popd

rm %buildroot%_docdir/html/libunwind/.buildinfo

%files
%doc libcxx/LICENSE.TXT libcxx/CREDITS.TXT libcxx/TODO.TXT
%_libdir/libc++.so.*

%files devel
%_includedir/c++
%exclude %_includedir/c++/v1/cxxabi.h
%exclude %_includedir/c++/v1/__cxxabi_config.h
%_libdir/libc++.so
%_libdir/libc++.modules.json
%dir %_datadir/libc++
%_datadir/libc++/v1

%files static
%_libdir/libc++.a
%_libdir/libc++experimental.a

%files -n libcxxabi
%doc libcxxabi/LICENSE.TXT libcxxabi/CREDITS.TXT
%_libdir/libc++abi.so.*

%files -n libcxxabi-devel
%_includedir/c++/v1/cxxabi.h
%_includedir/c++/v1/__cxxabi_config.h
%_libdir/libc++abi.so

%files -n libcxxabi-static
%_libdir/libc++abi.a

%files -n llvm-libunwind
%doc libunwind/LICENSE.TXT
%_libdir/libunwind.so.1
%_libdir/libunwind.so.1.0

%files -n llvm-libunwind-devel
%dir %_includedir/llvm-libunwind
%_includedir/llvm-libunwind/__libunwind_config.h
%_includedir/llvm-libunwind/libunwind.h
%_includedir/llvm-libunwind/libunwind.modulemap
%dir %_includedir/llvm-libunwind/mach-o
%_includedir/llvm-libunwind/mach-o/compact_unwind_encoding.h
%_includedir/llvm-libunwind/unwind.h
%_includedir/llvm-libunwind/unwind_arm_ehabi.h
%_includedir/llvm-libunwind/unwind_itanium.h
%dir %_libdir/llvm-unwind
%_libdir/llvm-unwind/libunwind.so

%files -n llvm-libunwind-static
%_libdir/libunwind.a

%files -n llvm-libunwind-doc
%doc libunwind/LICENSE.TXT
%_docdir/html/libunwind

%changelog
* Thu Dec 19 2024 L.A. Kostis <lakostis@altlinux.ru> 19.1.5-alt1
- Rebuild for ALTLinux.
- spec based on libcxx-19.1.5-1.fc42.
