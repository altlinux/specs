%define oname keystone

Name: openstack-%oname
Version: 14.0.1
Release: alt2
Epoch: 1
Summary: OpenStack Identity Service

%add_python_req_skip xmldsig

Group: System/Servers
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

Source1: %name.logrotate
Source3: %name.sysctl
Source4: %name.tmpfiles
Source5: %name.conf
Source6: %name.start

BuildArch: noarch

Requires(pre): python3-module-keystone = %EVR
Requires: python3-module-keystoneclient >= 3.8.0
Requires: python3-module-pymysql
Requires: apache2-mod_wsgi-py3
Requires: /usr/bin/uuidgen

Requires(pre): shadow-utils

BuildRequires: webserver-common rpm-build-webserver-common rpm-macros-apache2
BuildRequires: crudini
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-webob >= 1.7.1
BuildRequires: python-module-routes >= 2.3.1
BuildRequires: python-module-flask >= 1.0.2
BuildRequires: python-module-flask-restful >= 0.3.5
BuildRequires: python-module-cryptography >= 2.1
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-SQLAlchemy >= 1.0.10
BuildRequires: python-module-migrate >= 0.11.0
BuildRequires: python-module-stevedore >= 1.20.0
BuildRequires: python-module-passlib >= 1.7.0
BuildRequires: python-module-keystoneclient >= 3.8.0
BuildRequires: python-module-keystonemiddleware >= 4.17.0
BuildRequires: python-module-bcrypt >= 3.1.3
BuildRequires: python-module-scrypt >= 0.8.0

BuildRequires: python-module-oslo.cache >= 1.26.0
BuildRequires: python-module-oslo.concurrency >= 3.26.0
BuildRequires: python-module-oslo.config >= 5.2.0
BuildRequires: python-module-oslo.context >= 2.21.0
BuildRequires: python-module-oslo.messaging >= 5.29.0
BuildRequires: python-module-oslo.db >= 4.27.0
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-oslo.log >= 3.36.0
BuildRequires: python-module-oslo.middleware >= 3.31.0
BuildRequires: python-module-oslo.policy >= 1.30.0
BuildRequires: python-module-oslo.serialization >= 2.18.0
BuildRequires: python-module-oslo.utils >= 3.33.0

BuildRequires: python-module-oauthlib >= 0.6.2
BuildRequires: python-module-pysaml2 >= 4.5.0
BuildRequires: python-module-dogpile-cache >= 0.6.2
BuildRequires: python-module-jsonschema >= 2.6.0
BuildRequires: python-module-pycadf >= 1.1.0
BuildRequires: python-module-msgpack >= 0.4.0
BuildRequires: python-module-osprofiler >= 1.4.0
BuildRequires: python-module-pytz >= 2013.6

BuildRequires: python-module-webtest
BuildRequires: python-module-sphinx >= 1.6.2
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-reno >= 2.5.0
BuildRequires: python-module-sphinxcontrib-apidoc >= 0.2.0
BuildRequires: python-module-os-api-ref >= 1.4.0

BuildRequires: python-module-oslotest >= 3.2.0
BuildRequires: python-module-stestr >= 1.0.0
BuildRequires: python-module-testtools >= 2.2.0
BuildRequires: python-module-tempest >= 17.1.0

BuildRequires: python-module-freezegun >= 0.3.6
BuildRequires: python-module-oslo.db-tests

BuildRequires: python-module-ldap >= 3.0.0 python-module-ldappool >= 2.0.0
BuildRequires: python-module-memcached >= 1.56
BuildRequires: python-module-pymongo >= 3.0.2

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-webob >= 1.7.1
BuildRequires: python3-module-routes >= 2.3.1
BuildRequires: python3-module-flask >= 1.0.2
BuildRequires: python3-module-flask-restful >= 0.3.5
BuildRequires: python3-module-cryptography >= 2.1
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-SQLAlchemy >= 1.0.10
BuildRequires: python3-module-migrate >= 0.11.0
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-passlib >= 1.7.0
BuildRequires: python3-module-keystoneclient >= 3.8.0
BuildRequires: python3-module-keystonemiddleware >= 4.17.0
BuildRequires: python3-module-bcrypt >= 3.1.3
BuildRequires: python3-module-scrypt >= 0.8.0

BuildRequires: python3-module-oslo.cache >= 1.26.0
BuildRequires: python3-module-oslo.concurrency >= 3.26.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.context >= 2.21.0
BuildRequires: python3-module-oslo.messaging >= 5.29.0
BuildRequires: python3-module-oslo.db >= 4.27.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.middleware >= 3.31.0
BuildRequires: python3-module-oslo.policy >= 1.30.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0

BuildRequires: python3-module-oauthlib >= 0.6.2
BuildRequires: python3-module-pysaml2 >= 4.5.0
BuildRequires: python3-module-dogpile-cache >= 0.6.2
BuildRequires: python3-module-jsonschema >= 2.6.0
BuildRequires: python3-module-pycadf >= 1.1.0
BuildRequires: python3-module-msgpack >= 0.4.0
BuildRequires: python3-module-osprofiler >= 1.4.0
BuildRequires: python3-module-pytz >= 2013.6

BuildRequires: python3-module-webtest
BuildRequires: python3-module-sphinx >= 1.6.2
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-sphinxcontrib-apidoc >= 0.2.0
BuildRequires: python3-module-os-api-ref >= 1.4.0

BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-stestr >= 1.0.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-tempest >= 17.1.0

BuildRequires: python3-module-freezegun >= 0.3.6
BuildRequires: python3-module-oslo.db-tests

BuildRequires: python3-module-ldap >= 3.0.0 python3-module-ldappool >= 2.0.0
BuildRequires: python3-module-memcached >= 1.56
BuildRequires: python3-module-pymongo >= 3.0.2


%description
Keystone is a Python implementation of the OpenStack
(http://www.openstack.org) identity service API.

This package contains the Keystone daemon.

%package -n python-module-%oname
Summary: Keystone Python libraries
Group: Development/Python
Requires: openssl
Requires: python-module-oslo.cache >= 1.26.0
Requires: python-module-oslo.concurrency >= 3.26.0
Requires: python-module-oslo.config >= 5.2.0
Requires: python-module-oslo.context >= 2.21.0
Requires: python-module-oslo.messaging >= 5.29.0
Requires: python-module-oslo.db >= 4.27.0
Requires: python-module-oslo.i18n >= 3.15.3
Requires: python-module-oslo.log >= 3.36.0
Requires: python-module-oslo.middleware >= 3.31.0
Requires: python-module-oslo.policy >= 1.30.0
Requires: python-module-oslo.serialization >= 2.18.0
Requires: python-module-oslo.utils >= 3.33.0
# add not finded requires
Requires: python-module-dogpile-cache >= 0.6.2
Requires: python-module-pysaml2 >= 4.5.0

%description -n python-module-%oname
Keystone is a Python implementation of the OpenStack
(http://www.openstack.org) identity service API.

This package contains the Keystone Python library.


%package -n python-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description -n python-module-%oname-tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Keystone Python libraries
Group: Development/Python3
Requires: openssl
Requires: python3-module-oslo.cache >= 1.26.0
Requires: python3-module-oslo.concurrency >= 3.26.0
Requires: python3-module-oslo.config >= 5.2.0
Requires: python3-module-oslo.context >= 2.21.0
Requires: python3-module-oslo.messaging >= 5.29.0
Requires: python3-module-oslo.db >= 4.27.0
Requires: python3-module-oslo.i18n >= 3.15.3
Requires: python3-module-oslo.log >= 3.36.0
Requires: python3-module-oslo.middleware >= 3.31.0
Requires: python3-module-oslo.policy >= 1.30.0
Requires: python3-module-oslo.serialization >= 2.18.0
Requires: python3-module-oslo.utils >= 3.33.0
# add not finded requires
Requires: python3-module-dogpile-cache >= 0.6.2
Requires: python3-module-pysaml2 >= 4.5.0
Requires: python3-module-bcrypt >= 3.1.3
Requires: python3-module-scrypt >= 0.8.0

%description -n python3-module-%oname
Keystone is a Python implementation of the OpenStack
(http://www.openstack.org) identity service API.

This package contains the Keystone Python library.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Identity Service
Group: Development/Documentation

%description doc
Keystone is a Python implementation of the OpenStack
(http://www.openstack.org) identity service API.

This package contains documentation for Keystone.

%prep
%setup -n %oname-%version

find . \( -name .gitignore -o -name .placeholder \) -delete
find keystone -name \*.py -exec sed -i '/\/usr\/bin\/env python/d' {} \;
# Remove bundled egg-info
#rm -rf keystone.egg-info

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

rm -rf ../python3
cp -a . ../python3

%build
PYTHONPATH=. oslo-config-generator --config-file=config-generator/keystone.conf
PYTHONPATH=. oslo-config-generator --config-file=config-generator/keystone-policy-generator.conf
%python_build

python3 setup.py build_sphinx
rm -rf build/sphinx/html/.buildinfo
sphinx-build-3 -b man doc/source doc/build/man

pushd ../python3
%python3_build
popd

%install
%python_install
mv %buildroot%_bindir/keystone-manage %buildroot%_bindir/keystone-manage.py2

pushd ../python3
%python3_install
popd


install -d -m 755 %buildroot%_sysconfdir/keystone
install -d -m 755 %buildroot%_sysconfdir/keystone/keystone.conf.d/
install -d -m 770 %buildroot%_sysconfdir/keystone/credential-keys/
install -p -D -m 640 etc/keystone.conf.sample %buildroot%_sysconfdir/keystone/keystone.conf
install -p -D -m 640 etc/keystone.policy.yaml.sample %buildroot%_sysconfdir/keystone/keystone.policy.yaml
install -p -D -m 644 etc/keystone-paste.ini %buildroot%_sysconfdir/keystone/

install -p -D -m 644 etc/policy.v3cloudsample.json %buildroot%_sysconfdir/keystone/policy.v3cloudsample.json
install -p -D -m 640 etc/logging.conf.sample %buildroot%_sysconfdir/keystone/logging.conf
install -p -D -m 644 etc/default_catalog.templates %buildroot%_sysconfdir/keystone/default_catalog.templates
install -p -D -m 644 etc/sso_callback_template.html %buildroot%_sysconfdir/keystone/sso_callback_template.html
install -p -D -m 644 %SOURCE1 %buildroot%_sysconfdir/logrotate.d/openstack-keystone
install -d -m 755 %buildroot%_sysctldir
install -p -D -m 644 %SOURCE3 %buildroot%_sysctldir/openstack-keystone.conf
install -d -m 755 %buildroot%_tmpfilesdir
install -p -D -m 644 %SOURCE4 %buildroot%_tmpfilesdir/openstack-keystone.conf

install -m 0644 -D -p %SOURCE5 %buildroot%apache2_sites_available/openstack-keystone.conf
install -m 0644 -D -p %SOURCE6 %buildroot%apache2_sites_start/100-openstack-keystone.conf

mkdir -p %buildroot%apache2_sites_enabled
touch %buildroot%apache2_sites_enabled/openstack-keystone.conf

install -d -m 755 %buildroot%_sharedstatedir/keystone
install -d -m 750 %buildroot%_logdir/keystone
install -d -m 755 %buildroot%_runtimedir/keystone

mkdir -p %buildroot%_man1dir
install -p -D -m 644 doc/build/man/*.1 %buildroot%_man1dir/

# create keystone ssl dirs
install -d %buildroot%_sysconfdir/keystone/ssl/private
touch %buildroot%_sysconfdir/keystone/ssl/private/signing_key.pem
install -d %buildroot%_sysconfdir/keystone/ssl/certs
touch %buildroot%_sysconfdir/keystone/ssl/certs/signing_cert.pem

### set default configuration
%define keystone_conf %buildroot%_sysconfdir/keystone/keystone.conf.d/010-keystone.conf
crudini --set %keystone_conf DEFAULT log_dir /var/log/keystone

# cleanup
rm -rf %buildroot/usr/etc

%pre
# 163:163 for keystone (openstack-keystone)
%_sbindir/groupadd -r -g 163 -f keystone 2>/dev/null ||:
%_sbindir/useradd -r -u 163 -g keystone -c 'OpenStack Keystone Daemons' \
        -s /sbin/nologin  -d %_sharedstatedir/keystone keystone 2>/dev/null ||:

%_sbindir/a2enmod wsgi-py3

%post
keystone-manage fernet_setup --keystone-user keystone --keystone-group keystone
keystone-manage credential_setup --keystone-user keystone --keystone-group keystone
# keystone-manage will create a keystone.log file owned by root; fix that
if [ -f %_logdir/keystone/keystone-manage.log ]; then
    chown keystone:keystone %_logdir/keystone/keystone-manage.log
fi

#%preun
#%preun_service %name

%files
%doc LICENSE
%doc README.rst
%doc tools/sample_data.sh
%doc httpd/*
%config(noreplace) %apache2_sites_available/*.conf
%apache2_sites_start/*.conf
%ghost %apache2_sites_enabled/*.conf
%_tmpfilesdir/openstack-keystone.conf
%_bindir/keystone-wsgi-admin
%_bindir/keystone-wsgi-public
%dir %attr(0750, root, keystone) %_sysconfdir/keystone
%dir %attr(0750, root, keystone) %_sysconfdir/keystone/keystone.conf.d
%dir %attr(0770, root, keystone) %_sysconfdir/keystone/credential-keys
%dir %attr(0755, root, keystone) %_sysconfdir/keystone/ssl
%dir %attr(0755, root, keystone) %_sysconfdir/keystone/ssl/certs
%ghost %attr(0644, root, keystone) %_sysconfdir/keystone/ssl/certs/signing_cert.pem
%dir %attr(0750, root, keystone) %_sysconfdir/keystone/ssl/private
%ghost %attr(0640, root, keystone) %_sysconfdir/keystone/ssl/private/signing_key.pem
%config(noreplace) %attr(0640, root, keystone) %_sysconfdir/keystone/keystone.conf
%config(noreplace) %attr(0640, root, keystone) %_sysconfdir/keystone/keystone.conf.d/010-keystone.conf
%config(noreplace) %attr(0644, root, keystone) %_sysconfdir/keystone/logging.conf
%config %_sysconfdir/keystone/default_catalog.templates
%config %_sysconfdir/keystone/keystone-paste.ini
%config %_sysconfdir/keystone/keystone.policy.yaml
%config %_sysconfdir/keystone/policy.v3cloudsample.json
%config %_sysconfdir/keystone/sso_callback_template.html
%config(noreplace) %_sysconfdir/logrotate.d/openstack-keystone
%dir %attr(0755, keystone, keystone) %_sharedstatedir/keystone
%dir %attr(0750, keystone, keystone) %_logdir/keystone
%dir %attr(0755, keystone, keystone) %_runtimedir/keystone
%_sysctldir/openstack-keystone.conf

%files -n python-module-%oname
%python_sitelibdir/*
%_bindir/keystone-manage.py2
%_man1dir/keystone*.1.*
%exclude %python_sitelibdir/%oname/tests

%files -n python-module-%oname-tests
%python_sitelibdir/%oname/tests

%files -n python3-module-%oname
%python3_sitelibdir/*
%_bindir/keystone-manage
%_man1dir/keystone*.1.*
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests

%files doc
%doc LICENSE build/sphinx/html

%changelog
* Thu Jan 31 2019 Alexey Shabalin <shaba@altlinux.org> 1:14.0.1-alt2
- update Requires
- update apache config
- execute a2enmod wsgi-py3 in %%pre

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 1:14.0.1-alt1
- 14.0.1 Rocky release
- switch to python3

* Fri Jun 22 2018 Grigory Ustinov <grenka@altlinux.org> 1:11.0.3-alt2
- Fixed FTBFS (remove python-module-setuptools-tests from BR).

* Thu Aug 10 2017 Alexey Shabalin <shaba@altlinux.ru> 1:11.0.3-alt1
- 11.0.3

* Thu Jun 01 2017 Alexey Shabalin <shaba@altlinux.ru> 1:11.0.2-alt1
- 11.0.2 Ocata release
- add tests packages

* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 1:10.0.1-alt1
- 10.0.1

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 1:10.0.0-alt1
- 10.0.0 Newton release

* Fri Apr 08 2016 Alexey Shabalin <shaba@altlinux.ru> 1:9.0.0-alt1
- 9.0.0 Mitaka release

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 1:8.1.0-alt1
- 8.1.0

* Sat Feb 27 2016 Lenar Shakirov <snejok@altlinux.ru> 1:8.0.1-alt2
- links to wsgi-script fixed 

* Tue Dec 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1:8.0.1-alt1
- 8.0.1

* Tue Oct 27 2015 Alexey Shabalin <shaba@altlinux.ru> 1:8.0.0-alt1
- 8.0.0 Liberty release

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.2-alt1
- 2015.1.2
- add apcahe2 config to %%apache2_sites_available/openstack-keystone.conf

* Tue Aug 25 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.1-alt3
- update requires

* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.1-alt2
- drop "noreplace" from dist configs

* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.1-alt1
- 2015.1.1
- move dist configs from datadir to sysconfdir

* Thu May 14 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt1
- Release Kilo 2015.1.0

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b3.0
- 2015.1.0b3

* Wed Mar 11 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b2.0
- 2015.1.0b2

* Mon Feb 16 2015 Alexey Shabalin <shaba@altlinux.ru> 2014.2.2-alt1
- 2014.2.2
- backport patches from stable/juno
- add tmpfiles
- update systemd unit
- update init script

* Thu Aug 21 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.2.1-alt2
- Fix permission for /etc/keystone to (0700, keystone, keystone):
  * needs for "keystone-manage pki_setup" to generate certs
    in /etc/keystone/ssl, that runs in POSTIN script

* Tue Aug 12 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.2.1-alt1
- 2014.1.2.1

* Fri Jul 11 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt1
- New version - icehouse (based on Fedora)

* Mon Aug 26 2013 Vitaly Lipatov <lav@altlinux.ru> 2012.2.0.6-alt4
- cleanup spec

* Sat Mar 30 2013 Pavel Shilovsky <piastry@altlinux.org> 2012.2.0.6-alt3.1
- Add SysVinit support

* Wed Mar 06 2013 Pavel Shilovsky <piastry@altlinux.org> 2012.2.0.6-alt3
- Use post/preun_service scripts in spec

* Fri Mar 01 2013 Pavel Shilovsky <piastry@altlinux.org> 2012.2.0.6-alt2
- Fix python-module-keystone requires

* Thu Nov 08 2012 Pavel Shilovsky <piastry@altlinux.org> 2012.2.0.6-alt1
- Initial release for Sisyphus (based on Fedora)
