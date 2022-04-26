Name: libsigsegv
Version: 2.14
Release: alt1

Summary: Library for handling page faults in user mode
License: GPL-2.0-or-later
Group: System/Libraries

Url: https://www.gnu.org/software/libsigsegv/
# https://git.sv.gnu.org/git/libsigsegv
# git://git.altlinux.org/gears/l/libsigsegv
%define srcname %name-%version-%release
Source: %srcname.tar

BuildRequires: gnulib >= 0.1.4550.2a794

%define libname %{name}2

%description
This is a library for handling page faults in user mode.  A page fault
occurs when a program tries to access to a region of memory that is
currently not available.  Catching and handling a page fault is a useful
technique for implementing:
  - pageable virtual memory
  - memory-mapped access to persistent databases
  - generational garbage collectors
  - stack overflow handlers
  - distributed shared memory

%package -n %libname
Summary: Library for handling page faults in user mode
Group: System/Libraries
Provides: %name = %EVR
Obsoletes: %name < %version

%description -n %libname
This is a library for handling page faults in user mode.  A page fault
occurs when a program tries to access to a region of memory that is
currently not available.  Catching and handling a page fault is a useful
technique for implementing:
  - pageable virtual memory
  - memory-mapped access to persistent databases
  - generational garbage collectors
  - stack overflow handlers
  - distributed shared memory

%package devel
Summary: GNU libsigsegv development library and header files
Group: Development/C
Requires: %libname = %EVR
Obsoletes: libsigsegv0-devel < %version

%description devel
The development library and header files for building applications
with GNU libsigsegv.

%prep
%setup -n %srcname
# Build scripts expect to find the version in this file.
echo -n %version > .tarball-version

%build
GNULIB_SRCDIR=%_datadir/gnulib sh -x ./autogen.sh
%configure --disable-silent-rules --enable-shared --disable-static
%make_build

%install
%makeinstall_std

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%check
%make_build -k check

%files -n %libname
%_libdir/*.so.*
%doc AUTHORS README NEWS

%files devel
%_libdir/*.so
%_includedir/*

%changelog
* Fri Jan 07 2022 Dmitry V. Levin <ldv@altlinux.org> 2.14-alt1
- libsigsegv: v2.13-5-g8107f54 -> v2.14.

* Fri Sep 17 2021 Dmitry V. Levin <ldv@altlinux.org> 2.13.0.5.8107-alt2
- Fixed build with LTO enabled.

* Tue Apr 13 2021 Dmitry V. Levin <ldv@altlinux.org> 2.13.0.5.8107-alt1
- libsigsegv: v2.12-11-gf2e3824 -> v2.13-5-g8107f54.
- gnulib BR: v0.1-2433-g3043e43a7 -> v0.1-4550-g2a7948aad.

* Tue Mar 05 2019 Dmitry V. Levin <ldv@altlinux.org> 2.12.0.11.f2e3-alt1
- v2.10 -> v2.12-11-gf2e3824.
- Enabled LFS on 32-bit systems.

* Wed Sep 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.10-alt1
- Version 2.10

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8-alt4
- Rebuilt for debuginfo

* Fri Oct 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8-alt3
- Rebuilt for soname set-versions

* Mon Jun 07 2010 Dmitry V. Levin <ldv@altlinux.org> 2.8-alt2
- Renamed shared library subpackage to libsigsegv2.

* Sun Jun 06 2010 Dmitry V. Levin <ldv@altlinux.org> 2.8-alt1
- Updated to 2.8.
- Moved "make check" to %%check section.

* Wed Aug 05 2009 Ilya Mashkin <oddity@altlinux.ru> 2.6-alt3
- fixes based in wrar's spec:
   - package the shared library into its own package, not in -devel (Closes: #19895)
   - fix other specfile problems
   - enable tests

* Sat May 02 2009 Ilya Mashkin <oddity@altlinux.ru> 2.6-alt2
- move *.so to main package

* Fri Apr 10 2009 Ilya Mashkin <oddity@altlinux.ru> 2.6-alt1
- 2.6

* Fri Sep 21 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 2.4-alt2
- Remove Russian summary and description.

* Sun Oct 08 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 2.4-alt1
- Stable version 2.4.

* Sat Feb 19 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 2.1.20030818-alt3
- Reduild with gcc 3.4.

* Fri May 14 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 2.1.20030818-alt2
- BuildPreReq on autoconf 1.7.

* Sun May 09 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 2.1.20030818-alt1
- Rebuild.

* Tue Aug 19 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 2.1-alt1csv20030818
- CVS 18.08.2003.

* Sun Jul 06 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 2.1-alt1csv20030706
- CVS 06.07.2003.

* Sat Oct 19 2002 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 2.0.1-alt1csv20021019
- First ALT Linux release.
