
Name: openstack-glance
Version: 13.0.0
Release: alt2
Epoch: 1
Summary: OpenStack Image Service

Group: System/Servers
License: ASL 2.0
Url: http://glance.openstack.org
Source0: %name-%version.tar
Source1: %name-api.service
Source2: %name-registry.service
Source3: %name-scrubber.service
Source4: %name.logrotate

Source40: %name-api.init
Source41: %name-registry.init
Source42: %name-scrubber.init
Source43: %name.tmpfiles

Patch0001: 0001-notify-calling-process-we-are-ready-to-serve.patch

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-SQLAlchemy >= 1.0.10
BuildRequires: python-module-eventlet >= 0.18.2
BuildRequires: python-module-PasteDeploy >= 1.5.0
BuildRequires: python-module-routes >= 1.12.3
BuildRequires: python-module-migrate >= 0.9.6
BuildRequires: python-module-httplib2 >= 0.7.5
BuildRequires: python-module-pycrypto >= 2.6
BuildRequires: python-module-oslo.config >= 3.14.0
BuildRequires: python-module-oslo.concurrency >= 3.8.0
BuildRequires: python-module-oslo.context >= 0.2.9
BuildRequires: python-module-oslo.service >= 1.10.0
BuildRequires: python-module-oslo.utils >= 3.16.0
BuildRequires: python-module-stevedore >= 1.16.0
BuildRequires: python-module-futurist >= 0.11.0
BuildRequires: python-module-taskflow >= 1.26.0
BuildRequires: python-module-keystoneauth1 >= 2.10.0
BuildRequires: python-module-keystonemiddleware >= 4.0.0
BuildRequires: python-module-wsme >= 0.8
BuildRequires: python-module-prettytable >= 0.7
BuildRequires: python-module-paste
BuildRequires: python-module-jsonschema >= 2.0.0
BuildRequires: python-module-keystoneclient >= 2.0.0
BuildRequires: python-module-OpenSSL >= 0.14
BuildRequires: python-module-oslo.db >= 4.10.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.log >= 1.14.0
BuildRequires: python-module-oslo.messaging >= 5.2.0
BuildRequires: python-module-oslo.middleware >= 3.0.0
BuildRequires: python-module-oslo.policy >= 1.9.0
BuildRequires: python-module-retrying >= 1.2.3
BuildRequires: python-module-osprofiler >= 1.4.0

BuildRequires: python-module-glance_store >= 0.18.0
BuildRequires: python-module-semantic_version >= 2.3.1
BuildRequires: python-module-cryptography >= 1.0
BuildRequires: python-module-cursive >= 0.1.1
BuildRequires: python-module-debtcollector >= 1.2.0
BuildRequires: python-module-iso8601 >= 0.1.11
BuildRequires: python-module-monotonic >= 0.6

# Required to build module documents
BuildRequires: python-module-boto
BuildRequires: python-module-webob
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-sphinx
BuildRequires: python-module-elasticsearch
BuildRequires: python-module-reno >= 1.8.0
BuildRequires: python-modules-sqlite3
BuildRequires: python-module-networkx-drawing

Requires(pre): shadow-utils
Requires: python-module-glance = %EVR
Requires: python-module-glanceclient
Requires: python-module-PasteDeploy
Requires: /usr/bin/qemu-img

Requires: openstack-utils

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
Summary: Glance Python libraries
Group: Development/Python
Requires: python-module-keystoneclient >= 1.6.0
Requires: python-module-keystonemiddleware >= 4.0.0
Requires: python-module-oslo.config >= 3.7.0
Requires: python-module-oslo.concurrency >= 3.5.0
Requires: python-module-oslo.context >= 0.2.0
Requires: python-module-oslo.service >= 1.0.0
Requires: python-module-oslo.utils >= 3.5.0
Requires: python-module-oslo.log >= 1.14.0
Requires: python-module-oslo.db >= 4.1.0
Requires: python-module-oslo.i18n >= 2.1.0
Requires: python-module-oslo.messaging >= 4.0.0
Requires: python-module-oslo.policy >= 0.5.0
Requires: python-module-oslo.serialization >= 1.10.0

%description -n python-module-glance
OpenStack Image Service (code-named Glance) provides discovery, registration,
and delivery services for virtual disk images.

This package contains the glance Python library.

%package doc
Summary: Documentation for OpenStack Image Service
Group: Development/Documentation
Requires: %name = %EVR

%description doc
OpenStack Image Service (code-named Glance) provides discovery, registration,
and delivery services for virtual disk images.

This package contains documentation files for glance.

%prep
%setup
%patch0001 -p1

# Remove bundled egg-info
#rm -rf glance.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requiers_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

%build
%python_build

# disabling git call for last modification date from git repo
sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py
python setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/glance/tests
rm -f  %buildroot%python_sitelibdir/glance/openstack/common/test*

# Drop old glance CLI it has been deprecated
# and replaced glanceclient
rm -f %buildroot%_bindir/glance

mkdir -p %buildroot%_man1dir
install -p -D -m 644 doc/build/man/*.1 %buildroot%_man1dir/

install -d -m 0755 %buildroot%_sysconfdir/glance
install -d -m 0755 %buildroot%_sysconfdir/glance/metadefs
cp -pr etc/* %buildroot%_sysconfdir/glance
rm -rf %buildroot%_sysconfdir/glance/oslo-config-generator
mv %buildroot%_sysconfdir/glance/glance-swift.conf{.sample,}

install -d -m 755 %buildroot%_sharedstatedir/glance/images

# Initscripts
install -p -D -m 644 %SOURCE1 %buildroot%_unitdir/openstack-glance-api.service
install -p -D -m 644 %SOURCE2 %buildroot%_unitdir/openstack-glance-registry.service
install -p -D -m 644 %SOURCE3 %buildroot%_unitdir/openstack-glance-scrubber.service

# Initscripts
install -p -D -m 755 %SOURCE40 %buildroot%_initdir/openstack-glance-api
install -p -D -m 755 %SOURCE41 %buildroot%_initdir/openstack-glance-registry
install -p -D -m 755 %SOURCE42 %buildroot%_initdir/openstack-glance-scrubber

install -p -D -m 644 %SOURCE43 %buildroot%_tmpfilesdir/%name.conf

# Logrotate config
install -p -D -m 644 %SOURCE4 %buildroot%_sysconfdir/logrotate.d/openstack-glance

# Install pid directory
install -d -m 755 %buildroot%_runtimedir/glance

# Install log directory
install -d -m 770 %buildroot%_logdir/glance

# Delete unneeded files
rm -rf %buildroot/usr/etc/glance

%pre
# 161:161 for glance (openstack-glance)
%_sbindir/groupadd -r -g 161 -f glance 2>/dev/null ||:
%_sbindir/useradd -r -u 161 -g glance -c 'OpenStack Glance Daemons' \
        -s /sbin/nologin  -d %_sharedstatedir/glance glance 2>/dev/null ||:

%post
%post_service %name-api
%post_service %name-registry
%post_service %name-scrubber

%preun
%preun_service %name-api
%preun_service %name-registry
%preun_service %name-scrubber

%files
%doc README.rst
%_bindir/*
%_unitdir/*
%_initdir/*
%_tmpfilesdir/*

%_man1dir/*
%dir %_sysconfdir/glance
%config(noreplace) %attr(640, root, glance) %_sysconfdir/glance/*.conf
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

%files -n python-module-glance
%doc README.rst
%python_sitelibdir/glance
%python_sitelibdir/*.egg-info

%files doc
%doc doc/build/html

%changelog
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
