%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: dwz
Version: 0.14
Release: alt1

Summary: DWARF optimization and duplicate removal tool
License: GPL-2.0-or-later
Group: Development/Tools

Vcs: https://sourceware.org/git/?p=dwz.git
Url: https://sourceware.org/dwz/
Source: dwz-%version.tar

BuildRequires: dejagnu
BuildRequires: gcc-c++
BuildRequires: gdb
BuildRequires: libelf-devel

%description
dwz is a program that attempts to optimize DWARF debugging information
contained in ELF shared libraries and ELF executables for size, by
replacing DWARF information representation with equivalent smaller
representation where possible and by reducing the amount of duplication
using techniques from DWARF standard appendix E - creating
DW_TAG_partial_unit compilation units (CUs) for duplicated information
and using DW_TAG_imported_unit to import it into each CU that needs it.

%prep
%setup

%build
%make_build CFLAGS='%optflags'

%install
%makeinstall_std

%check
make check || { grep FAIL dwz.log; exit 1; }

%files
%doc COPYING COPYING.RUNTIME COPYING3
%_bindir/dwz
%_man1dir/dwz.1*

%changelog
* Sat Mar 13 2021 Vitaly Chikunov <vt@altlinux.org> 0.14-alt1
- Update to dwz-0.14 (2021-03-08).

* Sat Jan 09 2021 Vitaly Chikunov <vt@altlinux.org> 0.13-alt3
- Fix devel-ignore-size.sh test.

* Wed Dec 02 2020 Vitaly Chikunov <vt@altlinux.org> 0.13-alt2
- Fix pr24468.sh test.

* Thu Nov 26 2020 Vitaly Chikunov <vt@altlinux.org> 0.13-alt1
- Update to dwz-0.13 (2019-08-02).

* Fri Jan 05 2018 Alexey Tourbin <at@altlinux.ru> 0.12-alt1
- initial revision
