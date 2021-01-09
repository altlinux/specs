%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: dwz
Version: 0.13
Release: alt3

Summary: DWARF optimization and duplicate removal tool
License: GPLv2+
Group: Development/Tools

URL: https://sourceware.org/git/?p=dwz.git
Source: dwz-%version.tar

# Automatically added by buildreq on Fri Jan 05 2018
BuildRequires: libelf-devel
BuildRequires: dejagnu

%description
dwz is a program that attempts to optimize DWARF debugging information
contained in ELF shared libraries and ELF executables for size, by
replacing DWARF information representation with equivalent smaller
representation where possible and by reducing the amount of duplication
using techniques from DWARF standard appendix E - creating
DW_TAG_partial_unit compilation units (CUs) for duplicated information
and using DW_TAG_imported_unit to import it into each CU that needs it.

%prep
%setup -q

%build
%make_build CFLAGS='%optflags'

%install
install -pD -m755 dwz %buildroot%_bindir/dwz
install -pD -m644 dwz.1 %buildroot%_man1dir/dwz.1

%check
make check || { grep FAIL dwz.log; exit 1; }

%files
%_bindir/dwz
%_man1dir/dwz.1*

%changelog
* Sat Jan 09 2021 Vitaly Chikunov <vt@altlinux.org> 0.13-alt3
- Fix devel-ignore-size.sh test.

* Wed Dec 02 2020 Vitaly Chikunov <vt@altlinux.org> 0.13-alt2
- Fix pr24468.sh test.

* Thu Nov 26 2020 Vitaly Chikunov <vt@altlinux.org> 0.13-alt1
- Update to dwz-0.13 (2019-08-02).

* Fri Jan 05 2018 Alexey Tourbin <at@altlinux.ru> 0.12-alt1
- initial revision
