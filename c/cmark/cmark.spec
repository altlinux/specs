%define _unpackaged_files_terminate_build 1

Name: cmark
Version: 0.28.3
Release: alt1%ubt
Summary: CommonMark parsing and rendering
License: BSD and MIT
Group: Text tools
URL: https://github.com/commonmark/cmark

# https://github.com/commonmark/cmark.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: gcc-c++ cmake ctest

%description
cmark is the C reference implementation of CommonMark,
a rationalized version of Markdown syntax with a spec.

It provides a shared library (libcmark) with functions for parsing
CommonMark documents to an abstract syntax tree (AST), manipulating
the AST, and rendering the document to HTML, groff man, LaTeX,
CommonMark, or an XML representation of the AST.  It also provides a
command-line program (cmark) for parsing and rendering CommonMark
documents.

%package devel
Summary: Development files for cmark
Group: Development/C++
Requires: lib%name = %EVR

%description devel
This package provides the development files for cmark.

%package -n lib%name
Summary: CommonMark parsing and rendering library
Group: System/Libraries

%description -n lib%name
This package provides the cmark library.

%prep
%setup

%build
%cmake \
	-DCMARK_STATIC=OFF

%cmake_build

%install
%cmakeinstall_std

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%cmake_build test

%files
%doc COPYING
%_bindir/*
%_man1dir/*

%files -n lib%name
%doc COPYING
%_libdir/*.so.*

%files devel
%doc COPYING README.md
%_includedir/*
%_libdir/*.so
%_libdir/cmake/*
%_pkgconfigdir/libcmark.pc
%_man3dir/*

%changelog
* Tue May 29 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.28.3-alt1%ubt
- Initial build for ALT.
