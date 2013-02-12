Name: %apache2_name-mod_auth_ahttpd
Version: 1.0.0
Release: alt4.1

Summary: Alterator-FBI authentication module for Apache 2 HTTP Server
License: Apache (BSD-like)
Group: System/Servers

Url: http://git.altlinux.org/people/manowar/packages/mod_auth_ahttpd.git

Source0: mod_auth_ahttpd-%version.tar
Source1: auth_ahttpd.load
Source2: auth_ahttpd.start

Requires: %apache2_name-base > 2.2.22-alt15
Requires: %apache2_name-mmn = %apache2_mmn
Requires: %apache2_libaprutil_name >= %apache2_libaprutil_evr
Requires: %apache2_libapr_name >= %apache2_libapr_evr

BuildRequires(pre): apache2-devel > 2.2.22-alt15
BuildRequires: libcurl-devel libssl-devel libjson-devel libsqlite3-devel

%description
Alterator-FBI authentication module for Apache 2 HTTP Server. It uses
new ahttpd feature /ahttpd-cache/session/<session-id> to validate the
"session" cookie.

%prep
%setup -n mod_auth_ahttpd-%version

%build
%apache2_apxs -lssl -lcurl -ljson -lsqlite3 -c -Wc,-std=gnu99 mod_auth_ahttpd.c

%install
install -pDm0644 .libs/mod_auth_ahttpd.so %buildroot%apache2_moduledir/mod_auth_ahttpd.so
install -pDm0644 %SOURCE1 %buildroot%apache2_mods_available/auth_ahttpd.load
install -pDm0644 %SOURCE2 %buildroot%apache2_mods_start/100-auth_ahttpd.conf

# for %%ghost
mkdir -p %buildroot%apache2_mods_enabled/
touch %buildroot%apache2_mods_enabled/auth_ahttpd.load

%files
%config(noreplace) %apache2_mods_available/auth_ahttpd.load
%config(noreplace) %apache2_mods_start/100-auth_ahttpd.conf
%ghost %apache2_mods_enabled/*.load
%apache2_moduledir/*

%changelog
* Fri Feb 08 2013 Aleksey Avdeev <solo@altlinux.ru> 1.0.0-alt4.1
- Rebuild with apache2-2.2.22-alt16 (fix unmets).
- Add %%apache2_mods_start/100-auth_ahttpd.conf file for auto loading
  module.
- Add %%ghost for %%apache2_mods_enabled/*.load.

* Tue Feb 05 2013 Paul Wolneykien <manowar@altlinux.ru> 1.0.0-alt4
- Fix: do not require apache2-suexec.

* Mon Sep 24 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0.0-alt3
- Handle 404 response from the ahttpd server.
- Track the session IDs of protected sites (using an sqlite3 DB).

* Thu Sep 20 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0.0-alt2
- Fix the absolute path in the module loader.

* Thu Sep 20 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0.0-alt1
- Initial release for ALT Linux.
