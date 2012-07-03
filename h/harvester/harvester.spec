Name:		harvester
Summary:	OpenVZ stats harvester
Version:	0.1
Release:	alt2
Group:		Monitoring
License:	GPL
Packager: 	Mikhail Pokidko <pma@altlinux.org>
Source:		%name-%version-%release.tar

Requires: python-modules python-modules-encodings python-module-simplejson python-module-MySQLdb
BuildArch: noarch

%description
Harvester gathers OVZ-related information -- HN stats (mem, cpu, disk, etc) and VE stats (main ubc and VE state params)


%package web
Summary:	OpenVZ stats harvester. Web interface.
Group:		Monitoring
Requires: python-module-django >= 0.10-alt1

%description web
OVZ harvester web interface.

%prep
%setup -q

%install
mkdir -p %buildroot%_datadir/%name \
	%buildroot%_sbindir/ \
	%buildroot%_sysconfdir/%name \
	%buildroot%_sysconfdir/cron.d \
	%buildroot%_localstatedir/%name
install -pm 755 harvc.py %buildroot%_sbindir/%name
install -pm 644 %name.cron %buildroot%_sysconfdir/cron.d/%name
install scripts/* %buildroot%_datadir/%name/
install -pm 640 %name.conf %buildroot%_sysconfdir/%name/


%files
%_sbindir/%name
%dir %_localstatedir/%name
%dir %_sysconfdir/%name
%config %_sysconfdir/%name/%name.conf
%_sysconfdir/cron.d/%name
%_datadir/%name/

%files web


%changelog
* Mon Apr 09 2012 Mikhail Pokidko <pma@altlinux.org> 0.1-alt2
- _mysql_exception --> _mysql

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.1.1
- Rebuild with Python-2.7

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.1
- Rebuilt with python 2.6

* Thu Oct 08 2009 Mikhail Pokidko <pma@altlinux.org> 0.1-alt1
- Ste up from internal use. Initial build for ALT.


