Name:           openstack-ironic
Epoch: 1
Version:        13.0.1
Release:        alt1.1

Summary:        OpenStack Baremetal Hypervisor API (ironic)

License:        ASL 2.0
Group:          System/Servers
URL:            http://www.openstack.org

Source0:        %name-%version.tar

Source1:        openstack-ironic-api.service
Source2:        openstack-ironic-conductor.service
Source3:        ironic-rootwrap-sudoers

Patch0001: 0001-Set-default-DB-location.patch

BuildArch:      noarch
BuildRequires: python3-module-setuptools
BuildRequires: python3-devel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: openssl-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: gmp-devel
BuildRequires: python3-module-sphinx


%prep
%setup

rm requirements.txt test-requirements.txt

%build
%python3_build

%install
%python3_install


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
#install -p -D -m 640 etc/ironic/ironic.conf.sample %{buildroot}/%{_sysconfdir}/ironic/ironic.conf
#install -p -D -m 640 etc/ironic/policy.json %{buildroot}/%{_sysconfdir}/ironic/policy.json
install -p -D -m 640 etc/ironic/rootwrap.conf %{buildroot}/%{_sysconfdir}/ironic/rootwrap.conf
install -p -D -m 640 etc/ironic/rootwrap.d/* %{buildroot}/%{_sysconfdir}/ironic/rootwrap.d/


%description
Ironic provides an API for management and provisioning of physical machines

%package common
Summary: Ironic common
Group: System/Servers

Requires:       ipmitool
Requires:       python3-module-eventlet >= 0.18.2
Requires:       python3-module-greenlet
Requires:       python3-module-iso8601
Requires:       python3-module-jsonpatch >= 1.16
Requires:       python3-module-keystonemiddleware >= 4.17.0
Requires:       python3-module-lxml
Requires:       python3-module-migrate
Requires:       python3-module-mock
Requires:       python3-module-netaddr
Requires:       python3-module-oslo.concurrency >= 3.26.0
Requires:       python3-module-oslo.config >= 5.2.0
Requires:       python3-module-oslo.context >= 2.19.2
Requires:       python3-module-oslo.db >= 4.27.0
Requires:       python3-module-oslo.i18n >= 3.15.3
Requires:       python3-module-oslo.policy >= 1.30.0
Requires:       python3-module-oslo.rootwrap >= 5.8.0
Requires:       python3-module-oslo.serialization >= 2.18.0
Requires:       python3-module-oslo.utils >= 3.33.0
Requires:       python3-module-paramiko
Requires:       python3-module-pbr >= 2.0.0
Requires:       python3-module-pecan >= 1.0.0
Requires:       python3-module-retrying >= 1.2.3
Requires:       python3-module-requests >= 2.14.2
Requires:       python3-module-six >= 1.10.0
Requires:       python3-module-stevedore >= 1.20.0
Requires:       python3-module-webob
Requires:       python3-module-websockify
Requires:       python3-module-wsme
Requires:       python3-module-Crypto
Requires:       python3-module-SQLAlchemy
Requires:       python3-module-neutronclient
Requires:       python3-module-glanceclient
Requires:       python3-module-keystoneclient
Requires:       python3-module-swiftclient
Requires:       python3-module-jinja2
Requires:       python3-module-pyghmi
Requires:       python3-module-alembic >= 0.8.10
Requires:       python3-module-pysendfile >= 2.0.0

Requires(pre):  shadow-utils

%description common
Components common to all OpenStack Ironic services


%files common
%doc README.rst LICENSE
%{_bindir}/ironic-dbsync
%{_bindir}/ironic-rootwrap
%_bindir/ironic-status

%python3_sitelibdir/ironic*
%{_sysconfdir}/sudoers.d/ironic
%config(noreplace) %attr(-,root,ironic) %{_sysconfdir}/ironic
# TODO: fix packaging these files
%config(noreplace) %attr(-,root,ironic) %{_sysconfdir}/ironic/rootwrap.conf
%config(noreplace) %attr(-,root,ironic) %{_sysconfdir}/ironic/rootwrap.d/ironic-images.filters
%config(noreplace) %attr(-,root,ironic) %{_sysconfdir}/ironic/rootwrap.d/ironic-lib.filters
%config(noreplace) %attr(-,root,ironic) %{_sysconfdir}/ironic/rootwrap.d/ironic-utils.filters
# TODO-end
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

Requires: %{name}-common = %{?epoch:%epoch:}%{version}-%{release}

%description api
Ironic API for management and provisioning of physical machines


%files api
%doc LICENSE
%{_bindir}/ironic-api
%_bindir/ironic-api-wsgi
%{_unitdir}/openstack-ironic-api.service

%post api
%post_service openstack-ironic-api.service

%preun api
%preun_service openstack-ironic-api.service

%package conductor
Summary: The Ironic Conductor
Group: System/Servers

Requires: %{name}-common = %{?epoch:%epoch:}%{version}-%{release}

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
* Fri Oct 25 2019 Grigory Ustinov <grenka@altlinux.org> 1:13.0.1-alt1.1
- Update to 13.0.1.
- Transfer on python3.

* Wed Sep 23 2015 Lenar Shakirov <snejok@altlinux.ru> 2015.1.1-alt1
- First build for ALT (based on Fedora 2015.1.1-1.fc23.src)
