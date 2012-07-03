Name: nagios-plugins-nginx
Version: 1.0.1
Release: alt1.1

Summary: Nagios(R) plug-in for checking nginx status
License: GPL
Group: Monitoring

Url: http://www.nginxs.com/linux/441.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArchitectures: noarch

Requires: nagios-nrpe

# nagios uses /usr/lib for plugins in any arch
%define plugindir %_prefix/lib/nagios/plugins

%description
Nagios plugin for checking nginx status written in python.

%prep
%setup

%install
mkdir -p %buildroot%plugindir/
install -m755 check_nginx %buildroot%plugindir/

%files
%plugindir/check_nginx

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt1.1
- Rebuild with Python-2.7

* Wed May 04 2011 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Linux Sisyphus
