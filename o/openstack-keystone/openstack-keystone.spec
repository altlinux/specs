%def_without python3

Name:		openstack-keystone
Version:	2015.1.0
Release:	alt0.b2.0
Summary:	OpenStack Identity Service

%add_python_req_skip xmldsig

Group: System/Servers
License: ASL 2.0
URL: http://keystone.openstack.org/
Source0: %name-%version.tar
Source1: %name.logrotate
Source2: %name.service
Source3: %name.sysctl
Source4: %name.tmpfiles
Source5: %name-sample-data
Source20: keystone-dist.conf
Source100: %name.init

#
# patches_base=2014.1.2.1
#
Patch0001: 0001-remove-runtime-dep-on-python-pbr.patch
Patch0002: 0002-sync-parameter-values-with-keystone-dist.conf.patch

BuildArch: noarch

Requires(pre): python-module-keystone = %version-%release
Requires: python-module-keystoneclient >= 1.0.0
Requires: /usr/bin/uuidgen

Requires(pre): shadow-utils

BuildRequires: python-devel
BuildRequires: python-module-sphinx >= 1.0
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-pbr
BuildRequires: python-module-d2to1
BuildRequires: python-module-SQLAlchemy >= 0.9.7
BuildRequires: python-module-migrate >= 0.9.1
BuildRequires: python-module-jsonschema
BuildRequires: python-module-oslo.config >= 1.6.0
BuildRequires: python-module-oslo.messaging >= 1.6.0
BuildRequires: python-module-oslo.db >= 1.4.1
BuildRequires: python-module-oslo.i18n >= 1.3.0
BuildRequires: python-module-oslo.middleware >= 0.3.0
BuildRequires: python-module-oslo.serialization >= 1.2.0
BuildRequires: python-module-oslo.utils >= 1.2.0
BuildRequires: python-module-oslotest >= 1.1.0
BuildRequires: python-module-routes >= 1.12.3
BuildRequires: python-module-paste
BuildRequires: python-module-PasteDeploy >= 1.5.0
BuildRequires: python-module-keystoneclient >= 1.0.0
BuildRequires: python-module-dogpile-cache >= 0.5.3
BuildRequires: python-module-ldap
BuildRequires: python-module-oauthlib >= 0.6
BuildRequires: python-module-eventlet >= 0.16.1

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-sphinx >= 1.0
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-pbr
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-SQLAlchemy >= 0.9.7
BuildRequires: python3-module-migrate >= 0.9.1
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-oslo.config >= 1.6.0
BuildRequires: python3-module-oslo.messaging >= 1.6.0
BuildRequires: python3-module-oslo.db >= 1.4.1
BuildRequires: python3-module-oslo.i18n >= 1.3.0
BuildRequires: python3-module-oslo.middleware >= 0.3.0
BuildRequires: python3-module-oslo.serialization >= 1.2.0
BuildRequires: python3-module-oslo.utils >= 1.2.0
BuildRequires: python3-module-oslotest >= 1.1.0
BuildRequires: python3-module-routes >= 1.12.3
BuildRequires: python3-module-paste
BuildRequires: python3-module-PasteDeploy >= 1.5.0
BuildRequires: python3-module-keystoneclient >= 1.0.0
BuildRequires: python3-module-dogpile-cache >= 0.5.3
BuildRequires: python3-module-ldap
BuildRequires: python3-module-oauthlib >= 0.6
BuildRequires: python3-module-eventlet >= 0.16.1
%endif


%description
Keystone is a Python implementation of the OpenStack
(http://www.openstack.org) identity service API.

This package contains the Keystone daemon.

%package -n python-module-keystone
Summary: Keystone Python libraries
Group: Development/Python
Requires: openssl
Requires: python-module-oslo.config >= 1.6.0
Requires: python-module-oslo.messaging >= 1.6.0
Requires: python-module-oslo.db
Requires: python-module-oslo.i18n
Requires: python-module-oslo.utils
# add not finded requires
Requires: python-module-dogpile-cache

%description -n python-module-keystone
Keystone is a Python implementation of the OpenStack
(http://www.openstack.org) identity service API.

This package contains the Keystone Python library.

%package -n python3-module-keystone
Summary: Keystone Python libraries
Group: Development/Python3
Requires: openssl
Requires: python3-module-oslo.config >= 1.6.0
Requires: python3-module-oslo.messaging >= 1.6.0
Requires: python3-module-oslo.db
Requires: python3-module-oslo.i18n
Requires: python3-module-oslo.utils

# add not finded requires
Requires: python3-module-dogpile-cache

%description -n python3-module-keystone
Keystone is a Python implementation of the OpenStack
(http://www.openstack.org) identity service API.

This package contains the Keystone Python library.

%package doc
Summary:	Documentation for OpenStack Identity Service
Group:		Development/Documentation

%description doc
Keystone is a Python implementation of the OpenStack
(http://www.openstack.org) identity service API.

This package contains documentation for Keystone.

%prep
%setup

%patch0001 -p1
%patch0002 -p1

find . \( -name .gitignore -o -name .placeholder \) -delete
find keystone -name \*.py -exec sed -i '/\/usr\/bin\/env python/d' {} \;
# Remove bundled egg-info
rm -rf keystone.egg-info

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

# Remove dependency on pbr and set version as per rpm
sed -i s/REDHATKEYSTONEVERSION/%version/ bin/keystone-all keystone/cli.py keystone/server/eventlet.py
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
cp etc/keystone.conf.sample etc/keystone.conf
# distribution defaults are located in keystone-dist.conf
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/keystone-all %buildroot%_bindir/python3-keystone-all
mv %buildroot%_bindir/keystone-manage %buildroot%_bindir/python3-keystone-manage
%endif

%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

install -d -m 755 %buildroot%_sysconfdir/keystone
install -p -D -m 640 etc/keystone.conf %buildroot%_sysconfdir/keystone/keystone.conf
install -p -D -m 644 etc/keystone-paste.ini %buildroot%_datadir/keystone/keystone-dist-paste.ini
install -p -D -m 644 %SOURCE20 %buildroot%_datadir/keystone/keystone-dist.conf
install -p -D -m 640 etc/logging.conf.sample %buildroot%_sysconfdir/keystone/logging.conf
install -p -D -m 640 etc/default_catalog.templates %buildroot%_sysconfdir/keystone/default_catalog.templates
install -p -D -m 640 etc/policy.json %buildroot%_sysconfdir/keystone/policy.json
install -p -D -m 644 %SOURCE1 %buildroot%_sysconfdir/logrotate.d/openstack-keystone
install -p -D -m 644 %SOURCE2 %buildroot%_unitdir/openstack-keystone.service
install -d -m 755 %buildroot%_sysctldir
install -p -D -m 644 %SOURCE3 %buildroot%_sysctldir/openstack-keystone.conf
install -d -m 755 %buildroot%_tmpfilesdir
install -p -D -m 644 %SOURCE4 %buildroot%_tmpfilesdir/openstack-keystone.conf
install -p -D -m 755 %SOURCE100 %buildroot%_initdir/%name
# Install sample data script.
install -p -D -m 755 tools/sample_data.sh %buildroot%_datadir/keystone/sample_data.sh
install -p -D -m 755 %SOURCE5 %buildroot%_bindir/openstack-keystone-sample-data
# Install sample HTTPD integration files
install -p -D -m 644 httpd/keystone.py  %buildroot%_datadir/keystone/keystone.wsgi
install -p -D -m 644 httpd/wsgi-keystone.conf  %buildroot%_datadir/keystone/

install -d -m 755 %buildroot%_sharedstatedir/keystone
install -d -m 755 %buildroot%_logdir/keystone
install -d -m 755 %buildroot%_runtimedir/keystone

# docs generation requires everything to be installed first
export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
if [ -x /usr/bin/sphinx-apidoc ]; then
    make html
    make man
else
    make html SPHINXAPIDOC=echo
    make man SPHINXAPIDOC=echo
fi
mkdir -p %buildroot%_man1dir
install -p -D -m 644 build/man/*.1 %buildroot%_man1dir/
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo

%pre
# 163:163 for keystone (openstack-keystone)
%_sbindir/groupadd -r -g 163 -f keystone 2>/dev/null ||:
%_sbindir/useradd -r -u 163 -g keystone -c 'OpenStack Keystone Daemons' \
        -s /sbin/nologin  -d %_sharedstatedir/keystone keystone 2>/dev/null ||:


%post
%post_service %name

#Generate ssl certs for pki token support
su -l -s /bin/sh -c 'exec keystone-manage pki_setup' keystone

%preun
%preun_service %name

%files
%doc LICENSE
%doc README.rst
%_bindir/openstack-keystone-sample-data
%dir %_datadir/keystone
%attr(0644, root, keystone) %_datadir/keystone/keystone-dist.conf
%attr(0644, root, keystone) %_datadir/keystone/keystone-dist-paste.ini
%attr(0755, root, root) %_datadir/keystone/sample_data.sh
%attr(0644, root, keystone) %_datadir/keystone/keystone.wsgi
%attr(0644, root, keystone) %_datadir/keystone/wsgi-keystone.conf
%_unitdir/openstack-keystone.service
%_initdir/%name
%_tmpfilesdir/openstack-keystone.conf
%dir %attr(0700, keystone, keystone) %_sysconfdir/keystone
%config(noreplace) %attr(0640, keystone, keystone) %_sysconfdir/keystone/keystone.conf
%config(noreplace) %attr(0640, keystone, keystone) %_sysconfdir/keystone/logging.conf
%config(noreplace) %attr(0640, keystone, keystone) %_sysconfdir/keystone/default_catalog.templates
%config(noreplace) %attr(0640, keystone, keystone) %_sysconfdir/keystone/policy.json
%config(noreplace) %_sysconfdir/logrotate.d/openstack-keystone
%dir %attr(-, keystone, keystone) %_sharedstatedir/keystone
%dir %attr(0750, keystone, keystone) %_logdir/keystone
%dir %attr(-, keystone, keystone) %_runtimedir/keystone
%_sysctldir/openstack-keystone.conf

%files -n python-module-keystone
%_bindir/keystone-all
%_bindir/keystone-manage
%_man1dir/keystone*.1.*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-keystone
%_bindir/python3-keystone-all
%_bindir/python3-keystone-manage
%python3_sitelibdir/*
%endif

%files doc
%doc LICENSE doc/build/html

%changelog
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
