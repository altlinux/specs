%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: libmaa
Version: 1.5.1
Release: alt1

Summary: Library providing many low-level data structures
License: MIT
Group: System/Libraries

Url: http://sourceforge.net/projects/dict/
Source: %name-%version.tar
Packager: Aleksey Cheusov <cheusov@altlinux.org>

BuildRequires: mk-configure >= 0.34.2-alt4
BuildRequires: rpm-macros-mk-configure

%description
The libmaa library provides many low-level data
structures, including hash tables, sets, lists, debugging support, and
memory management. Although libmaa was designed and implemented as a
foundation for the kheperalong, the data structures are generally
applicable to a wide range of programming problems.

%package devel
Summary: Development files of libmaa
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains development files of libmaa.

%package devel-doc
Summary: Documentation for libmaa
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
This package contains development documentation for libmaa.

%prep
%setup

%define libmaa_docdir %_docdir/%name-%version
%define _mkc_env \
	export DOCDIR=%libmaa_docdir \
	export MKSTATICLIB=no \
	%mkc_env

%build
%add_optflags -D_FILE_OFFSET_BITS=64

%_mkc_env
%mkcmake_configure
%mkcmake_build

%check
%_mkc_env
%mkcmake test

%install
%_mkc_env
%mkcmake_install
%mkcmake install-doc DESTDIR=%buildroot

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

%files devel-doc
%libmaa_docdir/libmaa.600dpi.ps
%libmaa_docdir/README
%libmaa_docdir/LICENSE
%libmaa_docdir/TODO
%libmaa_docdir/NEWS

%changelog
* Wed May 29 2024 Aleksey Cheusov <cheusov@altlinux.org> 1.5.1-alt1
- Version 1.5.1

* Sat Feb 10 2024 Grigory Ustinov <grenka@altlinux.org> 1.4.7-alt6
- Dropped devel-static subpackage (Closes: #39377).

* Mon Oct 11 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.7-alt5
- Fixed build with LTO

* Fri Jan 08 2021 Aleksey Cheusov <cheusov@altlinux.org> 1.4.7-alt4
- 1.4.7-alt4: Split -devel package into -devel and -static-devel packages

* Tue May 26 2020 Aleksey Cheusov <cheusov@altlinux.org> 1.4.7-alt3
- 1.4.7-alt3: Fix warnings produced by hasher

* Fri May 22 2020 Aleksey Cheusov <cheusov@altlinux.org> 1.4.7-alt2
- 1.4.7-alt2: use rpm macro provided by mk-configure

* Sun May 17 2020 Aleksey Cheusov <cheusov@altlinux.org> 1.4.7-alt1
- Version 1.4.7

* Thu Sep 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1
- Version 1.3.2

* Mon Nov 07 2011 Michael Shigorin <mike@altlinux.org> 1.3.1-alt1
- NMU: 1.3.1 (gcc-4.6 ready)

* Thu Apr 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Version 1.3.0
- Disabled devel-static package

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt3
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2
- Rebuilt for soname set-versions

* Mon Jun 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus

