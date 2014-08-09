Name:		openstack-keystone
Version:	2014.1.1
Release:	alt1
Summary:	OpenStack Identity Service

Group:		System/Servers
License:	ASL 2.0
URL:		http://keystone.openstack.org/
Source0:	%{name}-%{version}.tar
Source1:	%{name}.logrotate
Source2:	%{name}.service
Source3:	%{name}.init
Source5:	%{name}-sample-data
Source20:	keystone-dist.conf

#
# patches_base=2014.1.1
#
Patch0001: 0001-remove-runtime-dep-on-python-pbr.patch
Patch0002: 0002-sync-parameter-values-with-keystone-dist.conf.patch
Patch0003: 0003-Refactor-service-readiness-notification.patch

BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	python-module-sphinx >= 1.0
BuildRequires:	python-module-oslo-sphinx
BuildRequires:	python-module-pbr
BuildRequires:	python-module-d2to1

Requires:	python-module-keystone = %{version}-%{release}
Requires:	python-module-keystoneclient

Requires(pre):	shadow-utils

%description
Keystone is a Python implementation of the OpenStack
(http://www.openstack.org) identity service API.

This package contains the Keystone daemon.

%package -n python-module-keystone
Summary:	Keystone Python libraries
Group:		Development/Python

Requires:	python-module-eventlet
Requires:	python-module-ldap
Requires:	python-module-lxml
Requires:	python-module-memcached
Requires:	python-module-migrate
Requires:	python-module-PasteDeploy
Requires:	python-module-routes
Requires:	python-module-SQLAlchemy
Requires:	python-module-webob
Requires:	python-module-passlib
Requires:	python-module-MySQLdb
Requires:	python-module-PAM
Requires:	python-module-iso8601
Requires:	python-module-oslo-config >= 1.2.0
Requires:	openssl
Requires:       python-module-netaddr
Requires:       python-module-six >= 1.4.1
Requires:       python-module-babel
Requires:       python-module-oauthlib
Requires:       python-module-dogpile-cache >= 0.5.0
Requires:       python-module-jsonschema
Requires:       python-module-oslo-messaging
Requires:       python-module-pycadf



%description -n python-module-keystone
Keystone is a Python implementation of the OpenStack
(http://www.openstack.org) identity service API.

This package contains the Keystone Python library.

%package doc
Summary:	Documentation for OpenStack Identity Service
Group:		Documentation

%description doc
Keystone is a Python implementation of the OpenStack
(http://www.openstack.org) identity service API.

This package contains documentation for Keystone.

%prep
%setup

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1

find . \( -name .gitignore -o -name .placeholder \) -delete
find keystone -name \*.py -exec sed -i '/\/usr\/bin\/env python/d' {} \;
# Remove bundled egg-info
rm -rf keystone.egg-info

# Remove dependency on pbr and set version as per rpm
sed -i s/REDHATKEYSTONEVERSION/%{version}/ bin/keystone-all keystone/cli.py

# make doc build compatible with python-oslo-sphinx RPM
sed -i 's/oslosphinx/oslo.sphinx/' doc/source/conf.py

%build
cp etc/keystone.conf.sample etc/keystone.conf
# distribution defaults are located in keystone-dist.conf
%python_build

%install
%python_install

# Delete tests
rm -fr %{buildroot}%{python_sitelibdir}}/keystone/tests

install -d -m 755 %{buildroot}%{_sysconfdir}/keystone
install -p -D -m 640 etc/keystone.conf %{buildroot}%{_sysconfdir}/keystone/keystone.conf
install -p -D -m 644 etc/keystone-paste.ini %{buildroot}%{_datadir}/keystone/keystone-dist-paste.ini
install -p -D -m 644 %{SOURCE20} %{buildroot}%{_datadir}/keystone/keystone-dist.conf
install -p -D -m 640 etc/logging.conf.sample %{buildroot}%{_sysconfdir}/keystone/logging.conf
install -p -D -m 640 etc/default_catalog.templates %{buildroot}%{_sysconfdir}/keystone/default_catalog.templates
install -p -D -m 640 etc/policy.json %{buildroot}%{_sysconfdir}/keystone/policy.json
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -p -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
install -p -D -m 755 %{SOURCE3} %{buildroot}%{_initdir}/%{name}
# Install sample data script.
install -p -D -m 755 tools/sample_data.sh %{buildroot}%{_datadir}/keystone/sample_data.sh
install -p -D -m 755 %{SOURCE5} %{buildroot}%{_bindir}/openstack-keystone-sample-data
# Install sample HTTPD integration files
install -p -D -m 644 httpd/keystone.py  %{buildroot}%{_datadir}/keystone/keystone.wsgi
install -p -D -m 644 httpd/wsgi-keystone.conf  %{buildroot}%{_datadir}/keystone/

install -d -m 755 %{buildroot}%{_sharedstatedir}/keystone
install -d -m 755 %{buildroot}%{_logdir}/keystone

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
mkdir -p %{buildroot}%{_mandir}/man1
install -p -D -m 644 build/man/*.1 %{buildroot}%{_mandir}/man1/
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo

%pre
# 163:163 for keystone (openstack-keystone) - rhbz#752842
getent group keystone >/dev/null || groupadd -r --gid 163 keystone
getent passwd keystone >/dev/null || \
useradd --uid 163 -r -g keystone -d %{_sharedstatedir}/keystone -s /sbin/nologin \
-c "OpenStack Keystone Daemons" keystone
exit 0

%post
%post_service %{name}

%preun
%preun_service %{name}

%files
%doc LICENSE
%doc README.rst
%{_mandir}/man1/keystone*.1.gz
%{_bindir}/keystone-all
%{_bindir}/keystone-manage
%{_bindir}/%{name}-sample-data
%dir %{_datadir}/keystone
%attr(0644, root, keystone) %{_datadir}/keystone/keystone-dist.conf
%attr(0644, root, keystone) %{_datadir}/keystone/keystone-dist-paste.ini
%attr(0755, root, root) %{_datadir}/keystone/sample_data.sh
%attr(0644, root, keystone) %{_datadir}/keystone/keystone.wsgi
%attr(0644, root, keystone) %{_datadir}/keystone/wsgi-keystone.conf
%{_unitdir}/%{name}.service
%{_initdir}/%{name}
%dir %attr(0750, root, keystone) %{_sysconfdir}/keystone
%config(noreplace) %attr(0640, root, keystone) %{_sysconfdir}/keystone/keystone.conf
%config(noreplace) %attr(0640, root, keystone) %{_sysconfdir}/keystone/logging.conf
%config(noreplace) %attr(0640, root, keystone) %{_sysconfdir}/keystone/default_catalog.templates
%config(noreplace) %attr(0640, keystone, keystone) %{_sysconfdir}/keystone/policy.json
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %attr(-, keystone, keystone) %{_sharedstatedir}/keystone
%dir %attr(0750, keystone, keystone) %{_logdir}/keystone

%files -n python-module-keystone
%doc LICENSE
%{python_sitelibdir}/keystone
%{python_sitelibdir}/keystone-%{version}-*.egg-info

%files doc
%doc LICENSE doc/build/html

%changelog
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
