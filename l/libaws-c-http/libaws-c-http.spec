%def_disable   check
%def_enable    devel
%{?!_disable_devel:%define _unpackaged_files_terminate_build 1}
%define        nomen aws-c-http

Name:          lib%nomen
Version:       1.0.0
Release:       alt1
Group:         Development/C
Summary:       C99 implementation of the HTTP/1.1 and HTTP/2 specifications
License:       Apache-2.0
Url:           https://github.com/awslabs/aws-c-common
Vcs:           https://github.com/awslabs/aws-c-common.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-cmake
%{?!_disable_check:BuildRequires: ctest}
BuildRequires: cmake
BuildRequires: clang-tools
BuildRequires: cmake(aws-c-common)
BuildRequires: cmake(aws-c-cal)
BuildRequires: cmake(aws-c-io)
BuildRequires: cmake(aws-c-compression)
BuildRequires: cmake(s2n)

%description
C99 implementation of the HTTP/1.1 and HTTP/2 specifications.


%if_enabled    devel
%package       devel
Group:         Development/C
Summary:       C99 implementation of the HTTP/1.1 and HTTP/2 development files
Requires:      ctest
Requires:      cmake
Requires:      clang-tools
Requires:      cmake(aws-c-common)
Requires:      cmake(aws-c-cal)
Requires:      cmake(aws-c-io)
Requires:      cmake(aws-c-compression)
Requires:      cmake(s2n)

%description   devel
C99 implementation of the HTTP/1.1 and HTTP/2 development files.

C99 implementation of the HTTP/1.1 and HTTP/2 specifications.
%endif


%package       -n elasticurl
Group:         Development/C
Summary:       C99 implementation of the HTTP/1.1 and HTTP/2 elastic url executable

%description   -n elasticurl
C99 implementation of the HTTP/1.1 and HTTP/2 elastic url executable.

C99 implementation of the HTTP/1.1 and HTTP/2 specifications.


%prep
%setup
%autopatch

%build
%cmake \
   -DCMAKE_MODULE_PATH=%_libdir/cmake \
   -DCMAKE_PREFIX_PATH=%_usr \
   -DBUILD_SHARED_LIBS=ON \
   -DCMAKE_C_COMPILER=clang \
%if_enabled check
   -DENABLE_PROXY_INTEGRATION_TESTS=ON \
   -DENABLE_LOCALHOST_INTEGRATION_TESTS=ON \
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
%_includedir/aws/http
%endif

%files         -n elasticurl
%_bindir/elasticurl
%_bindir/h2benchmark


%changelog
* Wed Oct 07 2026 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- ^ 0.8.0 -> 1.0.0

* Tue Jan 02 2024 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- Initial build v0.8.0 for Sisyphus
