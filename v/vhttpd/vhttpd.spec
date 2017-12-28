Name: vhttpd
Version: 0.7.8
Release: alt1

Summary: simple embedded web server
License: LGPL
Group: System/Servers

Source:%name-%version.tar

%ifarch e2k
Buildrequires: guile20-devel libguile20-devel /proc
%else
BuildRequires: guile22-devel >= 2.2.0-alt2
%endif
BuildPreReq: glib2-devel libssl-devel libgnutls-devel cgreen

Conflicts: alterator < 4.17-alt1
Conflicts: alterator-fbi < 5.26-alt1

%description
voins httpd - port of the first alterators web server.

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
Group: Development/Scheme
Requires(pre): lib%name = %version-%release

%description -n libguile-%name
guile bindings for %name

%prep
%setup
%ifarch e2k
sed -i 's:guile/2.2:guile/2.0:g' guile/Makefile
%endif

%build
%make_build

%check
%make check

%install
%makeinstall

%brp_strip_none %guile_ccachedir/vhttpd.go
%add_verify_elf_skiplist %guile_ccachedir/vhttpd.go
%add_findreq_skiplist %guile_ccachedir/vhttpd.go

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files utils
%_bindir/*

%files -n libguile-%name
%guile_extensiondir/libguile-vhttpd.so
%guile_ccachedir/vhttpd.go

%changelog
* Wed Dec 27 2017 Paul Wolneykien <manowar@altlinux.org> 0.7.8-alt1
- Fix: Make the Guile library locale-independent: use
  scm_from/to_utf8_string() instead of from/to_locale.
- Fix: Use LOG_ERR insstead of LOG_EMERG.
- Fix the dependency tracker: use CFLAGS instead of CPPFLAGS that
  is unset.

* Thu Nov 30 2017 Andrew Savchenko <bircoph@altlinux.org> 0.7.7-alt2
- Add E2K and guile20 support.

* Tue Apr 18 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.7-alt2
- cleanup fallout from guile2 transition

* Fri Mar 31 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.7-alt1
- rebuilt with guile2

* Tue Sep 15 2015 Mikhail Efremov <sem@altlinux.org> 0.7.6-alt1
- Declare request_server() in the http_client.h.
- Add missing include.
- Fix signed/unsigned comparison warning.
- Use retcode_t instead of int in struct error_entry_t.
- Fix buffer overflow in case of IPv6.

* Fri Aug 08 2014 Mikhail Efremov <sem@altlinux.org> 0.7.5-alt1
- Fix work without IPv6.

* Tue Dec 25 2012 Mikhail Efremov <sem@altlinux.org> 0.7.4-alt1
- Fix data recieving in case of SSL connection.

* Fri Aug 17 2012 Mikhail Efremov <sem@altlinux.org> 0.7.3-alt1
- tests: Increase delay after server's process start.
- tests: Add create_server_from_socket() test.
- Use IPv6 if possible.
- Create channels from an existing socket.

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
