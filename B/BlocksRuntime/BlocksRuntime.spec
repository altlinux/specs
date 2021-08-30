%define _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=strict

# clang doesn't know used LTO flags
%global optflags_lto %nil

Name: BlocksRuntime
Version: 0.3
Release: alt4
Summary: The runtime library for C blocks support
License: MIT
Group: Development/Tools
Url: https://sourceforge.net/projects/blocksruntime/

BuildRequires: ruby
BuildRequires: ruby-makeconf
BuildRequires: clang-devel

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
# remove bundled ruby gem
rm -rf makeconf

%build
export CC=clang

%configure \
	--disable-option-checking \
	--target=linux \
	--host=linux \
	%nil

%make

%install
%makeinstall_std

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Mon Aug 30 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3-alt4
- Disabled LTO.

* Wed Dec 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3-alt3
- Updated build dependencies and compiler flags.

* Tue Jan 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3-alt2
- Removed unsupported compiler flags.

* Wed Feb 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

