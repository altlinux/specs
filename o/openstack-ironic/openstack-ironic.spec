Name:           openstack-ironic
Summary:        OpenStack Baremetal Hypervisor API (ironic)
Group:          System/Servers
Version:        2015.1.1
Release:        alt1
License:        ASL 2.0
URL:            http://www.openstack.org
Source0:        %name-%version.tar

Source1:        openstack-ironic-api.service
Source2:        openstack-ironic-conductor.service
Source3:        ironic-rootwrap-sudoers

Patch0001: 0001-Set-default-DB-location.patch

BuildArch:      noarch
BuildRequires:  python-module-setuptools
BuildRequires:  python-devel
BuildRequires:  python-module-pbr
BuildRequires:  openssl-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  gmp-devel
BuildRequires:  python-module-sphinx


%prep
%setup

%patch0001 -p1

rm requirements.txt test-requirements.txt

%build
%python_build

%install
%python_install


# install systemd scripts
mkdir -p %{buildroot}%{_unitdir}
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}
install -p -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}

# install sudoers file
mkdir -p %{buildroot}%{_sysconfdir}/sudoers.d
install -p -D -m 440 %{SOURCE3} %{buildroot}%{_sysconfdir}/sudoers.d/ironic

mkdir -p %{buildroot}%{_sharedstatedir}/ironic/
mkdir -p %{buildroot}%{_sysconfdir}/ironic/rootwrap.d

#Populate the conf dir
install -p -D -m 640 etc/ironic/ironic.conf.sample %{buildroot}/%{_sysconfdir}/ironic/ironic.conf
install -p -D -m 640 etc/ironic/policy.json %{buildroot}/%{_sysconfdir}/ironic/policy.json
install -p -D -m 640 etc/ironic/rootwrap.conf %{buildroot}/%{_sysconfdir}/ironic/rootwrap.conf
install -p -D -m 640 etc/ironic/rootwrap.d/* %{buildroot}/%{_sysconfdir}/ironic/rootwrap.d/


%description
Ironic provides an API for management and provisioning of physical machines

%package common
Summary: Ironic common
Group: System/Servers

Requires:       ipmitool
Requires:       python-module-eventlet
Requires:       python-module-greenlet
Requires:       python-module-iso8601
Requires:       python-module-jsonpatch
Requires:       python-module-keystonemiddleware
Requires:       python-module-lxml
Requires:       python-module-migrate
Requires:       python-module-mock
Requires:       python-module-netaddr
Requires:       python-module-oslo.concurrency >= 1.8.0
Requires:       python-module-oslo.config
Requires:       python-module-oslo.context >= 0.2.0
Requires:       python-module-oslo.db
Requires:       python-module-oslo.i18n
Requires:       python-module-oslo.policy >= 0.3.1
Requires:       python-module-oslo.rootwrap
Requires:       python-module-oslo.serialization >= 1.4.0
Requires:       python-module-oslo.utils
Requires:       python-module-paramiko
Requires:       python-module-pbr
Requires:       python-module-pecan
Requires:       python-module-retrying
Requires:       python-module-requests >= 2.3.1
Requires:       python-module-six
Requires:       python-module-stevedore
Requires:       python-module-webob
Requires:       python-module-websockify
Requires:       python-module-wsme
Requires:       python-module-Crypto
Requires:       python-module-SQLAlchemy
Requires:       python-module-neutronclient
Requires:       python-module-glanceclient
Requires:       python-module-keystoneclient
Requires:       python-module-swiftclient
Requires:       python-module-jinja2
Requires:       python-module-pyghmi
Requires:       python-module-alembic
Requires:       python-module-pysendfile

Requires(pre):  shadow-utils

%description common
Components common to all OpenStack Ironic services


%files common
%doc README.rst LICENSE
%{_bindir}/ironic-dbsync
%{_bindir}/ironic-rootwrap
%python_sitelibdir/ironic*
%{_sysconfdir}/sudoers.d/ironic
%config(noreplace) %attr(-,root,ironic) %{_sysconfdir}/ironic
%attr(-,ironic,ironic) %{_sharedstatedir}/ironic

%pre common
getent group ironic >/dev/null || groupadd -r ironic
getent passwd ironic >/dev/null || \
    useradd -r -g ironic -d %{_sharedstatedir}/ironic -s /sbin/nologin \
-c "OpenStack Ironic Daemons" ironic
exit 0

%package api
Summary: The Ironic API
Group: System/Servers

Requires: %{name}-common = %{version}-%{release}

%description api
Ironic API for management and provisioning of physical machines


%files api
%doc LICENSE
%{_bindir}/ironic-api
%{_unitdir}/openstack-ironic-api.service

%post api
%post_service openstack-ironic-api.service

%preun api
%preun_service openstack-ironic-api.service

%package conductor
Summary: The Ironic Conductor
Group: System/Servers

Requires: %{name}-common = %{version}-%{release}

%description conductor
Ironic Conductor for management and provisioning of physical machines

%files conductor
%doc LICENSE
%{_bindir}/ironic-conductor
%{_unitdir}/openstack-ironic-conductor.service

%post conductor
%post_service openstack-ironic-conductor.service

%preun conductor
%preun_service openstack-ironic-conductor.service

%changelog
* Wed Sep 23 2015 Lenar Shakirov <snejok@altlinux.ru> 2015.1.1-alt1
- First build for ALT (based on Fedora 2015.1.1-1.fc23.src)

