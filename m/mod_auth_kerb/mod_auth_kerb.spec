Summary: An Apache authentication module using Kerberos.
Name: mod_auth_kerb
Version: 5.3
Release: alt1
License: GPL
Group: System/Servers
Packager: Boris Savelev <boris@altlinux.org>
Url: http://modauthkerb.sourceforge.net
Source: %name-%version.tar.gz
Source1: auth_krb5.load
Source2: auth_krb5.conf.sample

# Automatically added by buildreq on Mon Sep 29 2008
BuildRequires: apache-devel apache2-devel libcom_err-devel libkrb5-devel

%description
Mod_auth_kerb is a module that provides Kerberos user authentication to the Apache web server.
It allows to retrieve the username/password pair, and also supports full Kerberos authentication
(also known as Negotiate or SPNEGO based authentication).

%package -n apache-%name
Summary: An Apache authentication module using Kerberos.
Group: System/Servers

%package -n apache2-%name
Summary: An Apache 2 authentication module using Kerberos.
Group: System/Servers

%description -n apache-%name
Mod_auth_kerb is a module that provides Kerberos user authentication to the Apache web server.
It allows to retrieve the username/password pair, and also supports full Kerberos authentication
(also known as Negotiate or SPNEGO based authentication).
Build for apache.

%description -n apache2-%name
Mod_auth_kerb is a module that provides Kerberos user authentication to the Apache web server.
It allows to retrieve the username/password pair, and also supports full Kerberos authentication
(also known as Negotiate or SPNEGO based authentication).
Build for apache2.

%prep
%setup

%build
# apache-1
export APXS=%_sbindir/apxs
./configure \
			--with-krb5=%_prefix \
			--without-krb4
%make_build
cp -a src apache1
%make clean

# apache-2
export APXS=%_sbindir/apxs2
./configure \
			--with-krb5=%_prefix \
			--without-krb4
%make_build
cp -a src apache2

%install
mkdir -p %buildroot%apache_moduledir
mkdir -p %buildroot%apache2_moduledir
mkdir -p %buildroot%apache2_mods_available
install -m 644 apache1/*.so %buildroot%apache_moduledir
install -m 644 apache2/.libs/*.so %buildroot%apache2_moduledir
install -m 644 %SOURCE1 %buildroot%apache2_mods_available
install -m 644 %SOURCE2 %_builddir/%name-%version

%files -n apache-%name
%doc README INSTALL
%apache_moduledir/*.so

%files -n apache2-%name
%doc README INSTALL auth_krb5.conf.sample
%apache2_mods_available/*.load
%apache2_moduledir/*.so

%changelog
* Mon Sep 29 2008 Boris Savelev <boris@altlinux.org> 5.3-alt1
- initial build for Sisyphus

