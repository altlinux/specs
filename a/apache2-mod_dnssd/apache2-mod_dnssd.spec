%define apache_moduledir %apache2_moduledir

Name: apache2-mod_dnssd
Version: 0.6
Release: alt1

Summary: Apache 2.0 module which adds Zeroconf support via DNS-SD using Avahi.
License: Apache 2.0
Group: System/Servers
Url: http://0pointer.de/lennart/projects/mod_dnssd

Requires: %apache2_name-base > 2.2.22-alt15
Requires: %apache2_name-mmn = %apache2_mmn
Requires: %apache2_libaprutil_name >= %apache2_libaprutil_evr

Source: %name-%version-%release.tar
BuildRequires(pre): apache2-devel > 2.2.22-alt15
BuildRequires: libavahi-devel lynx

%description
An Apache 2.0 module which adds Zeroconf support via DNS-SD using Avahi.

%prep
%setup

%build
%autoreconf
%configure --with-apr-config --with-apxs=%apache2_sbindir
make

%install
install -pm0644 -D src/.libs/mod_dnssd.so %buildroot/%apache_moduledir/mod_dnssd.so
install -pm0644 -D alt/dnssd.conf %buildroot%apache2_mods_available/dnssd.conf
install -pm0644 -D alt/dnssd.load %buildroot%apache2_mods_available/dnssd.load
install -pm0644 -D alt/dnssd.start %buildroot%apache2_mods_start/100-dnssd.conf

# for %%ghost
mkdir -p %buildroot%apache2_mods_enabled/
touch %buildroot%apache2_mods_enabled/dnssd.conf
touch %buildroot%apache2_mods_enabled/dnssd.load

%files
%doc LICENSE README
%apache_moduledir/mod_dnssd.so
%config(noreplace) %apache2_mods_available/*.load
%config(noreplace) %apache2_mods_available/*.conf
%config(noreplace) %apache2_mods_start/*.conf
%ghost %apache2_mods_enabled/*.load
%ghost %apache2_mods_enabled/*.conf

%changelog
* Sat Feb 09 2013 Aleksey Avdeev <solo@altlinux.ru> 0.6-alt1
- New version

* Sat Feb 09 2013 Aleksey Avdeev <solo@altlinux.ru> 0.5-alt1.1
- Rebuild with apache2-2.2.22-alt16 (fix unmets).
- Add %%apache2_mods_start/100-dnssd.conf file for auto loading module.
- Add %%ghost for %%apache2_mods_enabled/*.{load,conf}.

* Mon Aug 27 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5-alt1
- Initial build.
