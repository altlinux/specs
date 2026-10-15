%def_disable   check
%def_enable    devel
%{?!_disable_devel:%define _unpackaged_files_terminate_build 1}
%define        nomen aws-c-compression

Name:          lib%nomen
Version:       0.3.3
Release:       alt1
Group:         Development/C
Summary:       C99 implementation of huffman encoding/decoding
License:       Apache-2.0
Url:           https://github.com/awslabs/aws-c-common
Vcs:           https://github.com/awslabs/aws-c-common.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-cmake
%{?!_disable_check:BuildRequires: ctest}
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: clang-tools
BuildRequires: cmake(aws-c-common)

%description
This is a cross-platform C99 implementation of compression algorithms such as
gzip, and huffman encoding/decoding. Currently only huffman is implemented.


%if_enabled    devel
%package       devel
Group:         Development/C
Summary:       C99 implementation of huffman encoding/decoding development files
Requires:      ctest
Requires:      cmake
Requires:      clang-tools
Requires:      cmake(aws-c-common)

%description   devel
Development headers and libraries for %nomen.

This is a cross-platform C99 implementation of compression algorithms such as
gzip, and huffman encoding/decoding. Currently only huffman is implemented.
%endif


%package       -n aws-c-compression-huffman-generator
Group:         Development/C
Summary:       C99 implementation of huffman encoding/decoding generator binary

%description   -n aws-c-compression-huffman-generator
C99 implementation of huffman encoding/decoding generator binary.

This is a cross-platform C99 implementation of compression algorithms such as
gzip, and huffman encoding/decoding. Currently only huffman is implemented.


%prep
%setup
%autopatch

%build
%cmake \
%{?!_disable_check: -DBUILD_TESTING=ON} \
   -DCMAKE_MODULE_PATH=%_libdir/cmake \
   -DCMAKE_PREFIX_PATH=%_usr \
   -DCMAKE_C_COMPILER=clang \
   -DBUILD_SHARED_LIBS=ON \
   -DBUILD_HUFFMAN_GENERATOR=ON \
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
%_libdir/cmake/*
%_includedir/aws/compression
%endif

%files         -n aws-c-compression-huffman-generator
%_bindir/aws-c-compression-huffman-generator


%changelog
* Tue Oct 06 2026 Pavel Skrylev <majioa@altlinux.org> 0.3.3-alt1
- ^ 0.2.17 -> 0.3.3
- * rebased to upstream git flow

* Tue Jan 02 2024 Pavel Skrylev <majioa@altlinux.org> 0.2.17-alt1
- Initial build v0.2.17 for Sisyphus
