%define _unpackaged_files_terminate_build 1

Name: bloaty
Version: 1.1
Release: alt2.git3f36ed

Summary: A size profiler for binaries

License: Apache-2.0
Group: Development/Tools
VCS: https://github.com/google/bloaty

Source: %name-%version.tar
Patch0: bloaty-alt-build_testing.patch
Patch1: bloaty-alt-system_demumble.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-ninja-build

BuildRequires: cmake gcc-c++
BuildRequires: python3
BuildRequires: ctest
BuildRequires: pkg-config
BuildRequires: ninja-build

BuildRequires: libabseil-cpp-devel
BuildRequires: libgmock-devel
BuildRequires: libgtest-devel
BuildRequires: capstone-devel
BuildRequires: protobuf-compiler
BuildRequires: libprotobuf-c-devel
BuildRequires: libprotobuf-devel
BuildRequires: libre2-devel
BuildRequires: zlib-devel
BuildRequires: libcxxabi-devel


%description
Bloaty performs a deep analysis of the binary. Using custom ELF,
DWARF,and Mach-O parsers, Bloaty aims to accurately attribute
every byte of the binary to the symbol or compileunit that
produced it. It will even disassemble the binary looking for
references to anonymous data.


%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%cmake \
	-GNinja \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	%nil
%cmake_build

%install
%ninja_install -C %_cmake__builddir

%check
# smoke test
cd  %_cmake__builddir
./bloaty `command -v ls`
./bloaty -n 100 -d rawsymbols   ./bloaty
./bloaty -n 100 -d symbols      ./bloaty
./bloaty -n 100 -d fullsymbols  ./bloaty
./bloaty -n 100 --demangle=full ./bloaty
# end of smoke test

%ninja_test


%files
%doc README.md doc/using.md doc/how-bloaty-works.md
%_bindir/*
%_target_libdir_noarch/Bloaty/*


%changelog
* Wed Apr 30 2025 Yaroslav Karpov <hellkar@altlinux.org> 1.1-alt2.git3f36ed
- release info fixed

* Thu Apr 24 2025 Yaroslav Karpov <hellkar@altlinux.org> 1.1-alt1
- Initial build for ALT

