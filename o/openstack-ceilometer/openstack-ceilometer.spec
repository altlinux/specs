%global _without_doc 1
%global with_doc %{!?_without_doc:1}%{?_without_doc:0}
%global pypi_name ceilometer

Name:             openstack-ceilometer
Version:          2014.1.1
Release:          alt1
Summary:          OpenStack measurement collection service

Group:            System/Servers
License:          ASL 2.0
URL:              https://wiki.openstack.org/wiki/Ceilometer
Source0:          %{name}-%{version}.tar
Source1:          %{pypi_name}-dist.conf
Source2:          %{pypi_name}.logrotate

Source10:         %{name}-api.service
Source11:         %{name}-collector.service
Source12:         %{name}-compute.service
Source13:         %{name}-central.service
Source14:         %{name}-alarm-notifier.service
Source15:         %{name}-alarm-evaluator.service
Source16:         %{name}-notification.service

#
# patches_base=d3899f186fee9ad4f050ec41a779814eed87258c
#
Patch0001: 0001-Ensure-routing-key-is-specified-in-the-address-for-a.patch
Patch0002: 0002-remove-token-from-notifier-middleware.patch

BuildArch:        noarch
BuildRequires:    python-module-sphinx
BuildRequires:    python-module-setuptools
BuildRequires:    python-module-pbr
BuildRequires:    python-module-d2to1
BuildRequires:    python-devel


%description
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.


%package -n       python-module-ceilometer
Summary:          OpenStack ceilometer python libraries
Group:            Development/Python

Requires:         python-module-qpid
Requires:         python-module-kombu

Requires:         python-module-babel
Requires:         python-module-eventlet
Requires:         python-module-greenlet
Requires:         python-module-iso8601
Requires:         python-module-lxml
Requires:         python-module-anyjson
Requires:         python-module-jsonpath-rw
Requires:         python-module-stevedore >= 0.14
Requires:         python-module-msgpack
Requires:         python-module-six >= 1.6

Requires:         python-module-SQLAlchemy
Requires:         python-module-alembic
Requires:         python-module-migrate

Requires:         python-module-webob
Requires:         python-module-oslo-config >= 1.2.0
Requires:         python-module-yaml

Requires:         python-module-pysnmp
Requires:         python-module-pytz
Requires:         python-module-croniter

# These were only added as global dependencies
# at the end of the Icehouse cycle with the change
# to cli.py referenced from in http://pad.lv/1317210
Requires:         python-module-pymongo
Requires:         python-module-flask
Requires:         python-module-pecan >= 0.4.5
Requires:         python-module-wsme >= 0.6
Requires:         python-module-novaclient
Requires:         python-module-keystoneclient
Requires:         python-module-glanceclient
Requires:         python-module-swiftclient
Requires:         python-module-ceilometerclient
Requires:         python-module-libvirt

%description -n   python-module-ceilometer
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains the ceilometer python library.


%package common
Summary:          Components common to all OpenStack ceilometer services
Group:            System/Servers

Requires:         python-module-ceilometer = %{version}-%{release}
Requires:         openstack-utils

Requires(pre):    shadow-utils


%description common
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains components common to all OpenStack
ceilometer services.


%package compute
Summary:          OpenStack ceilometer compute agent
Group:            System/Servers

Requires:         %{name}-common = %{version}-%{release}

Requires:         python-module-novaclient
Requires:         python-module-keystoneclient
Requires:         python-module-libvirt

%description compute
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains the ceilometer agent for
running on OpenStack compute nodes.


%package central
Summary:          OpenStack ceilometer central agent
Group:            System/Servers

Requires:         %{name}-common = %{version}-%{release}

Requires:         python-module-novaclient
Requires:         python-module-keystoneclient
Requires:         python-module-glanceclient
Requires:         python-module-swiftclient

%description central
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains the central ceilometer agent.


%package collector
Summary:          OpenStack ceilometer collector
Group:            System/Servers

Requires:         %{name}-common = %{version}-%{release}

# For compat with older provisioning tools.
# Remove when all reference the notification package explicitly
Requires:         %{name}-notification

Requires:         python-module-pymongo

%description collector
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains the ceilometer collector service
which collects metrics from the various agents.


%package notification
Summary:          OpenStack ceilometer notification agent
Group:            System/Servers

Requires:         %{name}-common = %{version}-%{release}

%description notification
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains the ceilometer notification agent
which pushes metrics to the collector service from the
various OpenStack services.


%package api
Summary:          OpenStack ceilometer API service
Group:            System/Servers

Requires:         %{name}-common = %{version}-%{release}

Requires:         python-module-pymongo
Requires:         python-module-flask
Requires:         python-module-pecan >= 0.4.5
Requires:         python-module-wsme >= 0.6

%description api
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains the ceilometer API service.


%package alarm
Summary:          OpenStack ceilometer alarm services
Group:            System/Servers

Requires:         %{name}-common = %{version}-%{release}
Requires:         python-module-ceilometerclient

%description alarm
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains the ceilometer alarm notification
and evaluation services.


%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack ceilometer
Group:            Documentation

# Required to build module documents
BuildRequires:    python-module-eventlet
BuildRequires:    python-module-sqlalchemy
BuildRequires:    python-module-webob
# while not strictly required, quiets the build down when building docs.
BuildRequires:    python-module-migrate, python-module-iso8601

%description      doc
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains documentation files for ceilometer.
%endif

%prep
%setup

%patch0001 -p1
%patch0002 -p1

find . \( -name .gitignore -o -name .placeholder \) -delete

find ceilometer -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

# TODO: Have the following handle multi line entries
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

# Programmatically update defaults in sample config
# which is installed at /etc/ceilometer/ceilometer.conf
# TODO: Make this more robust
# Note it only edits the first occurance, so assumes a section ordering in sample
# and also doesn't support multi-valued variables.
while read name eq value; do
  test "$name" && test "$value" || continue
  sed -i "0,/^# *$name=/{s!^# *$name=.*!#$name=$value!}" etc/ceilometer/ceilometer.conf.sample
done < %{SOURCE1}

%build
%python_build

%install
%python_install

# docs generation requires everything to be installed first
export PYTHONPATH="$( pwd ):$PYTHONPATH"

pushd doc

%if 0%{?with_doc}
SPHINX_DEBUG=1 sphinx-build -b html source build/html
# Fix hidden-file-or-dir warnings
rm -fr build/html/.doctrees build/html/.buildinfo
%endif

popd

# Setup directories
install -d -m 755 %{buildroot}%{_sharedstatedir}/ceilometer
install -d -m 755 %{buildroot}%{_sharedstatedir}/ceilometer/tmp
install -d -m 755 %{buildroot}%{_logdir}/ceilometer

# Install config files
install -d -m 755 %{buildroot}%{_sysconfdir}/ceilometer
install -p -D -m 640 %{SOURCE1} %{buildroot}%{_datadir}/ceilometer/ceilometer-dist.conf
install -p -D -m 640 etc/ceilometer/ceilometer.conf.sample %{buildroot}%{_sysconfdir}/ceilometer/ceilometer.conf
install -p -D -m 640 etc/ceilometer/policy.json %{buildroot}%{_sysconfdir}/ceilometer/policy.json
install -p -D -m 640 etc/ceilometer/sources.json %{buildroot}%{_sysconfdir}/ceilometer/sources.json
install -p -D -m 640 etc/ceilometer/pipeline.yaml %{buildroot}%{_sysconfdir}/ceilometer/pipeline.yaml

# Install initscripts for services
install -p -D -m 644 %{SOURCE10} %{buildroot}%{_unitdir}/%{name}-api.service
install -p -D -m 644 %{SOURCE11} %{buildroot}%{_unitdir}/%{name}-collector.service
install -p -D -m 644 %{SOURCE12} %{buildroot}%{_unitdir}/%{name}-compute.service
install -p -D -m 644 %{SOURCE13} %{buildroot}%{_unitdir}/%{name}-central.service
install -p -D -m 644 %{SOURCE14} %{buildroot}%{_unitdir}/%{name}-alarm-notifier.service
install -p -D -m 644 %{SOURCE15} %{buildroot}%{_unitdir}/%{name}-alarm-evaluator.service
install -p -D -m 644 %{SOURCE16} %{buildroot}%{_unitdir}/%{name}-notification.service

# Install logrotate
install -p -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Remove unneeded in production stuff
rm -f %{buildroot}%{_bindir}/ceilometer-debug
rm -fr %{buildroot}%{python_sitelibdir}/tests/
rm -fr %{buildroot}%{python_sitelibdir}/run_tests.*
rm -f %{buildroot}/usr/share/doc/ceilometer/README*
rm -f %{buildroot}/%{python_sitelibdir}/ceilometer/api/v1/static/LICENSE.*


%pre common
getent group ceilometer >/dev/null || groupadd -r ceilometer --gid 166
if ! getent passwd ceilometer >/dev/null; then
  # Id reservation request: https://bugzilla.redhat.com/923891
  useradd -u 166 -r -g ceilometer -G ceilometer,nobody -d %{_sharedstatedir}/ceilometer -s /sbin/nologin -c "OpenStack ceilometer Daemons" ceilometer
fi
exit 0

%post compute
%post_service %{name}-compute

%post collector
%post_service %{name}-collector

%post notification
%post_service %{name}-notification

%post api
%post_service %{name}-api

%post central
%post_service %{name}-central

%post alarm
%post_service %{name}-alarm-notifier
%post_service %{name}-alarm-evaluator

%preun compute
%preun_service %{name}-compute

%preun collector
%preun_service %{name}-collector

%preun notification
%preun_service %{name}-notification

%preun api
%preun_service %{name}-api

%preun central
%preun_service %{name}-central

%preun alarm
%preun_service %{name}-alarm-notifier
%preun_service %{name}-alarm-evaluator

%files common
%doc LICENSE
%dir %{_sysconfdir}/ceilometer
%attr(-, root, ceilometer) %{_datadir}/ceilometer/ceilometer-dist.conf
%config(noreplace) %attr(-, root, ceilometer) %{_sysconfdir}/ceilometer/ceilometer.conf
%config(noreplace) %attr(-, root, ceilometer) %{_sysconfdir}/ceilometer/policy.json
%config(noreplace) %attr(-, root, ceilometer) %{_sysconfdir}/ceilometer/sources.json
%config(noreplace) %attr(-, root, ceilometer) %{_sysconfdir}/ceilometer/pipeline.yaml
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}

%dir %attr(0755, ceilometer, root) %{_logdir}/ceilometer

%{_bindir}/ceilometer-dbsync
%{_bindir}/ceilometer-expirer
%{_bindir}/ceilometer-send-sample


%defattr(-, ceilometer, ceilometer, -)
%dir %{_sharedstatedir}/ceilometer
%dir %{_sharedstatedir}/ceilometer/tmp


%files -n python-module-ceilometer
%{python_sitelibdir}/ceilometer
%{python_sitelibdir}/ceilometer-%{version}*.egg-info


%if 0%{?with_doc}
%files doc
%doc doc/build/html
%endif


%files compute
%{_bindir}/ceilometer-agent-compute
%{_unitdir}/%{name}-compute.service


%files collector
%{_bindir}/ceilometer-collector*
%{_unitdir}/%{name}-collector.service

%files notification
%{_bindir}/ceilometer-agent-notification
%{_unitdir}/%{name}-notification.service

%files api
%doc ceilometer/api/v1/static/LICENSE.*
%{_bindir}/ceilometer-api
%{_unitdir}/%{name}-api.service


%files central
%{_bindir}/ceilometer-agent-central
%{_unitdir}/%{name}-central.service


%files alarm
%{_bindir}/ceilometer-alarm-notifier
%{_bindir}/ceilometer-alarm-evaluator
%{_unitdir}/%{name}-alarm-notifier.service
%{_unitdir}/%{name}-alarm-evaluator.service


%changelog
* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt1
- First build for ALT (based on Fedora 2014.1.1-3.fc21.src)
