%set_verify_elf_method unresolved=strict

Name: BlocksRuntime
Version: 0.3
Release: alt1
Summary: The runtime library for C blocks support
License: MIT
Group: Development/Tools
Url: https://sourceforge.net/projects/blocksruntime/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: ruby-makeconf clang-devel

Source: %name-%version.tar

%description
Blocks are a proposed extension to the C, Objective C, and C++ languages
developed by Apple to support the Grand Central Dispatch concurrency
engine.

%package -n lib%name
Summary: The runtime library for C blocks support
Group: System/Libraries

%description -n lib%name
Blocks are a proposed extension to the C, Objective C, and C++ languages
developed by Apple to support the Grand Central Dispatch concurrency
engine.

%package -n lib%name-devel
Summary: Development files of BlocksRuntime
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Blocks are a proposed extension to the C, Objective C, and C++ languages
developed by Apple to support the Grand Central Dispatch concurrency
engine.

This package contains development files of BlocksRuntime.

%prep
%setup

%build
export CC=clang
%configure \
	--disable-option-checking \
	--target=linux \
	--host=linux

%make
 
%install
%makeinstall_std

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Wed Feb 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

