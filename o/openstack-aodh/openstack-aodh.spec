%global oname aodh

Name: openstack-%oname
Version: 7.0.0
Release: alt1
Summary: OpenStack Telemetry Alarming
Group: System/Servers
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
BuildArch: noarch

Source2: aodh.logrotate
Source6: aodh.conf
Source9: %name.tmpfiles
Source10: %name-api.service
Source11: %name-evaluator.service
Source12: %name-notifier.service
Source13: %name-expirer.service
Source14: %name-listener.service

Source110: %name-api.init
Source111: %name-evaluator.init
Source112: %name-notifier.init
Source113: %name-expirer.init
Source114: %name-listener.init

Requires: python3-module-PasteDeploy
Requires(pre):    shadow-utils

BuildRequires: crudini
BuildRequires: webserver-common rpm-build-webserver-common rpm-macros-apache2
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-tenacity >= 3.2.1
BuildRequires: python-module-croniter >= 0.3.4
BuildRequires: python-module-futures >= 3.0
BuildRequires: python-module-futurist >= 0.11.0
BuildRequires: python-module-jsonschema >= 2.0.0
BuildRequires: python-module-keystonemiddleware >= 2.2.0
BuildRequires: python-module-gnocchiclient >= 3.1.0
BuildRequires: python-module-lxml >= 2.3
BuildRequires: python-module-oslo.db >= 4.8.0
BuildRequires: python-module-oslo.config >= 2.6.0
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-oslo.log >= 1.2.0
BuildRequires: python-module-oslo.policy >= 0.5.0
BuildRequires: python-module-PasteDeploy >= 1.5.0
BuildRequires: python-module-pecan >= 0.8.0
BuildRequires: python-module-oslo.messaging >= 5.2.0
BuildRequires: python-module-oslo.middleware >= 3.22.0
BuildRequires: python-module-oslo.utils >= 3.5.0
BuildRequires: python-module-keystoneclient >= 1.6.0
BuildRequires: python-module-pytz >= 2013.6
BuildRequires: python-module-requests >= 2.5.2
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-stevedore >= 1.5.0
BuildRequires: python-module-tooz >= 1.28.0
BuildRequires: python-module-voluptuous >= 0.8.10
BuildRequires: python-module-webob >= 1.2.3
BuildRequires: python-module-wsme >= 0.8
BuildRequires: python-module-cachetools >= 1.1.6
BuildRequires: python-module-cotyledon
BuildRequires: python-module-keystoneauth1 >= 2.1
BuildRequires: python-module-debtcollector >= 1.2.0

BuildRequires: python-module-openstackdocstheme >= 1.11.0
BuildRequires: python-module-reno >= 0.1.1
BuildRequires: python-module-sphinx >= 1.6.2
#BuildRequires: python-module-sphinxcontrib-httpdomain
#BuildRequires: python-module-sphinxcontrib-pecanwsme >= 0.8

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-tenacity >= 3.2.1
BuildRequires: python3-module-croniter >= 0.3.4
BuildRequires: python3-module-futurist >= 0.11.0
BuildRequires: python3-module-jsonschema >= 2.0.0
BuildRequires: python3-module-keystonemiddleware >= 2.2.0
BuildRequires: python3-module-gnocchiclient >= 3.1.0
BuildRequires: python3-module-lxml >= 2.3
BuildRequires: python3-module-oslo.db >= 4.8.0
BuildRequires: python3-module-oslo.config >= 2.6.0
BuildRequires: python3-module-oslo.i18n >= 1.5.0
BuildRequires: python3-module-oslo.log >= 1.2.0
BuildRequires: python3-module-oslo.policy >= 0.5.0
BuildRequires: python3-module-PasteDeploy >= 1.5.0
BuildRequires: python3-module-pecan >= 0.8.0
BuildRequires: python3-module-oslo.messaging >= 5.2.0
BuildRequires: python3-module-oslo.middleware >= 3.22.0
BuildRequires: python3-module-oslo.utils >= 3.5.0
BuildRequires: python3-module-keystoneclient >= 1.6.0
BuildRequires: python3-module-pytz >= 2013.6
BuildRequires: python3-module-requests >= 2.5.2
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-stevedore >= 1.5.0
BuildRequires: python3-module-tooz >= 1.28.0
BuildRequires: python3-module-voluptuous >= 0.8.10
BuildRequires: python3-module-webob >= 1.2.3
BuildRequires: python3-module-wsme >= 0.8
BuildRequires: python3-module-cachetools >= 1.1.6
BuildRequires: python3-module-cotyledon
BuildRequires: python3-module-keystoneauth1 >= 2.1
BuildRequires: python3-module-debtcollector >= 1.2.0

BuildRequires: python3-module-openstackdocstheme >= 1.11.0
BuildRequires: python3-module-reno >= 0.1.1
BuildRequires: python3-module-sphinx >= 1.6.2
#BuildRequires: python3-module-sphinxcontrib-httpdomain
#BuildRequires: python3-module-sphinxcontrib-pecanwsme >= 0.8

%description
Aodh is the alarm engine of the Ceilometer project.

%package compat
Summary: OpenStack aodh compat
Group: System/Servers

Provides: openstack-ceilometer-alarm = %version-%release
Obsoletes: openstack-ceilometer-alarm < 1:6.0.0

Requires: python3-module-aodh  = %version-%release
Requires: %name-common
Requires: %name-api
Requires: %name-evaluator
Requires: %name-notifier
Requires: %name-expirer
Requires: %name-listener

%description compat
This package only exists to help transition openstack-ceilometer-alarm users
to the new package split. It will be removed after one distribution release
cycle, please do not reference it or depend on it in any way.

%package -n python-module-%oname
Summary: OpenStack aodh python libraries
Group: Development/Python
Requires: python-module-PasteDeploy

%description -n python-module-%oname
OpenStack aodh provides API and services for managing alarms.

This package contains the aodh python library.

%package -n python3-module-%oname
Summary: OpenStack aodh python libraries
Group: Development/Python3
Requires: python3-module-PasteDeploy

%description -n python3-module-%oname
OpenStack aodh provides API and services for managing alarms.

This package contains the aodh python3 library.

%package common
Summary: Components common to all OpenStack aodh services
Group: System/Servers

Requires: python3-module-aodh = %version-%release
Requires: python3-module-ceilometerclient

%description common
OpenStack aodh provides API and services for managing alarms.

%package api
Summary: OpenStack aodh api
Group: System/Servers

Requires: %name-common = %version-%release
Requires: python3-module-ceilometerclient

%description api
OpenStack aodh provides API and servicesfor managing alarms.

This package contains the aodh API service.

%package evaluator
Summary: OpenStack aodh evaluator
Group: System/Servers

Requires: %name-common = %version-%release

%description evaluator
OpenStack aodh provides API and services for managing alarms.

This package contains the aodh evaluator service.

%package notifier
Summary: OpenStack aodh notifier
Group: System/Servers

Requires: %name-common = %version-%release

%description notifier
OpenStack aodh provides API and services for managing alarms.

This package contains the aodh notifier service.

%package listener
Summary: OpenStack aodh listener
Group: System/Servers

Requires: %name-common = %version-%release

%description listener
OpenStack aodh provides API and services for managing alarms.

This package contains the aodh listener service.

%package expirer
Summary: OpenStack aodh expirer
Group: System/Servers

Requires: %name-common = %version-%release

%description expirer
OpenStack aodh provides API and services for managing alarms.

This package contains the aodh expirer service.

%package -n python-module-%oname-tests
Summary: Aodh tests
Group: Development/Python
Requires: python-module-aodh = %version-%release

%description -n python-module-%oname-tests
OpenStack aodh provides API and services for managing alarms.

This package contains the Aodh test files.

%package -n python3-module-%oname-tests
Summary: Aodh tests
Group: Development/Python3
Requires: python3-module-aodh = %version-%release

%description -n python3-module-%oname-tests
OpenStack aodh provides API and services for managing alarms.

This package contains the Aodh test files.


%prep
%setup -n %oname-%version

find . \( -name .gitignore -o -name .placeholder \) -delete

find aodh -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

rm -rf {test-,}requirements.txt tools/{pip,test}-requires


rm -rf ../python3
cp -a . ../python3

%build

%python_build

# Generate config file
PYTHONPATH=. oslo-config-generator --config-file=build/lib/aodh/cmd/aodh-config-generator.conf --output-file aodh.conf.sample

# Generate i18n files
#python setup.py compile_catalog -d build/lib/%oname/locale

pushd ../python3
%python3_build
popd

%install
%python_install

for f in $(ls -1 %buildroot%_bindir)
    do mv %buildroot%_bindir/$f %buildroot%_bindir/$f.py2
done

pushd ../python3
%python3_install
popd


# Install config files
install -d -m 755 %buildroot%_sysconfdir/aodh
install -d -m 755 %buildroot%_sysconfdir/aodh/aodh.conf.d
install -p -D -m 640 aodh.conf.sample %buildroot%_sysconfdir/aodh/aodh.conf

# Setup directories
install -d -m 755 %buildroot%_sharedstatedir/aodh
install -d -m 755 %buildroot%_sharedstatedir/aodh/tmp
install -d -m 755 %buildroot%_logdir/aodh
# Install pid directory
install -d -m 775 %buildroot%_runtimedir/aodh
install -p -D -m 644 %SOURCE9 %buildroot%_tmpfilesdir/%name.conf

# Install logrotate
install -p -D -m 644 %SOURCE2 %buildroot%_sysconfdir/logrotate.d/%name

# Install systemd unit services
install -p -D -m 644 %SOURCE10 %buildroot%_unitdir/%name-api.service
install -p -D -m 644 %SOURCE11 %buildroot%_unitdir/%name-evaluator.service
install -p -D -m 644 %SOURCE12 %buildroot%_unitdir/%name-notifier.service
install -p -D -m 644 %SOURCE13 %buildroot%_unitdir/%name-expirer.service
install -p -D -m 644 %SOURCE14 %buildroot%_unitdir/%name-listener.service

# Install sysv init scripts
install -p -D -m 755 %SOURCE110 %buildroot%_initdir/%name-api
install -p -D -m 755 %SOURCE111 %buildroot%_initdir/%name-evaluator
install -p -D -m 755 %SOURCE112 %buildroot%_initdir/%name-notifier
install -p -D -m 755 %SOURCE113 %buildroot%_initdir/%name-expirer
install -p -D -m 755 %SOURCE114 %buildroot%_initdir/%name-listener

# Install sample HTTPD integration files
install -p -D -m 644 aodh/api/app.wsgi %buildroot%_datadir/aodh/aodh.wsgi

install -m 0644 -D -p %SOURCE6 %buildroot%apache2_sites_available/openstack-aodh.conf
mkdir -p %buildroot%apache2_sites_enabled
touch %buildroot%apache2_sites_enabled/openstack-aodh.conf
mkdir -p %buildroot%webserver_cgibindir
ln -s %_datadir/aodh/aodh.wsgi %buildroot%webserver_cgibindir/aodh-wsgi

### set default configuration
%define aodh_conf %buildroot%_sysconfdir/aodh/aodh.conf.d/010-aodh.conf
crudini --set %aodh_conf DEFAULT log_dir /var/log/aodh
crudini --set %aodh_conf DEFAULT state_path /var/lib/aodh
crudini --set %aodh_conf oslo_concurrency lock_path /var/run/aodh

# Install i18n .mo files (.po and .pot are not required)
#install -d -m 755 %buildroot%_datadir
#rm -f %buildroot%python_sitelibdir/%oname/locale/*/LC_*/%{oname}*po
#rm -f %buildroot%python_sitelibdir/%oname/locale/*pot
#mv %buildroot%python_sitelibdir/%oname/locale %buildroot%_datadir/locale

# Find language files
#%find_lang %oname --all-name

# Remove unused files
rm -fr %buildroot/usr/etc

%pre common
%_sbindir/groupadd -r -f aodh 2>/dev/null ||:
%_sbindir/useradd -r -g aodh -G aodh  -c 'OpenStack aodh Daemons' \
        -s /sbin/nologin  -d %_sharedstatedir/aodh aodh 2>/dev/null ||:

%post -n %name-api
%post_service %name-api

%preun -n %name-api
%preun_service %name-api

%post -n %name-evaluator
%post_service %name-evaluator

%preun -n %name-evaluator
%preun_service %name-evaluator

%post -n %name-notifier
%post_service  %name-notifier

%preun -n %name-notifier
%preun_service %name-notifier

%post -n %name-listener
%post_service %name-listener

%preun -n %name-listener
%preun_service %name-listener

%post -n %name-expirer
%post_service %name-expirer

%preun -n %name-expirer
%preun_service %name-expirer

%files compat

%files -n python-module-aodh
%_bindir/*.py2
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files -n python-module-aodh-tests
%python_sitelibdir/*/tests

%files -n python3-module-aodh
%_bindir/*
%exclude %_bindir/*.py2
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-aodh-tests
%python3_sitelibdir/*/tests

%files common
#-f %oname.lang
%doc README.rst
%dir %_sysconfdir/aodh
%dir %_sysconfdir/aodh/aodh.conf.d
%config(noreplace) %attr(640, root, aodh) %_sysconfdir/aodh/aodh.conf
%config(noreplace) %attr(640, root, aodh) %_sysconfdir/aodh/aodh.conf.d/010-aodh.conf
%config(noreplace) %_sysconfdir/logrotate.d/%name
%_tmpfilesdir/%name.conf

%dir %attr(0770, root, aodh) %_logdir/aodh
%dir %attr(0775, root, aodh) %_runtimedir/aodh
%dir %attr(0755, aodh, aodh) %_sharedstatedir/aodh
#%dir %attr(0755, aodh, aodh) %_cachedir/aodh

%files api
%_unitdir/%name-api.service
%_initdir/%name-api
%dir %_datadir/aodh
%_datadir/aodh/*
%config(noreplace) %apache2_sites_available/*.conf
%ghost %apache2_sites_enabled/*.conf
%webserver_cgibindir/*

%files evaluator
%_unitdir/%name-evaluator.service
%_initdir/%name-evaluator

%files notifier
%_unitdir/%name-notifier.service
%_initdir/%name-notifier

%files listener
%_unitdir/%name-listener.service
%_initdir/%name-listener

%files expirer
%_unitdir/%name-expirer.service
%_initdir/%name-expirer

%changelog
* Fri Jan 11 2019 Alexey Shabalin <shaba@altlinux.org> 7.0.0-alt1
- 7.0.0 Rocky release
- switch to python3

* Fri Jun 22 2018 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt2
- Fixed FTBFS (remove python-module-setuptools-tests from BR).

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Thu Jun 22 2017 Alexey Shabalin <shaba@altlinux.ru> 4.0.0-alt2
- update default config
- Fix the migration to use alarm_history

* Tue Jun 13 2017 Alexey Shabalin <shaba@altlinux.ru> 4.0.0-alt1
- 4.0.0

* Wed Apr 12 2017 Alexey Shabalin <shaba@altlinux.ru> 3.0.2-alt1
- 3.0.2

* Wed Nov 23 2016 Alexey Shabalin <shaba@altlinux.ru> 3.0.1-alt1
- initial build
