%define        _unpackaged_files_terminate_build 1
%define        oname aws-c-s3

Name:          lib%oname
Version:       0.4.9
Release:       alt1
Group:         Development/C
Summary:       C99 library implementation for communicating with the S3 service
License:       Apache-2.0
Url:           https://github.com/awslabs/aws-c-s3
Vcs:           https://github.com/awslabs/aws-c-s3.git

Source:        %name-%version.tar
Patch:         path.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: libaws-c-common-devel
BuildRequires: libaws-c-auth-devel
BuildRequires: libaws-checksums-devel

%description
C99 library implementation for communicating with the S3 service, designed for
maximizing throughput on high bandwidth EC2 instances.


%package       devel
Group:         Development/C
Summary:       C99 library implementation for communicating with the S3 service development files
Requires:      /proc
Requires:      cmake
Requires:      libaws-c-common-devel
Requires:      libaws-c-auth-devel
Requires:      libaws-checksums-devel

%description   devel
Development headers and libraries for %oname.

C99 library implementation for communicating with the S3 service, designed for
maximizing throughput on high bandwidth EC2 instances.


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
%cmake_insource \
   -DCMAKE_MODULE_PATH=%_libdir/cmake \
   -DBUILD_SHARED_LIBS=ON \
   -DBUILD_TESTING=ON

%cmake_build

%install
%cmakeinstall_std

%check
#%make test


%files
%doc README*
%_libdir/%name.so.*

%files         devel
%doc README*
%_libdir/%name.so
%_libdir/cmake/%oname
%_includedir/aws/s3

%files         -n s3
%_bindir/s3


%changelog
* Wed Jan 03 2024 Pavel Skrylev <majioa@altlinux.org> 0.4.9-alt1
- Initial build v0.4.9 for Sisyphus
