Name: apache2-mod_auth_ahttpd
Version: 1.0.0
Release: alt3

Summary: Alterator-FBI authentication module for Apache 2 HTTP Server
License: Apache (BSD-like)
Group: System/Servers

Url: http://git.altlinux.org/people/manowar/packages/mod_auth_ahttpd.git

Source0: mod_auth_ahttpd-%version.tar
Source1: auth_ahttpd.load

Requires: apache2

BuildRequires: apache2-devel apache2-suexec man libcurl-devel libssl-devel libjson-devel libsqlite3-devel

%description
Alterator-FBI authentication module for Apache 2 HTTP Server. It uses
new ahttpd feature /ahttpd-cache/session/<session-id> to validate the
"session" cookie.

%prep
%setup -n mod_auth_ahttpd-%version

%build
%_sbindir/apxs2 -lssl -lcurl -ljson -lsqlite3 -c -Wc,-std=gnu99 mod_auth_ahttpd.c

%install
install -pDm0644 .libs/mod_auth_ahttpd.so %buildroot%_libdir/apache2/modules/mod_auth_ahttpd.so
install -pDm0644 %SOURCE1 %buildroot%_sysconfdir/httpd2/conf/mods-available/auth_ahttpd.load

%post
a2enmod auth_ahttpd >/dev/null
%_initdir/httpd2 condreload

%preun
if [ $1 -eq 0 ]; then
	a2dismod auth_ahttpd
	%_initdir/httpd2 condreload
fi

%files
%config(noreplace) %_sysconfdir/httpd2/conf/mods-available/auth_ahttpd.load
%_libdir/apache2/modules/*

%changelog
* Mon Sep 24 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0.0-alt3
- Handle 404 response from the ahttpd server.
- Track the session IDs of protected sites (using an sqlite3 DB).

* Thu Sep 20 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0.0-alt2
- Fix the absolute path in the module loader.

* Thu Sep 20 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0.0-alt1
- Initial release for ALT Linux.
