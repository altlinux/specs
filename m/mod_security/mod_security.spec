Name: mod_security
Version: 1.9.5
Release: alt2

Summary: Tighten web applications security for Apache 1.3
License: GPL
Group: System/Servers

Url: http://www.modsecurity.org
Source0: %url/download/modsecurity-apache_%version.tar.gz
Source1: %name.apache.conf
Source2: %name.apache2.conf
Source3: %name.README.ALT
#Source4: %name.modsec.sh
Source5: %name.altdefaults.conf
Packager: Vladimir V Kamarzin <vvk@altlinux.ru>

Requires: apache, %name-common

# Automatically added by buildreq on Sat Dec 06 2008
BuildRequires: apache-devel

BuildPreReq: rpm-build-apache

%define modsec_uploaddir %_cachedir/httpd/modsec

%description
Mod_security is an Apache 1.x/2.x module whose purpose is to tighten the Web
application security. Effectively, it is an intrusion detection and prevention
system for the web server.

At the moment its main features are:
* Audit log; store full request details in a separate file, including POST
payloads.
* Request filtering; incoming requests can be analysed and offensive requests
can be rejected (or simply logged, if that is what you want). This feature
can be used to prevent many types of attacks (e.g. XSS attacks, SQL
injection, ...) and even allow you to run insecure applications on your
servers (if you have no other choice, of course).

%package common
Summary: Common stuff for %name module
Group: System/Servers

%description common
%summary

%package doc
Summary: Documentation for %name module
Group: System/Servers
BuildArch: noarch

%description doc
%summary

%prep
%setup -q -n modsecurity-apache_%version
subst 's,#SecUploadDir /tmp$,SecUploadDir %modsec_uploaddir,' %SOURCE1

%build
%_sbindir/apxs -c apache1/mod_security.c

%install
install -pD -m644 apache1/%name.so %buildroot%_libdir/apache/%name.so
install -pD -m644 %SOURCE1 %buildroot%_sysconfdir/httpd/conf/addon-modules.d/%name.conf
install -p -m644 %SOURCE3 README.ALT

# gotroot rules updater (apache1)
#install -p -m0755 %%SOURCE4 modsec-apache1.sh
#subst "s,/usr/local/apache2/bin/apachectl,%_sbindir/apachectl,g" modsec-apache1.sh
#subst "s,/usr/local/apache2/conf/modsecurity,%_sysconfdir/%name,g" modsec-apache1.sh

# gotroot rules updater (apache2)
#install -p -m0755 %%SOURCE4 modsec-apache2.sh
#subst "s,/usr/local/apache2/bin/apachectl,%_sbindir/apachectl2,g" modsec-apache2.sh
#subst "s,/usr/local/apache2/conf/modsecurity,%_sysconfdir/%name,g" modsec-apache2.sh

# alt default ruleset
install -pD -m644 %SOURCE5 %buildroot%_sysconfdir/%name/altdefaults.conf

# private SecUploadDir
install -d -m1770 %buildroot%modsec_uploaddir

%post
# fix stale actions
# FIXME: should be replaced with addon-modules.d/ file
subst "/Include conf\/addon-modules\/mod_security\.conf/d" %_sysconfdir/httpd/conf/httpd.conf
%_sbindir/apachectl reload

%postun
%_sbindir/apachectl reload

%files
%_libdir/apache/%name.so
%config(noreplace) %_sysconfdir/httpd/conf/addon-modules.d/%name.conf
%dir %attr(1770,root,%apache_group) %modsec_uploaddir

%files common
%config(noreplace) %_sysconfdir/%name/*
%dir %_sysconfdir/%name

%files doc
%doc CHANGES README* httpd.conf.example-minimal util doc

%changelog
* Tue Apr 28 2009 Denis Smirnov <mithraen@altlinux.ru> 1.9.5-alt2
- comment SecRule

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 1.9.5-alt1
- 1.9.5
- minor spec cleanup
- noarch docs
- buildreq

* Tue Oct 02 2007 Michael Shigorin <mike@altlinux.org> 1.9.4-alt6
- Moved default SecUploadDir
  from implicit /tmp
    to explicit %modsec_uploaddir
  (works better with /tmp being non-writable for apache user)

* Thu Apr 05 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.9.4-alt5
- Add workaround for fix security bug in mod_security < 2.1.0 (Closes: #11035)

* Fri Mar 09 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.9.4-alt4
- Build only apache1 module

* Fri Oct 06 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.9.4-alt3
- Whoops, really fix path to module (Closes: #10089)

* Tue Sep 26 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.9.4-alt2
- Don't use full path to mod_security.so in apache config because it make
  troubles on x86_64 (reported by thresh@)

* Thu Jun 01 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.9.4-alt1
- 1.9.4

* Thu Apr 20 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.9.3-alt1
- 1.9.3

* Wed Feb 01 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.9.2-alt1
- New version
- Don't use %%a_libexecdir macros

* Mon Dec 12 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.9.1-alt1
- New version (bugfix release)
- Provide default apache-related config with some rules
- Common stuff moved into -common package
- Updated README.ALT

* Mon Nov 07 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.9-alt1
- New version

* Thu Sep 01 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.8.7-alt3
- Splited to several parts by reason:
- Now building module for apache2 also
- Minor spec cleanup
- Changed Group

* Wed Aug 24 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.8.7-alt2
- Fixed config installation (should really go to addonconfdir.d/) (thanks to mike@)
- Remove previous config inclusion from httpd.conf (thanks to mike@)
- Minor spec cleanup
- Added README.ALT (mike@)

* Wed Jul 20 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.8.7-alt1
- Initial build for Sisyphus
