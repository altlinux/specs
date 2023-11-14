%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define sover 4
Name:		libev4
Version:	4.33
Release:	alt3
Summary:	libev - an event notification library
License: BSD-2-Clause OR GPL-2.0-or-later
URL: http://software.schmorp.de/pkg/libev.html
Vcs: http://cvs.schmorp.de/libev/
Group:		System/Libraries

# Source-url: http://dist.schmorp.de/libev/libev-%version.tar.gz
Source:		%name-%version.tar
Source1:	libev.pc.in
Source2:	%name.watch

%description
The libev API provides a mechanism to execute a callback function when
a specific event occurs on a file descriptor or after a timeout has
been reached. It is meant to replace the asynchronous event loop found
in event-driven network servers.

%package -n libev-devel
Summary:	Header files for libev library
Group:		Development/C
Requires:	%name = %EVR

%description -n libev-devel
%summary.

%package -n libev-libevent-devel
Summary:	libevent compatibility header for libev library
Group:		Development/C
Requires:	libev-devel = %EVR
Conflicts: libevent-devel

%description -n libev-libevent-devel
The package contains libevent compatibility header, only core events supported.

%prep
%setup
# Add pkgconfig support
cp -p %{SOURCE1} .
sed -i.pkgconfig -e 's|Makefile|Makefile libev.pc|' configure.ac
sed -i.pkgconfig -e 's|lib_LTLIBRARIES|pkgconfigdir = $(libdir)/pkgconfig\n\npkgconfig_DATA = libev.pc\n\nlib_LTLIBRARIES|' Makefile.am

%build
%ifarch x86_64
%add_optflags -fanalyzer
%endif
%add_optflags %(getconf LFS_CFLAGS) -fno-strict-aliasing -Wno-unused -Wno-comment
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall

%files
%doc Changes LICENSE README
%_libdir/libev.so.%sover
%_libdir/libev.so.%sover.*

%files -n libev-devel
%_libdir/libev.so
%_includedir/ev.h
%_includedir/ev++.h
%_libdir/pkgconfig/libev.pc
%_man3dir/*

%files -n libev-libevent-devel
%_includedir/event.h

%changelog
* Mon Nov 13 2023 Vitaly Chikunov <vt@altlinux.org> 4.33-alt3
- Update sources from CVS for Jun 2023 (contain bug fixes).
- spec: Update License, Url, Vcs tags. Enable strict brp checks.
- Remove static library package.
- Move libevent compatibility header event.h into libev-libevent-devel package
  instead of packaging headers into /usr/include/libev. The result is the same
  as Debian and Fedora have it.

* Mon Oct 11 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.33-alt2
- Fixed build with LTO

* Sun Jan 24 2021 Pavel Vainerman <pv@altlinux.ru> 4.33-alt1
- new version (4.33) with rpmgs script

* Sun Jan 26 2020 Pavel Vainerman <pv@altlinux.ru> 4.24-alt2
- added patch for c++11 ot higher

* Mon Mar 27 2017 Denis Smirnov <mithraen@altlinux.ru> 4.24-alt1
- new version 4.24

* Wed Dec 23 2015 Denis Smirnov <mithraen@altlinux.ru> 4.22-alt1
- new version 4.22

* Wed Jun 24 2015 Denis Smirnov <mithraen@altlinux.ru> 4.20-alt1
- new version 4.20

* Sun Sep 28 2014 Denis Smirnov <mithraen@altlinux.ru> 4.19-alt1
- new version 4.19

* Mon Sep 15 2014 Denis Smirnov <mithraen@altlinux.ru> 4.18-alt1
- new version 4.18

* Mon Sep 15 2014 Denis Smirnov <mithraen@altlinux.ru> 4.15-alt2
- add watch-file

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.15-alt1.1
- Fixed build

* Tue Sep 10 2013 Denis Smirnov <mithraen@altlinux.ru> 4.15-alt1
- 4.15

* Sat Oct 13 2012 Denis Smirnov <mithraen@altlinux.ru> 4.11-alt1
- 4.11

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 4.04-alt1
- 4.04

* Mon Dec 06 2010 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.43-alt3
- Rebuilt for soname set-versions

* Tue Mar 09 2010 Timur Batyrshin <erthad@altlinux.org> 3.43-alt2
- removed obsolete %post/%postun sections

* Tue Aug 26 2008 Kirill A. Shutemov <kas@altlinux.ru> 3.43-alt1
- First build for ALT Linux
