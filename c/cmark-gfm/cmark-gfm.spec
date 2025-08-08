%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: cmark-gfm
Version: 0.29.0.gfm.13
Release: alt2

%define soversion %version

Summary: GitHub's fork of CommonMark parsing and rendering library and program in C
License: BSD-2-Clause and MIT
Group: Text tools
Url: https://github.com/github/cmark-gfm
Vcs: https://github.com/github/cmark-gfm.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake
BuildRequires: gcc-c++ ctest

%description
cmark-gfm is an extended version of the C reference implementation of
CommonMark, a rationalized version of Markdown syntax with a spec.
This repository adds GitHub Flavored Markdown extensions to the
upstream implementation, as defined in the spec.

%package -n libcmark-gfm-devel
Summary: Development files for cmark-gfm
Group: Development/C++

%description -n libcmark-gfm-devel
This package provides the development files for cmark-gfm.

%package -n libcmark-gfm%soversion
Summary: CommonMark parsing and rendering library
Group: System/Libraries

%description -n libcmark-gfm%soversion
This package provides the cmark-gfm library.

%prep
%setup

%build
%add_optflags -D_FILE_OFFSET_BITS=64

%cmake \
	-DCMARK_STATIC=OFF \
	%nil

%cmake_build

%install
%cmake_install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%cmake_build --target test

%files
%doc COPYING
%_bindir/cmark-gfm
%_man1dir/cmark-gfm.1.xz

%files -n libcmark-gfm%soversion
%doc COPYING
%_libdir/libcmark-gfm-extensions.so.%soversion
%_libdir/libcmark-gfm.so.%soversion

%files -n libcmark-gfm-devel
%doc COPYING README.md
%_includedir/cmark-gfm*
%_libdir/libcmark-gfm.so
%_libdir/libcmark-gfm-extensions.so
%_libdir/cmake/*
%_libdir/cmake-gfm-extensions/*
%_pkgconfigdir/libcmark-gfm.pc
%_man3dir/cmark-gfm.3.xz

%changelog
* Fri Aug 08 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.29.0.gfm.13-alt2
- Fix license tag.
- Move cmark-gfm to "Text tools" group.

* Tue Jul 01 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.29.0.gfm.13-alt1
- Initial build.
