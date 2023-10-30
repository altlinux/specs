%define sover 4.0

Name: zydis
Version: 4.0.0
Release: alt2

Summary: Fast and lightweight x86/x86-64 disassembler and code generation library.
License: MIT
Group: System/Libraries

Url: https://%name.re/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/zyantific/%name/archive/refs/tags/v%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch3500: zydis-loongarch64.patch

BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: graphviz
BuildRequires: libzycore-devel

%description
Fast and lightweight x86/x86-64 disassembler and code generation library.

%package -n lib%name%sover
Summary: Fast and lightweight x86/x86-64 disassembler and code generation library.
Group: System/Libraries

%description -n lib%name%sover
Fast and lightweight x86/x86-64 disassembler and code generation library.

%package -n lib%name-devel
Summary: Header files for lib%name
Group: Development/C

%description -n lib%name-devel
Header files for lib%name

%package tools
Summary: Development tools for %name
Group: Development/Tools

%description tools
Development tools for %name

%prep
%setup
%patch3500 -p1

%build
%cmake \
	-DZYDIS_BUILD_SHARED_LIB:BOOL=TRUE \
	-DZYAN_SYSTEM_ZYCORE:BOOL=TRUE
%cmake_build

%install
%cmake_install

%files -n lib%name%sover
%doc LICENSE README.md SECURITY.md
%_libdir/libZydis.so.*

%files -n lib%name-devel
%_libdir/cmake/%name
%_libdir/libZydis.so
%_includedir/Zydis
%_defaultdocdir/Zydis

%files tools
%_bindir/Zydis*

%changelog
* Mon Oct 30 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 4.0.0-alt2
- NMU: fixed FTBFS on LoongArch

* Mon May 29 2023 Nazarov Denis <nenderus@altlinux.org> 4.0.0-alt1
- Initial build for ALT Linux
