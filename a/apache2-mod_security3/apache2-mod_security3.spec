# Spec file for mod_security module for Apache 2.0 server

%define real_name    ModSecurity-apache
%define module_name  mod_security3
%define version      0.0.9
%define release      alt1.git2368a66a


Name: apache2-%module_name
Version: %version
Release: %release

Summary: web application firewall for Apache 2.x based on ModSecurity framework

License: %asl
Group:   System/Servers
URL:     https://github.com/SpiderLabs/ModSecurity-apache

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %real_name-%version.tar
Patch0:  %real_name-%version-%release.patch

Source1: security3.load
Source2: security3.conf

BuildRequires(pre): apache2-devel >= 2.2.5
BuildRequires(pre): rpm-build-licenses rpm-macros-webserver-common

# Automatically added by buildreq on Fri Jul 16 2021
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libapr1-devel libaprutil1-devel libsasl2-3 perl python3 python3-base python3-module-paste ruby ruby-stdlibs sh4
BuildRequires: libmodsecurity-devel

BuildRequires: %apache2_apr_buildreq

Requires(pre): apache2 >= %apache2_version-%apache2_release

%description
ModSecurity is an open source, cross platform web application
firewall (WAF) engine for Apache, IIS and Nginx that is developed
by Trustwave's SpiderLabs. It has a robust event-based programming
language which provides protection from a range of attacks against
web applications and allows for HTTP traffic monitoring, logging
and real-time analysys.

This package contains Apache 2.x module that use ModSecurity WAF
engine.


%define	conf_dir	%_sysconfdir/%module_name

%prep
%setup -q -n %real_name-%version
%patch0 -p1

%build
%autoreconf
%configure	--with-apxs=%apache2_apxs \
		--with-apr=%apache2_apr_config \
		--with-libmodsecurity=%_libdir \
		--without-apache \
		%nil
%make_build


%install
mv -f -- LICENSE LICENSE.orig
ln -s -- $(relative %_licensedir/Apache-2.0 %_docdir/%name/LICENSE) LICENSE

/bin/install -pDm644 -- src/.libs/mod_security3.so %buildroot%apache2_libexecdir/mod_security3.so

/bin/install -pDm644 -- %SOURCE1 %buildroot%apache2_mods_available/security3.load
/bin/install -pDm644 -- %SOURCE2 %buildroot%apache2_mods_available/security3.conf


%files
%doc README.md AUTHORS CHANGES
%doc --no-dereference LICENSE

%apache2_libexecdir/mod_security3.so

%apache2_mods_available/security3.load
%config(noreplace) %apache2_mods_available/security3.conf


%changelog
* Fri Jul 16 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.0.9-alt1.git2368a66a
- Initial build for ALT Linux Sisyphus
