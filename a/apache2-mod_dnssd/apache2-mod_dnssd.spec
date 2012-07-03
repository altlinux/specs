%define apache_confdir %_sysconfdir/httpd2/conf
%define apache_moduledir %_libdir/apache2/modules

Name: apache2-mod_dnssd
Version: 0.5
Release: alt1

Summary: Apache 2.0 module which adds Zeroconf support via DNS-SD using Avahi.
License: Apache 2.0
Group: System/Servers
Url: http://0pointer.de/lennart/projects/mod_dnssd

PreReq: apache2-common

Source: %name-%version-%release.tar
BuildRequires: apache2-devel libaprutil1-devel libapr1-devel libavahi-devel lynx

%description
An Apache 2.0 module which adds Zeroconf support via DNS-SD using Avahi.

%prep
%setup
sed -i 's@%_libdir/apache2/@@' debian/mod-dnssd.load

%build
%__autoreconf
%configure --with-apr-config --with-apxs=%_sbindir
make

%install
install -pm0644 -D src/.libs/mod_dnssd.so %buildroot/%apache_moduledir/mod_dnssd.so
install -pm0644 -D debian/mod-dnssd.conf %buildroot%apache_confdir/mods-available/dnssd.conf
install -pm0644 debian/mod-dnssd.load %buildroot%apache_confdir/mods-available/dnssd.load

%files
%doc LICENSE README
%apache_moduledir/mod_dnssd.so
%apache_confdir/*

%changelog
* Mon Aug 27 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5-alt1
- Initial build.
