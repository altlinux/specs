%def_disable   check
%def_enable    devel
%{?!_disable_devel:%define _unpackaged_files_terminate_build 1}
%define        nomen aws-checksums

Name:          lib%nomen
Version:       1.0.1
Release:       alt1
Group:         Development/C
Summary:       Cross-Platform HW accelerated CRC32c and CRC32 with fallback to efficient SW implementations
License:       Apache-2.0
Url:           https://github.com/awslabs/aws-checksums
Vcs:           https://github.com/awslabs/aws-checksums.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-cmake
%{?!_disable_check:BuildRequires: ctest}
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: clang-tools
BuildRequires: cmake(aws-c-common)

%description
Cross-Platform HW accelerated CRC32c and CRC32 with fallback to efficient SW
implementations. C interface with language bindings for each of our SDKs.


%if_enabled    devel
%package       devel
Group:         Development/C
Summary:       Cross-Platform HW accelerated CRC32c and CRC32 with fallback to efficient SW implementations development files
Requires:      ctest
Requires:      cmake
Requires:      clang-tools
Requires:      cmake(aws-c-common)

%description   devel
Development headers and libraries for %nomen.

Cross-Platform HW accelerated CRC32c and CRC32 with fallback to efficient SW
implementations. C interface with language bindings for each of our SDKs.
%endif


%package       -n checksum-profile
Group:         Development/C
Summary:       Cross-Platform HW accelerated CRC32c and CRC32 with fallback to efficient SW implementations executable

%description   -n checksum-profile
Executables for %nomen.

Cross-Platform HW accelerated CRC32c and CRC32 with fallback to efficient SW
implementations. C interface with language bindings for each of our SDKs.


%prep
%setup
%autopatch

%build
%cmake \
%{?!_disable_check:-DBUILD_TESTING=ON} \
   -DCMAKE_MODULE_PATH=%_libdir/cmake \
   -DCMAKE_PREFIX_PATH=%_usr \
   -DCMAKE_C_COMPILER=clang \
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
%_includedir/aws/checksums
%endif

%files         -n checksum-profile
%doc README*
%_bindir/checksum-profile

%changelog
* Wed Oct 07 2026 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- ^ 0.1.17 -> 1.0.1

* Wed Jan 03 2024 Pavel Skrylev <majioa@altlinux.org> 0.1.17-alt1
- Initial build v0.1.17 for Sisyphus
