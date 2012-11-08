#
# This is 2012.2 folsom-3 milestone
#
Name:		openstack-glance
Version:	2012.2.0.4
Release:	alt1
Summary:	OpenStack Image Service

Group:		System/Servers
License:	ASL 2.0
URL:		http://glance.openstack.org
Source0:	%{name}-%{version}.tar.gz
Source1:	openstack-glance-api.service
Source2:	openstack-glance-registry.service
Source3:	openstack-glance.logrotate

#
# patches_base=folsom-3
#
Patch0001:	openstack-glance-don-t-access-the-net-while-building-docs.patch
Patch0002:	openstack-glance-fix-no-handlers-can-be-found-for-logger.patch
Patch0003:	openstack-glance-do-not-auto-create-DB.patch

BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	python-module-distribute
BuildRequires:	intltool

Requires(post):		systemd-units
Requires(preun):	systemd-units
Requires(postun):	systemd-units
Requires(pre):	shadow-utils
Requires:	python-module-glance = %{version}-%{release}
Requires:	python-module-glanceclient
Requires:	python-module-greenlet >= 0.3.1

%description
OpenStack Image Service (code-named Glance) provides discovery,
registration, and delivery services for virtual disk images. The Image
Service API server provides a standard REST interface for querying
information about virtual disk images stored in a variety of back-end
stores, including OpenStack Object Storage. Clients can register new
virtual disk images with the Image Service, query for information on
publicly available disk images, and use the Image Service's client
library for streaming virtual disk images.

This package contains the API and registry servers.

%package -n python-module-glance
Summary:	Glance Python libraries
Group:		Development/Python

Requires:	python-module-MySQLdb
Requires:	python-module-pysendfile
Requires:	python-module-eventlet
Requires:	python-module-httplib2
Requires:	python-module-iso8601
Requires:	python-module-jsonschema
Requires:	python-module-migrate
Requires:	python-module-PasteDeploy
Requires:	python-module-routes
Requires:	python-module-SQLAlchemy >= 0.7.8
Requires:	python-module-webob
Requires:	python-module-Crypto
Requires:	python-module-pyxattr
Requires:	python-module-swiftclient
Requires:	python-module-qpid

#test deps: python-mox python-nose python-requests
#test and optional store:
#ceph - glance.store.rdb
#python-boto - glance.store.s3

%description -n python-module-glance
OpenStack Image Service (code-named Glance) provides discovery,
registration, and delivery services for virtual disk images.

This package contains the glance Python library.

%package doc
Summary:	Documentation for OpenStack Image Service
Group:		Documentation

Requires:	%{name} = %{version}-%{release}

BuildRequires:	systemd-units
BuildRequires:	python-module-sphinx
BuildRequires:	graphviz

# Required to build module documents
BuildRequires:	python-module-boto
BuildRequires:	python-module-eventlet
BuildRequires:	python-module-routes
BuildRequires:	python-module-SQLAlchemy
BuildRequires:	python-module-webob

%description doc
OpenStack Image Service (code-named Glance) provides discovery,
registration, and delivery services for virtual disk images.

This package contains documentation files for glance.

%prep
%setup -q

%patch0001 -p1
%patch0002 -p2
%patch0003 -p2

# Remove bundled egg-info
rm -rf glance.egg-info
sed -i '/\/usr\/bin\/env python/d' glance/common/config.py glance/common/crypt.py glance/db/sqlalchemy/migrate_repo/manage.py
# versioninfo is missing in f3 tarball
echo %{version} > glance/versioninfo

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Delete tests
rm -fr %{buildroot}%{python_sitelibdir}/tests

# Drop old glance CLI it has been deprecated
# and replaced glanceclient
rm -f %{buildroot}%{_bindir}/glance

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html source build/html
sphinx-build -b man source build/man

mkdir -p %{buildroot}%{_mandir}/man1
install -p -D -m 644 build/man/*.1 %{buildroot}%{_mandir}/man1/
popd

# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo
rm -f %{buildroot}%{_sysconfdir}/glance*.conf
rm -f %{buildroot}%{_sysconfdir}/glance*.ini
rm -f %{buildroot}%{_sysconfdir}/logging.cnf.sample
rm -f %{buildroot}%{_sysconfdir}/policy.json
rm -f %{buildroot}%{_sysconfdir}/schema-image.json
rm -f %{buildroot}/usr/share/doc/glance/README.rst

# Setup directories
install -d -m 755 %{buildroot}%{_sharedstatedir}/glance/images

# Config file
install -p -D -m 640 etc/glance-api.conf %{buildroot}%{_sysconfdir}/glance/glance-api.conf
install -p -D -m 640 etc/glance-api-paste.ini %{buildroot}%{_sysconfdir}/glance/glance-api-paste.ini
install -p -D -m 640 etc/glance-registry.conf %{buildroot}%{_sysconfdir}/glance/glance-registry.conf
install -p -D -m 640 etc/glance-registry-paste.ini %{buildroot}%{_sysconfdir}/glance/glance-registry-paste.ini
install -p -D -m 640 etc/glance-cache.conf %{buildroot}%{_sysconfdir}/glance/glance-cache.conf
install -p -D -m 640 etc/glance-scrubber.conf %{buildroot}%{_sysconfdir}/glance/glance-scrubber.conf
install -p -D -m 640 etc/policy.json %{buildroot}%{_sysconfdir}/glance/policy.json
install -p -D -m 640 etc/schema-image.json %{buildroot}%{_sysconfdir}/glance/schema-image.json

# Initscripts
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/openstack-glance-api.service
install -p -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/openstack-glance-registry.service

# Logrotate config
install -p -D -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/openstack-glance

# Install pid directory
install -d -m 755 %{buildroot}%{_runtimedir}/glance

# Install log directory
install -d -m 755 %{buildroot}%{_logdir}/glance

%pre
getent group glance >/dev/null || groupadd -r glance -g 161
getent passwd glance >/dev/null || \
useradd -u 161 -r -g glance -d %{_sharedstatedir}/glance -s /sbin/nologin \
-c "OpenStack Glance Daemons" glance
exit 0

%post
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi


%preun
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable openstack-glance-api.service > /dev/null 2>&1 || :
    /bin/systemctl --no-reload disable openstack-glance-registry.service > /dev/null 2>&1 || :
    /bin/systemctl stop openstack-glance-api.service > /dev/null 2>&1 || :
    /bin/systemctl stop openstack-glance-registry.service > /dev/null 2>&1 || :
fi

%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart openstack-glance-api.service >/dev/null 2>&1 || :
    /bin/systemctl try-restart openstack-glance-registry.service >/dev/null 2>&1 || :
fi

%files
%doc README.rst
%{_bindir}/glance-api
%{_bindir}/glance-control
%{_bindir}/glance-manage
%{_bindir}/glance-registry
%{_bindir}/glance-cache-cleaner
%{_bindir}/glance-cache-manage
%{_bindir}/glance-cache-prefetcher
%{_bindir}/glance-cache-pruner
%{_bindir}/glance-scrubber
%{_bindir}/glance-replicator

%{_unitdir}/openstack-glance-api.service
%{_unitdir}/openstack-glance-registry.service
%{_mandir}/man1/glance*.1.gz
%dir %{_sysconfdir}/glance
%config(noreplace) %attr(-, root, glance) %{_sysconfdir}/glance/glance-api.conf
%config(noreplace) %attr(-, root, glance) %{_sysconfdir}/glance/glance-api-paste.ini
%config(noreplace) %attr(-, root, glance) %{_sysconfdir}/glance/glance-registry.conf
%config(noreplace) %attr(-, root, glance) %{_sysconfdir}/glance/glance-registry-paste.ini
%config(noreplace) %attr(-, root, glance) %{_sysconfdir}/glance/glance-cache.conf
%config(noreplace) %attr(-, root, glance) %{_sysconfdir}/glance/glance-scrubber.conf
%config(noreplace) %attr(-, root, glance) %{_sysconfdir}/glance/policy.json
%config(noreplace) %attr(-, root, glance) %{_sysconfdir}/glance/schema-image.json
%config(noreplace) %attr(-, root, glance) %{_sysconfdir}/logrotate.d/openstack-glance
%dir %attr(0755, glance, nobody) %{_sharedstatedir}/glance
%dir %attr(0755, glance, nobody) %{_logdir}/glance
%dir %attr(0755, glance, nobody) %{_runtimedir}/glance

%files -n python-module-glance
%doc README.rst
%{python_sitelibdir}/glance
%{python_sitelibdir}/glance-%{version}-*.egg-info


%files doc
%doc doc/build/html

%changelog
* Thu Nov 08 2012 Pavel Shilovsky <piastry@altlinux.org> 2012.2.0.4-alt1
- Initial relase for Sisyphus (based on Fedora)
