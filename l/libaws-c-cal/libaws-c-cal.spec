%define        _unpackaged_files_terminate_build 1
%define        oname aws-c-cal

Name:          lib%oname
Version:       0.6.9
Release:       alt1
Group:         Development/C
Summary:       Aws Crypto Abstraction Layer
License:       Apache-2.0
Url:           https://github.com/awslabs/aws-c-cal
Vcs:           https://github.com/awslabs/aws-c-cal.git

Source:        %name-%version.tar
Patch:         path.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-ninja-build
BuildRequires: cmake
BuildRequires: libssl-devel
BuildRequires: libaws-c-common-devel

%description
Aws Crypto Abstraction Layer: Cross-Platform, C99 wrapper for cryptography
primitives.


%package       devel
Group:         Development/C
Summary:       Aws Crypto Abstraction Layer development files
Requires:      cmake
Requires:      libssl-devel
Requires:      libaws-c-common-devel

%description   devel
Development headers and libraries for %oname.

Aws Crypto Abstraction Layer: Cross-Platform, C99 wrapper for cryptography
primitives.


%package       -n x-platform-fuzz-corpus
Group:         Development/C
Summary:       Aws Crypto Abstraction Layer executables

%description   -n x-platform-fuzz-corpus
Aws Crypto Abstraction Layer executables.

Aws Crypto Abstraction Layer: Cross-Platform, C99 wrapper for cryptography
primitives.


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
%make test


%files
%doc README*
%_libdir/%name.so.*

%files         devel
%doc README*
%_libdir/%name.so
%_libdir/cmake/%oname
%_includedir/aws/cal

%files         -n x-platform-fuzz-corpus
%_bindir/produce_x_platform_fuzz_corpus
%_bindir/run_x_platform_fuzz_corpus
%_bindir/sha256_profile


%changelog
* Wed Jan 03 2024 Pavel Skrylev <majioa@altlinux.org> 0.6.9-alt1
- Initial build for Sisyphus
