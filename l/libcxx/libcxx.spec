# If you need to bootstrap this, turn this on.
# Otherwise, you have a loop with libcxxabi
%def_with bootstrap

%define optflags_lto -flto=thin
%define so_ver 1
%define llvm_ver 12

Name: libcxx
Version: 12.0.1
Release: alt1

Summary: C++ standard library targeting C++11

License: MIT or NCSA
Group: System/Libraries
Url: https://%name.llvm.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

ExcludeArch: %arm

# https://github.com/llvm/llvm-project/releases/download/llvmorg-%version/%name-%version.src.tar.xz
Source: %name-%version.src.tar

Patch0: %name-remove-monorepo-requirement.patch

BuildRequires: clang%llvm_ver.0
BuildRequires: cmake
BuildRequires: llvm%llvm_ver.0-devel
BuildRequires: ninja-build
BuildRequires: python3

%if_with bootstrap
%add_verify_elf_skiplist %_libdir/libc++.so.1.0
# make cmake compiler test happy
BuildRequires: libstdc++-devel
%else
BuildRequires: libc++-devel
BuildRequires: libc++abi-devel
%endif

%description
libc++ is a new implementation of the C++ standard library, targeting C++11.

%package -n libc++%so_ver
Summary: %summary
Group: System/Libraries
Provides: %name = %EVR
Obsoletes: %name <= 7.0.0-alt1

%description -n libc++%so_ver
libc++ is a new implementation of the C++ standard library, targeting C++11.

%package -n libc++-devel
Summary: Headers and libraries for libcxx devel
Group: Development/C++
Requires: libc++%so_ver = %EVR
%if_without bootstrap
Requires: libc++abi-devel
%endif
Provides: %name-devel = %EVR
Obsoletes: %name-devel <= 7.0.0-alt1

%description -n libc++-devel
%summary.

%package -n libc++-devel-static
Group: Development/C++
Summary: Static libraries for %name
Requires: libc++-devel = %EVR
Provides: %name-static = %EVR
Obsoletes: %name-static <= 7.0.0-alt1

%description -n libc++-devel-static
%summary.

%prep
%setup -n %name-%version.src
%patch0 -p2

%build

%if_with bootstrap
export LDFLAGS="-Wl,--build-id"
%else
export LDFLAGS="-Wl,--build-id -stdlib=libc++ -lc++abi"
%endif
%cmake \
	-DCMAKE_C_COMPILER:PATH="clang-%llvm_ver" \
	-DCMAKE_CXX_COMPILER:PATH=%_bindir/clang++-%llvm_ver \
%if_without bootstrap
	-DLIBCXX_CXX_ABI=libcxxabi \
	-DLIBCXX_CXX_ABI_INCLUDE_PATHS=%_includedir \
	-DLIBCXX_ENABLE_ABI_LINKER_SCRIPT:BOOL=TRUE \
%endif
%if %_lib == "lib64"
	-DLIBCXX_LIBDIR_SUFFIX:STRING=64 \
%endif
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-GNinja

%cmake_build

%install
%cmake_install

# Install header files that libcxxabi needs
%__mkdir_p %buildroot%_includedir/%name-internal
%__install -m 0644 src/include/* %buildroot%_includedir/%name-internal/

%files -n libc++%so_ver
%doc LICENSE.TXT CREDITS.TXT TODO.TXT
%_libdir/libc++.so.*

%files -n libc++-devel
%_includedir/c++
%_includedir/%name-internal
%_libdir/libc++.so

%files -n libc++-devel-static
%_libdir/libc++*.a

%changelog
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
- initial build for ALT Sisyphus

* Fri Sep  8 2017 Tom Callaway <spot@fedoraproject.org> - 5.0.0-1
- update to 5.0.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Tom Callaway <spot@fedoraproject.org> - 4.0.1-1
- update to 4.0.1

* Sat Apr 22 2017 Tom Callaway <spot@fedoraproject.org> - 4.0.0-1
- update to 4.0.0

* Wed Mar  8 2017 Tom Callaway <spot@fedoraproject.org> - 3.9.1-1
- update to 3.9.1

* Fri Mar  3 2017 Tom Callaway <spot@fedoraproject.org> - 3.9.0-4
- LIBCXX_ENABLE_ABI_LINKER_SCRIPT=ON

* Wed Mar  1 2017 Tom Callaway <spot@fedoraproject.org> - 3.9.0-3
- disable bootstrap

* Tue Feb 21 2017 Dan Horák <dan[at]danny.cz> - 3.9.0-2
- apply s390(x) workaround only in Fedora < 26

* Mon Feb 20 2017 Tom Callaway <spot@fedoraproject.org> - 3.9.0-1
- update to 3.9.0 (match clang)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 26 2016 Tom Callaway <spot@fedoraproject.org> - 3.8.1-1
- update to 3.8.1

* Thu Jun 09 2016 Dan Horák <dan[at]danny.cz> - 3.8.0-4
- exclude Power only in EPEL
- default to z10 on s390(x)

* Thu May 19 2016 Tom Callaway <spot@fedoraproject.org> - 3.8.0-3
- use gcc on el7, fedora < 24. use clang on el6 and f24+
  MAGIC.
- bootstrap on

* Tue May 3 2016 Tom Callaway <spot@fedoraproject.org> - 3.8.0-2
- bootstrap off

* Tue May 3 2016 Tom Callaway <spot@fedoraproject.org> - 3.8.0-1
- initial package
- bootstrap on
