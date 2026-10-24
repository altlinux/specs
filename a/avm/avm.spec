%define _unpackaged_files_terminate_build 1
%set_verify_elf_method strict

%define soversion 1
%define libname libavm%soversion

Name: avm
Version: 1.0.0
Release: alt1

Summary: AV2 video codec reference implementation
License: BSD-3-Clause-Clear AND AOMPL-1.0
Group: Video
Url: https://aomedia.org/
Vcs: https://github.com/AOMediaCodec/avm
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ perl
%ifarch %ix86 x86_64
BuildRequires: yasm
%endif

%description
AVM is the Alliance for Open Media reference implementation of the AV2
video codec.

%package tools
Summary: AV2 video encoder and decoder tools
Group: Video

%description tools
Command-line avmenc encoder and avmdec decoder for the AV2 video codec.

%package -n %libname
Summary: AV2 video codec shared library
Group: System/Libraries

%description -n %libname
Shared library for encoding and decoding AV2 video. The runtime package
is named after its SONAME ABI version to allow parallel installation of
incompatible ABI versions.

%package -n libavm-devel
Summary: Development files for the AV2 video codec library
Group: Development/C
Requires: %libname = %EVR

%description -n libavm-devel
Headers, linker symlink and pkg-config metadata for developing applications
with the AV2 video codec library.

%prep
%setup

%build
%cmake \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DCMAKE_INSTALL_LIBDIR:STRING=%_lib \
    -DCMAKE_INSTALL_INCLUDEDIR:STRING=include \
    -DCMAKE_INSTALL_BINDIR:STRING=bin \
    -DENABLE_DOCS:BOOL=OFF \
    -DENABLE_TESTS:BOOL=OFF \
    -DENABLE_TESTDATA:BOOL=OFF \
    -DENABLE_EXAMPLES:BOOL=ON \
    -DENABLE_TOOLS:BOOL=OFF \
    -DCONFIG_ML_PART_SPLIT=0 \
    -DCONFIG_DIP_EXT_PRUNING=0
# The two ML encoder optimizations above require bundled TensorFlow Lite.
%cmake_build

%install
%cmakeinstall_std
rm -f %buildroot%_libdir/libavm.a

%check
# Fail on an ABI bump until the runtime package name is updated.
readelf -d %buildroot%_libdir/libavm.so.%soversion | \
    grep -F 'Library soname: [libavm.so.%soversion]'
export LD_LIBRARY_PATH=%buildroot%_libdir
%buildroot%_bindir/avmenc --help > /dev/null
%buildroot%_bindir/avmdec --help > /dev/null

%files tools
%doc LICENSE PATENTS README.md
%_bindir/avmenc
%_bindir/avmdec

%files -n %libname
%doc LICENSE PATENTS
%_libdir/libavm.so.%soversion
%_libdir/libavm.so.%{soversion}.*

%files -n libavm-devel
%_includedir/avm/
%_libdir/libavm.so
%_pkgconfigdir/avm.pc

%changelog
* Sat Oct 24 2026 Anton Farygin <rider@altlinux.org> 1.0.0-alt1
- Initial build for ALT Linux.
