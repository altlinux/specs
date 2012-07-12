Name: medusa
Version: 2.0
Release: alt1.5

Summary: Medusa is intended to be a speedy, massively parallel, modular, login brute-forcer
License: GPLv2
Group: Networking/Other
Url: http://www.foofus.net
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
Source0: %name-%version.tar.gz
Patch0: medusa-2.0-alt-DSO.patch

# Automatically added by buildreq on Tue May 26 2009
BuildRequires: libssh2-devel libncp-devel libssl-devel libapr1-devel postgresql-devel librtmp-devel libsubversion-devel postfix telnet perl-LWPx-ParanoidAgent
#BuildRequires: libapr1-devel libsubversion-devel

%description
Medusa is intended to be a speedy, massively parallel,  modular,  login
brute-forcer.   The  goal  is  to  support as many services which allow
remote authentication as possible. The author considers following items
to some of the key features of this application:

*Thread-based  parallel  testing.  Brute-force testing can be performed
against multiple hosts, users or passwords concurrently.

*Flexible user input. Target information  (host/user/password)  can  be
specified  in a variety of ways. For example, each item can be either a
single entry or a file containing  multiple  entries.  Additionally,  a
combination file format allows the user to refine their target listing.

*Modular  design.  Each  service  module  exists as an independent .mod
file. This means that no modifications are necessary to the core appli-
cation  in  order  when  extending  the  supported list of services for
brute-forcing.

%package doc
Summary: Documentation for %name
Group: Documentation
Requires: %name = %version-%release
%description doc
Documentation for %name

%package module-ncp
Summary: Brute force module for NCP sessions
Group: Networking/Other
Requires: %name = %version-%release
%description module-ncp
Brute force module for NCP sessions

%package module-postgres
Summary: Brute force module for PostgreSQL sessions
Group: Networking/Other
Requires: %name = %version-%release
%description module-postgres
Brute force module for PostgreSQL sessions

%package module-mail
Summary: Brute force module for mail services
Group: Networking/Other
Requires: %name = %version-%release
%description module-mail
Brute force module for mail services

%package module-http
Summary: Brute force module for HTTP
Group: Networking/Other
Requires: %name = %version-%release
%description module-http
Brute force module for HTTP

%package module-wrapper
Summary: Generic Wrapper Module
Group: Networking/Other
Requires: %name = %version-%release
%description module-wrapper
Generic Wrapper Module

%package module-svn
Summary: Brute force module for svn
Group: Networking/Other
Requires: %name = %version-%release libsubversion
%description module-svn
Brute force module for svn

%prep
%setup
%patch0 -p2
sed -i "s|/include/postgresql|/include/pgsql|g" configure.in
sed -i "s|/usr/local/include|/usr/include|g" configure.in
sed -i "s|/usr/local/ssl/include|/usr/include/openssl|g" configure.in
sed -i "s|/usr/local/lib|%_libdir|g" configure.in
sed -i "s|apr-1.0|apr-1|g" configure.in


%build
%autoreconf
%configure
%make LIBS="-lssl -lcrypto -rdynamic -ldl -lrt -lm -lncp -lssh2 -lpostfix-$(rpmquery --qf %%{version} postfix) -lpq"

%install
%makeinstall_std
mkdir -p %buildroot%perl_vendor_privlib/%name
install -m644 src/modsrc/wrapper/apache-userdir.pl %buildroot%perl_vendor_privlib/%name/
install -m644 src/modsrc/wrapper/null-session.pl %buildroot%perl_vendor_privlib/%name/
install -m644 src/modsrc/wrapper/sample-single.pl %buildroot%perl_vendor_privlib/%name/
install -m644 src/modsrc/wrapper/sample-stdin.pl %buildroot%perl_vendor_privlib/%name/


%files
%_bindir/*
%_libdir/%name
%_man1dir/*

%exclude %_libdir/%name/modules/ncp.mod
%exclude %_libdir/%name/modules/postgres.mod
%exclude %_libdir/%name/modules/smtp*
%exclude %_libdir/%name/modules/pop3.mod
%exclude %_libdir/%name/modules/imap.mod
%exclude %_libdir/%name/modules/http.mod
%exclude %_libdir/%name/modules/wrapper.mod
%exclude %_libdir/%name/modules/svn.mod


%files doc
%doc doc/*.html

%files module-ncp
%_libdir/%name/modules/ncp.mod

%files module-postgres
%_libdir/%name/modules/postgres.mod

%files module-mail
%_libdir/%name/modules/smtp*
%_libdir/%name/modules/pop3.mod
%_libdir/%name/modules/imap.mod

%files module-http
%_libdir/%name/modules/http.mod

%files module-wrapper
%_libdir/%name/modules/wrapper.mod
%perl_vendor_privlib/%name

%files module-svn
%_libdir/%name/modules/svn.mod

%changelog
* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.5
- Fixed build

* Thu Jul 14 2011 Dmitry V. Levin <ldv@altlinux.org> 2.0-alt1.4
- Blind rebuild with postfix-2.5.14.

* Mon May 09 2011 Dmitry V. Levin <ldv@altlinux.org> 2.0-alt1.3
- Blind rebuild with postfix-2.5.13.

* Tue Mar 08 2011 Dmitry V. Levin <ldv@altlinux.org> 2.0-alt1.2
- Blind rebuild with postfix-2.5.12.

* Sat Dec 04 2010 Dmitry V. Levin <ldv@altlinux.org> 2.0-alt1.1
- Blind rebuild with postfix-2.5.11.

* Wed Oct 20 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0-alt1
- New version

* Tue May 26 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.5-alt1
- Build for ALT
