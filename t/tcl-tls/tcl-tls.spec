Name: tcl-tls
Version: 1.6.1
Release: alt1

Summary: A tcl extension, wich adds SSL ability to any Tcl channel
License: BSD
Group: Development/Tcl
Url: http://tls.sourceforge.net/

Source: %name-%version.tar

BuildPreReq:  rpm-build-tcl >= 0.2-alt1
BuildRequires: libssl-devel tcl-devel >= 8.4.0-alt1
Requires: tcl >= 8.4.0-alt1

%description
TLS is a Tcl extension, wich adds SSL ability to any Tcl channel.
Both client and server-side sockets are possible, and this code should work
on any platform as it uses a generic mechanism for layering on SSL and Tcl. 

%prep
%setup
%teapatch

%build
autoconf
%configure --disable-rpath
make

%install
%makeinstall

%files
%doc ChangeLog README.txt license.terms tls.htm
%_tcllibdir/libtls%version.so
%_tcldatadir/tls%version

%changelog
* Mon Dec 06 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.1-alt1
- 1.6.1 released

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.5.1-alt4.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Mon Jun 25 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt4
- CVS snapshot @20070623

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.5.1-alt3.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sat Jul 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt3
- fixed build on x86_64

* Fri Jan 20 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt2
- fixed unresolved symbols, appeared in prev build

* Tue Jan 10 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt1
- CVS snapshot @20050208

* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.0-alt2
- CVS snapshot @20040629

* Fri May 14 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Wed May 12 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.4.1-alt9.1.1
- Rebuilt with openssl-0.9.7d.

* Wed May 12 2004 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt9.1
- Fixed packager tag.

* Tue Sep 24 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.4.1-alt9
- rebuilt with tcl 8.4

* Fri Jun  7 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.4.1-alt8
- updated from cvs
- rebuilt in new env
- src rpm splitted
