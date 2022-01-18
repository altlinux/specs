%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: cmark
Version: 0.30.2
Release: alt1
Summary: CommonMark parsing and rendering
License: BSD and MIT
Group: Text tools
URL: https://github.com/commonmark/cmark

# https://github.com/commonmark/cmark.git
Source: %name-%version.tar

Source2: %name.watch

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
* Mon Jan 17 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.30.2-alt1
- Updated to upstream version 0.30.2.

* Tue Sep 07 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.30.1-alt1
- Updated to upstream version 0.30.1.

* Mon May 31 2021 Arseny Maslennikov <arseny@altlinux.org> 0.29.0-alt1.1
- NMU: spec: adapted to new cmake macros.

* Thu Jul 25 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.29.0-alt1
- Updated to upstream version 0.29.0.

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.28.3-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.28.3-alt2
- NMU: remove %%ubt from release

* Tue May 29 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.28.3-alt1
- Initial build for ALT.
