%def_without apache1

Summary: An Apache authentication module using Kerberos.
Name: mod_auth_kerb
Version: 5.4
Release: alt1
License: GPL
Group: System/Servers
Packager: Boris Savelev <boris@altlinux.org>
Url: http://modauthkerb.sourceforge.net
Source: %name-%version.tar.gz
Source2: auth_krb5.conf.sample
Patch1: mod_auth_kerb-5.4-rcopshack.patch
Patch2: mod_auth_kerb-5.4-fixes.patch
Patch3: mod_auth_kerb-5.4-s4u2proxy.patch
Patch4: mod_auth_kerb-5.4-httpd24.patch
Patch5: mod_auth_kerb-5.4-delegation.patch
Patch6: mod_auth_kerb-5.4-cachedir.patch
Patch7: mod_auth_kerb-5.4-longuser.patch
Patch8: mod_auth_kerb-5.4-handle-continue.patch

# Automatically added by buildreq on Mon Sep 29 2008
BuildRequires: apache2-devel libcom_err-devel libkrb5-devel
%{?_with_apache1:BuildRequires: apache-devel}

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
%patch1 -p1 -b .rcopshack
%patch2 -p1 -b .fixes
%patch3 -p1 -b .s4u2proxy
%patch4 -p1 -b .httpd24
%patch5 -p1 -b .delegation
%patch6 -p1 -b .cachedir
%patch7 -p1 -b .longuser
%patch8 -p1 -b .continue

%build

%if_with apache1
# apache-1
export APXS=%_sbindir/apxs
./configure \
			--with-krb5=%_prefix \
			--without-krb4
%make_build
cp -a src apache1
%make clean
%endif

# apache-2
export APXS=%_sbindir/apxs2
# XXX for GSSAPI libraries support SPNEGO
CPPFLAGS="$CPPFLAGS -Wl,--no-as-needed" ./configure \
			--with-krb5=%_prefix \
			--without-krb4
%make_build
cp -a src apache2

%install
mkdir -p %buildroot%apache_moduledir
mkdir -p %buildroot%apache2_moduledir
mkdir -p %buildroot%apache2_mods_available
%if_with apache1
install -m 644 apache1/*.so %buildroot%apache_moduledir
%endif
install -m 644 apache2/.libs/*.so %buildroot%apache2_moduledir
install -m 644 %SOURCE2 %_builddir/%name-%version

mkdir -p %buildroot/{%apache2_mods_available,%apache2_mods_start}
cat > %buildroot/%apache2_mods_available/auth_krb5.load <<EOF
LoadModule auth_kerb_module %apache2_moduledir/mod_auth_kerb.so
EOF

cat > %buildroot/%apache2_mods_start/100-auth_krb5.conf << EOF
auth_krb5=yes
EOF

# Credentials cache
mkdir -p %buildroot%_tmpfilesdir
cat > %buildroot%_tmpfilesdir/httpd2-krbcache.conf <<EOF
d /var/run/httpd2/krbcache 700 apache2 apache2
EOF
mkdir -p %buildroot%_runtimedir/httpd2/krbcache

# for %%ghost
mkdir -p %buildroot%apache2_mods_enabled/
touch %buildroot%apache2_mods_enabled/auth_krb5.load

%if_with apache1
%files -n apache-%name
%doc README INSTALL
%apache_moduledir/*.so
%endif

%files -n apache2-%name
%doc README INSTALL auth_krb5.conf.sample
%config(noreplace) %apache2_mods_available/*
%config(noreplace) %apache2_mods_start/*
%ghost %apache2_mods_enabled/*.load
%apache2_moduledir/*.so
%_tmpfilesdir/httpd2-krbcache.conf
%attr(0700,apache2,apache2) %dir %_runtimedir/httpd2/krbcache

%changelog
* Thu Mar 17 2016 Alexey Shabalin <shaba@altlinux.ru> 5.4-alt1
- 5.4
- add patches from fedora
- disable build apache1 module

* Fri Dec 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt1.S1
- Fixed build with gcc 4.7

* Mon Sep 29 2008 Boris Savelev <boris@altlinux.org> 5.3-alt1
- initial build for Sisyphus

