# If you need to bootstrap this, turn this on.
# Otherwise, you have a loop with libcxxabi
%def_with bootstrap

Name: libcxx
Version: 5.0.0
Release: alt1

Summary: C++ standard library targeting C++11

License: MIT or NCSA
Group: System/Libraries
Url: http://libcxx.llvm.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://llvm.org/releases/%version/libcxx-%version.src.tar.xz
Source: %name-%version.tar

BuildRequires: clang4.0 llvm4.0-devel cmake llvm4.0-devel-static

%if_with bootstrap
%add_verify_elf_skiplist %_libdir/libc++.so.1.0
# make cmake compiler test happy
BuildRequires: libstdc++-devel
%else
BuildRequires: libcxxabi-devel
BuildRequires: python3
%endif

%description
libc++ is a new implementation of the C++ standard library, targeting C++11.

%package devel
Summary: Headers and libraries for libcxx devel
Requires: %name = %EVR
Group: System/Libraries
%if_without bootstrap
Requires: libcxxabi-devel
%endif

%description devel
%summary.

%package static
Group: System/Libraries
Summary: Static libraries for libcxx
Requires: %name-devel = %EVR

%description static
%summary.

%prep
%setup

%build

%if_with bootstrap
export LDFLAGS="-Wl,--build-id"
%else
export LDFLAGS="-Wl,--build-id -stdlib=libc++"
%endif
# Clang in older releases than f24 can't build this code without crashing.
# So, we use gcc there. But the really old version in RHEL 6 works. Huh.
%cmake \
	-DCMAKE_C_COMPILER=%_bindir/clang \
	-DCMAKE_CXX_COMPILER=%_bindir/clang++ \
	-DLLVM_CONFIG=%_bindir/llvm-config \
%if_without bootstrap
	-DLIBCXX_CXX_ABI=libcxxabi \
	-DLIBCXX_CXX_ABI_INCLUDE_PATHS=%_includedir \
	-DPYTHONINTERP_FOUND=ON \
	-DPYTHON_EXECUTABLE=%_bindir/python3 \
	-DLIBCXX_ENABLE_ABI_LINKER_SCRIPT=ON \
%endif
%if %_lib == "lib64"
	-DLIBCXX_LIBDIR_SUFFIX:STRING=64 \
%endif
	-DCMAKE_BUILD_TYPE=RelWithDebInfo

%cmake_build

%install
%cmakeinstall_std

%files
%doc LICENSE.TXT
%doc CREDITS.TXT TODO.TXT
%_libdir/libc++.so.*

%files devel
%_includedir/c++/
%_libdir/libc++.so

%files static
%doc LICENSE.TXT
%_libdir/libc++*.a

%changelog
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
