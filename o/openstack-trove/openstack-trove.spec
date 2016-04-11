%define with_doc 0
%define project trove

Name: openstack-%project
Version: 5.0.0
Release: alt1
Epoch: 1
Summary: OpenStack DBaaS (%project)

Group: System/Servers
License: ASL 2.0
Url: https://wiki.openstack.org/wiki/Trove
Source: %name-%version.tar

Source2: %project.logrotate

Source10: %name-api.service
Source11: %name-taskmanager.service
Source12: %name-conductor.service
Source13: %name-guestagent.service


BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-SQLAlchemy >= 1.0.10
BuildRequires: python-module-eventlet >= 0.18.2
BuildRequires: python-module-keystonemiddleware >= 4.0.0
BuildRequires: python-module-routes >= 1.12.3
BuildRequires: python-module-webob >= 1.2.3
BuildRequires: python-module-PasteDeploy >= 1.5.0
BuildRequires: python-module-migrate >= 0.9.6
BuildRequires: python-module-netaddr >= 0.7.12
BuildRequires: python-module-netifaces >= 0.10.4
BuildRequires: python-module-httplib2 >= 0.7.5
BuildRequires: python-module-lxml >= 2.3
BuildRequires: python-module-passlib >= 1.6
BuildRequires: python-module-heatclient >= 0.6.0
BuildRequires: python-module-novaclient >= 2.29.0
BuildRequires: python-module-cinderclient >= 1.3.1
BuildRequires: python-module-keystoneclient >= 1.6.0
BuildRequires: python-module-swiftclient >= 2.2.0
BuildRequires: python-module-designateclient >= 1.5.0
BuildRequires: python-module-neutronclient >= 2.6.0
BuildRequires: python-module-iso8601 >= 0.1.9
BuildRequires: python-module-jsonschema >= 2.0.0
BuildRequires: python-module-jinja2 >= 2.8
BuildRequires: python-module-pexpect >= 3.1
BuildRequires: python-module-oslo.config >= 3.7.0
BuildRequires: python-module-oslo.context >= 0.2.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.middleware >= 3.0.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.service >= 1.0.0
BuildRequires: python-module-oslo.utils >= 3.5.0
BuildRequires: python-module-oslo.concurrency >= 3.5.0
BuildRequires: python-module-pymysql
BuildRequires: python-module-babel >= 1.3
BuildRequires: python-module-stevedore >= 1.5.0
BuildRequires: python-module-oslo.messaging >= 4.0.0
BuildRequires: python-module-osprofiler >= 1.1.0
BuildRequires: python-module-oslo.log >= 1.14.0
BuildRequires: python-module-oslo.db >= 4.1.0
BuildRequires: python-module-enum34

Requires: %name-api = %EVR
Requires: %name-taskmanager = %EVR
Requires: %name-conductor = %EVR

%description
OpenStack DBaaS (codename %project) provisioning service.

%package common
Summary: Components common to all OpenStack %project services
Group: System/Servers

Requires: python-module-%project = %EVR
Requires(pre):    shadow-utils

%description common
OpenStack DBaaS (codename %project) provisioning service.

This package contains scripts, config and dependencies shared
between all the OpenStack %project services.

%package api
Summary: OpenStack %project API service
Group: System/Servers

Requires: %name-common = %EVR

%description api
OpenStack DBaaS (codename %project) provisioning service.

This package contains the %project interface daemon.

%package taskmanager
Summary: OpenStack %project taskmanager service
Group: System/Servers

Requires: %name-common = %EVR

%description taskmanager
OpenStack DBaaS (codename %project) provisioning service.

This package contains the %project taskmanager service.

%package conductor
Summary: OpenStack %project conductor service
Group: System/Servers

Requires: %name-common = %EVR

%description conductor
OpenStack DBaaS (codename %project) provisioning service.

This package contains the %project conductor service.

%package guestagent
Summary: OpenStack %project guest agent
Group: System/Servers
Requires: python-module-pexpect
Requires: %name-common = %EVR

%description guestagent
OpenStack DBaaS (codename %project) provisioning service.

This package contains the %project guest agent service
that runs within the database VM instance.

%package -n       python-module-%project
Summary: %project Python libraries
Group: System/Servers

Requires: python-module-SQLAlchemy
Requires: python-module-migrate
Requires: python-module-PasteDeploy

Requires: python-module-troveclient
Requires: python-module-novaclient
Requires: python-module-cinderclient
Requires: python-module-heatclient
Requires: python-module-swiftclient
Requires: python-module-keystoneclient >= 0.4.1

Requires: python-module-oslo-config >= 1.2.0
Requires: python-module-jsonschema

%description -n   python-module-%project
OpenStack DBaaS (codename %project) provisioning service.

This package contains the %project python library.

%if 0%{?with_doc}
%package doc
Summary: Documentation for OpenStack %project
Group: Documentation

%description doc
OpenStack DBaaS (codename %project) provisioning service.

This package contains documentation files for %project.
%endif

%prep
%setup

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

%build
%python_build


%install
%python_install

# docs generation requires everything to be installed first
export PYTHONPATH="$( pwd ):$PYTHONPATH"

%if 0%{?with_doc}
pushd doc

SPHINX_DEBUG=1 sphinx-build -b html source build/html
# Fix hidden-file-or-dir warnings
rm -fr build/html/.doctrees build/html/.buildinfo

# Create dir link to avoid a sphinx-build exception
mkdir -p build/man/.doctrees/
ln -s .  build/man/.doctrees/man
SPHINX_DEBUG=1 sphinx-build -b man -c source source/man build/man
mkdir -p %buildroot%_mandir/man1
install -p -D -m 644 build/man/*.1 %buildroot%_mandir/man1/

popd
%endif

# Setup directories
install -d -m 755 %buildroot%_unitdir
install -d -m 755 %buildroot%_datadir/%project
install -d -m 755 %buildroot%_sharedstatedir/%project
install -d -m 755 %buildroot%_logdir/%project

# Install config files
install -d -m 755 %buildroot%_sysconfdir/%project
install -p -D -m 644 etc/%project/api-paste.ini %buildroot%_sysconfdir/%project/api-paste.ini
install -p -D -m 640 etc/%project/%project.conf.sample %buildroot%_sysconfdir/%project/%project.conf
install -p -D -m 640 etc/%project/trove-taskmanager.conf.sample %buildroot%_sysconfdir/%project/trove-taskmanager.conf
install -p -D -m 640 etc/%project/trove-conductor.conf.sample %buildroot%_sysconfdir/%project/trove-conductor.conf
install -p -D -m 640 etc/%project/trove-guestagent.conf.sample %buildroot%_sysconfdir/%project/trove-guestagent.conf

# Install initscripts
install -p -m 755 %SOURCE10 %SOURCE11 %SOURCE12 %SOURCE13 %buildroot%_unitdir

# Install logrotate
install -p -D -m 644 %SOURCE2 %buildroot%_sysconfdir/logrotate.d/%name

# Install pid directory
install -d -m 755 %buildroot%_runtimedir/%project

# Remove unneeded in production stuff
rm -fr %buildroot%_bindir/trove-fake-mode
rm -fr %buildroot%python_sitelibdir/%project/tests/
rm -fr %buildroot%python_sitelibdir/run_tests.*

%pre common
%_sbindir/groupadd -r -f trove 2>/dev/null ||:
%_sbindir/useradd -r -g trove -c 'OpenStack Trove Daemons' \
        -s /sbin/nologin  -d %_sharedstatedir/%project trove 2>/dev/null ||:


%post api
%post_service %name-api

%post taskmanager
%post_service %name-taskmanager

%post conductor
%post_service %name-conductor

%post guestagent
%post_service %name-guestagent

%preun api
%preun_service %name-api

%preun taskmanager
%preun_service %name-taskmanager

%preun conductor
%preun_service %name-conductor

%preun guestagent
%preun_service %name-guestagent

%files
%doc LICENSE

%files common
%doc LICENSE
%dir %_sysconfdir/%project
%config(noreplace) %attr(0640, root, %project) %_sysconfdir/%project/%project.conf
%config(noreplace) %attr(0640, root, %project) %_sysconfdir/%project/api-paste.ini
%config(noreplace) %_sysconfdir/logrotate.d/%name

%dir %attr(0755, %project, root) %_logdir/%project
%dir %attr(0755, %project, root) %_runtimedir/%project

%_bindir/%project-manage
%_bindir/trove-mgmt-taskmanager

%_datadir/%project

%defattr(-, %project, %project, -)
%dir %_sharedstatedir/%project

%files api
%_bindir/%project-api
%_unitdir/%name-api.service

%files taskmanager
%_bindir/%project-taskmanager
%_unitdir/%name-taskmanager.service
%config(noreplace) %attr(0640, root, %project) %_sysconfdir/%project/%project-taskmanager.conf

%files conductor
%_bindir/%project-conductor
%_unitdir/%name-conductor.service
%config(noreplace) %attr(0640, root, %project) %_sysconfdir/%project/%project-conductor.conf

%files guestagent
%_bindir/%project-guestagent
%_unitdir/%name-guestagent.service
%config(noreplace) %attr(0640, root, %project) %_sysconfdir/%project/%project-guestagent.conf

%files -n python-module-%project
%doc LICENSE
%python_sitelibdir/*

%if 0%{?with_doc}
%files doc
%doc LICENSE doc/build/html
%endif

%changelog
* Tue Apr 19 2016 Alexey Shabalin <shaba@altlinux.ru> 1:5.0.0-alt1
- 5.0.0

* Tue Nov 03 2015 Alexey Shabalin <shaba@altlinux.ru> 1:4.0.0-alt1
- 4.0.0 Liberty release

* Sat Aug 16 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1-alt1
- First build for ALT (based on Fedora 2014.1-1.fc20.src)

