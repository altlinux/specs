%def_enable    check
%def_enable    devel
%{?!_disable_check:%define _unpackaged_files_terminate_build 1}
%define        nomen aws-c-cal

Name:          lib%nomen
Version:       1.0.0
Release:       alt1
Group:         Development/C
Summary:       Aws Crypto Abstraction Layer
License:       Apache-2.0
Url:           https://github.com/awslabs/aws-c-cal
Vcs:           https://github.com/awslabs/aws-c-cal.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-cmake
%{?!_disable_check:BuildRequires: ctest}
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: clang-tools
BuildRequires: pkgconfig(libssl)
BuildRequires: cmake(aws-c-common)

%description
Aws Crypto Abstraction Layer: Cross-Platform, C99 wrapper for cryptography
primitives.


%if_enabled    devel
%package       devel
Group:         Development/C
Summary:       Aws Crypto Abstraction Layer development files
Requires:      ctest
Requires:      cmake
Requires:      clang-tools
Requires:      pkgconfig(libssl)
Requires:      cmake(aws-c-common)

%description   devel
Development headers and libraries for %nomen.

Aws Crypto Abstraction Layer: Cross-Platform, C99 wrapper for cryptography
primitives.
%endif


%prep
%setup

%build
%cmake \
%{?!_disable_check:-DBUILD_TESTING=ON} \
   -DCMAKE_MODULE_PATH=%_libdir/cmake \
   -DCMAKE_PREFIX_PATH=%_usr \
   -DBUILD_SHARED_LIBS=ON \
   %nil
%cmake_build

%install
%cmakeinstall_std

%check
%ctest


%files
%doc README*
%_libdir/%name.so.*

%if_enabled    devel
%files         devel
%doc README*
%_libdir/%name.so
%_libdir/cmake/%nomen
%_includedir/aws/cal
%endif


%changelog
* Tue Oct 06 2026 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- ^ 0.6.9 -> 1.0.0
- * rebased to upstream git flow

* Wed Jan 03 2024 Pavel Skrylev <majioa@altlinux.org> 0.6.9-alt1
- Initial build for Sisyphus
