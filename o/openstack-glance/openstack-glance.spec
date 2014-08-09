Name:		openstack-glance
Version:	2014.1
Release:	alt1
Summary:	OpenStack Image Service

Group:		System/Servers
License:	ASL 2.0
URL:		http://glance.openstack.org
Source0:	%name-%version.tar
Source1:	%name-api.service
Source2:	%name-registry.service
Source3:	%name-scrubber.service
Source4:	%name.logrotate

Source5:          glance-api-dist.conf
Source6:          glance-registry-dist.conf
Source7:          glance-cache-dist.conf
Source8:          glance-scrubber-dist.conf

Source40:	%name-api.init
Source50:	%name-registry.init

#
# patches_base=2014.1
#
Patch0001: 0001-Don-t-access-the-net-while-building-docs.patch
Patch0002: 0002-Remove-runtime-dep-on-python-pbr.patch
Patch0003: 0003-avoid-unsupported-storage-drivers.patch

BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	python-module-distribute
BuildRequires:	python-module-setuptools
BuildRequires:	intltool

Requires(pre):	shadow-utils
Requires:	python-module-glance = %{version}-%{release}
Requires:	python-module-glanceclient
#FIXME
#Requires:	openstack-utils


%description
OpenStack Image Service (code-named Glance) provides discovery, registration,
and delivery services for virtual disk images. The Image Service API server
provides a standard REST interface for querying information about virtual disk
images stored in a variety of back-end stores, including OpenStack Object
Storage. Clients can register new virtual disk images with the Image Service,
query for information on publicly available disk images, and use the Image
Service's client library for streaming virtual disk images.

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
Requires:	python-module-SQLAlchemy
Requires:	python-module-webob
Requires:	python-module-Crypto
Requires:	python-module-pyxattr
Requires:	python-module-swiftclient
Requires:	python-module-cinderclient
Requires:	python-module-keystoneclient
Requires:	python-module-oslo-config >= 1.2.0
Requires:	python-module-oslo-messaging

#test deps: python-mox python-nose python-requests
#test and optional store:
#ceph - glance.store.rdb
#python-boto - glance.store.s3

%description -n python-module-glance
OpenStack Image Service (code-named Glance) provides discovery, registration,
and delivery services for virtual disk images.

This package contains the glance Python library.

%package doc
Summary:	Documentation for OpenStack Image Service
Group:		Documentation

Requires:         %{name} = %{version}-%{release}

BuildRequires:	python-module-sphinx
BuildRequires:	graphviz

# Required to build module documents
BuildRequires:	python-module-boto
BuildRequires:	python-module-eventlet
BuildRequires:	python-module-routes
BuildRequires:	python-module-SQLAlchemy
BuildRequires:	python-module-webob
BuildRequires:	python-module-pbr
BuildRequires:	python-module-oslo-sphinx

%description doc
OpenStack Image Service (code-named Glance) provides discovery, registration,
and delivery services for virtual disk images.

This package contains documentation files for glance.

%prep
%setup

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1

# Remove bundled egg-info
rm -rf glance.egg-info
sed -i '/\/usr\/bin\/env python/d' glance/common/config.py glance/common/crypt.py glance/db/sqlalchemy/migrate_repo/manage.py
# versioninfo is missing in f3 tarball
echo %{version} > glance/versioninfo

sed -i '/setuptools_git/d; /setup_requires/d; /install_requires/d; /dependency_links/d' setup.py
sed -i s/REDHATGLANCEVERSION/%{version}/ glance/version.py
sed -i s/REDHATGLANCERELEASE/%{release}/ glance/version.py

# make doc build compatible with python-oslo-sphinx RPM
sed -i 's/oslosphinx/oslo.sphinx/' doc/source/conf.py

# Remove the requirements file so that pbr hooks don't add it
# to distutils requiers_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

# Programmatically update defaults in example config
api_dist=%{SOURCE5}
registry_dist=%{SOURCE6}
cache_dist=%{SOURCE7}
scrubber_dist=%{SOURCE8}
for svc in api registry cache scrubber; do
  #  First we ensure all values are commented in appropriate format.
  #  Since icehouse, there was an uncommented keystone_authtoken section
  #  at the end of the file which mimics but also conflicted with our
  #  distro editing that had been done for many releases.
  sed -i '/^[^#[]/{s/^/#/; s/ //g}; /^#[^ ]/s/ = /=/' etc/glance-$svc.conf

  #  TODO: Make this more robust
  #  Note it only edits the first occurance, so assumes a section ordering in sample
  #  and also doesn't support multi-valued variables like dhcpbridge_flagfile.
  eval dist_conf=\$${svc}_dist
  while read name eq value; do
    test "$name" && test "$value" || continue
    sed -i "0,/^# *$name=/{s!^# *$name=.*!#$name=$value!}" etc/glance-$svc.conf
  done < $dist_conf
done

%build
%python_build

%install
%python_install

# Delete tests
rm -fr %{buildroot}%{python_sitelibdir}/glance/tests

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
install -d -m 755 %{buildroot}%{_datadir}/glance
install -d -m 755 %{buildroot}%{_sharedstatedir}/glance/images

# Config file
install -p -D -m 640 etc/glance-api.conf %{buildroot}%{_sysconfdir}/glance/glance-api.conf
install -p -D -m 644 %{SOURCE5} %{buildroot}%{_datadir}/glance/glance-api-dist.conf
install -p -D -m 644 etc/glance-api-paste.ini %{buildroot}%{_datadir}/glance/glance-api-dist-paste.ini
install -p -D -m 640 etc/glance-registry.conf %{buildroot}%{_sysconfdir}/glance/glance-registry.conf
install -p -D -m 644 %{SOURCE6} %{buildroot}%{_datadir}/glance/glance-registry-dist.conf
install -p -D -m 644 etc/glance-registry-paste.ini %{buildroot}%{_datadir}/glance/glance-registry-dist-paste.ini
install -p -D -m 640 etc/glance-cache.conf %{buildroot}%{_sysconfdir}/glance/glance-cache.conf
install -p -D -m 644 %{SOURCE7} %{buildroot}%{_datadir}/glance/glance-cache-dist.conf
install -p -D -m 640 etc/glance-scrubber.conf %{buildroot}%{_sysconfdir}/glance/glance-scrubber.conf
install -p -D -m 644 %{SOURCE8} %{buildroot}%{_datadir}/glance/glance-scrubber-dist.conf
install -p -D -m 640 etc/policy.json %{buildroot}%{_sysconfdir}/glance/policy.json
install -p -D -m 640 etc/schema-image.json %{buildroot}%{_sysconfdir}/glance/schema-image.json

# Initscripts
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/openstack-glance-api.service
install -p -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/openstack-glance-registry.service
install -p -D -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/openstack-glance-scrubber.service

# Initscripts
install -p -D -m 755 %{SOURCE40} %{buildroot}%{_initdir}/openstack-glance-api
install -p -D -m 755 %{SOURCE50} %{buildroot}%{_initdir}/openstack-glance-registry

# Logrotate config
install -p -D -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/openstack-glance

# Install pid directory
install -d -m 755 %{buildroot}%{_runtimedir}/glance

# Install log directory
install -d -m 755 %{buildroot}%{_logdir}/glance

# Programmatically update defaults in sample config
# which is installed at /etc/$project/$program.conf
# TODO: Make this more robust
# Note it only edits the first occurance, so assumes a section ordering in sample
# and also doesn't support multi-valued variables.
for svc in api registry cache scrubber; do
  cfg=%{buildroot}%{_sysconfdir}/glance/glance-$svc.conf
  test -e $cfg || continue
  while read name eq value; do
    test "$name" && test "$value" || continue
    # Note some values in upstream glance config may not be commented
    # and if not, they might not match the default value in code.
    # So we comment out both froms to have dist config take precedence.
    sed -i "0,/^#* *$name *=/{s!^#* *$name *=.*!#$name=$value!}" $cfg
  done < %{buildroot}%{_datadir}/glance/glance-$svc-dist.conf
done


%pre
getent group glance >/dev/null || groupadd -r glance -g 161
getent passwd glance >/dev/null || \
useradd -u 161 -r -g glance -d %{_sharedstatedir}/glance -s /sbin/nologin \
-c "OpenStack Glance Daemons" glance
exit 0

%post
%post_service %name-api
%post_service %name-registry
%post_service %name-glance-scrubber

%preun
%preun_service %name-api
%preun_service %name-registry
%preun_service %name-glance-scrubber

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

%{_datadir}/glance/glance-api-dist.conf
%{_datadir}/glance/glance-registry-dist.conf
%{_datadir}/glance/glance-cache-dist.conf
%{_datadir}/glance/glance-scrubber-dist.conf
%{_datadir}/glance/glance-api-dist-paste.ini
%{_datadir}/glance/glance-registry-dist-paste.ini

%{_unitdir}/%name-api.service
%{_unitdir}/%name-registry.service
%{_unitdir}/%name-scrubber.service
%{_initdir}/%name-api
%{_initdir}/%name-registry

%{_mandir}/man1/glance*.1.gz
%dir %{_sysconfdir}/glance
%config(noreplace) %attr(-, root, glance) %{_sysconfdir}/glance/glance-api.conf
%config(noreplace) %attr(-, root, glance) %{_sysconfdir}/glance/glance-registry.conf
%config(noreplace) %attr(-, root, glance) %{_sysconfdir}/glance/glance-cache.conf
%config(noreplace) %attr(-, root, glance) %{_sysconfdir}/glance/glance-scrubber.conf
%config(noreplace) %attr(-, root, glance) %{_sysconfdir}/glance/policy.json
%config(noreplace) %attr(-, root, glance) %{_sysconfdir}/glance/schema-image.json
%config(noreplace) %attr(-, root, glance) %{_sysconfdir}/logrotate.d/%name
%dir %attr(0755, glance, nobody) %{_sharedstatedir}/glance
%dir %attr(0750, glance, glance) %{_logdir}/glance
%dir %attr(0755, glance, nobody) %{_runtimedir}/glance

%files -n python-module-glance
%doc README.rst
%{python_sitelibdir}/glance
%{python_sitelibdir}/glance-%{version}*.egg-info


%files doc
%doc doc/build/html

%changelog
* Fri Jul 11 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1-alt1
- New version - icehouse (based on Fedora)

* Wed Aug 28 2013 Pavel Shilovsky <piastry@altlinux.org> 2012.2.0.4-alt3
- Cleanup spec

* Sat Mar 30 2013 Pavel Shilovsky <piastry@altlinux.org> 2012.2.0.4-alt2.1
- Add SysVinit support

* Wed Mar 06 2013 Pavel Shilovsky <piastry@altlinux.org> 2012.2.0.4-alt2
- Use post/preun_service scripts in spec

* Thu Nov 08 2012 Pavel Shilovsky <piastry@altlinux.org> 2012.2.0.4-alt1
- Initial release for Sisyphus (based on Fedora)
