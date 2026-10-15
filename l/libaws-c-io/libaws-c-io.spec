%def_disable   check
%def_enable    devel
%{?!_disable_devel:%define _unpackaged_files_terminate_build 1}
%define        nomen aws-c-io

Name:          lib%nomen
Version:       1.0.0
Release:       alt1
Group:         Development/C
Summary:       This is a module for the AWS SDK for C
License:       Apache-2.0
Url:           https://github.com/awslabs/aws-c-io
Vcs:           https://github.com/awslabs/aws-c-io.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-cmake
%{?!_disable_check:BuildRequires: ctest}
BuildRequires: cmake
BuildRequires: clang
BuildRequires: pkgconfig(libssl)
BuildRequires: cmake(s2n)
BuildRequires: cmake(aws-c-common)
BuildRequires: cmake(aws-c-cal)

%description
This is a module for the AWS SDK for C. It handles all IO and TLS work for
application protocols.


%if_enabled    devel
%package       devel
Group:         Development/C
Summary:       This is a module for the AWS SDK for C development files
Requires:      ctest
Requires:      cmake
Requires:      clang
Requires:      pkgconfig(libssl)
Requires:      cmake(s2n)
Requires:      cmake(aws-c-common)
Requires:      cmake(aws-c-cal)


%description   devel
Development headers and libraries for %nomen.

This is a module for the AWS SDK for C. It handles all IO and TLS work for
application protocols.
%endif


%prep
%setup
%autopatch

%build
%cmake \
   -DCMAKE_MODULE_PATH=%_libdir/cmake \
   -DCMAKE_PREFIX_PATH=%_usr \
   -DCMAKE_C_COMPILER=clang \
   -DBUILD_SHARED_LIBS=ON \
   -DAWS_USE_SECITEM=ON \
   -DBUILD_RELOCATABLE_BINARIES=ON \
   -DBYO_CRYPTO=OFF \
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
%_includedir/aws/io
%_includedir/aws/testing
%endif


%changelog
* Tue Oct 06 2026 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- ^ 0.14.0 -> 1.0.0
- * rebased to upstream git flow

* Tue Jan 02 2024 Pavel Skrylev <majioa@altlinux.org> 0.14.0-alt1
- Initial build v0.14.0 for Sisyphus
