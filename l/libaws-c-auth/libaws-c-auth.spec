%def_disable   check
%def_enable    devel
%if_enabled    devel
%define _unpackaged_files_terminate_build 1
%endif
%define        oname aws-c-auth

Name:          lib%oname
Version:       1.0.0
Release:       alt1
Group:         Development/C
Summary:       C99 library implementation of AWS client-side authentication
License:       Apache-2.0
Url:           https://github.com/awslabs/aws-c-auth
Vcs:           https://github.com/awslabs/aws-c-auth.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-cmake
%{?!_disable_check:BuildRequires: ctest}
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: clang-tools
BuildRequires: cmake(aws-c-common)
BuildRequires: cmake(aws-c-sdkutils)
BuildRequires: cmake(aws-c-cal)
BuildRequires: cmake(aws-c-http)

%description
C99 library implementation of AWS client-side authentication: standard
credentials providers and signing.


%if_enabled    devel
%package       devel
Group:         Development/C
Summary:       C99 library implementation of AWS client-side authentication development files
Requires:      ctest
Requires:      cmake
Requires:      clang-tools
Requires:      cmake(aws-c-common)
Requires:      cmake(aws-c-sdkutils)
Requires:      cmake(aws-c-cal)
Requires:      cmake(aws-c-http)

%description   devel
Development headers and libraries for %oname.

C99 library implementation of AWS client-side authentication: standard
credentials providers and signing.
%endif


%prep
%setup
%autopatch

%build
%cmake \
%{?!_disable_check:-DBUILD_TESTING=ON} \
   -DCMAKE_MODULE_PATH=%_libdir/cmake \
   -DCMAKE_PREFIX_PATH=%_usr \
   -DCMAKE_C_COMPILER=clang \
   -DBUILD_RELOCATABLE_BINARIES=ON \
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
%_libdir/cmake/%oname
%_includedir/aws/auth
%endif


%changelog
* Wed Oct 07 2026 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- ^ 0.7.11 -> 1.0.0

* Wed Jan 03 2024 Pavel Skrylev <majioa@altlinux.org> 0.7.11-alt1
- Initial build v0.7.11 for Sisyphus
