%def_with bootstrap

Name: libcxxabi
Version: 5.0.0
Release: alt1

Summary: Low level support for a standard C++ library

License: MIT or NCSA
Group: System/Libraries
Url: http://libcxxabi.llvm.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://llvm.org/releases/%version/libcxxabi-%version.src.tar.xz
Source: %name-%version.tar

BuildRequires: clang4.0 llvm4.0-devel cmake llvm4.0-devel-static
BuildRequires: libcxx-devel >= %version

%if_with bootstrap
# make cmake compiler test happy
BuildRequires: libstdc++-devel
%endif

%description
libcxxabi provides low level support for a standard C++ library.

%package devel
Summary: Headers and libraries for libcxxabi devel
Requires: %name = %EVR
Group: System/Libraries

%description devel
%summary.

%package static
Summary: Static libraries for libcxxabi
Group: System/Libraries
Requires: %name-devel = %EVR

%description static
%summary.

%prep
%setup

# TODO: macro
%__subst 's|${LLVM_BINARY_DIR}/share/llvm/cmake|%_datadir/cmake/Modules/llvm|g' CMakeLists.txt

%build
%ifarch armv7hl
# disable ARM exception handling
%__subst 's|LIBCXXABI_ARM_EHABI 1|LIBCXXABI_ARM_EHABI 0|g' include/__cxxabi_config.h
%endif

%if_with bootstrap
export LDFLAGS="-Wl,--build-id"
%else
export LDFLAGS="-Wl,--build-id -stdlib=libc++"
%endif

%cmake \
	-DCMAKE_C_COMPILER=%_bindir/clang \
	-DCMAKE_CXX_COMPILER=%_bindir/clang++ \
	-DLLVM_CONFIG=%_bindir/llvm-config \
	-DCMAKE_CXX_FLAGS="-std=c++11" \
	-DLIBCXXABI_LIBCXX_INCLUDES=%_includedir/c++/v1/ \
%if %{_lib} == "lib64"
	-DLIBCXXABI_LIBDIR_SUFFIX:STRING=64 \
%endif
	-DCMAKE_BUILD_TYPE=RelWithDebInfo

%cmake_build

%install
%cmakeinstall_std

mkdir -p %buildroot%_includedir/
cp -a include/* %buildroot%_includedir

%files
%doc LICENSE.TXT
%doc CREDITS.TXT
%_libdir/libc++abi.so.*

%files devel
%_includedir/*.h
%_libdir/libc++abi.so

%files static
%_libdir/libc++abi.a

%changelog
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
