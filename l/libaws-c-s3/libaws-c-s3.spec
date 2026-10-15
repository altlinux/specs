%def_disable   check
%def_enable    devel
%{?!_disable_devel:%define _unpackaged_files_terminate_build 1}
%define        nomen aws-c-s3

Name:          lib%nomen
Version:       1.3.0
Release:       alt1
Group:         Development/C
Summary:       C99 library implementation for communicating with the S3 service
License:       Apache-2.0
Url:           https://github.com/awslabs/aws-c-s3
Vcs:           https://github.com/awslabs/aws-c-s3.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-cmake
%{?!_disable_check:BuildRequires: ctest}
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: clang
BuildRequires: cmake(aws-c-common)
BuildRequires: cmake(aws-c-auth)
BuildRequires: cmake(aws-checksums)

%description
C99 library implementation for communicating with the S3 service, designed for
maximizing throughput on high bandwidth EC2 instances.


%if_enabled    devel
%package       devel
Group:         Development/C
Summary:       C99 library implementation for communicating with the S3 service development files
Requires:      ctest
Requires:      cmake
Requires:      clang
Requires:      cmake(aws-c-common)
Requires:      cmake(aws-c-auth)
Requires:      cmake(aws-checksums)

%description   devel
Development headers and libraries for %nomen.

C99 library implementation for communicating with the S3 service, designed for
maximizing throughput on high bandwidth EC2 instances.
%endif


%package       -n s3
Group:         Development/C
Summary:       C99 library implementation for communicating with the S3 service executables

%description   -n s3
C99 library implementation for communicating with the S3 service executables.

C99 library implementation for communicating with the S3 service, designed for
maximizing throughput on high bandwidth EC2 instances.


%prep
%setup
%autopatch

%build
%cmake \
   -DCMAKE_MODULE_PATH=%_libdir/cmake \
   -DCMAKE_PREFIX_PATH=%_usr \
   -DCMAKE_C_COMPILER=clang \
   -DBUILD_SHARED_LIBS=ON \
   -DASSERT_LOCK_HELD=ON \
   -DAWS_ENABLE_S3_ENDPOINT_RESOLVER=ON \
%if_enabled check
   -DBUILD_TESTING=ON \
   -DENABLE_MOCK_SERVER_TESTS=ON \
   -DENABLE_MRAP_TESTS=ON \
%endif
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
%_includedir/aws/s3
%endif

%files         -n s3
%_bindir/s3


%changelog
* Wed Oct 07 2026 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- ^ 0.4.9 -> 1.3.0

* Wed Jan 03 2024 Pavel Skrylev <majioa@altlinux.org> 0.4.9-alt1
- Initial build v0.4.9 for Sisyphus
