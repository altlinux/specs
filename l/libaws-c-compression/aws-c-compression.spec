%define        _unpackaged_files_terminate_build 1
%define        oname aws-c-compression

Name:          lib%oname
Version:       0.2.17
Release:       alt1
Group:         Development/C
Summary:       C99 implementation of huffman encoding/decoding
License:       Apache-2.0
Url:           https://github.com/awslabs/aws-c-common
Vcs:           https://github.com/awslabs/aws-c-common.git

Source:        %name-%version.tar
Patch:         path.patch
Patch1:        bin-compile.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: libaws-c-common-devel

%description
This is a cross-platform C99 implementation of compression algorithms such as
gzip, and huffman encoding/decoding. Currently only huffman is implemented.


%package       devel
Group:         Development/C
Summary:       C99 implementation of huffman encoding/decoding development files
Requires:      cmake
Requires:      libaws-c-common-devel

%description   devel
Development headers and libraries for %oname.

This is a cross-platform C99 implementation of compression algorithms such as
gzip, and huffman encoding/decoding. Currently only huffman is implemented.


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
%cmake_insource \
   -DCMAKE_MODULE_PATH=%_libdir/cmake \
   -DBUILD_SHARED_LIBS=ON \
   -DBUILD_HUFFMAN_GENERATOR=ON \
   -DBUILD_TESTING=ON

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
%_libdir/cmake/*
%_includedir/aws/compression

%files         -n aws-c-compression-huffman-generator
%_bindir/aws-c-compression-huffman-generator


%changelog
* Tue Jan 02 2024 Pavel Skrylev <majioa@altlinux.org> 0.2.17-alt1
- Initial build v0.2.17 for Sisyphus
