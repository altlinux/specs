Name: opm-wh_nagios
Version: 2.3
Release: alt1

Summary: Nagios stat warehouse for Open PostgreSQL Monitoring
License: BSD like
Group: Monitoring

Url: https://github.com/OPMDG/opm-wh_nagios

Source: %name-%version.tar

BuildArchitectures: noarch

%add_perl_lib_path %_datadir/opm-core/ui/lib

Requires: opm-core = 2.3

BuildPreReq: postgresql9.3-devel perl-podlators
BuildPreReq: perl-Mojolicious >= 4.50
BuildPreReq: opm-core = 2.3

%description
Open PostgreSQL Monitoring Nagios stat warehouse.

%package postgresql
Summary: PostgreSQL extension for OPM
Group: Development/Python
Requires: postgresql9.3-server postgresql9.3-contrib

%description postgresql
PostgreSQL extension for Open PostgreSQL Monitoring Nagios stat warehouse.

%package -n opm-nagios_dispatcher
Summary: nagios_dispatcher for OPM
Group: Development/Python
Requires: libdbi-drivers-dbd-pgsql perl-DBD-Pg perl-podlators

%description -n opm-nagios_dispatcher
opm-nagios_dispatcher for Open PostgreSQL Monitoring.

%prep
%setup

%install
cd pg
%makeinstall_std
cd -
mkdir -p %buildroot/%_datadir/opm-core/
cp -a ui %buildroot/%_datadir/opm-core/
mkdir -p %buildroot/%_sbindir/
install -m655 bin/nagios_dispatcher.pl %buildroot/%_sbindir/

# create conf in normal place
#mkdir -p %buildroot%_sysconfdir/%name/
#cp ui/opm.conf-dist %buildroot%_sysconfdir/%name/opm.conf
#ln -s %_sysconfdir/%name/opm.conf %buildroot%_datadir/%name/ui/opm.conf


%files
%_datadir/opm-core/ui/

%files postgresql
%_datadir/pgsql/extension/wh_nagios*

%files -n opm-nagios_dispatcher
%_sbindir/nagios_dispatcher.pl

%changelog
* Sun Sep 14 2014 Vitaly Lipatov <lav@altlinux.ru> 2.3-alt1
- initial build for ALT Linux Sisyphus
