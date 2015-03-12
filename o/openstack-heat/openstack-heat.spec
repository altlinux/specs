# TODO: fix build docs
%def_disable doc

Name: openstack-heat
Summary: OpenStack Orchestration (heat)
Version: 2015.1.0
Release: alt0.b2.0
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
Source22: heat.conf.sample

#
# patches_base=2014.1.2+1
#
Patch0001: 0001-remove-pbr-runtime-dependency.patch

BuildArch: noarch
BuildRequires: git
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-argparse
BuildRequires: python-module-eventlet
BuildRequires: python-module-greenlet
BuildRequires: python-module-httplib2
BuildRequires: python-module-iso8601
BuildRequires: python-module-kombu
BuildRequires: python-module-lxml
BuildRequires: python-module-netaddr
BuildRequires: python-module-memcached
BuildRequires: python-module-migrate
BuildRequires: python-module-six
BuildRequires: python-module-yaml
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
# These are required to build due to the requirements check added
BuildRequires: python-module-PasteDeploy
BuildRequires: python-module-routes
BuildRequires: python-module-SQLAlchemy
BuildRequires: python-module-webob
BuildRequires: python-module-pbr
BuildRequires: python-module-d2to1
BuildRequires: python-module-qpid


BuildRequires: python-module-oslo.config >= 1.6.0
BuildRequires: python-module-oslo.context >= 0.1.0
BuildRequires: python-module-oslo.db >= 1.4.1
BuildRequires: python-module-oslo.i18n >= 1.3.0
BuildRequires: python-module-oslo.messaging >= 1.4.0
BuildRequires: python-module-oslo.middleware >= 0.3.0
BuildRequires: python-module-oslo.serialization >= 1.2.0
BuildRequires: python-module-oslo.utils >= 1.2.0

BuildRequires: python-module-cinderclient
BuildRequires: python-module-keystoneclient
BuildRequires: python-module-novaclient
BuildRequires: python-module-neutronclient
BuildRequires: python-module-swiftclient
BuildRequires: python-module-heatclient

Requires: %name-common = %version-%release
Requires: %name-engine = %version-%release
Requires: %name-api = %version-%release
Requires: %name-api-cfn = %version-%release
Requires: %name-api-cloudwatch = %version-%release

%description
Heat provides AWS CloudFormation and CloudWatch functionality for OpenStack.

%package common
Summary: Heat common
Group: System/Servers

Requires: python-module-ceilometerclient
Requires: python-module-cinderclient
Requires: python-module-glanceclient
Requires: python-module-heatclient
Requires: python-module-keystoneclient
Requires: python-module-neutronclient
Requires: python-module-novaclient
Requires: python-module-swiftclient
Requires: python-module-troveclient

Requires(pre): shadow-utils

%description common
Components common to all OpenStack Heat services

%package engine
Summary: The Heat engine
Group: System/Servers

Requires: %name-common = %version-%release

%description engine
OpenStack API for starting CloudFormation templates on OpenStack

%package api
Summary: The Heat API
Group: System/Servers

Requires: %name-common = %version-%release

%description api
OpenStack-native ReST API to the Heat Engine

%package api-cfn
Summary: Heat CloudFormation API
Group: System/Servers

Requires: %name-common = %version-%release

%description api-cfn
AWS CloudFormation-compatible API to the Heat Engine

%package api-cloudwatch
Summary: Heat CloudWatch API
Group: System/Servers

Requires: %name-common = %version-%release

%description api-cloudwatch
AWS CloudWatch-compatible API to the Heat Engine

%prep
%setup

%patch0001 -p1

sed -i s/REDHATHEATVERSION/%version/ heat/version.py
sed -i s/REDHATHEATRELEASE/%release/ heat/version.py


# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

# Remove tests in contrib
find contrib -name tests -type d | xargs rm -r

install -p -D -m 640 %SOURCE22 etc/heat/heat.conf.sample

# Programmatically update defaults in sample config
# which is installed at /etc/heat/heat.conf

#  First we ensure all values are commented in appropriate format.
#  Since icehouse, there was an uncommented keystone_authtoken section
#  at the end of the file which mimics but also conflicted with our
#  distro editing that had been done for many releases.
sed -i '/^[^#[]/{s/^/#/; s/ //g}; /^#[^ ]/s/ = /=/' etc/heat/heat.conf.sample
sed -i -e "s/^#heat_revision=.*$/heat_revision=%version-%release/I" etc/heat/heat.conf.sample

#  TODO: Make this more robust
#  Note it only edits the first occurance, so assumes a section ordering in sample
#  and also doesn't support multi-valued variables.
while read name eq value; do
  test "$name" && test "$value" || continue
  sed -i "0,/^# *$name=/{s!^# *$name=.*!#$name=$value!}" etc/heat/heat.conf.sample
done < %SOURCE20

%build
%python_build


%install
%python_install
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

mkdir -p %buildroot%_sharedstatedir/heat
mkdir -p %buildroot%_sysconfdir/heat

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
rm -f %buildroot/usr/bin/cinder-keystone-setup
rm -rf %buildroot/%python_sitelibdir/heat/tests

install -p -D -m 640 %_builddir/%name-%version/etc/heat/heat.conf.sample %buildroot/%_sysconfdir/heat/heat.conf
install -p -D -m 640 %SOURCE20 %buildroot%_datadir/heat/heat-dist.conf
install -p -D -m 640 %_builddir/%name-%version/etc/heat/api-paste.ini %buildroot/%_datadir/heat/api-paste-dist.ini
install -p -D -m 640 etc/heat/policy.json %buildroot/%_sysconfdir/heat

# TODO: move this to setup.cfg
cp -vr etc/heat/templates %buildroot/%_sysconfdir/heat
cp -vr etc/heat/environment.d %buildroot/%_sysconfdir/heat



%pre common
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

%files common
%doc LICENSE
%_bindir/heat-manage
%_bindir/heat-keystone-setup
%_bindir/heat-keystone-setup-domain
%python_sitelibdir/heat*
%attr(-, root, heat) %_datadir/heat/heat-dist.conf
%attr(-, root, heat) %_datadir/heat/api-paste-dist.ini
%dir %attr(0755,heat,root) %_logdir/heat
%dir %attr(0755,heat,root) %_runtimedir/heat
%dir %attr(0755,heat,root) %_sharedstatedir/heat
%dir %attr(0755,heat,root) %_sysconfdir/heat
%_tmpfilesdir/%name.conf
%config(noreplace) %_sysconfdir/logrotate.d/openstack-heat
%config(noreplace) %attr(-, root, heat) %_sysconfdir/heat/heat.conf
%config(noreplace) %attr(-, root, heat) %_sysconfdir/heat/policy.json
%config(noreplace) %attr(-, root, heat) %_sysconfdir/heat/environment.d
%config(noreplace) %attr(-, root, heat) %_sysconfdir/heat/templates
%if_enabled doc
%_mandir/man1/heat-keystone-setup.1.gz
%_mandir/man1/heat-manage.1.gz
%endif

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
%_unitdir/%name-api.service
%_initdir/%name-api

%files api-cfn
%doc README.rst LICENSE
%if_enabled doc
%doc doc/build/html/man/heat-api-cfn.html
%_man1dir/heat-api-cfn.1.*
%endif
%_bindir/heat-api-cfn
%_unitdir/%name-api-cfn.service
%_initdir/%name-api-cfn

%files api-cloudwatch
%doc README.rst LICENSE
%if_enabled doc
%doc doc/build/html/man/heat-api-cloudwatch.html
%_man1dir/heat-api-cloudwatch.1.*
%endif
%_bindir/heat-api-cloudwatch
%_unitdir/%name-api-cloudwatch.service
%_initdir/%name-api-cloudwatch

%changelog
* Fri Mar 13 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b2.0
- 2015.1.0b2

* Fri Aug 15 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.2-alt2
- Patch added: 0100-migration-to-work-w-MySQL-5.6.patch

* Tue Aug 12 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.2-alt1
- First build for ALT (based on Fedora 2014.1.2-0.4.fc21.src)

