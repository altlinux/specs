Name:             openstack-cinder
Version:          2014.1.1
Release:          alt1
Summary:          OpenStack Volume service

Group:            System/Servers
License:          ASL 2.0
URL:              http://www.openstack.org/software/openstack-storage/
Source0:          %{name}-%{version}.tar
Source1:          cinder-dist.conf
Source2:          cinder.logrotate
Source3:          cinder-tgt.conf

Source10:         openstack-cinder-api.service
Source11:         openstack-cinder-scheduler.service
Source12:         openstack-cinder-volume.service
Source13:         openstack-cinder-backup.service

Source20:         cinder-sudoers

#
# patches_base=2014.1.1
#
Patch0001: 0001-Ensure-we-don-t-access-the-net-when-building-docs.patch
Patch0002: 0002-Remove-runtime-dep-on-python-pbr-python-d2to1.patch
Patch0003: 0003-Revert-Switch-over-to-oslosphinx.patch
Patch0005: 0005-notify-calling-process-we-are-ready-to-serve.patch
Patch0006: 0006-Move-notification-point-to-a-better-place.patch

BuildArch:        noarch
BuildRequires:    python-module-d2to1
BuildRequires:    python-module-oslo-sphinx
BuildRequires:    python-module-pbr
BuildRequires:    python-module-sphinx
BuildRequires:    python-module-setuptools
BuildRequires:    python-module-netaddr
BuildRequires:    crudini

Requires:         openstack-utils
Requires:         python-module-cinder = %{version}-%{release}

# as convenience
Requires:         python-module-cinderclient

Requires(pre):    shadow-utils

Requires:         lvm2
Requires:         targetcli
Requires:         python-module-rtslib
Requires:         sysfsutils

%description
OpenStack Volume (codename Cinder) provides services to manage and
access block storage volumes for use by Virtual Machine instances.


%package -n       python-module-cinder
Summary:          OpenStack Volume Python libraries
Group:            System/Servers

Requires:         sudo

Requires:         python-module-MySQLdb

Requires:         qemu-img
Requires:         sysfsutils

Requires:         python-module-paramiko

Requires:         python-module-qpid
Requires:         python-module-kombu
Requires:         python-module-amqplib

Requires:         python-module-eventlet
Requires:         python-module-greenlet
Requires:         python-module-iso8601
Requires:         python-module-netaddr
Requires:         python-module-lxml
Requires:         python-module-anyjson
Requires:         python-module-cheetah
Requires:         python-module-stevedore
Requires:         python-module-suds

Requires:         python-module-SQLAlchemy
Requires:         python-module-migrate

Requires:         python-module-PasteDeploy
Requires:         python-module-routes
Requires:         python-module-webob

Requires:         python-module-glanceclient
Requires:         python-module-swiftclient >= 1.2
Requires:         python-module-keystoneclient
Requires:         python-module-novaclient >= 2.15

Requires:         python-module-oslo-config >= 1.2.0
Requires:         python-module-six >= 1.5.0

Requires:         python-module-babel
Requires:         python-module-lockfile

Requires:         python-module-oslo-rootwrap
Requires:         python-module-taskflow
Requires:         python-module-oslo-messaging >= 1.3.0-0.1.a9

%description -n   python-module-cinder
OpenStack Volume (codename Cinder) provides services to manage and
access block storage volumes for use by Virtual Machine instances.

This package contains the cinder Python library.

%package doc
Summary:          Documentation for OpenStack Volume
Group:            Documentation

Requires:         %{name} = %{version}-%{release}

BuildRequires:    systemd-units
BuildRequires:    graphviz

# Required to build module documents
BuildRequires:    python-module-eventlet
BuildRequires:    python-module-routes
BuildRequires:    python-module-SQLAlchemy
BuildRequires:    python-module-webob
# while not strictly required, quiets the build down when building docs.
BuildRequires:    python-module-migrate, python-module-iso8601

%description      doc
OpenStack Volume (codename Cinder) provides services to manage and
access block storage volumes for use by Virtual Machine instances.

This package contains documentation files for cinder.

%prep
%setup

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0005 -p1
%patch0006 -p1

find . \( -name .gitignore -o -name .placeholder \) -delete

find cinder -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

# TODO: Have the following handle multi line entries
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

# We add REDHATCINDERVERSION/RELEASE with the pbr removal patch
sed -i s/REDHATCINDERVERSION/%{version}/ cinder/version.py
sed -i s/REDHATCINDERRELEASE/%{release}/ cinder/version.py

#FIXME:
#Hack for ALT Autoreq mechanism:
# - python2.7(hp3parclient) in cinder/volume/drivers/san/hp/ and cinder/tests/test_hp3par.py
rm -rfv cinder/volume/drivers/san/hp/ \
cinder/tests/test_hp3par.py

%build

# Move authtoken configuration out of paste.ini
crudini --del etc/cinder/api-paste.ini filter:authtoken admin_tenant_name
crudini --del etc/cinder/api-paste.ini filter:authtoken admin_user
crudini --del etc/cinder/api-paste.ini filter:authtoken admin_password
crudini --del etc/cinder/api-paste.ini filter:authtoken auth_host
crudini --del etc/cinder/api-paste.ini filter:authtoken auth_port
crudini --del etc/cinder/api-paste.ini filter:authtoken auth_protocol

%python_build

%install
%python_install

# docs generation requires everything to be installed first
export PYTHONPATH="$( pwd ):$PYTHONPATH"

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

# Setup directories
install -d -m 755 %{buildroot}%{_sharedstatedir}/cinder
install -d -m 755 %{buildroot}%{_sharedstatedir}/cinder/tmp
install -d -m 755 %{buildroot}%{_logdir}/cinder

# Install config files
install -d -m 755 %{buildroot}%{_sysconfdir}/cinder
install -p -D -m 640 %{SOURCE1} %{buildroot}%{_datadir}/cinder/cinder-dist.conf
install -p -D -m 640 etc/cinder/cinder.conf.sample %{buildroot}%{_sysconfdir}/cinder/cinder.conf
install -d -m 755 %{buildroot}%{_sysconfdir}/cinder/volumes
install -p -D -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/tgt/conf.d/cinder.conf
install -p -D -m 640 etc/cinder/rootwrap.conf %{buildroot}%{_sysconfdir}/cinder/rootwrap.conf
install -p -D -m 640 etc/cinder/api-paste.ini %{buildroot}%{_sysconfdir}/cinder/api-paste.ini
install -p -D -m 640 etc/cinder/policy.json %{buildroot}%{_sysconfdir}/cinder/policy.json

# Install initscripts for services
install -p -D -m 644 %{SOURCE10} %{buildroot}%{_unitdir}/openstack-cinder-api.service
install -p -D -m 644 %{SOURCE11} %{buildroot}%{_unitdir}/openstack-cinder-scheduler.service
install -p -D -m 644 %{SOURCE12} %{buildroot}%{_unitdir}/openstack-cinder-volume.service
install -p -D -m 644 %{SOURCE13} %{buildroot}%{_unitdir}/openstack-cinder-backup.service

# Install sudoers
install -p -D -m 400 %{SOURCE20} %{buildroot}%{_sysconfdir}/sudoers.d/cinder

# Install logrotate
install -p -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/openstack-cinder

# Install pid directory
install -d -m 755 %{buildroot}%{_runtimedir}/cinder

# Install rootwrap files in /usr/share/cinder/rootwrap
mkdir -p %{buildroot}%{_datadir}/cinder/rootwrap/
install -p -D -m 644 etc/cinder/rootwrap.d/* %{buildroot}%{_datadir}/cinder/rootwrap/

# Remove unneeded in production stuff
rm -f %{buildroot}%{_bindir}/cinder-debug
rm -fr %{buildroot}%{python_sitelibdir}/cinder/tests/
rm -fr %{buildroot}%{python_sitelibdir}/run_tests.*
rm -f %{buildroot}/usr/share/doc/cinder/README*

%pre
getent group cinder >/dev/null || groupadd -r cinder --gid 165
if ! getent passwd cinder >/dev/null; then
  useradd -u 165 -r -g cinder -G cinder,nobody,wheel -d %{_sharedstatedir}/cinder -s /sbin/nologin -c "OpenStack Cinder Daemons" cinder
fi
exit 0

%post
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ] ; then
    for svc in volume api scheduler backup; do
        /bin/systemctl --no-reload disable openstack-cinder-${svc}.service > /dev/null 2>&1 || :
        /bin/systemctl stop openstack-cinder-${svc}.service > /dev/null 2>&1 || :
    done
fi

%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in volume api scheduler backup; do
        /bin/systemctl try-restart openstack-cinder-${svc}.service >/dev/null 2>&1 || :
    done
fi

%files
%doc LICENSE

%dir %{_sysconfdir}/cinder
%config(noreplace) %attr(-, root, cinder) %{_sysconfdir}/cinder/cinder.conf
%config(noreplace) %attr(-, root, cinder) %{_sysconfdir}/cinder/api-paste.ini
%config(noreplace) %attr(-, root, cinder) %{_sysconfdir}/cinder/rootwrap.conf
%config(noreplace) %attr(-, root, cinder) %{_sysconfdir}/cinder/policy.json
%config(noreplace) %{_sysconfdir}/logrotate.d/openstack-cinder
%config(noreplace) %{_sysconfdir}/sudoers.d/cinder
%config(noreplace) %{_sysconfdir}/tgt/conf.d/cinder.conf
%attr(-, root, cinder) %{_datadir}/cinder/cinder-dist.conf

%dir %attr(0750, cinder, root) %{_logdir}/cinder
%dir %attr(0755, cinder, root) %{_runtimedir}/cinder
%dir %attr(0755, cinder, root) %{_sysconfdir}/cinder/volumes

%{_bindir}/cinder-*
%{_unitdir}/*.service
%{_datadir}/cinder
%{_mandir}/man1/cinder*.1.gz

%defattr(-, cinder, cinder, -)
%dir %{_sharedstatedir}/cinder
%dir %{_sharedstatedir}/cinder/tmp

%files -n python-module-cinder
%doc LICENSE
%{python_sitelibdir}/cinder
%{python_sitelibdir}/cinder-%{version}*.egg-info

%files doc
%doc doc/build/html

%changelog
* Tue Aug 12 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt1
- 2014.1.1

* Sat Aug 09 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1-alt3
- sysfsutils added to Requires: warning about systool

* Tue Aug 05 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1-alt2
- user cinder added to wheel group, for cinder-rootwrap

* Fri Jul 11 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1-alt1
- Initial build for Sisyphus (based on Fedora)
- New version - icehouse

