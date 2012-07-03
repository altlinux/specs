%define oname mod_authz_external
Summary: flexible tools for building custom basic authentication systems for the Apache HTTP Daemon
Name: apache2-mod_authz_external
Version: 3.2.4
Release: alt1
License: GPL
Group: System/Servers
Packager: Boris Savelev <boris@altlinux.org>
Url: http://code.google.com/p/mod-auth-external/
Source: %oname-%version.tar

# Automatically added by buildreq on Mon Sep 29 2008
BuildRequires: apache2-devel

%description
Mod_authnz_external and mod_auth_external are flexible tools for
building custom basic authentication systems for the Apache HTTP Daemon.
"Basic Authentication" is a type of authentication built into the HTTP protocol,
in which the browser automatically pops up a login box when the user requests a
protected resource, and the login ids and passwords entered are checked by
Apache. Mod_auth*_external allows the password checking normally done inside
Apache to be done by an separate external program running outside of Apache.

%prep
%setup -n %oname-%version

%build
%make APXS=%apache2_apxs build

%install
mkdir -p %buildroot{%apache2_moduledir,%apache2_mods_available,%_datadir/%oname}
install -m 644 .libs/*.so %buildroot%apache2_moduledir
install -m 644 authz_external.load %buildroot%apache2_mods_available

%files
%doc README INSTALL INSTALL.HARDCODE AUTHENTICATORS CHANGES UPGRADE TODO
%apache2_mods_available/*.load
%apache2_moduledir/*.so

%changelog
* Tue Aug 25 2009 Boris Savelev <boris@altlinux.org> 3.2.4-alt1
- intial build

