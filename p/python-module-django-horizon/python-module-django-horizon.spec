%global with_compression 1

Name:       python-module-django-horizon
Version:    2014.1.1
Release:    alt1
Summary:    Django application for talking to Openstack

Group:      System/Servers
# Code in horizon/horizon/utils taken from django which is BSD
License:    ASL 2.0 and BSD
URL:        http://horizon.openstack.org/
Source0:    %{name}-%{version}.tar
Source1:    openstack-dashboard.conf
Source2:    openstack-dashboard-httpd-2.4.conf

# demo config for separate logging
Source4:    openstack-dashboard-httpd-logging.conf

# custom icons
Source10:   rhfavicon.ico
Source11:   rh-logo.png

#
# patches_base=2014.1.1
#
Patch0001: 0001-Don-t-access-the-net-while-building-docs.patch
Patch0002: 0002-disable-debug-move-web-root.patch
Patch0003: 0003-change-lockfile-location-to-tmp-and-also-add-localho.patch
Patch0004: 0004-Add-a-customization-module-based-on-RHOS.patch
Patch0005: 0005-move-RBAC-policy-files-and-checks-to-etc-openstack-d.patch
Patch0006: 0006-move-SECRET_KEY-secret_key_store-to-tmp.patch
Patch0007: 0007-RCUE-navbar-and-login-screen.patch
Patch0008: 0008-Added-a-hook-for-redhat-openstack-access-plugin.patch
Patch0009: 0009-fix-flake8-issues.patch
Patch0010: 0010-remove-runtime-dep-to-python-pbr.patch
Patch0011: 0011-Add-Change-password-link-to-the-RCUE-theme.patch
Patch0012: 0012-Re-enable-offline-compression.patch


BuildArch:  noarch

BuildRequires:   python-module-django
BuildRequires:   python-module-django-tests
BuildRequires:   python-module-greenlet
BuildRequires:   python-module-django-dbbackend-sqlite3
Requires:   python-module-django
Requires:   python-module-django-tests
Requires:   python-module-django-dbbackend-mysql

Requires:   python-module-dateutil
Requires:   python-module-pytz
Requires:   python-module-lockfile
Requires:   python-module-pbr

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-d2to1
BuildRequires: python-module-pbr >= 0.5.21
BuildRequires: python-module-lockfile
BuildRequires: python-module-eventlet

BuildRequires:   python-module-django-nose
BuildRequires:   python-module-coverage
BuildRequires:   python-module-mox
BuildRequires:   python-module-nose-exclude
BuildRequires:   python-module-nose
BuildRequires:   git

BuildRequires:   python-module-netaddr
BuildRequires:   python-module-kombu
BuildRequires:   python-module-anyjson
BuildRequires:   python-module-pytz
BuildRequires:   python-module-iso8601


# additional provides to be consistent with other django packages
Provides: django-horizon = %{version}-%{release}

%description
Horizon is a Django application for providing Openstack UI components.
It allows performing site administrator (viewing account resource usage,
configuring users, accounts, quotas, flavors, etc.) and end user
operations (start/stop/delete instances, create/restore snapshots, view
instance VNC console, etc.)


%package -n openstack-dashboard
Summary:    Openstack web user interface reference implementation
Group:      System/Servers

Requires:   apache2-base
Requires:   apache2-mod_wsgi
Requires:   python-module-django-horizon >= %{version}
Requires:   python-module-django-openstack-auth >= 1.1.3
Requires:   python-module-django-compressor >= 1.3
%if %{with_compression} > 0
Requires: python-module-lesscpy
%endif

Requires:   python-module-django-appconf
Requires:   python-module-glanceclient
Requires:   python-module-keystoneclient >= 0.3.2
Requires:   python-module-novaclient
Requires:   python-module-neutronclient
Requires:   python-module-cinderclient >= 1.0.6
Requires:   python-module-swiftclient
Requires:   python-module-heatclient
Requires:   python-module-ceilometerclient
Requires:   python-module-troveclient >= 1.0.0
Requires:   python-module-netaddr
Requires:   python-module-oslo-config
Requires:   python-module-eventlet

BuildRequires: python-devel
BuildRequires: python-module-django-openstack-auth >= 1.1.3
BuildRequires: python-module-django-compressor >= 1.3
BuildRequires: python-module-django-appconf
BuildRequires: python-module-lesscpy
BuildRequires: python-module-oslo-config

BuildRequires:   python-module-pytz
%description -n openstack-dashboard
Openstack Dashboard is a web user interface for Openstack. The package
provides a reference implementation using the Django Horizon project,
mostly consisting of JavaScript and CSS to tie it altogether as a standalone
site.


%package doc
Summary:    Documentation for Django Horizon
Group:      Documentation

Requires:   %{name} = %{version}-%{release}
BuildRequires: python-module-sphinx >= 1.1.3

# Doc building basically means we have to mirror Requires:
BuildRequires: python-module-dateutil
BuildRequires: python-module-glanceclient
BuildRequires: python-module-keystoneclient >= 0.3.2
BuildRequires: python-module-novaclient
BuildRequires: python-module-neutronclient
BuildRequires: python-module-cinderclient
BuildRequires: python-module-swiftclient
BuildRequires: python-module-heatclient
BuildRequires: python-module-ceilometerclient
BuildRequires: python-module-troveclient >= 1.0.0
BuildRequires: python-module-oslo-sphinx

%description doc
Documentation for the Django Horizon application for talking with Openstack

%package -n openstack-dashboard-theme
Summary: OpenStack web user interface reference implementation theme module
Group:   System/Servers
Requires: openstack-dashboard = %{version}

%description -n openstack-dashboard-theme
Customization module for OpenStack Dashboard to provide a branded logo.

%prep
%setup

# Use git to manage patches.
# http://rwmj.wordpress.com/2011/08/09/nice-rpm-git-patch-management-trick/
git init
git config user.email "python-django-horizon-owner@fedoraproject.org"
git config user.name "python-django-horizon"
git add .
git commit -a -q -m "%{version} baseline"
git am ../../SOURCES/0001-Don-t-access-the-net-while-building-docs.patch \
../../SOURCES/0002-disable-debug-move-web-root.patch \
../../SOURCES/0003-change-lockfile-location-to-tmp-and-also-add-localho.patch \
../../SOURCES/0004-Add-a-customization-module-based-on-RHOS.patch \
../../SOURCES/0005-move-RBAC-policy-files-and-checks-to-etc-openstack-d.patch \
../../SOURCES/0006-move-SECRET_KEY-secret_key_store-to-tmp.patch \
../../SOURCES/0007-RCUE-navbar-and-login-screen.patch \
../../SOURCES/0008-Added-a-hook-for-redhat-openstack-access-plugin.patch \
../../SOURCES/0009-fix-flake8-issues.patch \
../../SOURCES/0010-remove-runtime-dep-to-python-pbr.patch \
../../SOURCES/0011-Add-Change-password-link-to-the-RCUE-theme.patch \
../../SOURCES/0012-Re-enable-offline-compression.patch

# remove unnecessary .po files
find . -name "django*.po" -exec rm -f '{}' \;

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

# make doc build compatible with python-oslo-sphinx RPM
sed -i 's/oslosphinx/oslo.sphinx/' doc/source/conf.py

# create images for custom theme
mkdir -p openstack_dashboard_theme/static/dashboard/img
cp %{SOURCE10} openstack_dashboard_theme/static/dashboard/img
cp %{SOURCE11} openstack_dashboard_theme/static/dashboard/img

# drop config snippet
cp -p %{SOURCE4} .

%build
%python_build

# compress css, js etc.
cp openstack_dashboard/local/local_settings.py.example openstack_dashboard/local/local_settings.py
# dirty hack to make SECRET_KEY work:
sed -i 's:^SECRET_KEY =.*:SECRET_KEY = "badcafe":' openstack_dashboard/local/local_settings.py

%if %{with_compression} > 0
%{__python} manage.py collectstatic --noinput
%{__python} manage.py compress
cp -a static/dashboard $RPM_BUILD_ROOT
%else
sed -i 's:COMPRESS_OFFLINE = True:COMPRESS_OFFLINE = False:' openstack_dashboard/settings.py
%endif

# build docs
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# undo hack
cp openstack_dashboard/local/local_settings.py.example openstack_dashboard/local/local_settings.py

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%install
%python_install

# drop httpd-conf snippet
install -m 0644 -D -p %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd2/conf/extra-available/openstack-dashboard.conf
install -d -m 755 %{buildroot}%{_sysconfdir}/httpd2/conf/extra-enabled
ln -s %{_sysconfdir}/httpd2/conf/extra-available/openstack-dashboard.conf %{buildroot}%{_sysconfdir}/httpd2/conf/extra-enabled/openstack-dashboard.conf

# httpd-2.4 changed the syntax
# install -m 0644 -D -p %{SOURCE2} %{buildroot}%{_sysconfdir}/httpd/conf.d/openstack-dashboard.conf

install -d -m 755 %{buildroot}%{_datadir}/openstack-dashboard
install -d -m 755 %{buildroot}%{_sharedstatedir}/openstack-dashboard
install -d -m 755 %{buildroot}%{_sysconfdir}/openstack-dashboard

# Copy everything to /usr/share
mv %{buildroot}%{python_sitelibdir}/openstack_dashboard \
   %{buildroot}%{_datadir}/openstack-dashboard
cp manage.py %{buildroot}%{_datadir}/openstack-dashboard
rm -rf %{buildroot}%{python_sitelibdir}/openstack_dashboard

# move customization stuff to /usr/share
mv openstack_dashboard_theme %{buildroot}%{_datadir}/openstack-dashboard

# Move config to /etc, symlink it back to /usr/share
mv %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/local_settings.py.example %{buildroot}%{_sysconfdir}/openstack-dashboard/local_settings
ln -s ../../../../../%{_sysconfdir}/openstack-dashboard/local_settings %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/local_settings.py

mv %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/conf/*.json %{buildroot}%{_sysconfdir}/openstack-dashboard

%find_lang django
%find_lang djangojs

grep "\/usr\/share\/openstack-dashboard" django.lang > dashboard.lang
grep "\/site-packages\/horizon" django.lang > horizon.lang

cat djangojs.lang >> horizon.lang

# copy static files to %{_datadir}/openstack-dashboard/static
mkdir -p %{buildroot}%{_datadir}/openstack-dashboard/static
cp -a openstack_dashboard/static/* %{buildroot}%{_datadir}/openstack-dashboard/static
cp -a horizon/static/* %{buildroot}%{_datadir}/openstack-dashboard/static
cp -a static/* %{buildroot}%{_datadir}/openstack-dashboard/static

# create /var/run/openstack-dashboard/ and own it
mkdir -p %{buildroot}%{_sharedstatedir}/openstack-dashboard

# create /var/log/horizon and own it
mkdir -p %{buildroot}%{_var}/log/horizon


%check
sed -i 's:^SECRET_KEY =.*:SECRET_KEY = "badcafe":' openstack_dashboard/local/local_settings.py
./run_tests.sh -N -P

%files -f horizon.lang
%doc LICENSE README.rst openstack-dashboard-httpd-logging.conf
%dir %{python_sitelibdir}/horizon
%{python_sitelibdir}/horizon/*.py*
%{python_sitelibdir}/horizon/browsers
%{python_sitelibdir}/horizon/conf
%{python_sitelibdir}/horizon/forms
%{python_sitelibdir}/horizon/management
%{python_sitelibdir}/horizon/static
%{python_sitelibdir}/horizon/tables
%{python_sitelibdir}/horizon/tabs
%{python_sitelibdir}/horizon/templates
%{python_sitelibdir}/horizon/templatetags
%{python_sitelibdir}/horizon/test
%{python_sitelibdir}/horizon/utils
%{python_sitelibdir}/horizon/workflows
%dir %{python_sitelibdir}/horizon/locale/
%dir %{python_sitelibdir}/horizon/locale/*/
%dir %{python_sitelibdir}/horizon/locale/*/LC_MESSAGES/
%{python_sitelibdir}/*.egg-info

%files -n openstack-dashboard -f dashboard.lang
%dir %{_datadir}/openstack-dashboard/
%{_datadir}/openstack-dashboard/*.py*
%{_datadir}/openstack-dashboard/static
%{_datadir}/openstack-dashboard/openstack_dashboard/*.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/api
%{_datadir}/openstack-dashboard/openstack_dashboard/dashboards
%{_datadir}/openstack-dashboard/openstack_dashboard/enabled
%{_datadir}/openstack-dashboard/openstack_dashboard/local
%{_datadir}/openstack-dashboard/openstack_dashboard/openstack
%{_datadir}/openstack-dashboard/openstack_dashboard/static
%{_datadir}/openstack-dashboard/openstack_dashboard/templates
%{_datadir}/openstack-dashboard/openstack_dashboard/test
%{_datadir}/openstack-dashboard/openstack_dashboard/usage
%{_datadir}/openstack-dashboard/openstack_dashboard/utils
%{_datadir}/openstack-dashboard/openstack_dashboard/wsgi
%dir %{_datadir}/openstack-dashboard/openstack_dashboard
%dir %{_datadir}/openstack-dashboard/openstack_dashboard/locale
%dir %{_datadir}/openstack-dashboard/openstack_dashboard/locale/??
%dir %{_datadir}/openstack-dashboard/openstack_dashboard/locale/??_??
%dir %{_datadir}/openstack-dashboard/openstack_dashboard/locale/??/LC_MESSAGES
%dir %{_datadir}/openstack-dashboard/openstack_dashboard/locale/??_??/LC_MESSAGES

%dir %attr(0750, root, apache2) %{_sysconfdir}/openstack-dashboard
%dir %attr(0750, apache2, apache2) %{_sharedstatedir}/openstack-dashboard
%dir %attr(0750, apache2, apache2) %{_var}/log/horizon
%config(noreplace) %{_sysconfdir}/httpd2/conf/extra-available/openstack-dashboard.conf
%config(noreplace) %{_sysconfdir}/httpd2/conf/extra-enabled/openstack-dashboard.conf
%config(noreplace) %attr(0640, root, apache2) %{_sysconfdir}/openstack-dashboard/local_settings
%config(noreplace) %attr(0640, root, apache2) %{_sysconfdir}/openstack-dashboard/keystone_policy.json
%config(noreplace) %attr(0640, root, apache2) %{_sysconfdir}/openstack-dashboard/cinder_policy.json
%config(noreplace) %attr(0640, root, apache2) %{_sysconfdir}/openstack-dashboard/glance_policy.json
%config(noreplace) %attr(0640, root, apache2) %{_sysconfdir}/openstack-dashboard/nova_policy.json

%files doc
%doc html

%files -n openstack-dashboard-theme
%{_datadir}/openstack-dashboard/openstack_dashboard_theme

%changelog
* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt1
- New version (based on Fedora 2014.1.1-1.fc20.src)

* Mon Aug 26 2013 Vitaly Lipatov <lav@altlinux.ru> 2012.2.3-alt2
- cleanup spec, fix groups
- build with django 1.4.x

* Mon Jul 15 2013 Pavel Shilovsky <piastry@altlinux.org> 2012.2.3-alt1
- Initial release for Sisyphus (based on Fedora)
