%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%global optflags_lto %optflags_lto -ffat-lto-objects

Name: dap
Version: 3.10
Release: alt2
Summary: A small statistics and graphics package based on C
Url: http://www.gnu.org/software/dap/
Group: Sciences/Mathematics
License: GPL
Source: %name-%version.tar
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
This directory and its subdirectories contain the source code for
Dap, which is a small statistics and graphics package based on C.
It provides core methods of data management, analysis, and graphics
that are commonly used in statistical consulting practice.  Anyone
familiar with the basic syntax of C programs can learn to use Dap
quickly and easily from the manual and the examples contained in
it; advanced features of C are not necessary, although they are
available.  (The manual contains a brief introduction to the C
syntax needed for Dap.)  Because Dap processes files one line at a
time, rather than reading entire files into memory, it can be, and
has been, used on data sets that have very many lines and/or very
many variables.

%package devel
Group: Development/C
Summary: Development environment for %name, %summary
%description devel
%summary

%prep
%setup

%build
%add_optflags -D_FILE_OFFSET_BITS=64

%configure --with-pic
%make_build

%install
%makeinstall

%files
%doc AUTHORS INSTALL NEWS README TODO
%doc examples
%_infodir/%{name}*
%_bindir/*

%files devel
%_libdir/*.a
%_includedir/*

%changelog
* Mon Sep 13 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.10-alt2
- Fixed build with LTO.

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 3.10-alt1.1
- NMU: added BR: texinfo

* Mon May 12 2014 Fr. Br. George <george@altlinux.ru> 3.10-alt1
- Autobuild version bump to 3.10

* Sat Mar 22 2014 Fr. Br. George <george@altlinux.ru> 3.9-alt1
- Autobuild version bump to 3.9

* Sat Mar 22 2014 Fr. Br. George <george@altlinux.ru> 3.8-alt1
- Initial build for ALT

