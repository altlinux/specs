Name: vhttpd
Version: 0.7.2
Release: alt1

Source:%name-%version.tar

Summary: simple embedded web server
License: LGPL
Group: System/Servers

Packager: Stanislav Ievlev <inger@altlinux.org>

BuildPreReq: glib2-devel libssl-devel libgnutls-devel guile18-devel cgreen

Conflicts: alterator < 4.17-alt1
Conflicts: alterator-fbi < 5.26-alt1

%description
voins httpd - port of the first alterator's web server.

%package -n lib%name
Summary: simple embedded web server (shared library)
License: LGPL
Group: System/Libraries

%description -n lib%name
shared library for the vhttpd


%package -n lib%name-devel
Summary: simple embedded web server (development library)
License: LGPL
Group: Development/C
Requires: lib%name = %version-%release
Requires: glib2-devel

%description -n lib%name-devel
development library for the vhttpd

%package utils
Summary: utils for library
License: LGPL
Group: System/Libraries
Requires: lib%name = %version-%release

%description utils
utils for library:
    certvalidate - server side certificate validation


%package -n libguile-%name
Summary: guile bindings for %name
License: LGPL
Group: System/Libraries
Requires(pre): lib%name = %version-%release
Requires: guile18

%description -n libguile-%name
guile bindings for %name

%prep
%setup

%build
%make_build

%check
%make check

%install
%makeinstall

%files -n lib%name
%_libdir/*.so.*
%exclude %_libdir/libguile-*.so.*

%files -n lib%name-devel
%_libdir/*.so
%exclude %_libdir/libguile-*.so
%_includedir/*

%files utils
%_bindir/*

%files -n libguile-%name
%_datadir/guile/1.8/*
%_libdir/libguile-*

%changelog
* Thu Mar 24 2011 Mikhail Efremov <sem@altlinux.org> 0.7.2-alt1
- tests: fix for glib >= 2.28.

* Tue Dec 21 2010 Michael Shigorin <mike@altlinux.org> 0.7.1-alt1
- applied connection close patch by slazav@ (closes: #24795)
- tiny spec cleanup

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Thu Dec 03 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt1
- major code improvements
- new API
- support both client and server connections

* Tue Nov 10 2009 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- preliminary support of http clients was added
- more unit tests

* Thu Oct 15 2009 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- socket.c: add support for unix domain sockets
- (vhttpd): add (make-unix-server-socket) and (make-unix-client-socket)

* Thu Jul 23 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt9
- fix utf-8 encoding name in content-type detection code

* Thu May 21 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt8
- add "close-on-exec" flag to all used descriptors

* Wed May 06 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt7
- fix content-type field value in file responses

* Tue May 05 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt6
- fix buffer length calculation

* Wed Apr 22 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt5
- scm_to_local_string: rewrite to modern style
- remove wrong printf

* Tue Apr 21 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt4
- fix make-string-response function

* Thu Mar 12 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt3
- use RPM_OPT_FLAGS
- fix work with va_args

* Thu Dec 11 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- little updates for guile-1.8
- improve makefile
- export encode-url-component

* Tue Dec 09 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- switch to guile-1.8

* Mon Nov 24 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt8
- fix format string error

* Thu Nov 20 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt7
- fix requires

* Tue Nov 18 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt6
- new utils: encode-url-component, decode-url-component

* Tue Nov 11 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt5
- add unit tests

* Thu Sep 25 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt4
- little code improvements

* Fri Aug 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt3
- remove libvhttpdutil library

* Thu Aug 21 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt2
- rebuild

* Mon Aug 18 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- add functions for daemon creation (daemonize, drop_privs)
- add guile bindings

* Mon Jun 30 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt12
- basic_auth_get_cred: fix latest fix

* Thu Jun 26 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt11
- fix segfault

* Sun May 04 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt10
- parse cookie header

* Mon Apr 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt9
- fix error with retcode in tls_openssl.c/_handshake

* Fri Mar 14 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt8
- fix tls shutdown, minor code improvements

* Fri Feb 15 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt7
- fix typo

* Fri Feb 15 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt6
- use openssl

* Wed Feb 13 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt5
- add utils subpackage

* Tue Feb 12 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4
- use '%%m' instead of strerror

* Mon Feb 11 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- fix start-line parsing (doesn't allow tabs)
- add raw start line to message (useful for logs)

* Fri Feb 08 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- add config file reload feature

* Sun Feb 03 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- add http_strerror function

* Wed Jan 16 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt10
- add support for if-modified-since header

* Mon Jan 14 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt9
- add more additional information to request package

* Mon Jan 14 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt8
- improve API (rename log_error to runtime_error)

* Sat Jan 12 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt7
- improve message logging

* Wed Dec 12 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt6
- cookie support

* Tue Dec 11 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt5
- add basic auth support

* Fri Dec 07 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- add config file support

* Tue Dec 04 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- add static handler to util library

* Fri Nov 30 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- ssl are ready to use

* Fri Nov 23 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
