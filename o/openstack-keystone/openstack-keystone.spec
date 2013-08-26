#
# This is 2012.2 folsom-3 milestone
#
Name:		openstack-keystone
Version:	2012.2.0.6
Release:	alt4
Summary:	OpenStack Identity Service

Group:		System/Servers
License:	ASL 2.0
URL:		http://keystone.openstack.org/
Source0:	%{name}-%{version}.tar
Source1:	%{name}.logrotate
Source2:	%{name}.service
Source3:	%{name}.init
Source5:	%{name}-sample-data

#
# patches_base=folsom-3
#
Patch0001:	%{name}-allow-middleware-configuration-from-app-config.patch
Patch0002:	%{name}-match-egg-and-spec-requires.patch
Patch0003:	%{name}-check-for-expected-cfg-impl-bug-1043479.patch
Patch0004:	%{name}-require-authz-to-update-user-s-tenant-bug-1040626.patch

BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	python-module-sphinx >= 1.0
BuildRequires:	python-module-iniparse

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

Requires:	python-module-keystone-auth-token = %{version}-%{release}

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
Requires:	python-module-swift

%description -n python-module-keystone
Keystone is a Python implementation of the OpenStack
(http://www.openstack.org) identity service API.

This package contains the Keystone Python library.

%package -n python-module-keystone-auth-token
Summary:	Keystone Authentication Middleware.
Group:		Development/Python

Requires:	python-module-iso8601
Requires:	python-module-memcached
Requires:	python-module-webob

%description -n python-module-keystone-auth-token
Keystone is a Python implementation of the OpenStack
(http://www.openstack.org) identity service API.

This package contains the Keystone Authentication Middleware.

%package doc
Summary:	Documentation for OpenStack Identity Service
Group:		Documentation

%description doc
Keystone is a Python implementation of the OpenStack
(http://www.openstack.org) identity service API.

This package contains documentation for Keystone.

%prep
%setup -q

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1

find . \( -name .gitignore -o -name .placeholder \) -delete
find keystone -name \*.py -exec sed -i '/\/usr\/bin\/env python/d' {} \;


%build
cp etc/keystone.conf.sample etc/keystone.conf
%python_build

%install
%python_install

# Delete tests
rm -fr %{buildroot}%{python_sitelibdir}/tests
rm -fr %{buildroot}%{python_sitelibdir}/run_tests.*

install -d -m 755 %{buildroot}%{_sysconfdir}/keystone
install -p -D -m 640 etc/keystone.conf %{buildroot}%{_sysconfdir}/keystone/keystone.conf
install -p -D -m 640 etc/logging.conf.sample %{buildroot}%{_sysconfdir}/keystone/logging.conf
install -p -D -m 640 etc/default_catalog.templates %{buildroot}%{_sysconfdir}/keystone/default_catalog.templates
install -p -D -m 640 etc/policy.json %{buildroot}%{_sysconfdir}/keystone/policy.json
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -p -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
install -p -D -m 755 %{SOURCE3} %{buildroot}%{_initdir}/%{name}
# Install sample data script.
install -p -D -m 755 tools/sample_data.sh %{buildroot}%{_datadir}/%{name}/sample_data.sh
install -p -D -m 755 %{SOURCE5} %{buildroot}%{_bindir}/openstack-keystone-sample-data

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
# FIXME:
# 163:163 for keystone (openstack-keystone) - rhbz#752842
getent group keystone >/dev/null || groupadd -r --gid 163 keystone
getent passwd keystone >/dev/null || \
useradd --uid 163 -r -g keystone -d %{_sharedstatedir}/keystone -s /sbin/nologin \
-c "OpenStack Keystone Daemons" keystone
exit 0

%post
%post_service %{name}

%post -n python-module-keystone-auth-token
# workaround for rhbz 824034#c14
if [ ! -e %{python_sitelibdir}/keystone/__init__.py ]; then
    > %{python_sitelibdir}/keystone/__init__.py
fi
if [ ! -e %{python_sitelibdir}/keystone/middleware/__init__.py ]; then
    > %{python_sitelibdir}/keystone/middleware/__init__.py
fi

%triggerpostun -n python-module-keystone-auth-token -- python-module-keystone
# edge case: removing python-module-keystone with overlapping files
if [ $2 -eq 0 ] ; then
    # Package removal, not upgrade
    > %{python_sitelibdir}/keystone/__init__.py
    > %{python_sitelibdir}/keystone/middleware/__init__.py
fi

%preun
%preun_service %{name}

%files
%doc LICENSE
%doc README.rst
%{_mandir}/man1/keystone*.1.gz
%{_bindir}/keystone-all
%{_bindir}/keystone-manage
%{_bindir}/%{name}-sample-data
%{_datadir}/%{name}
%{_unitdir}/%{name}.service
%{_initdir}/%{name}
%dir %{_sysconfdir}/keystone
%config(noreplace) %attr(-, root, keystone) %{_sysconfdir}/keystone/keystone.conf
%config(noreplace) %attr(-, root, keystone) %{_sysconfdir}/keystone/logging.conf
%config(noreplace) %attr(-, root, keystone) %{_sysconfdir}/keystone/default_catalog.templates
%config(noreplace) %attr(-, keystone, keystone) %{_sysconfdir}/keystone/policy.json
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %attr(-, keystone, keystone) %{_sharedstatedir}/keystone
%dir %attr(-, keystone, keystone) %{_logdir}/keystone

%files -n python-module-keystone
%doc LICENSE
%{python_sitelibdir}/keystone
%exclude %{python_sitelibdir}/keystone/middleware/auth_token.py*
%{python_sitelibdir}/keystone-*.egg-info

%files -n python-module-keystone-auth-token
%doc LICENSE
%dir %{python_sitelibdir}/keystone
%ghost %{python_sitelibdir}/keystone/__init__.py
%dir %{python_sitelibdir}/keystone/middleware
%ghost %{python_sitelibdir}/keystone/middleware/__init__.py
%{python_sitelibdir}/keystone/middleware/auth_token.py*

%files doc
%doc LICENSE doc/build/html

%changelog
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
