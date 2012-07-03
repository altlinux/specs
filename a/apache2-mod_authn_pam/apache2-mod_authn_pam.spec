%define oname mod_authn_pam
Summary: PAM authentication module for Apache
Name: apache2-mod_authn_pam
Version: 0.0.1
Release: alt1
License: GPL
Group: System/Servers
Packager: Boris Savelev <boris@altlinux.org>
Url: http://mod-auth.sourceforge.net
Source: %oname-%version.tar.gz
Source1: authn_pam.load
Source2: authn_pam.usage
Source3: httpd2

# Automatically added by buildreq on Mon Sep 29 2008
BuildRequires: apache2-devel libpam-devel

%description
The PAM authentication module implements Basic authentication on top of the
Pluggable Authentication Module library. Thereby it supports standard unix
passwd, shadow, NIS, SMB auth and radius authentication transparently and
easily interchangeable, wherever the HTTP protocol allows it.
Build for apache2.

%prep
%setup -n %oname-%version
subst 's|pam_servicename = "httpd"|pam_servicename = "apache2"|g' src/%oname.c

%build
cd src && %apache2_apxs -c -o mod_authn_pam.so -lpam mod_authn_pam.c

%install
mkdir -p %buildroot%apache2_moduledir
mkdir -p %buildroot%apache2_mods_available
mkdir -p %buildroot%_sysconfdir/pam.d
install -m 644 src/.libs/*.so %buildroot%apache2_moduledir
install -m 644 %SOURCE1 %buildroot%apache2_mods_available
install -m 644 %SOURCE2 %_builddir/%oname-%version
install -m 644 %SOURCE3 %buildroot%_sysconfdir/pam.d/apache2

%files
%doc README INSTALL authn_pam.usage
%apache2_mods_available/*.load
%apache2_moduledir/*.so
%_sysconfdir/pam.d/apache2

%changelog
* Mon Aug 24 2009 Boris Savelev <boris@altlinux.org> 0.0.1-alt1
- initial build

