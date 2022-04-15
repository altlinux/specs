%define soname 10
%define soname_lite 10
%define runuser shibd
%define realname shibboleth
%define pkgdocdir %_docdir/%realname
%define _localstatedir %_var

Name: shibboleth-sp
Version: 3.3.0
Release: alt1

Summary: Open source system for attribute-based Web SSO

License: Apache-2.0
Group: Networking/Other
Url: https://shibboleth.net/

Source: https://shibboleth.net/downloads/service-provider/latest/%name-%version.tar.gz
Source1: shibd.service

BuildRequires: gcc-c++ boost-devel-headers liblog4cpp-devel libxerces-c-devel libxml-security-c-devel libxmltooling-devel libsaml-devel
BuildRequires: libsystemd-devel libmemcached-devel apache2-devel libunixODBC-devel libkrb5-devel

%description
Shibboleth is a Web Single Sign-On implementations based on OpenSAML
that supports multiple protocols, federated identity, and the extensible
exchange of rich attributes subject to privacy controls.

This package contains the Shibboleth Service Provider runtime libraries,
daemon, default plugins, and Apache modules.

%package -n libshibsp%soname
Summary: Shared Library for Shibboleth
Group: System/Libraries

%description -n libshibsp%soname
Shibboleth is a Web Single Sign-On implementations based on OpenSAML
that supports multiple protocols, federated identity, and the extensible
exchange of rich attributes subject to privacy controls.

This package contains just the shared library.

%package -n libshibsp-lite%soname_lite
Summary: Shared Library for Shibboleth
Group: System/Libraries

%description -n libshibsp-lite%soname_lite
Shibboleth is a Web Single Sign-On implementations based on OpenSAML
that supports multiple protocols, federated identity, and the extensible
exchange of rich attributes subject to privacy controls.

%package devel
Summary: Shibboleth Development Headers
Group: Development/C++

%description devel
Shibboleth is a Web Single Sign-On implementations based on OpenSAML
that supports multiple protocols, federated identity, and the extensible
exchange of rich attributes subject to privacy controls.

This package includes files needed for development with Shibboleth.

%prep
%setup

%__subst "s|%_bindir/env bash|/bin/bash|" \
		configs/metagen.sh

%build
export CXXFLAGS="%optflags --std=c++11"
%autoreconf
%configure --with-gssapi --enable-systemd --with-memcached
%make_build pkgdocdir=%pkgdocdir

%install
%makeinstall_std NOKEYGEN=1 pkgdocdir=%pkgdocdir

install -D -m 644 %SOURCE1 %buildroot%_unitdir/shibd.service
ln -sf /sbin/service %buildroot%_sbindir/rcshibd

# %__subst "s|/var/log/httpd|/var/log/apache2|g" \
# 		%buildroot%_sysconfdir%realname/native.logger


# Delete unnecessary files
pushd %buildroot%_sysconfdir/%realname
rm shibd-debian shibd-redhat shibd-amazon shibd-suse shibd-osx.plist apache.config apache2.config apache22.config shibd-systemd
rm *.dist
popd
find %buildroot -type f -name "*.la" -delete -print

# Plug the SP into the Apache
touch rpm.filelist
APACHE_CONFIG="no"
if [ -f %buildroot%_libdir/%realname/mod_shib_24.so ] ; then
	APACHE_CONFIG="apache24.config"
fi

if [ "$APACHE_CONFIG" != "no" ] ; then
	APACHE_CONFD="no"
	if [ -d %_sysconfdir/apache2/conf.d ] ; then
		APACHE_CONFD="%_sysconfdir/apache2/conf.d"
	fi
	if [ "$APACHE_CONFD" != "no" ] ; then
		mkdir -p %buildroot$APACHE_CONFD
		cp -p %buildroot%_sysconfdir/%realname/$APACHE_CONFIG %buildroot$APACHE_CONFD/shib.conf
		echo "%config(noreplace) $APACHE_CONFD/shib.conf" >> rpm.filelist
	fi
fi

# Get run directory created at boot time.
mkdir -p %buildroot%_tmpfilesdir
echo "%attr(0444,-,-) %_tmpfilesdir/%realname.conf" >> rpm.filelist
cat > %buildroot%_tmpfilesdir/%realname.conf <<EOF
d /run/%realname 755 %runuser %runuser -
EOF

%post
%post_service shibd.service

%preun
%preun_service shibd.service

%files -f rpm.filelist
%_sbindir/shibd
%_sbindir/rcshibd
%_bindir/mdquery
%_bindir/resolvertest
%dir %_libdir/%realname
%_libdir/%realname/*
%_unitdir/shibd.service
%attr(0750,%runuser,%runuser) %dir %_logdir/%realname
%attr(0755,%runuser,%runuser) %dir %_cachedir/%realname
# %ghost %attr(0755,%runuser,%runuser) %dir /run/%realname
%dir %_datadir/xml/%realname
%_datadir/xml/%realname/*
%dir %_datadir/%realname
%_datadir/%realname/*
%dir %_sysconfdir/%realname
%config(noreplace) %_sysconfdir/%realname/*.xml
%config(noreplace) %_sysconfdir/%realname/*.html
%config(noreplace) %_sysconfdir/%realname/*.logger
%_tmpfilesdir/%realname.conf
%_sysconfdir/%realname/apache24.config
%attr(0755,root,root) %_sysconfdir/%realname/keygen.sh
%attr(0755,root,root) %_sysconfdir/%realname/metagen.sh
%attr(0755,root,root) %_sysconfdir/%realname/seckeygen.sh
%doc %pkgdocdir
%exclude %pkgdocdir/

%files -n libshibsp%soname
%_libdir/libshibsp.so.%{soname}*

%files -n libshibsp-lite%soname_lite
%_libdir/libshibsp-lite.so.%{soname_lite}*

%files devel
%_includedir/*
%_libdir/libshibsp.so
%_libdir/libshibsp-lite.so
%_pkgconfigdir/*.pc
%doc %pkgdocdir/

%changelog
* Thu Apr 14 2022 Leontiy Volodin <lvol@altlinux.org> 3.3.0-alt1
- Initial build for ALT Sisyphus.
