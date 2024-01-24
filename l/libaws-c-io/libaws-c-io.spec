%define        _unpackaged_files_terminate_build 1
%define        oname aws-c-io

Name:          lib%oname
Version:       0.14.0
Release:       alt1
Group:         Development/C
Summary:       This is a module for the AWS SDK for C
License:       Apache-2.0
Url:           https://github.com/awslabs/aws-c-io
Vcs:           https://github.com/awslabs/aws-c-io.git

Source:        %name-%version.tar
Patch:         path.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: libssl-devel
BuildRequires: libs2n-devel
BuildRequires: libaws-c-common-devel
BuildRequires: libaws-c-cal-devel

%description
This is a module for the AWS SDK for C. It handles all IO and TLS work for
application protocols.


%package       devel
Group:         Development/C
Summary:       This is a module for the AWS SDK for C development files
Requires:      %name = %EVR
Requires:      cmake

%description   devel
Development headers and libraries for %oname.

This is a module for the AWS SDK for C. It handles all IO and TLS work for
application protocols.


%prep
%setup
%autopatch

%build
%cmake_insource \
   -DCMAKE_MODULE_PATH=%_libdir/cmake \
   -DBUILD_SHARED_LIBS=ON

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
%_includedir/aws/io
%_includedir/aws/testing


%changelog
* Tue Jan 02 2024 Pavel Skrylev <majioa@altlinux.org> 0.14.0-alt1
- Initial build v0.14.0 for Sisyphus
