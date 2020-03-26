# nagios uses /usr/lib for plugins in any arch
%define plugindir %_prefix/lib/nagios/plugins

Name: nagios-plugins-smartmon
Version: 1.1
Release: alt5

Summary: Nagios(R) plug-in for checking SMART parameters
License: GPL
Group: Monitoring
Url: http://altlinux.org/%name
Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Source: %name-%version.tar
Patch0: port-to-python3.patch

BuildRequires(pre): rpm-build-python3
Requires: nagios-nrpe smartmontools

Provides: nagios-nrpe-checksmartmon
Obsoletes: nagios-nrpe-checksmartmon

%description
Nagios plugin for checking SMART parameters at hard drives written in python.

See docs at %url.

%prep
%setup
%patch0 -p2

%install
mkdir -p %buildroot%plugindir
install -m755 bin/* %buildroot%plugindir/

%files
%plugindir/check_smartmon

%changelog
* Thu Mar 26 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1-alt5
- Porting to python3.

* Sat Feb 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt4
- use python2 for the script

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

