%def_disable doc
%add_python_req_skip senlinclient

Name: openstack-heat
Summary: OpenStack Orchestration (heat)
Version: 6.1.0
Release: alt1
Epoch: 1
License: ASL 2.0
Group: System/Servers
Url: http://www.openstack.org
Source0: %name-%version.tar

Source1: heat.logrotate
Source2: openstack-heat-api.service
Source3: openstack-heat-api-cfn.service
Source4: openstack-heat-engine.service
Source5: openstack-heat-api-cloudwatch.service

Source12: openstack-heat-api.init
Source13: openstack-heat-api-cfn.init
Source14: openstack-heat-engine.init
Source15: openstack-heat-api-cloudwatch.init

Source20: heat-dist.conf
Source21: %name.tmpfiles

Patch0: %name-6.1.0-remove-bash3-header.patch

BuildArch: noarch
BuildRequires: git
BuildRequires: python-devel
BuildRequires: python-module-stevedore >= 1.5.0
BuildRequires: python-module-oslo.cache >= 0.4.0
BuildRequires: python-module-oslo.context >= 0.2.0
BuildRequires: python-module-oslo.middleware >= 2.8.0
BuildRequires: python-module-oslo.policy >= 0.5.0
BuildRequires: python-module-oslo.messaging >= 1.16.0
BuildRequires: python-module-setuptools
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-oslo.db >= 2.4.1
BuildRequires: python-module-oslo.utils >= 2.0.0
BuildRequires: python-module-oslo.log >= 1.8.0
BuildRequires: python-module-oslo.versionedobjects >= 0.9.0
BuildRequires: python-module-argparse
BuildRequires: python-module-eventlet >= 0.17.4
BuildRequires: python-module-greenlet >= 0.3.2
BuildRequires: python-module-httplib2
BuildRequires: python-module-iso8601
BuildRequires: python-module-kombu >= 3.0.7
BuildRequires: python-module-lxml >= 2.3
BuildRequires: python-module-netaddr >= 0.7.12
BuildRequires: python-module-memcached
BuildRequires: python-module-migrate >= 0.9.6
BuildRequires: python-module-osprofiler >= 1.2.0
BuildRequires: python-module-qpid
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-yaml
BuildRequires: python-module-sphinx
BuildRequires: python-module-paramiko
BuildRequires: python-module-dogpile.cache

# These are required to build due to the requirements check added
BuildRequires: python-module-PasteDeploy
BuildRequires: python-module-routes >= 1.12.3
BuildRequires: python-module-SQLAlchemy >= 0.9.9
BuildRequires: python-module-webob
BuildRequires: python-module-d2to1
BuildRequires: python-module-cryptography >= 1.0

BuildRequires: python-module-oslo.config >= 3.7.0
BuildRequires: python-module-redis-py
BuildRequires: python-module-zmq
BuildRequires: python-module-retrying
BuildRequires: python-module-keystoneclient >= 1.6.0

%if_enabled doc
BuildRequires: python-module-cinderclient >= 1.3.1
BuildRequires: python-module-novaclient >= 2.28.1
BuildRequires: python-module-saharaclient >= 0.10.0
BuildRequires: python-module-neutronclient >= 2.6.0
BuildRequires: python-module-swiftclient >= 2.2.0
BuildRequires: python-module-heatclient >= 0.3.0
BuildRequires: python-module-ceilometerclient >= 1.5.0
BuildRequires: python-module-glanceclient >= 0.18.0
BuildRequires: python-module-troveclient >= 1.2.0
%endif

Requires: %name = %epoch:%version-%release
Requires: %name-engine = %epoch:%version-%release
Requires: %name-api = %epoch:%version-%release
Requires: %name-api-cfn = %epoch:%version-%release
Requires: %name-api-cloudwatch = %epoch:%version-%release

Requires: python-module-heat = %EVR
Requires(pre): shadow-utils

Provides: %name-common  = %EVR
Obsoletes: %name-common  < %EVR

%description
Heat provides AWS CloudFormation and CloudWatch functionality for OpenStack.

%package -n python-module-heat
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

%description -n python-module-heat
This package contains the core Python module of OpenStack Heat.

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
Requires: %name = %EVR
Requires: %name-engine = %EVR

%description plugin-heat_docker
This plugin enables using Docker containers as resources in a Heat template.

%package -n python-module-heat-tests
Summary:        Heat tests
Group:   Development/Python
Requires:       %name = %epoch:%version-%release

%description -n python-module-heat-tests
Heat provides AWS CloudFormation and CloudWatch functionality for OpenStack.
This package contains the Heat test files.

%prep
%setup
%patch0 -p2

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

# Remove tests in contrib
find contrib -name tests -type d | xargs rm -r

%build
%python_build
# Generate sample config
PYTHONPATH=. oslo-config-generator --config-file=config-generator.conf

#pushd contrib/heat_docker
#OSLO_PACKAGE_VERSION=%version python setup.py build
#popd

%install
%python_install

pushd contrib/heat_docker
OSLO_PACKAGE_VERSION=%version python setup.py install --prefix=%_prefix --root=%buildroot
# no need for the egg-info file
rm -r %buildroot%python_sitelibdir/heat_contrib_docker-*.egg-info
popd

sed -i -e '/^#!/,1 d' %buildroot/%python_sitelibdir/heat/db/sqlalchemy/migrate_repo/manage.py
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
install -d -m 755 %buildroot%_sysconfdir/heat

%if_enabled doc
export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees source build/html
sphinx-build -b man -d build/doctrees source build/man

mkdir -p %buildroot%_man1dir
install -p -D -m 644 build/man/*.1 %buildroot%_man1dir
popd
%endif

rm -f %buildroot/%_bindir/heat-db-setup
rm -f %buildroot/%_mandir/man1/heat-db-setup.*
rm -rf %buildroot/var/lib/heat/.dummy
rm -f %{buildroot}/usr/bin/cinder-keystone-setup

install -p -D -m 640 etc/heat/heat.conf.sample %buildroot/%_sysconfdir/heat/heat.conf
install -p -D -m 640 %SOURCE20 %buildroot%_datadir/heat/heat-dist.conf
install -p -D -m 640 etc/heat/api-paste.ini %buildroot/%_datadir/heat/api-paste-dist.ini
install -p -D -m 640 etc/heat/policy.json %buildroot/%_sysconfdir/heat

# TODO: move this to setup.cfg
cp -vr etc/heat/templates %{buildroot}/%{_sysconfdir}/heat
cp -vr etc/heat/environment.d %{buildroot}/%{_sysconfdir}/heat

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
%_bindir/heat-manage
%_bindir/heat-keystone-setup
%_bindir/heat-keystone-setup-domain
%attr(-, root, heat) %_datadir/heat/heat-dist.conf
%attr(-, root, heat) %_datadir/heat/api-paste-dist.ini
%dir %attr(0755,heat,root) %_logdir/heat
%dir %attr(0755,heat,root) %_runtimedir/heat
%dir %attr(0755,heat,root) %_sharedstatedir/heat
%dir %attr(0755,heat,root) %{_sysconfdir}/heat
%_tmpfilesdir/%name.conf
%config(noreplace) %_sysconfdir/logrotate.d/openstack-heat
%config(noreplace) %attr(-, root, heat) %_sysconfdir/heat/heat.conf
%config(noreplace) %attr(-, root, heat) %_sysconfdir/heat/policy.json
%config(noreplace) %attr(-, root, heat) %_sysconfdir/heat/environment.d/
%config(noreplace) %attr(-, root, heat) %_sysconfdir/heat/templates/
%if_enabled doc
%_mandir/man1/heat-keystone-setup.1.gz
%_mandir/man1/heat-keystone-setup-domain.1.gz
%_mandir/man1/heat-manage.1.gz
%endif

%files -n python-module-heat
%python_sitelibdir/*
%exclude %python_sitelibdir/heat/tests

%files engine
%doc README.rst LICENSE
%if_enabled doc
%doc doc/build/html/man/heat-engine.html
%_man1dir/heat-engine.1.*
%endif
%_bindir/heat-engine
%_unitdir/%name-engine.service
%_initdir/%name-engine

%files api
%doc README.rst LICENSE
%if_enabled doc
%doc doc/build/html/man/heat-api.html
%_man1dir/heat-api.1.*
%endif
%_bindir/heat-api
%_bindir/heat-wsgi-api
%_unitdir/%name-api.service
%_initdir/%name-api

%files api-cfn
%doc README.rst LICENSE
%if_enabled doc
%doc doc/build/html/man/heat-api-cfn.html
%_man1dir/heat-api-cfn.1.*
%endif
%_bindir/heat-api-cfn
%_bindir/heat-wsgi-api-cfn
%_unitdir/%name-api-cfn.service
%_initdir/%name-api-cfn

%files api-cloudwatch
%doc README.rst LICENSE
%if_enabled doc
%doc doc/build/html/man/heat-api-cloudwatch.html
%_man1dir/heat-api-cloudwatch.1.*
%endif
%_bindir/heat-api-cloudwatch
%_bindir/heat-wsgi-api-cloudwatch
%_unitdir/%name-api-cloudwatch.service
%_initdir/%name-api-cloudwatch

%files plugin-heat_docker
%_prefix/lib/heat/docker

%changelog
* Thu Nov 11 2016 Lenar Shakirov <snejok@altlinux.ru> 1:6.1.0-alt1
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
