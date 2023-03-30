# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libpfm
Version: 4.13.0
Release: alt1
Summary: Library to encode performance events for use by perf tool
License: MIT
Group: System/Libraries
Url: http://perfmon2.sourceforge.net/

# Expunge libpapi containing libpfm.
Conflicts: libpapi < 6.0.0-alt6

Source: %name-%version.tar

%description
libpfm4 is a library to help encode events for use with operating system
kernels performance monitoring interfaces. The current version provides
support for the perf_events interface available in upstream Linux kernels
since v2.6.31.

%package devel
Summary: Development library to encode performance events for perf_events based tools
Requires: libpfm = %EVR
Group: Development/C

%description devel
Development library and header files to create performance monitoring
applications for the perf_events interface.

%prep
%setup

%build
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%add_optflags %(getconf LFS_CFLAGS)
%ifarch ppc64le
# Possible upstream bug: https://gcc.gnu.org/bugzilla/show_bug.cgi?id=100332
%add_optflags -Wno-error=maybe-uninitialized
%endif
%make_build OPTIM="%optflags"

%install
%make install \
     PREFIX=%buildroot%_prefix \
     LIBDIR=%buildroot%_libdir \
     LDCONFIG=/bin/true
rm %buildroot%_libdir/libpfm.a
install -D -p -m 0755 examples/check_events %buildroot%_bindir/check_events
install -D -p -m 0755 examples/showevtinfo  %buildroot%_bindir/showevtinfo
install -D -p -m 0755 perf_examples/evt2raw %buildroot%_bindir/evt2raw

%check
tests/validate -A
%buildroot%_bindir/showevtinfo -L | fmt -w 111

%files
%doc COPYING
%_libdir/libpfm.so.*

%files devel
%doc README
%_bindir/*
%_includedir/perfmon/
%_libdir/libpfm.so
%_man3dir/*pfm*.3*

%changelog
* Wed Mar 29 2023 Vitaly Chikunov <vt@altlinux.org> 4.13.0-alt1
- Update to v4.13.0 (2023-03-28).

* Tue Sep 20 2022 Vitaly Chikunov <vt@altlinux.org> 4.12.1-alt1
- Update to v4.12.1 (2022-09-20).

* Sat Jun 04 2022 Vitaly Chikunov <vt@altlinux.org> 4.11.1-alt2
- Fix rebuild after switching to GCC 12.

* Mon Jan 03 2022 Vitaly Chikunov <vt@altlinux.org> 4.11.1-alt1
- Imported upstream v4.11.1-51-g45d2888 (2021-11-30) into this standalone
  package. Previously libpfm was built from the source bundled in papi.
- Packaged libpfm4 tools.
