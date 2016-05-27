%define vermajor 1
%define verminor 5.9
%define version %vermajor.%verminor

Name: keyutils
Version: %version
Release: alt2

Summary: Linux Key Management Utilities
License: GPL/LGPL
Group: System/Base
Url: http://people.redhat.com/~dhowells/keyutils/

Source0: %name-%version-%release.tar

BuildRequires: glibc-kernheaders

%description
Utilities to control the kernel key management facility and to provide
a mechanism by which the kernel call back to userspace to get a key
instantiated.

%package -n lib%name
Summary: Key utilities library
Group: System/Libraries

%package -n lib%name-devel
Summary: Development package for building linux key management utilities
Group: Development/C
Requires: lib%name == %version-%release

%description -n lib%name
This package provides a wrapper library for the key management facility system
calls.

%description -n lib%name-devel
This package provides headers and libraries for building key utilities.

%prep
%setup

%build
make \
    NO_ARLIB=1 \
    LIBDIR=/%_lib \
    USRLIBDIR=%_libdir \
    RELEASE=.%release \
    NO_GLIBC_KEYERR=1 \
    CFLAGS="-Wall $RPM_OPT_FLAGS -Werror"

%install
make \
    NO_ARLIB=1 \
    DESTDIR=%buildroot \
    LIBDIR=/%_lib \
    USRLIBDIR=%_libdir \
    install
ln -snf ../../%_lib/lib%name.so.1 %buildroot%_libdir/lib%name.so

%files
%doc README LICENCE.GPL
%config(noreplace) %_sysconfdir/request-key.conf
%dir %_sysconfdir/request-key.d
/sbin/*
/bin/*
%_datadir/%name
%_man1dir/*
%_man5dir/*
%_man7dir/*
%_man8dir/*

%files -n lib%name
/%_lib/lib%name.so.*

%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/*
%_man3dir/*

%changelog
* Fri May 27 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.9-alt2
- cifs-related config entries dropped (closes #32146)

* Fri Apr 25 2014 Alexey Shabalin <shaba@altlinux.ru> 1.5.9-alt1
- 1.5.9 released

* Mon Feb 03 2014 Alexey Shabalin <shaba@altlinux.ru> 1.5.8-alt1
- 1.5.8 released

* Fri Aug 19 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt1
- 1.5.1 released

* Mon Feb 28 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4-alt2
- added nfsidmap-related entry to request-key.conf

* Mon Sep 13 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4-alt1
- 1.4 released

* Fri Mar 27 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2-alt3
- added CIFS-related enties into request-key.conf

* Sat Dec  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2-alt2
- obsolete by filetriggers macros removed

* Sat Jan  5 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2-alt1
- built for %%distribution

* Tue Aug 22 2006 David Howells <dhowells@redhat.com> - 1.2-1
- Remove syscall manual pages (section 2) to man-pages package [BZ 203582]
- Don't write to serial port in debugging script

* Mon Jun 5 2006 David Howells <dhowells@redhat.com> - 1.1-4
- Call ldconfig during (un)installation.

* Fri May 5 2006 David Howells <dhowells@redhat.com> - 1.1-3
- Don't include the release number in the shared library filename
- Don't build static library

* Fri May 5 2006 David Howells <dhowells@redhat.com> - 1.1-2
- More bug fixes from Fedora reviewer.

* Thu May 4 2006 David Howells <dhowells@redhat.com> - 1.1-1
- Fix rpmlint errors

* Mon Dec 5 2005 David Howells <dhowells@redhat.com> - 1.0-2
- Add build dependency on glibc-kernheaders with key management syscall numbers

* Tue Nov 29 2005 David Howells <dhowells@redhat.com> - 1.0-1
- Add data pipe-in facility for keyctl request2

* Mon Nov 28 2005 David Howells <dhowells@redhat.com> - 1.0-1
- Rename library and header file "keyutil" -> "keyutils" for consistency
- Fix shared library version naming to same way as glibc.
- Add versioning for shared library symbols
- Create new keyutils-libs package and install library and main symlink there
- Install base library symlink in /usr/lib and place in devel package
- Added a keyutils archive library
- Shorten displayed key permissions list to just those we actually have

* Thu Nov 24 2005 David Howells <dhowells@redhat.com> - 0.3-4
- Add data pipe-in facilities for keyctl add, update and instantiate

* Fri Nov 18 2005 David Howells <dhowells@redhat.com> - 0.3-3
- Added stdint.h inclusion in keyutils.h
- Made request-key.c use request_key() rather than keyctl_search()
- Added piping facility to request-key

* Thu Nov 17 2005 David Howells <dhowells@redhat.com> - 0.3-2
- Added timeout keyctl option
- request_key auth keys must now be assumed
- Fix keyctl argument ordering for debug negate line in request-key.conf

* Thu Jul 28 2005 David Howells <dhowells@redhat.com> - 0.3-1
- Must invoke initialisation from perror() override in libkeyutils
- Minor UI changes

* Wed Jul 20 2005 David Howells <dhowells@redhat.com> - 0.2-2
- Bump version to permit building in main repositories.

* Tue Jul 12 2005 David Howells <dhowells@redhat.com> - 0.2-1
- Don't attempt to define the error codes in the header file.
- Pass the release ID through to the makefile to affect the shared library name.

* Tue Jul 12 2005 David Howells <dhowells@redhat.com> - 0.1-3
- Build in the perror() override to get the key error strings displayed.

* Tue Jul 12 2005 David Howells <dhowells@redhat.com> - 0.1-2
- Need a defattr directive after each files directive.

* Tue Jul 12 2005 David Howells <dhowells@redhat.com> - 0.1-1
- Package creation.
