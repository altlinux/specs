%def_with bootstrap

%define optflags_lto -flto=thin
%define so_ver 1
%define llvm_ver 12.0

Name: libcxxabi
Version: 12.0.1
Release: alt3

Summary: Low level support for a standard C++ library

License: MIT or NCSA
Group: System/Libraries
Url: https://libcxxabi.llvm.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# https://github.com/llvm/llvm-project/releases/download/llvmorg-%version/%name-%version.src.tar.xz
Source: %name-%version.src.tar

Patch0: %name-include-refstring.h-from-system-incl.patch
Patch1: %name-remove-monorepo-requirement.patch

BuildRequires: clang%llvm_ver
BuildRequires: cmake
BuildRequires: libc++-devel >= %version
# make cmake compiler test happy
BuildRequires: libstdc++-devel
BuildRequires: llvm%llvm_ver-devel
BuildRequires: ninja-build
BuildRequires: python3

%description
libcxxabi provides low level support for a standard C++ library.

%package -n libc++abi%so_ver
Summary: %summary
Group: System/Libraries
Provides: %name = %EVR
Obsoletes: %name <= 7.0.0-alt1

%description -n libc++abi%so_ver
libcxxabi provides low level support for a standard C++ library.

%package -n libc++abi-devel
Summary: Headers and libraries for libcxxabi devel
Group: Development/C++
Requires: libc++abi%so_ver = %EVR
Provides: %name-devel = %EVR
Obsoletes: %name-devel <= 7.0.0-alt1

%description -n libc++abi-devel
%summary.

%package -n libc++abi-devel-static
Summary: Static libraries for libcxxabi
Group: Development/C++
Requires: libc++abi-devel = %EVR
Provides: %name-static = %EVR
Obsoletes: %name-static <= 7.0.0-alt1

%description -n libc++abi-devel-static
%summary.

%prep
%setup -n %name-%version.src
%patch0 -p2
%patch1 -p2

%build
export ALTWRAP_LLVM_VERSION=%llvm_ver

%ifarch %arm
# disable ARM exception handling
%__subst 's|LIBCXXABI_ARM_EHABI 1|LIBCXXABI_ARM_EHABI 0|g' include/__cxxabi_config.h
%endif

%if_with bootstrap
export LDFLAGS="-Wl,--build-id"
%else
export LDFLAGS="-Wl,--build-id -stdlib=libc++"
%endif

%cmake \
	-DCMAKE_C_COMPILER:STRING=clang \
	-DCMAKE_CXX_COMPILER:STRING=clang++ \
	-DCMAKE_RANLIB:PATH=%_bindir/llvm-ranlib \
	-DCMAKE_AR:PATH=%_bindir/llvm-ar \
	-DCMAKE_NM:PATH=%_bindir/llvm-nm \
	-DCMAKE_EXE_LINKER_FLAGS:STRING="-fuse-ld=lld" \
	-DCMAKE_CXX_FLAGS:STRING="-std=c++11" \
	-DLIBCXXABI_LIBCXX_INCLUDES:PATH=%_includedir/c++/v1 \
%if %_lib == "lib64"
	-DLIBCXXABI_LIBDIR_SUFFIX:STRING=64 \
%endif
	-DCMAKE_BUILD_TYPE:SRING=RelWithDebInfo \
	-GNinja

%cmake_build

%install
%cmake_install

%__mkdir_p %buildroot%_includedir
%__cp -a include/* %buildroot%_includedir

%files -n libc++abi%so_ver
%doc LICENSE.TXT CREDITS.TXT
%_libdir/libc++abi.so.*

%files -n libc++abi-devel
%_includedir/*.h
%_libdir/libc++abi.so

%files -n libc++abi-devel-static
%_libdir/libc++abi.a

%changelog
* Sun Jan 09 2022 Nazarov Denis <nenderus@altlinux.org> 12.0.1-alt3
- Fix BR

* Sun Jan 09 2022 Nazarov Denis <nenderus@altlinux.org> 12.0.1-alt2
- Set ALTWRAP_LLVM_VERSION to select correct LLVM version
- Use LLVM Linker
- Build on ARM

* Sat Jan 08 2022 Nazarov Denis <nenderus@altlinux.org> 12.0.1-alt1
- Version 12.0.1

* Sat Nov 24 2018 Vitaly Lipatov <lav@altlinux.ru> 7.0.0-alt1
- new version 7.0.0 (with rpmrb script)

* Sat Jul 07 2018 Vitaly Lipatov <lav@altlinux.ru> 6.0.1-alt1
- new version 6.0.1 (with rpmrb script)

* Tue May 15 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.0.0-alt1
- Updated to upstream version 6.0.0.

* Tue Jan 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.0-alt2
- Removed unsupported compiler flags.

* Wed Dec 20 2017 Vitaly Lipatov <lav@altlinux.ru> 5.0.0-alt1
- new version (5.0.0) with rpmgs script

* Wed Dec 20 2017 Vitaly Lipatov <lav@altlinux.ru> 4.0.1-alt1
- initial build for ALT Sisyphus

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Tom Callaway <spot@fedoraproject.org> - 4.0.1-1
- update to 4.0.1

* Sat Apr 22 2017 Tom Callaway <spot@fedoraproject.org> - 4.0.0-1
- update to 4.0.0

* Mon Feb 20 2017 Tom Callaway <spot@fedoraproject.org> - 3.9.0-1
- update to 3.9.0
- apply fixes from libcxx

* Wed Sep  7 2016 Tom Callaway <spot@fedoraproject.org> - 3.8.1-1
- update to 3.8.1

* Mon Jul 25 2016 Tom Callaway <spot@fedoraproject.org> - 3.8.0-2
- make static subpackage

* Tue May 3 2016 Tom Callaway <spot@fedoraproject.org> - 3.8.0-1
- initial package
