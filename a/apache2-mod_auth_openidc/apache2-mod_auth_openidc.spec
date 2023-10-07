# Spec file for mod_auth_openidc module for Apache 2.4 server

%define real_name    mod_auth_openidc
%define module_name  mod_auth_openidc


Name: apache2-%module_name
Version: 2.4.14.3
Release: alt1

Summary: Apache 2.x OpenID Connect Relying Party authentication and authorization module

License: %asl
Group:   System/Servers
URL:     https://github.com/zmartzone/mod_auth_openidc

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %real_name-%version.tar
Patch0:  %real_name-%version.patch

Source1: auth_openidc.load
Source2: auth_openidc.conf

BuildRequires(pre): apache2-devel >= 2.2.5
BuildRequires(pre): rpm-build-licenses

Requires(pre): apache2 >= %apache2_version-%apache2_release

BuildRequires: libssl-devel libuuid-devel libcjose-devel libcurl-devel libpcre-devel

%description
mod_auth_openidc is a certified authentication and authorization
module for the Apache 2.x HTTP server that implements the OpenID
Connect Relying Party functionality.

This module enables an Apache 2.x web server to operate as
an OpenID Connect Relying Party (RP) towards an OpenID Connect
Provider (OP). It relays end user authentication to a Provider
and receives user identity information from that Provider.
It then passes on that identity information (a.k.a. claims)
to applications protected by the Apache web server and establishes
an authentication session for the identified user.

The protected content, applications and services can be hosted by
the Apache server itself or served from origin server(s) residing
behind it by configuring Apache as a Reverse Proxy in front of
those servers. The latter allows for adding OpenID Connect based
authentication to existing applications/services/SPAs without
modifying those applications, possibly migrating them away from
legacy authentication mechanisms to standards-based OpenID Connect
Single Sign On (SSO).

Custom fine-grained authorization rules - based on Apache's
Require primitives - can be specified to match against the set of
claims provided in the id_token/ userinfo claims. Clustering for
resilience and performance can be configured using a number of
the supported cache backends options.


%prep
%setup -q -n %real_name-%version
%patch0 -p1

mv -f -- LICENSE.txt LICENSE.txt.orig
ln -s -- $(relative %_licensedir/Apache-2.0 %_docdir/%name/LICENSE.txt) LICENSE.txt

%build
%autoreconf
%configure --with-apxs=%apache2_apxs
%make_build

%install
/bin/install -pDm644 .libs/mod_auth_openidc.so %buildroot%apache2_libexecdir/mod_auth_openidc.so

/bin/install -pDm644 %SOURCE1 %buildroot%apache2_mods_available/auth_openidc.load
/bin/install -pDm644 %SOURCE2 %buildroot%apache2_mods_available/auth_openidc.conf

/bin/mkdir -p %buildroot%apache2_spooldir/%module_name

%post
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:

if [ -e %apache2_mods_enabled/%module_name.load ]; then
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
        service %apache2_dname condrestart ||:
    else
        echo "Some errors detected in Apache2 configuration!"
        echo "To use %real_name check configuration and start %apache2_dname service."
    echo
    fi
else
    echo "Apache2 %real_name module had been installed, but does't enabled."
    echo "Check %apache2_mods_start directory for files with '%module_name=no' lines."
    echo
fi

%preun
if [ "$1" = "0" ] ; then # last uninstall
    [ -e %apache2_mods_enabled/%module_name.load ] && %apache2_sbindir/a2dismod %module_name 2>&1 >/dev/null ||:
fi


%postun
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:
if [ "$1" = "0" ] ; then # last uninstall
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
        service %apache2_dname condrestart ||:
    else
        echo "Some errors detected in Apache2 configuration!"
        echo "To complete %real_name uninstalling check configuration and restart %apache2_dname service."
        echo
    fi
fi


%files
%doc README.md ChangeLog AUTHORS SECURITY.md
%doc --no-dereference LICENSE.txt

%apache2_libexecdir/mod_auth_openidc.so
%apache2_mods_available/auth_openidc.load
%config(noreplace) %apache2_mods_available/auth_openidc.conf

%dir %apache2_spooldir/%module_name

%changelog
* Sat Oct 07 2023 Nikolay A. Fetisov <naf@altlinux.org> 2.4.14.3-alt1
- New version

* Wed Mar 23 2022 Nikolay A. Fetisov <naf@altlinux.org> 2.4.11-alt1
- Initial build for ALT Linux Sisyphus
