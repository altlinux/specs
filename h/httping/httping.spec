Name: httping
Version: 1.5.2
Release: alt1

Summary: Ping alike tool for http requests
License: GPLv2
Group: Monitoring

Url: http://www.vanheusden.com/httping/
Source: %url/httping-%version.tgz

# Automatically added by buildreq on Fri Feb 20 2009
BuildRequires: libssl-devel

%description
Httping is like 'ping' but for http-requests. Give it an url, and it'll
show you how long it takes to connect, send a request and retrieve the
reply. Be aware that the transmission across the network also takes time!

%prep
%setup

%build
subst 's/#include "str.h"//' http.c main.c
subst 's/-O./%optflags/; s/str.o//' Makefile
%make_build

%install
install -d %buildroot{%_bindir/,%_man1dir/}
%makeinstall_std STRIP=#

%files
%doc license.txt license.OpenSSL readme.txt
%_bindir/*
%_man1dir/*

%changelog
* Sat Aug 13 2011 Victor Forsiuk <force@altlinux.org> 1.5.2-alt1
- 1.5.2

* Sun Jul 31 2011 Victor Forsiuk <force@altlinux.org> 1.5.1-alt1
- 1.5.1

* Tue Dec 07 2010 Victor Forsiuk <force@altlinux.org> 1.4.4-alt2
- Rebuild with libssl10.

* Fri Aug 13 2010 Victor Forsiuk <force@altlinux.org> 1.4.4-alt1
- 1.4.4

* Mon Jul 12 2010 Victor Forsiuk <force@altlinux.org> 1.4.3-alt1
- 1.4.3

* Thu Jan 14 2010 Victor Forsyuk <force@altlinux.org> 1.4.1-alt1
- 1.4.1

* Thu Aug 06 2009 Victor Forsyuk <force@altlinux.org> 1.3.1-alt1
- 1.3.1

* Mon Jun 15 2009 Victor Forsyuk <force@altlinux.org> 1.3.0-alt2
- Fix FTBFS due to conflicting definitions.

* Fri Feb 20 2009 Victor Forsyuk <force@altlinux.org> 1.3.0-alt1
- 1.3.0

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.9-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Wed Jul 30 2008 Victor Forsyuk <force@altlinux.org> 1.2.9-alt1
- 1.2.9

* Tue Jul 01 2008 Victor Forsyuk <force@altlinux.org> 1.2.8-alt1
- 1.2.8

* Mon May 26 2008 Victor Forsyuk <force@altlinux.org> 1.2.6-alt1
- 1.2.6

* Mon Jul 30 2007 Victor Forsyuk <force@altlinux.org> 1.2.5-alt1
- 1.2.5

* Tue Jul 10 2007 Victor Forsyuk <force@altlinux.org> 1.2.4-alt1
- 1.2.4

* Mon May 07 2007 Victor Forsyuk <force@altlinux.org> 1.2.3-alt1
- 1.2.3

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.2-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Wed Nov 22 2006 Victor Forsyuk <force@altlinux.org> 1.2.2-alt1
- 1.2.2

* Thu Aug 03 2006 Victor Forsyuk <force@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Tue Jan 17 2006 Victor Forsyuk <force@altlinux.ru> 1.0.10-alt1
- 1.0.10

* Mon Nov 21 2005 Victor Forsyuk <force@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Mon Nov 07 2005 Victor Forsyuk <force@altlinux.ru> 1.0.6-alt1
- Initial build.
