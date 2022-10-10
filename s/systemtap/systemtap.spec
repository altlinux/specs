# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: systemtap
Version: 4.7
Release: alt1
Summary: Programmable system-wide instrumentation system
License: GPL-2.0-or-later
Group: System/Kernel and hardware
Url: https://sourceware.org/systemtap/
Vcs: https://sourceware.org/git/systemtap.git

Source: %name-%version.tar

BuildRequires: rpm-build-python3

%description
%summary.

%package sdt-devel
Summary: Static probe (USDT) support tools
Group: Development/C
Requires: python3-module-pyparsing

%description sdt-devel
This package includes the <sys/sdt.h> header file used for static
instrumentation compiled into userspace programs and libraries, along
with the optional dtrace-compatibility preprocessor to process related
.d files into tracing-macro-laden .h headers.

%package sdt-devel-checkinstall
Summary: %summary
Group: Development/Other
Requires: rpm-build
Requires: systemtap-sdt-devel = %EVR

%description sdt-devel-checkinstall
%summary.

%prep
%setup

%build
sed s=@preferred_python@=%__python3= dtrace.in | sed s=@prefix@=%_prefix= >dtrace
sed -e 's/@support_section_question@/1/' < includes/sys/sdt-config.h.in > includes/sys/sdt-config.h

%install
install -Dpm0755 dtrace -t %buildroot%_bindir/
install -Dpm0644 man/dtrace.1 -t %buildroot%_man1dir/
install -Dpm0644 includes/sys/*.h -t %buildroot%_includedir/sys/

%post sdt-devel-checkinstall
set -ex -o pipefail
cd /tmp
DATADIR=%_defaultdocdir/%name-sdt-devel-checkinstall-%version
  dtrace -s $DATADIR/sdt_misc_.d -G
  dtrace -s $DATADIR/dtrace.d -h
  dtrace -s $DATADIR/dtrace.d -h -C
  gcc $DATADIR/sdt.c
  eu-readelf --notes=.note.stapsdt a.out | grep -q 'stapsdt.*Version'
  eu-readelf --notes=.note.stapsdt a.out | grep -q 'Provider: test, Name: mark_a, Args:'
  eu-readelf --notes=.note.stapsdt a.out
rm *.o *.h a.out

%files sdt-devel
%doc README COPYING AUTHORS NEWS
%_bindir/dtrace
%_man1dir/dtrace.1*
%_includedir/sys/sdt*.h

%files sdt-devel-checkinstall
%doc testsuite/systemtap.base/dtrace.d
%doc testsuite/systemtap.base/sdt_misc_.d
%doc testsuite/systemtap.base/sdt.c

%changelog
* Mon Oct 10 2022 Vitaly Chikunov <vt@altlinux.org> 4.7-alt1
- First import release-4.7 (2022-05-02).
- Build only systemtap-sdt-devel package.
