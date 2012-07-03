Name: nagios-plugins-smartmon
Version: 1.1
Release: alt3.1

Summary: Nagios(R) plug-in for checking SMART parameters
License: GPL
Group: Monitoring

Url: http://altlinux.org/%name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArchitectures: noarch

Requires: nagios-nrpe, smartmontools

Provides: nagios-nrpe-checksmartmon
Obsoletes: nagios-nrpe-checksmartmon

# nagios uses /usr/lib for plugins in any arch
%define plugindir %_prefix/lib/nagios/plugins

%description
Nagios plugin for checking SMART parameters at hard drives written in python.

See docs at %url.

%prep
%setup

%install
mkdir -p %buildroot%plugindir
install -m755 bin/* %buildroot%plugindir/

%files
%plugindir/check_smartmon

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt3.1
- Rebuild with Python-2.7

* Thu Jul 08 2010 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt3
- make package noarch

* Tue Jul 06 2010 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt2
- move plugin to common /usr/lib/nagios/plugins dir

* Thu Jun 17 2010 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- rename package
- build for ALT Linux Sisyphus
- move plugin to plugins dir

* Sat Apr 24 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt2
- Testing

* Sat Apr 24 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt1
- Initial build

