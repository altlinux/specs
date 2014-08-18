%define with_doc 0
%define project trove

Name:             openstack-%{project}
Version:          2014.1
Release:          alt1
Summary:          OpenStack DBaaS (%{project})

Group:            System/Servers
License:          ASL 2.0
URL:              https://wiki.openstack.org/wiki/Trove
Source0:          %{name}-%{version}.tar

Source1:          %{project}-dist.conf
Source2:          %{project}.logrotate

Source10:         %{name}-api.service
Source11:         %{name}-taskmanager.service
Source12:         %{name}-conductor.service
Source13:         %{name}-guestagent.service

Patch0:           version.diff
Patch1:           authtoken.diff
Patch2:           db-config.diff

#
# patches_base=2014.1
#

BuildArch:        noarch
BuildRequires:    python-module-sphinx
BuildRequires:    python-module-setuptools
BuildRequires:    python-module-pbr
BuildRequires:    python-module-d2to1
BuildRequires:    python-devel

Requires:         %{name}-api = %{version}-%{release}
Requires:         %{name}-taskmanager = %{version}-%{release}
Requires:         %{name}-conductor = %{version}-%{release}


%description
OpenStack DBaaS (codename %{project}) provisioning service.

%package common
Summary:          Components common to all OpenStack %{project} services
Group:            System/Servers

Requires:         python-module-%{project} = %{version}-%{release}

Requires(post):   systemd-units
Requires(preun):  systemd-units
Requires(postun): systemd-units
Requires(pre):    shadow-utils

%description common
OpenStack DBaaS (codename %{project}) provisioning service.

This package contains scripts, config and dependencies shared
between all the OpenStack %{project} services.


%package api
Summary:          OpenStack %{project} API service
Group:            System/Servers

Requires:         %{name}-common = %{version}-%{release}

%description api
OpenStack DBaaS (codename %{project}) provisioning service.

This package contains the %{project} interface daemon.


%package taskmanager
Summary:          OpenStack %{project} taskmanager service
Group:            System/Servers

Requires:         %{name}-common = %{version}-%{release}

%description taskmanager
OpenStack DBaaS (codename %{project}) provisioning service.

This package contains the %{project} taskmanager service.


%package conductor
Summary:          OpenStack %{project} conductor service
Group:            System/Servers

Requires:         %{name}-common = %{version}-%{release}

%description conductor
OpenStack DBaaS (codename %{project}) provisioning service.

This package contains the %{project} conductor service.


%package guestagent
Summary:          OpenStack %{project} guest agent
Group:            System/Servers
%if 0%{?rhel}
Requires:         pexpect
%else
Requires:         python-module-pexpect
%endif

Requires:         %{name}-common = %{version}-%{release}

%description guestagent
OpenStack DBaaS (codename %{project}) provisioning service.

This package contains the %{project} guest agent service
that runs within the database VM instance.


%package -n       python-module-%{project}
Summary:          %{project} Python libraries
Group:            System/Servers

Requires:         python-module-MySQLdb

Requires:         python-module-qpid
Requires:         python-module-kombu

Requires:         python-module-eventlet
Requires:         python-module-greenlet
Requires:         python-module-iso8601
Requires:         python-module-netaddr
Requires:         python-module-lxml

Requires:         python-module-SQLAlchemy
Requires:         python-module-migrate

Requires:         python-module-PasteDeploy
Requires:         python-module-routes
Requires:         python-module-webob

Requires:         python-module-troveclient
Requires:         python-module-novaclient
Requires:         python-module-cinderclient
Requires:         python-module-heatclient
Requires:         python-module-swiftclient
Requires:         python-module-keystoneclient >= 0.4.1

Requires:         python-module-oslo-config >= 1.2.0
Requires:         python-module-jsonschema
Requires:         python-module-babel
Requires:         python-module-jinja2

Requires:         python-module-httplib2
Requires:         python-module-passlib


%description -n   python-module-%{project}
OpenStack DBaaS (codename %{project}) provisioning service.

This package contains the %{project} python library.

%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack %{project}
Group:            Documentation


%description      doc
OpenStack DBaaS (codename %{project}) provisioning service.

This package contains documentation files for %{project}.
%endif

%prep
%setup

%patch0 -p1
%patch1 -p1
%patch2 -p1

sed -i 's/REDHATVERSION/%{version}/; s/REDHATRELEASE/%{release}/' %{project}/version.py

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

%build
%python_build

# Programmatically update defaults in sample config
# which is installed at /etc/trove/trove.conf

#  First we ensure all values are commented in appropriate format.
#  Since icehouse, there was an uncommented keystone_authtoken section
#  at the end of the file which mimics but also conflicted with our
#  distro editing that had been done for many releases.
sed -i '/^[^#[]/{s/^/#/; s/ //g}; /^#[^ ]/s/ = /=/' etc/%{project}/%{project}.conf.sample

#  TODO: Make this more robust
#  Note it only edits the first occurance, so assumes a section ordering in sample
#  and also doesn't support multi-valued variables like dhcpbridge_flagfile.
while read name eq value; do
  test "$name" && test "$value" || continue
  sed -i "0,/^# *$name=/{s!^# *$name=.*!#$name=$value!}" etc/%{project}/%{project}.conf.sample
done < %{SOURCE1}

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
mkdir -p %{buildroot}%{_mandir}/man1
install -p -D -m 644 build/man/*.1 %{buildroot}%{_mandir}/man1/

popd
%endif

# Setup directories
install -d -m 755 %{buildroot}%{_unitdir}
install -d -m 755 %{buildroot}%{_datadir}/%{project}
install -d -m 755 %{buildroot}%{_sharedstatedir}/%{project}
install -d -m 755 %{buildroot}%{_logdir}/%{project}

# Install config files
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/%{project}/%{project}-dist.conf
install -p -D -m 644 etc/%{project}/api-paste.ini %{buildroot}%{_datadir}/%{project}/%{project}-dist-paste.ini
install -d -m 755 %{buildroot}%{_sysconfdir}/%{project}
install -p -D -m 640 etc/%{project}/%{project}.conf.sample %{buildroot}%{_sysconfdir}/%{project}/%{project}.conf
install -p -D -m 640 etc/%{project}/trove-taskmanager.conf.sample %{buildroot}%{_sysconfdir}/%{project}/trove-taskmanager.conf
install -p -D -m 640 etc/%{project}/trove-conductor.conf.sample %{buildroot}%{_sysconfdir}/%{project}/trove-conductor.conf
install -p -D -m 640 etc/%{project}/trove-guestagent.conf.sample %{buildroot}%{_sysconfdir}/%{project}/trove-guestagent.conf

# Install initscripts
install -p -m 755 %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{buildroot}%{_unitdir}

# Install logrotate
install -p -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Install pid directory
install -d -m 755 %{buildroot}%{_runtimedir}/%{project}

# Remove unneeded in production stuff
rm -fr %{buildroot}%{_bindir}/trove-fake-mode
rm -fr %{buildroot}%{python_sitelibdir}/%{project}/tests/
rm -fr %{buildroot}%{python_sitelibdir}/run_tests.*

%pre common
# Origin: http://fedoraproject.org/wiki/Packaging:UsersAndGroups#Dynamic_allocation
USERNAME=%{project}
GROUPNAME=$USERNAME
HOMEDIR=%{_sharedstatedir}/$USERNAME
getent group $GROUPNAME >/dev/null || groupadd -r $GROUPNAME
getent passwd $USERNAME >/dev/null || \
  useradd -r -g $GROUPNAME -G $GROUPNAME -d $HOMEDIR -s /sbin/nologin \
    -c "$USERNAME Daemons" $USERNAME
exit 0

%post api
%post_service %{name}-api
%post taskmanager
%post_service %{name}-taskmanager
%post conductor
%post_service %{name}-conductor
%post guestagent
%post_service %{name}-guestagent

%preun api
%preun_service %{name}-api

%preun taskmanager
%preun_service %{name}-taskmanager

%preun conductor
%preun_service %{name}-conductor

%preun guestagent
%preun_service %{name}-guestagent

%files
%doc LICENSE

%files common
%doc LICENSE
%dir %{_sysconfdir}/%{project}
%config(noreplace) %attr(0640, root, %{project}) %{_sysconfdir}/%{project}/%{project}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}

%dir %attr(0755, %{project}, root) %{_logdir}/%{project}
%dir %attr(0755, %{project}, root) %{_runtimedir}/%{project}

%{_bindir}/%{project}-manage
%{_bindir}/trove-mgmt-taskmanager

%{_datadir}/%{project}

%defattr(-, %{project}, %{project}, -)
%dir %{_sharedstatedir}/%{project}

%files api
%{_bindir}/%{project}-api
%{_unitdir}/%{name}-api.service

%files taskmanager
%{_bindir}/%{project}-taskmanager
%{_unitdir}/%{name}-taskmanager.service
%config(noreplace) %attr(0640, root, %{project}) %{_sysconfdir}/%{project}/%{project}-taskmanager.conf

%files conductor
%{_bindir}/%{project}-conductor
%{_unitdir}/%{name}-conductor.service
%config(noreplace) %attr(0640, root, %{project}) %{_sysconfdir}/%{project}/%{project}-conductor.conf

%files guestagent
%{_bindir}/%{project}-guestagent
%{_unitdir}/%{name}-guestagent.service
%config(noreplace) %attr(0640, root, %{project}) %{_sysconfdir}/%{project}/%{project}-guestagent.conf

%files -n python-module-%{project}
%doc LICENSE
%{python_sitelibdir}/%{project}
%{python_sitelibdir}/%{project}-%{version}*.egg-info

%if 0%{?with_doc}
%files doc
%doc LICENSE doc/build/html
%endif

%changelog
* Sat Aug 16 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1-alt1
- First build for ALT (based on Fedora 2014.1-1.fc20.src)

