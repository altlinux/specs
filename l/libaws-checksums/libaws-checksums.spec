%define        _unpackaged_files_terminate_build 1
%define        oname aws-checksums

Name:          lib%oname
Version:       0.1.17
Release:       alt1
Group:         Development/C
Summary:       Cross-Platform HW accelerated CRC32c and CRC32 with fallback to efficient SW implementations
License:       Apache-2.0
Url:           https://github.com/awslabs/aws-checksums
Vcs:           https://github.com/awslabs/aws-checksums.git

Source:        %name-%version.tar
Patch:         path.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: libaws-c-common-devel

%description
Cross-Platform HW accelerated CRC32c and CRC32 with fallback to efficient SW
implementations. C interface with language bindings for each of our SDKs.


%package       devel
Group:         Development/C
Summary:       Cross-Platform HW accelerated CRC32c and CRC32 with fallback to efficient SW implementations development files

%description   devel
Development headers and libraries for %oname.

Cross-Platform HW accelerated CRC32c and CRC32 with fallback to efficient SW
implementations. C interface with language bindings for each of our SDKs.


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
%make test


%files
%doc README*
%_libdir/%name.so.*

%files         devel
%doc README*
%_libdir/%name.so
%_libdir/cmake/%oname
%_includedir/aws/checksums


%changelog
* Wed Jan 03 2024 Pavel Skrylev <majioa@altlinux.org> 0.1.17-alt1
- Initial build v0.1.17 for Sisyphus
