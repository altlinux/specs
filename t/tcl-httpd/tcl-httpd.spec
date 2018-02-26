%define teaname tclhttpd
%define docroot %_var/www/%teaname
%define sitedir %_datadir/site-%teaname

Name: tcl-httpd
Version: 3.5.1
Release: alt1

%define docdir %_defaultdocdir/%name-%version/
%define htdocs %docdir/htdocs

Summary: A pure-tcl implementation of a Web server
License: BSD
Group: Development/Tcl
Url: http://%teaname.sourceforge.net/

Source0: %name-%version-%release.tar
 
Requires: tcl >= 8.4.0-alt1
BuildRequires: tcl-devel >= 8.4.0-alt1 rpm-build >= 4.0.4-alt41

%package core
Summary: A core of tcl implementation of a Web server
Group: Development/Tcl
Provides: %sitedir
Provides: %docroot

%package server
Summary: A standalone %teaname server
Group: System/Servers
Requires: %name-core = %version-%release
Provides: %_sysconfdir/%teaname/config.d

%package manual
Summary: A %teaname documentation
Group: System/Servers
Requires: %_sysconfdir/%teaname/config.d
Requires: %name-server = %version-%release

%package extra
Summary: Compiled addons to a %teaname
Group: Development/Tcl
Requires: tcl >= 8.4.0-alt1

# {{{ descriptions

%description
While this server works fine as a stand alone web server, the intent
is to embed the server in other applications in order to "web enable"
them. A Tcl-based web server is ideal for embedding because Tcl was
designed from the start to support embedding into other applications.
The interpreted nature of Tcl allows dynamic reconfiguration of the
server. Once the core interface between the web server and the hosting
application is defined, it is possible to manage the web server,
upload Safe-Tcl control scripts, download logging information, and
otherwise debug the Tcl part of the application without restarting the
hosting application.

%description core
While this server works fine as a stand alone web server, the intent
is to embed the server in other applications in order to "web enable"
them. A Tcl-based web server is ideal for embedding because Tcl was
designed from the start to support embedding into other applications.
The interpreted nature of Tcl allows dynamic reconfiguration of the
server. Once the core interface between the web server and the hosting
application is defined, it is possible to manage the web server,
upload Safe-Tcl control scripts, download logging information, and
otherwise debug the Tcl part of the application without restarting the
hosting application.

This package provides core of a %name and can be used as base
for custom/embedded httpd implementation 

%description server
While this server works fine as a stand alone web server, the intent
is to embed the server in other applications in order to "web enable"
them. A Tcl-based web server is ideal for embedding because Tcl was
designed from the start to support embedding into other applications.
The interpreted nature of Tcl allows dynamic reconfiguration of the
server. Once the core interface between the web server and the hosting
application is defined, it is possible to manage the web server,
upload Safe-Tcl control scripts, download logging information, and
otherwise debug the Tcl part of the application without restarting the
hosting application.

This package provides setup for runnig standalone %name

%description manual
While this server works fine as a stand alone web server, the intent
is to embed the server in other applications in order to "web enable"
them. A Tcl-based web server is ideal for embedding because Tcl was
designed from the start to support embedding into other applications.
The interpreted nature of Tcl allows dynamic reconfiguration of the
server. Once the core interface between the web server and the hosting
application is defined, it is possible to manage the web server,
upload Safe-Tcl control scripts, download logging information, and
otherwise debug the Tcl part of the application without restarting the
hosting application.

This package provides online manual for a %name

%description extra
While this server works fine as a stand alone web server, the intent
is to embed the server in other applications in order to "web enable"
them. A Tcl-based web server is ideal for embedding because Tcl was
designed from the start to support embedding into other applications.
The interpreted nature of Tcl allows dynamic reconfiguration of the
server. Once the core interface between the web server and the hosting
application is defined, it is possible to manage the web server,
upload Safe-Tcl control scripts, download logging information, and
otherwise debug the Tcl part of the application without restarting the
hosting application.

This package provides two compiled addons to a %name:
- crypt, another interface to  crypt(); other option is tcl-trf
  package (recommended) or builtin tcl-only realization (quite slow);
- limit, interface to set|getrlimit(RLIMIT_NOFILE, ...);
Alltough, these packages can be used independenty too.

# }}}
 
%prep
%setup
sed -i 's/@lib@/%_lib/' *_pkgIndex.tcl.in

%build
%__autoconf
%configure \
	--with-serverroot=%docroot \
	--with-sitedir=%sitedir \
	--with-htdocs=%htdocs

%make_build

%install
%make_install DESTDIR=%buildroot install
mkdir -p %buildroot{%_sysconfdir/%teaname/{config.d,certs},%_logdir/%teaname,%_var/run/%teaname}
cp -a sampleapp %buildroot%docdir
mv %buildroot%docroot/README* %buildroot%docdir
mv %buildroot%_man1dir/httpd.1 %buildroot%_man1dir/%teaname.1
install -pm0755 -D bin/tclhttpd %buildroot%_sbindir/%teaname
install -pm0644 bin/config %buildroot%_sysconfdir/%teaname/config
install -pm0644 bin/httpdthread.tcl %buildroot%_sysconfdir/%teaname/main
install -m0755 -D tclhttpd.init %buildroot%_initdir/%teaname
cat <<EOF > %buildroot%_sysconfdir/%teaname/config.d/manual
#Config docRoot %htdocs
EOF

%pre server
%_sbindir/groupadd -r -f webmaster &>/dev/null ||:
%_sbindir/groupadd -r -f %teaname &>/dev/null ||:
%_sbindir/useradd -r -g %teaname -d %_var/www/%teaname -s /dev/null \
    -c "TclHTTPD Web Server" -M -n %teaname &>/dev/null ||:

%post server
%post_service %teaname

%preun server
%preun_service %teaname

%post manual
%post_service %teaname

%files core
%_tcldatadir/%teaname%version
%dir %sitedir
%sitedir/zzzdodirs.tcl
%_defaultdocdir/%name-%version/README*
%_man1dir/*

%files server
%dir %_sysconfdir/%teaname
%dir %_sysconfdir/%teaname/config.d
%attr(0750,root,%teaname) %dir %_sysconfdir/%teaname/certs
%config(noreplace) %_sysconfdir/%teaname/config
%config(noreplace) %_sysconfdir/%teaname/main
%_initdir/%teaname
%_sbindir/%teaname
%attr(2775,root,webmaster) %dir %docroot
%attr(2770,root,%teaname) %dir %_logdir/%teaname
%attr(0730,root,%teaname) %dir %_var/run/%teaname

%files manual
%config(noreplace) %_sysconfdir/%teaname/config.d/manual
%_defaultdocdir/%name-%version/sampleapp
%_defaultdocdir/%name-%version/htdocs
%sitedir/faq.tcl
%sitedir/mypage.tcl
%sitedir/hello.tcl

%files extra
%_tcllibdir/libcrypt1.0.so
%_tcllibdir/liblimit1.0.so
%_tcldatadir/crypt1.0 
%_tcldatadir/limit1.0

%changelog
* Sun Aug 31 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.5.1-alt1
- rebuilt against tcl8.5

* Mon Jan  7 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.5.1-alt0.5
- CVS snapshot @20061110

* Sun Jul 23 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.5.1-alt0.4
- CVS snapshot @20050426
- fixed indices on x86_64

* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.5.1-alt0.3
- CVS snapshot @20041028

* Mon Sep 20 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.5.1-alt0.2
- CVS snapshot @20040905

* Tue May 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.5.1-alt0.1
- first build for %distribution
