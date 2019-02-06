%define oname glance

Name: openstack-%oname
Version: 17.0.0
Release: alt2
Epoch: 1
Summary: OpenStack Image Service

Group: System/Servers
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
Source1: %name-api.service
Source2: %name-registry.service
Source3: %name-scrubber.service
Source4: %name.logrotate
Source6: %name-glare.service

Source40: %name-api.init
Source41: %name-registry.init
Source42: %name-scrubber.init
Source43: %name.tmpfiles
Source46: %name-glare.init

Patch1: glance-fix-recursion.patch

BuildArch: noarch

Requires(pre): shadow-utils
Requires: python3-module-glance = %EVR
Requires: python3-module-glanceclient
Requires: python3-module-PasteDeploy
Requires: /usr/bin/qemu-img

BuildRequires: python-devel
BuildRequires: crudini
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-defusedxml >= 0.5.0
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-SQLAlchemy >= 1.0.10
BuildRequires: python-module-eventlet >= 0.18.2
BuildRequires: python-module-PasteDeploy >= 1.5.0
BuildRequires: python-module-routes >= 2.3.1
BuildRequires: python-module-migrate >= 0.11.0
BuildRequires: python-module-sqlparse >= 0.2.2
BuildRequires: python-module-alembic >= 0.8.10
BuildRequires: python-module-httplib2 >= 0.9.1
BuildRequires: python-module-oslo.config >= 5.2.0
BuildRequires: python-module-oslo.concurrency >= 3.26.0
BuildRequires: python-module-oslo.context >= 2.19.2
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-stevedore >= 1.20.0
BuildRequires: python-module-futurist >= 1.2.0
BuildRequires: python-module-taskflow >= 2.16.0
BuildRequires: python-module-keystoneauth1 >= 3.4.0
BuildRequires: python-module-keystonemiddleware >= 4.17.0
BuildRequires: python-module-wsme >= 0.8.0
BuildRequires: python-module-prettytable >= 0.7.1
BuildRequires: python-module-paste >= 2.0.2
BuildRequires: python-module-jsonschema >= 2.6.0
BuildRequires: python-module-OpenSSL >= 17.1.0
BuildRequires: python-module-oslo.db >= 4.27.0
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-oslo.log >= 3.36.0
BuildRequires: python-module-oslo.messaging >= 5.29.0
BuildRequires: python-module-oslo.middleware >= 3.31.0
BuildRequires: python-module-oslo.policy >= 1.30.0
BuildRequires: python-module-retrying >= 1.2.3
BuildRequires: python-module-osprofiler >= 1.4.0

BuildRequires: python-module-glance_store >= 0.26.1
BuildRequires: python-module-debtcollector >= 1.2.0
BuildRequires: python-module-cryptography >= 2.1
BuildRequires: python-module-cursive >= 0.2.1

BuildRequires: python-module-iso8601 >= 0.1.11
BuildRequires: python-module-monotonic >= 0.6

# Required to build module documents
BuildRequires: python-module-sphinx
BuildRequires: python-module-os-api-ref >= 1.4.0
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-reno >= 2.5.0
BuildRequires: python-module-sphinxcontrib-apidoc >= 0.2.0
BuildRequires: python-modules-sqlite3
#BuildRequires: python-modules-xattr >= 0.9.2


BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-defusedxml >= 0.5.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-SQLAlchemy >= 1.0.10
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-PasteDeploy >= 1.5.0
BuildRequires: python3-module-routes >= 2.3.1
BuildRequires: python3-module-migrate >= 0.11.0
BuildRequires: python3-module-sqlparse >= 0.2.2
BuildRequires: python3-module-alembic >= 0.8.10
BuildRequires: python3-module-httplib2 >= 0.9.1
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.concurrency >= 3.26.0
BuildRequires: python3-module-oslo.context >= 2.19.2
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-futurist >= 1.2.0
BuildRequires: python3-module-taskflow >= 2.16.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-keystonemiddleware >= 4.17.0
BuildRequires: python3-module-wsme >= 0.8.0
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-paste >= 2.0.2
BuildRequires: python3-module-jsonschema >= 2.6.0
BuildRequires: python3-module-OpenSSL >= 17.1.0
BuildRequires: python3-module-oslo.db >= 4.27.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.messaging >= 5.29.0
BuildRequires: python3-module-oslo.middleware >= 3.31.0
BuildRequires: python3-module-oslo.policy >= 1.30.0
BuildRequires: python3-module-retrying >= 1.2.3
BuildRequires: python3-module-osprofiler >= 1.4.0

BuildRequires: python3-module-glance_store >= 0.26.1
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-cryptography >= 2.1
BuildRequires: python3-module-cursive >= 0.2.1

BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-monotonic >= 0.6

# Required to build module documents
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-os-api-ref >= 1.4.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-sphinxcontrib-apidoc >= 0.2.0
BuildRequires: python3-modules-sqlite3
#BuildRequires: python3-modules-xattr >= 0.9.2

%description
OpenStack Image Service (code-named Glance) provides discovery, registration,
and delivery services for virtual disk images. The Image Service API server
provides a standard REST interface for querying information about virtual disk
images stored in a variety of back-end stores, including OpenStack Object
Storage. Clients can register new virtual disk images with the Image Service,
query for information on publicly available disk images, and use the Image
Service's client library for streaming virtual disk images.

This package contains the API and registry servers.

%package -n python-module-%oname
Summary: Glance Python libraries
Group: Development/Python
Requires: python-module-keystoneauth1 >= 3.4.0
Requires: python-module-keystonemiddleware >= 4.17.0
Requires: python-module-oslo.config >= 5.2.0
Requires: python-module-oslo.concurrency >= 3.26.0
Requires: python-module-oslo.context >= 2.19.2
Requires: python-module-oslo.utils >= 3.33.0
Requires: python-module-oslo.log >= 3.36.0
Requires: python-module-oslo.db >= 4.27.0
Requires: python-module-oslo.i18n >= 3.15.3
Requires: python-module-oslo.messaging >= 5.29.0
Requires: python-module-oslo.policy >= 1.30.0

%add_python_req_skip glance.cmd.cache_manage

%description -n python-module-%oname
OpenStack Image Service (code-named Glance) provides discovery, registration,
and delivery services for virtual disk images.

This package contains the glance Python library.

%package -n python-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python

%description -n python-module-%oname-tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Glance Python libraries
Group: Development/Python3
Requires: python3-module-keystoneauth1 >= 3.4.0
Requires: python3-module-keystonemiddleware >= 4.17.0
Requires: python3-module-oslo.config >= 5.2.0
Requires: python3-module-oslo.concurrency >= 3.26.0
Requires: python3-module-oslo.context >= 2.19.2
Requires: python3-module-oslo.utils >= 3.33.0
Requires: python3-module-oslo.log >= 3.36.0
Requires: python3-module-oslo.db >= 4.27.0
Requires: python3-module-oslo.i18n >= 3.15.3
Requires: python3-module-oslo.messaging >= 5.29.0
Requires: python3-module-oslo.policy >= 1.30.0

%add_python3_req_skip glance.cmd.cache_manage

%description -n python3-module-%oname
OpenStack Image Service (code-named Glance) provides discovery, registration,
and delivery services for virtual disk images.

This package contains the glance Python library.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Image Service
Group: Development/Documentation
Requires: %name = %EVR

%description doc
OpenStack Image Service (code-named Glance) provides discovery, registration,
and delivery services for virtual disk images.

This package contains documentation files for glance.

%prep
%setup -n %oname-%version
%patch1 -p1

# Remove bundled egg-info
#rm -rf glance.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requiers_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build

#python3 setup.py build_sphinx
#python3 setup.py build_sphinx -b man
# Fix hidden-file-or-dir warnings
#rm -fr build/sphinx/html/.buildinfo
# regenerate the sample config files
#for service in api registry scrubber cache manage glare; do
#    PYTHONPATH=. oslo-config-generator --config-file etc/oslo-config-generator/glance-$service.conf
#done
popd

%install
%python_install
mv %buildroot%_bindir/glance-api %buildroot%_bindir/glance-api.py2
mv %buildroot%_bindir/glance-cache-cleaner %buildroot%_bindir/glance-cache-cleaner.py2
mv %buildroot%_bindir/glance-cache-manage %buildroot%_bindir/glance-cache-manage.py2
mv %buildroot%_bindir/glance-cache-prefetcher %buildroot%_bindir/glance-cache-prefetcher.py2
mv %buildroot%_bindir/glance-cache-pruner %buildroot%_bindir/glance-cache-pruner.py2
mv %buildroot%_bindir/glance-control %buildroot%_bindir/glance-control.py2
mv %buildroot%_bindir/glance-manage %buildroot%_bindir/glance-manage.py2
mv %buildroot%_bindir/glance-registry %buildroot%_bindir/glance-registry.py2
mv %buildroot%_bindir/glance-replicator %buildroot%_bindir/glance-replicator.py2
mv %buildroot%_bindir/glance-scrubber %buildroot%_bindir/glance-scrubber.py2
mv %buildroot%_bindir/glance-wsgi-api %buildroot%_bindir/glance-wsgi-api.py2

install -d -m 0755 %buildroot%_sysconfdir/glance
install -d -m 0755 %buildroot%_sysconfdir/glance/metadefs

### configuration files
install -d -m 755 %buildroot%_sysconfdir/glance
install -d -m 755 %buildroot%_sysconfdir/glance/glance.conf.d/
install -d -m 755 %buildroot%_sysconfdir/glance/glance-api.conf.d/
install -d -m 755 %buildroot%_sysconfdir/glance/glance-registry.conf.d/

pushd ../python3
%python3_install
cp -pr etc/* %buildroot%_sysconfdir/glance

#for service in api registry scrubber cache manage glare swift; do
#for service in image-import swift; do
#    mv %buildroot%_sysconfdir/glance/glance-$service.conf{.sample,}
#done

# documentation
#install -d %buildroot%_mandir/man1
#install -m 644 doc/build/man/*.1 %buildroot%_mandir/man1

popd

rm -rf %buildroot%_sysconfdir/glance/oslo-config-generator

install -d -m 755 %buildroot%_sharedstatedir/glance/images

# Initscripts
install -p -D -m 644 %SOURCE1 %buildroot%_unitdir/openstack-glance-api.service
install -p -D -m 644 %SOURCE2 %buildroot%_unitdir/openstack-glance-registry.service
install -p -D -m 644 %SOURCE3 %buildroot%_unitdir/openstack-glance-scrubber.service
install -p -D -m 644 %SOURCE6 %buildroot%_unitdir/openstack-glance-glare.service

# Initscripts
install -p -D -m 755 %SOURCE40 %buildroot%_initdir/openstack-glance-api
install -p -D -m 755 %SOURCE41 %buildroot%_initdir/openstack-glance-registry
install -p -D -m 755 %SOURCE42 %buildroot%_initdir/openstack-glance-scrubber
install -p -D -m 755 %SOURCE46 %buildroot%_initdir/openstack-glance-glare

install -p -D -m 644 %SOURCE43 %buildroot%_tmpfilesdir/%name.conf

# Logrotate config
install -p -D -m 644 %SOURCE4 %buildroot%_sysconfdir/logrotate.d/openstack-glance

# Install pid directory
install -d -m 755 %buildroot%_runtimedir/glance

# Install log directory
install -d -m 770 %buildroot%_logdir/glance

# Delete unneeded files
rm -rf %buildroot/usr/etc

### set default configuration
%define glance_conf %buildroot%_sysconfdir/glance/glance.conf.d/010-glance.conf
crudini --set %glance_conf DEFAULT log_dir /var/log/glance
crudini --set %glance_conf oslo_concurrency lock_path /var/run/glance
crudini --set %glance_conf paste_deploy flavor keystone

%pre
# 161:161 for glance (openstack-glance)
%_sbindir/groupadd -r -g 161 -f glance 2>/dev/null ||:
%_sbindir/useradd -r -u 161 -g glance -c 'OpenStack Glance Daemons' \
        -s /sbin/nologin  -d %_sharedstatedir/glance glance 2>/dev/null ||:

%post
%post_service %name-api
%post_service %name-registry
%post_service %name-scrubber
%post_service %name-glare

%preun
%preun_service %name-api
%preun_service %name-registry
%preun_service %name-scrubber
%preun_service %name-glare

%files
%doc README.rst
%_unitdir/*
%_initdir/*
%_tmpfilesdir/*

#%_man1dir/*
%dir %_sysconfdir/glance
%dir %_sysconfdir/glance/glance.conf.d
%config(noreplace) %attr(640, root, glance) %_sysconfdir/glance/*.conf
%config(noreplace) %attr(640, root, glance) %_sysconfdir/glance/glance.conf.d/010-glance.conf
%config %_sysconfdir/glance/*.ini
%config %_sysconfdir/glance/*.json
%config %_sysconfdir/glance/*.sample
%dir %_sysconfdir/glance/metadefs
%_sysconfdir/glance/metadefs/README
%config %_sysconfdir/glance/metadefs/*.json
%config(noreplace) %_sysconfdir/logrotate.d/%name
%dir %attr(0775, root, glance) %_sharedstatedir/glance
%dir %attr(0775, root, glance) %_sharedstatedir/glance/images
%dir %attr(0770, root, glance) %_logdir/glance
%dir %attr(0775, root, glance) %_runtimedir/glance

%files -n python-module-%oname
%doc README.rst
%_bindir/*.py2
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests

%files -n python-module-%oname-tests
%python_sitelibdir/%oname/tests

%files -n python3-module-%oname
%doc README.rst
%_bindir/*
%exclude %_bindir/*.py2
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests

#%files doc
#%doc doc/build/html

%changelog
* Wed Feb 06 2019 Alexey Shabalin <shaba@altlinux.org> 1:17.0.0-alt2
- py3: fix recursion issue

* Mon Dec 24 2018 Alexey Shabalin <shaba@altlinux.org> 1:17.0.0-alt1
- 17.0.0 Rocky release
- switch to python3

* Fri Jun 22 2018 Grigory Ustinov <grenka@altlinux.org> 1:14.0.0-alt4
- Fixed FTBFS (remove python-module-setuptools-tests from BR).

* Wed Jul 19 2017 Alexey Shabalin <shaba@altlinux.ru> 1:14.0.0-alt3
- fix lock_path in default config

* Thu Jun 22 2017 Alexey Shabalin <shaba@altlinux.ru> 1:14.0.0-alt2
- drop signing_dir from default config

* Fri Jun 02 2017 Alexey Shabalin <shaba@altlinux.ru> 1:14.0.0-alt1
- 14.0.0 Ocata release
- add tests package

* Tue Nov 22 2016 Alexey Shabalin <shaba@altlinux.ru> 1:13.0.0-alt4
- fix logrotate

* Wed Nov 09 2016 Alexey Shabalin <shaba@altlinux.ru> 1:13.0.0-alt3
- add unit and init for glare
- update systemd units

* Wed Nov 09 2016 Alexey Shabalin <shaba@altlinux.ru> 1:13.0.0-alt2
- fix dir permitions

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1:13.0.0-alt1
- 13.0.0 (Newton Release)

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 1:12.0.0-alt1
- 12.0.0

* Wed Dec 30 2015 Alexey Shabalin <shaba@altlinux.ru> 1:11.0.1-alt1
- 11.0.1

* Mon Nov 09 2015 Alexey Shabalin <shaba@altlinux.ru> 1:11.0.0-alt2
- update systemd patch

* Fri Oct 30 2015 Alexey Shabalin <shaba@altlinux.ru> 1:11.0.0-alt1
- 11.0.0 Liberty release

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.2-alt1
- 2015.1.2

* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.1-alt1
- 2015.1.1

* Wed May 20 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt1
- 2015.1.0 Kilo Release

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b3.0
- 2015.1.0.b3

* Wed Mar 11 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b2.0
- 2015.1.0.b2

* Fri Mar 06 2015 Alexey Shabalin <shaba@altlinux.ru> 2014.2.2-alt1
- 2014.2.2

* Fri Sep 05 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt3
- BuildReq: graphviz, python-module-distribute removed

* Fri Sep 05 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt2
- {post,preun}_service openstack-glance-scrubber fixed

* Tue Aug 12 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt1
- 2014.1.1

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
