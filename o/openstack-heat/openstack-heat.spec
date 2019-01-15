%def_disable doc
%add_python_req_skip senlinclient
%define oname heat

Name: openstack-%oname
Summary: OpenStack Orchestration (heat)
Version: 11.0.0
Release: alt1
Epoch: 1
License: ASL 2.0
Group: System/Servers
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

Source1: heat.logrotate
Source2: openstack-heat-api.service
Source3: openstack-heat-api-cfn.service
Source4: openstack-heat-engine.service
Source5: openstack-heat-api-cloudwatch.service

Source12: openstack-heat-api.init
Source13: openstack-heat-api-cfn.init
Source14: openstack-heat-engine.init
Source15: openstack-heat-api-cloudwatch.init

Source21: %name.tmpfiles

Patch0: %name-6.1.0-remove-bash3-header.patch

BuildArch: noarch

Requires: python3-module-heat = %EVR
Requires(pre): shadow-utils


Requires: %name = %EVR
Requires: %name-engine = %EVR
Requires: %name-api = %EVR
Requires: %name-api-cfn = %EVR
Requires: %name-api-cloudwatch = %EVR

Provides: %name-common  = %EVR
Obsoletes: %name-common  < %EVR

BuildRequires: crudini
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-croniter >= 0.3.4
BuildRequires: python-module-cryptography >= 2.1
BuildRequires: python-module-eventlet >= 0.18.2
BuildRequires: python-module-keystoneauth1 >= 3.4.0
BuildRequires: python-module-keystonemiddleware >= 4.17.0
BuildRequires: python-module-lxml >= 3.4.1
BuildRequires: python-module-netaddr >= 0.7.18
BuildRequires: python-module-neutron-lib >= 1.14.0
BuildRequires: python-module-openstacksdk >= 0.11.2
BuildRequires: python-module-oslo.cache >= 1.26.0
BuildRequires: python-module-oslo.config >= 5.2.0
BuildRequires: python-module-oslo.concurrency >= 3.26.0
BuildRequires: python-module-oslo.context >= 2.19.2
BuildRequires: python-module-oslo.db >= 4.27.0
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-oslo.log >= 3.36.0
BuildRequires: python-module-oslo.messaging >= 5.29.0
BuildRequires: python-module-oslo.middleware >= 3.31.0
BuildRequires: python-module-oslo.policy >= 1.30.0
BuildRequires: python-module-oslo.reports >= 1.18.0
BuildRequires: python-module-oslo.serialization >= 2.18.0
BuildRequires: python-module-oslo.service >= 1.24.0
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-osprofiler >= 1.4.0
BuildRequires: python-module-oslo.versionedobjects >= 1.31.2
BuildRequires: python-module-PasteDeploy >= 1.5.0
BuildRequires: python-module-aodhclient >= 0.9.0
BuildRequires: python-module-barbicanclient >= 4.5.2
BuildRequires: python-module-blazarclient >= 1.0.0
BuildRequires: python-module-cinderclient >= 3.3.0
BuildRequires: python-module-designateclient >= 2.7.0
BuildRequires: python-module-glanceclient >= 2.8.0
BuildRequires: python-module-heatclient >= 1.10.0
BuildRequires: python-module-keystoneclient >= 3.8.0
BuildRequires: python-module-magnumclient >= 2.1.0
BuildRequires: python-module-manilaclient >= 1.16.0
BuildRequires: python-module-mistralclient >= 3.1.0
BuildRequires: python-module-monascaclient >= 1.12.0
BuildRequires: python-module-neutronclient >= 6.7.0
BuildRequires: python-module-novaclient >= 9.1.0
BuildRequires: python-module-octaviaclient >= 1.3.0
BuildRequires: python-module-openstackclient >= 3.12.0
BuildRequires: python-module-saharaclient >= 1.4.0
BuildRequires: python-module-swiftclient >= 3.2.0
BuildRequires: python-module-troveclient >= 2.2.0
BuildRequires: python-module-zaqarclient >= 1.0.0
BuildRequires: python-module-zunclient >= 2.0.0
BuildRequires: python-module-pytz >= 2013.6
BuildRequires: python-module-yaml >= 3.12
BuildRequires: python-module-requests >= 2.14.2
BuildRequires: python-module-tenacity >= 4.4.0
BuildRequires: python-module-routes >= 2.3.1
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-SQLAlchemy >= 1.0.10
BuildRequires: python-module-migrate >= 0.11.0
BuildRequires: python-module-stevedore >= 1.20.0
BuildRequires: python-module-webob >= 1.7.1
BuildRequires: python-module-yaql >= 1.1.3


# doc
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-os-api-ref >= 1.4.0
BuildRequires: python-module-sphinx >= 1.6.2
BuildRequires: python-module-reno >= 2.5.0
BuildRequires: python-module-sphinxcontrib-apidoc >= 0.2.0
BuildRequires: python-module-sphinxcontrib-httpdomain >= 1.3.0


BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-croniter >= 0.3.4
BuildRequires: python3-module-cryptography >= 2.1
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-keystonemiddleware >= 4.17.0
BuildRequires: python3-module-lxml >= 3.4.1
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-neutron-lib >= 1.14.0
BuildRequires: python3-module-openstacksdk >= 0.11.2
BuildRequires: python3-module-oslo.cache >= 1.26.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.concurrency >= 3.26.0
BuildRequires: python3-module-oslo.context >= 2.19.2
BuildRequires: python3-module-oslo.db >= 4.27.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.messaging >= 5.29.0
BuildRequires: python3-module-oslo.middleware >= 3.31.0
BuildRequires: python3-module-oslo.policy >= 1.30.0
BuildRequires: python3-module-oslo.reports >= 1.18.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.service >= 1.24.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-osprofiler >= 1.4.0
BuildRequires: python3-module-oslo.versionedobjects >= 1.31.2
BuildRequires: python3-module-PasteDeploy >= 1.5.0
BuildRequires: python3-module-aodhclient >= 0.9.0
BuildRequires: python3-module-barbicanclient >= 4.5.2
BuildRequires: python3-module-blazarclient >= 1.0.0
BuildRequires: python3-module-cinderclient >= 3.3.0
BuildRequires: python3-module-designateclient >= 2.7.0
BuildRequires: python3-module-glanceclient >= 2.8.0
BuildRequires: python3-module-heatclient >= 1.10.0
BuildRequires: python3-module-keystoneclient >= 3.8.0
BuildRequires: python3-module-magnumclient >= 2.1.0
BuildRequires: python3-module-manilaclient >= 1.16.0
BuildRequires: python3-module-mistralclient >= 3.1.0
BuildRequires: python3-module-monascaclient >= 1.12.0
BuildRequires: python3-module-neutronclient >= 6.7.0
BuildRequires: python3-module-novaclient >= 9.1.0
BuildRequires: python3-module-octaviaclient >= 1.3.0
BuildRequires: python3-module-openstackclient >= 3.12.0
BuildRequires: python3-module-saharaclient >= 1.4.0
BuildRequires: python3-module-swiftclient >= 3.2.0
BuildRequires: python3-module-troveclient >= 2.2.0
BuildRequires: python3-module-zaqarclient >= 1.0.0
BuildRequires: python3-module-zunclient >= 2.0.0
BuildRequires: python3-module-pytz >= 2013.6
BuildRequires: python3-module-yaml >= 3.12
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-tenacity >= 4.4.0
BuildRequires: python3-module-routes >= 2.3.1
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-SQLAlchemy >= 1.0.10
BuildRequires: python3-module-migrate >= 0.11.0
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-webob >= 1.7.1
BuildRequires: python3-module-yaql >= 1.1.3


# doc
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-os-api-ref >= 1.4.0
BuildRequires: python3-module-sphinx >= 1.6.2
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-sphinxcontrib-apidoc >= 0.2.0
#BuildRequires: python3-module-sphinxcontrib-httpdomain >= 1.3.0

%description
Heat provides AWS CloudFormation and CloudWatch functionality for OpenStack.

%package -n python-module-%oname
Summary: Openstack Orchestration (Heat) - Python module
Group:   Development/Python

Requires: python-module-argparse
Requires: python-module-PasteDeploy
Requires: python-module-ceilometerclient
Requires: python-module-cinderclient
Requires: python-module-glanceclient
Requires: python-module-heatclient
Requires: python-module-keystoneclient
Requires: python-module-keystonemiddleware
Requires: python-module-neutronclient
Requires: python-module-novaclient
Requires: python-module-saharaclient
Requires: python-module-swiftclient
Requires: python-module-troveclient

%description -n python-module-%oname
This package contains the core Python module of OpenStack Heat.

%package -n python-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description -n python-module-%oname-tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Openstack Orchestration (Heat) - Python3 module
Group:   Development/Python3


%description -n python3-module-%oname
This package contains the core Python3 module of OpenStack Heat.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package engine
Summary: The Heat engine
Group: System/Servers
Requires: %name = %EVR

%description engine
OpenStack API for starting CloudFormation templates on OpenStack

%package api
Summary: The Heat API
Group: System/Servers
Requires: %name = %EVR

%description api
OpenStack-native ReST API to the Heat Engine

%package api-cfn
Summary: Heat CloudFormation API
Group: System/Servers
Requires: %name = %EVR

%description api-cfn
AWS CloudFormation-compatible API to the Heat Engine

%package api-cloudwatch
Summary: Heat CloudWatch API
Group: System/Servers
Requires: %name = %EVR

%description api-cloudwatch
AWS CloudWatch-compatible API to the Heat Engine

%package plugin-heat_docker
Summary: OpenStack Orchestration (Heat) - Support for Docker
Group: System/Servers
Requires: %name-engine = %EVR
AutoReq: yes, nopython

%description plugin-heat_docker
This plugin enables using Docker containers as resources in a Heat template.

%prep
%setup -n %oname-%version
%patch0 -p2

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

# Remove tests in contrib
find contrib -name tests -type d | xargs rm -r

#NOTE: Kill heat Sphinx extension, we're only building manpages:
sed -i -e "s/'ext.resources',\{0,1\}//" doc/source/conf.py

rm -rf ../python3
cp -a . ../python3

%build
%python_build

PBR_VERSION=%version sphinx-build -b man doc/source/ doc/build/man

# Generate sample config
PYTHONPATH=. oslo-config-generator --config-file=config-generator.conf
PYTHONPATH=. oslopolicy-sample-generator --config-file=etc/heat/heat-policy-generator.conf --output etc/heat/policy.json
rm -f etc/heat/heat-policy-generator.conf

#pushd contrib/heat_docker
#OSLO_PACKAGE_VERSION=%version python setup.py build
#popd

pushd ../python3
%python3_build
popd

%install
%python_install
for f in heat-all heat-api-cfn heat-api heat-engine heat-keystone-setup-domain heat-manage heat-wsgi-api-cfn heat-wsgi-api
    do mv %buildroot%_bindir/$f %buildroot%_bindir/$f.py2
done

pushd ../python3
%python3_install
popd

pushd contrib/heat_docker
OSLO_PACKAGE_VERSION=%version python setup.py install --prefix=%_prefix --root=%buildroot
# no need for the egg-info file
rm -r %buildroot%python_sitelibdir/heat_contrib_docker-*.egg-info

OSLO_PACKAGE_VERSION=%version python3 setup.py install --prefix=%_prefix --root=%buildroot
rm -r %buildroot%python3_sitelibdir/heat_contrib_docker-*.egg-info
popd

sed -i -e '/^#!/,1 d' %buildroot/%python_sitelibdir/heat/db/sqlalchemy/migrate_repo/manage.py
sed -i -e '/^#!/,1 d' %buildroot/%python3_sitelibdir/heat/db/sqlalchemy/migrate_repo/manage.py
mkdir -p %buildroot%_logdir/heat
mkdir -p %buildroot%_runtimedir/heat
install -p -D -m 644 %SOURCE1 %buildroot%_sysconfdir/logrotate.d/openstack-heat

install -p -D -m 644 %SOURCE21 %buildroot%_tmpfilesdir/%name.conf

# install systemd unit files
install -p -D -m 644 %SOURCE2 %buildroot%_unitdir/openstack-heat-api.service
install -p -D -m 644 %SOURCE3 %buildroot%_unitdir/openstack-heat-api-cfn.service
install -p -D -m 644 %SOURCE4 %buildroot%_unitdir/openstack-heat-engine.service
install -p -D -m 644 %SOURCE5 %buildroot%_unitdir/openstack-heat-api-cloudwatch.service

# install sysv init scripts
install -p -D -m 755 %SOURCE12 %buildroot%_initdir/openstack-heat-api
install -p -D -m 755 %SOURCE13 %buildroot%_initdir/openstack-heat-api-cfn
install -p -D -m 755 %SOURCE14 %buildroot%_initdir/openstack-heat-engine
install -p -D -m 755 %SOURCE15 %buildroot%_initdir/openstack-heat-api-cloudwatch

install -d -m 755 %buildroot%_sharedstatedir/heat

%if_enabled doc
export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees source build/html
popd
%endif

mkdir -p %buildroot%_man1dir
install -p -D -m 644 doc/build/man/*.1 %buildroot%_man1dir

rm -f %buildroot/%_bindir/heat-db-setup
rm -f %buildroot/%_mandir/man1/heat-db-setup.*
rm -rf %buildroot/var/lib/heat/.dummy
rm -f %buildroot/usr/bin/cinder-keystone-setup

install -d -m 755 %buildroot%_sysconfdir/heat
install -d -m 755 %buildroot%_sysconfdir/heat/heat.conf.d

mv etc/heat/heat.conf{.sample,}
install -p -m 644 etc/heat/*.{conf,json,ini} %buildroot%_sysconfdir/heat/
install -d -m 755  %buildroot%_sysconfdir/heat/{environment.d,templates}
install -p -m 644 etc/heat/environment.d/*.yaml %buildroot%_sysconfdir/heat/environment.d
install -p -m 644 etc/heat/templates/*.yaml %buildroot%_sysconfdir/heat/templates

### set default configuration
%define heat_conf %buildroot%_sysconfdir/heat/heat.conf.d/010-heat.conf
crudini --set %heat_conf DEFAULT log_dir /var/log/heat
crudini --set %heat_conf oslo_concurrency lock_path %_runtimedir/heat

# cleanup
rm -rf %buildroot/usr/etc/

%pre
# 187:187 for heat (openstack-heat)
%_sbindir/groupadd -r -g 187 -f heat 2>/dev/null ||:
%_sbindir/useradd -r -u 187 -g heat -c 'OpenStack Heat Daemons' \
        -s /sbin/nologin  -d %_sharedstatedir/heat heat 2>/dev/null ||:

%post engine
%post_service %name-engine
%preun engine
%preun_service %name-engine

%post api
%post_service %name-api
%preun api
%preun_service %name-api

%post api-cfn
%post_service %name-api-cfn
%preun api-cfn
%preun_service %name-api-cfn

%post api-cloudwatch
%post_service %name-api-cloudwatch
%preun api-cloudwatch
%preun_service %name-api-cloudwatch

%files
%doc LICENSE
%dir %attr(0775,root,heat) %_logdir/heat
%dir %attr(0775,root,heat) %_runtimedir/heat
%dir %attr(0775,root,heat) %_sharedstatedir/heat
%_tmpfilesdir/%name.conf
%config(noreplace) %_sysconfdir/logrotate.d/openstack-heat
%dir %attr(0755,root,heat) %_sysconfdir/heat
%dir %attr(0755,root,heat) %_sysconfdir/heat/heat.conf.d
%config(noreplace) %attr(0640, root, heat) %_sysconfdir/heat/heat.conf
%config(noreplace) %attr(0640, root, heat) %_sysconfdir/heat/heat.conf.d/010-heat.conf
%config(noreplace) %attr(0640, root, heat) %_sysconfdir/heat/api-paste.ini
%config(noreplace) %_sysconfdir/heat/policy.json
%config %_sysconfdir/heat/environment.d
%config %_sysconfdir/heat/templates
%_man1dir/heat-keystone-setup.1*
%_man1dir/heat-keystone-setup-domain.1*
%_man1dir/heat-manage.1*

%files -n python-module-%oname
%_bindir/*.py2
%python_sitelibdir/*
%exclude %python_sitelibdir/heat_integrationtests
%exclude %python_sitelibdir/%oname/tests

%files -n python-module-%oname-tests
%python_sitelibdir/%oname/tests
%python_sitelibdir/heat_integrationtests
%exclude %python_sitelibdir/heat_integrationtests/pre_test_hook.sh

%files -n python3-module-%oname
%_bindir/*
%exclude %_bindir/*.py2
%python3_sitelibdir/*
%exclude %python3_sitelibdir/heat_integrationtests
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/heat_integrationtests
%exclude %python3_sitelibdir/heat_integrationtests/pre_test_hook.sh

%files engine
%doc README.rst LICENSE
%if_enabled doc
%doc doc/build/html/man/heat-engine.html
%endif
%_man1dir/heat-engine.1.*
%_unitdir/%name-engine.service
%_initdir/%name-engine

%files api
%doc README.rst LICENSE
%if_enabled doc
%doc doc/build/html/man/heat-api.html
%endif
%_man1dir/heat-api.1.*
%_unitdir/%name-api.service
%_initdir/%name-api

%files api-cfn
%doc README.rst LICENSE
%if_enabled doc
%doc doc/build/html/man/heat-api-cfn.html
%endif
%_man1dir/heat-api-cfn.1.*
%_unitdir/%name-api-cfn.service
%_initdir/%name-api-cfn

%files api-cloudwatch
%doc README.rst LICENSE
%if_enabled doc
%doc doc/build/html/man/heat-api-cloudwatch.html
%_man1dir/heat-api-cloudwatch.1.*
%endif
%_unitdir/%name-api-cloudwatch.service
%_initdir/%name-api-cloudwatch

%files plugin-heat_docker
%_prefix/lib/heat/docker/*.py

%changelog
* Mon Jan 14 2019 Alexey Shabalin <shaba@altlinux.org> 1:11.0.0-alt1
- 11.0.0 Rocky release
- switch to python3

* Fri Jun 22 2018 Grigory Ustinov <grenka@altlinux.org> 1:8.0.3-alt2
- Fixed FTBFS (remove python-module-setuptools-tests from BR).

* Thu Aug 10 2017 Alexey Shabalin <shaba@altlinux.ru> 1:8.0.3-alt1
- 8.0.3

* Thu Jun 22 2017 Alexey Shabalin <shaba@altlinux.ru> 1:8.0.2-alt2
- drop signing_dir from default config

* Tue Jun 13 2017 Alexey Shabalin <shaba@altlinux.ru> 1:8.0.2-alt1
- 8.0.2

* Tue Jun 13 2017 Alexey Shabalin <shaba@altlinux.ru> 1:8.0.1-alt1
- 8.0.1 Ocata release

* Wed Apr 12 2017 Alexey Shabalin <shaba@altlinux.ru> 1:7.0.2-alt1
- 7.0.2

* Tue Nov 22 2016 Alexey Shabalin <shaba@altlinux.ru> 1:7.0.1-alt1
- 7.0.1
- fix dir permitions
- fix logrotate
- drop dist config in datadir again

* Fri Nov 11 2016 Lenar Shakirov <snejok@altlinux.ru> 1:6.1.0-alt1
- 6.1.0 Mitaka Release

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 1:5.0.1-alt1
- 5.0.1

* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1:5.0.0-alt1
- 5.0.0 Liberty Release

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.2-alt1
- 2015.1.2

* Mon Aug 31 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.1-alt1
- 2015.1.1
- drop common package
- drop dist config in datadir

* Mon Jun 01 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt1
- 2015.1.0 Kilo release

* Fri Mar 13 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b2.0
- 2015.1.0b2

* Fri Aug 15 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.2-alt2
- Patch added: 0100-migration-to-work-w-MySQL-5.6.patch

* Tue Aug 12 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.2-alt1
- First build for ALT (based on Fedora 2014.1.2-0.4.fc21.src)
