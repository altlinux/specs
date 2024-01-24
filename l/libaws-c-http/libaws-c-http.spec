%define        _unpackaged_files_terminate_build 1
%define        oname aws-c-http

Name:          lib%oname
Version:       0.8.0
Release:       alt1
Group:         Development/C
Summary:       C99 implementation of the HTTP/1.1 and HTTP/2 specifications
License:       Apache-2.0
Url:           https://github.com/awslabs/aws-c-common
Vcs:           https://github.com/awslabs/aws-c-common.git

Source:        %name-%version.tar
Patch:         path.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: libaws-c-common-devel
BuildRequires: libaws-c-cal-devel
BuildRequires: libaws-c-io-devel
BuildRequires: libaws-c-compression-devel
BuildRequires: libs2n-devel

%description
C99 implementation of the HTTP/1.1 and HTTP/2 specifications.


%package       devel
Group:         Development/C
Summary:       C99 implementation of the HTTP/1.1 and HTTP/2 development files
Requires:      cmake
Requires:      libaws-c-common-devel
Requires:      libaws-c-cal-devel
Requires:      libaws-c-io-devel
Requires:      libaws-c-compression-devel
Requires:      libs2n-devel

%description   devel
C99 implementation of the HTTP/1.1 and HTTP/2 development files.

C99 implementation of the HTTP/1.1 and HTTP/2 specifications.


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
   -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmakeinstall_std


%files
%doc README*
%_libdir/%name.so.*

%files         devel
%doc README*
%_libdir/%name.so
%_libdir/cmake/%oname
%_includedir/aws/http

%files         -n elasticurl
%_bindir/elasticurl


%changelog
* Tue Jan 02 2024 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- Initial build v0.8.0 for Sisyphus
