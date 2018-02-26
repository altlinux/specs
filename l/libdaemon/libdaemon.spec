%def_disable static

Name: libdaemon
Version: 0.14
Release: alt2

Summary: Lightweight C library which eases the writing of UNIX daemons
License: LGPL
Group: System/Libraries
Url: http://0pointer.de/lennart/projects/libdaemon/

Source: %name-%version-%release.tar

BuildRequires: doxygen lynx

%description
libdaemon is a leightweight C library which eases the writing of UNIX daemons.
It consists of the following parts:

 * A wrapper around fork() which does the correct daemonization
   procedure of a process
 * A wrapper around syslog() for simpler and compatible log output to
   Syslog or STDERR
 * An API for writing PID files
 * An API for serializing UNIX signals into a pipe for usage with
   select() or poll()

Routines like these are included in most of the daemon software available. It
is not that simple to get it done right and code duplication cannot be a goal.

%package devel
Summary: Development part of libdaemon
Group: Development/C
Requires: %name = %version-%release

%package devel-static
Summary: Static libraries from libdaemon
Group: Development/C
Requires: %name-devel = %version-%release

%description devel
This is the development part (header files and documentation) for 
%name.

%description devel-static
This package contains static library to build statically linked %name
applications.

%prep
%setup

%build
%autoreconf
%configure %{subst_enable static} 
make all doxygen

%install
%makeinstall
install -d %buildroot%_man3dir
cp -a doc/reference/man/* %buildroot%_mandir/

%files
%_libdir/*.so.*

%files devel
%doc doc/README doc/reference/html/
%_man3dir/*
%_libdir/*.so
%_pkgconfigdir/*
%_includedir/%name/

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Fri Nov 11 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14-alt2
- rebuilt for debuginfo

* Mon Sep 13 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14-alt1
- 0.14 released

* Wed Dec 24 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13-alt2
- symbol versioning added (#18320)

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 0.13-alt1
- 0.13
- applied repocop patch

* Sat Mar 29 2008 Michael Shigorin <mike@altlinux.org> 0.12-alt2
- updated Url:

* Tue Jul 10 2007 Michael Shigorin <mike@altlinux.org> 0.12-alt1
- 0.12: makes daemon_close_all() actually work properly

* Tue Jun 26 2007 Michael Shigorin <mike@altlinux.org> 0.11-alt1
- 0.11

* Sun Dec 24 2006 Michael Shigorin <mike@altlinux.org> 0.10-alt2
- added %_includedir/%name/ to package filelist (fixes: #10512)

* Sat Aug 05 2006 Michael Shigorin <mike@altlinux.org> 0.10-alt1
- 0.10
  + feature complete release
  + 0.9 changed license from GPL to LGPL
  + compatibility and portability fixes since 0.6
- disabled static build by default

* Thu Apr 08 2004 Michael Shigorin <mike@altlinux.ru> 0.6-alt1
- 0.6

* Mon Jan 26 2004 Michael Shigorin <mike@altlinux.ru> 0.4-alt1
- 0.4

* Wed Dec 17 2003 Michael Shigorin <mike@altlinux.ru> 0.3-alt2
- removed *.la
- disabled static library packaging by default

* Sun Oct 26 2003 Michael Shigorin <mike@altlinux.ru> 0.3-alt1
- 0.3

* Wed Sep 10 2003 Michael Shigorin <mike@altlinux.ru> 0.2-alt1
- built for ALT Linux (ifplugd dependency)

