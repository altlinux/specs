%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Version: 1.10.7
Summary: Cisco-like telnet command-line library
Name: libcli
Release: alt1
License: LGPL-2.1-only
Group: System/Libraries
Source: %name-%version.tar
Url: http://github.com/dparrish/libcli

%description
libcli provides a shared library for including a Cisco-like command-line
interface into other software. It's a telnet interface which supports
command-line editing, history, authentication and callbacks for a
user-definable function tree.

%package devel
Group: Development/C
Summary: Header files for developing programs using %name
Requires: %name = %version-%release

%description devel
This package contains the header files needed to develop programs
based on %name.

%prep
%setup
sed -i 's|/lib|/%_lib|g' Makefile
sed -i 's/calloc(\(.*\), 1)/calloc(1, \1)/' libcli.c

%build
%define optflags_lto %nil
%make_build CFLAGS='%optflags' STATIC_LIB=0

%install
%makeinstall_std PREFIX=%_prefix STATIC_LIB=0

%files
%doc COPYING
%_libdir/libcli.so.*

%files devel
%doc README.md doc/*.md
%_libdir/libcli.so
%_includedir/libcli.h

%changelog
* Sat Dec 13 2025 Vitaly Chikunov <vt@altlinux.org> 1.10.7-alt1
- Update to V1.10.7 (2021-02-25).

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.9.5-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Dec 19 2010 Terechkov Evgenii <evg@altlinux.org> 1.9.5-alt1
- Initial build for ALT Linux Sisyphus
