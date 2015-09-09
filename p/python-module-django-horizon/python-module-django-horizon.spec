%add_findreq_skiplist %_datadir/openstack-dashboard/openstack_dashboard/management/commands/horizon.wsgi.template

%global with_compression 1

Name: python-module-django-horizon
Version: 2015.1.1
Release: alt1
Summary: Django application for talking to Openstack

Group: System/Servers
# Code in horizon/horizon/utils taken from django which is BSD
License: ASL 2.0 and BSD
Url: http://horizon.openstack.org/
Source0: %name-%version.tar
Source1: openstack-dashboard-httpd-2.2.conf

Patch0001: 0001-disable-debug-move-web-root.patch
Patch0002: 0002-remove-runtime-dep-to-python-pbr.patch
Patch0004: 0004-Configurable-token-hashing.patch
Patch0005: 0005-Do-not-call-_assertNotContains-override-in-Django-ne.patch
Patch0006: 0006-Use-charset-instead-of-_charset-for-dj18-response.patch
Patch0007: 0007-Don-t-escape-request.get_full_path-in-Django1.8.patch
Patch0008: 0008-Remove-un-related-nova-quota-in-test-data.patch
Patch0009: 0009-Compatibility-fix-for-pyscss-1.3.4.patch
Patch1011: 0001-Do-not-load-jasmine-without-DEBUG-setting.patch

Source2: openstack-dashboard-httpd-2.4.conf

# systemd snippet to collect static files and compress on httpd restart
Source3:    python-django-horizon-systemd.conf

# demo config for separate logging
Source4: openstack-dashboard-httpd-logging.conf

# logrotate config
Source5:    python-django-horizon-logrotate.conf

BuildArch: noarch

# additional provides to be consistent with other django packages
Provides: django-horizon = %version-%release

Requires: python-module-django
Requires: python-module-django-openstack-auth >= 1.1.7
Requires: python-module-django-compressor >= 1.5
Requires: python-module-django-appconf
Requires: python-module-django-pyscss >= 2.0.2

Requires: python-module-lesscpy
Requires: python-module-glanceclient >= 0.15.0
Requires: python-module-keystoneclient >= 1.1.0
Requires: python-module-novaclient >= 2.18.0
Requires: python-module-neutronclient >= 2.3.11
Requires: python-module-cinderclient >= 1.1.0
Requires: python-module-swiftclient >= 2.2.0
Requires: python-module-heatclient >= 0.3.0
Requires: python-module-ceilometerclient >= 1.0.6
Requires: python-module-troveclient >= 1.0.7
Requires: python-module-saharaclient >= 0.7.6
Requires: python-module-selenium

Requires: python-module-netaddr
Requires: python-module-kombu
Requires: python-module-anyjson
Requires: python-module-iso8601
Requires: python-module-oslo.concurrency >= 1.4.1
Requires: python-module-oslo.config >= 1.9.0
Requires: python-module-oslo.i18n >= 1.3.0
Requires: python-module-oslo.serialization >= 1.2.0
Requires: python-module-oslo.utils >= 1.2.0

Requires: python-module-glanceclient >= 0.15.0
Requires: python-module-keystoneclient >= 1.0.0
Requires: python-module-novaclient >= 2.18.0
Requires: python-module-neutronclient >= 2.3.6
Requires: python-module-cinderclient >= 1.1.0
Requires: python-module-swiftclient >= 2.2.0
Requires: python-module-heatclient >= 0.2.9
Requires: python-module-ceilometerclient >= 1.0.6
Requires: python-module-troveclient >= 1.0.7
Requires: python-module-saharaclient >= 0.7.6

Requires: python-module-xstatic
Requires: python-module-xstatic-angular
Requires: python-module-xstatic-angular-bootstrap
Requires: python-module-xstatic-irdragndrop
Requires: python-module-xstatic-bootstrap-scss
Requires: python-module-xstatic-bootstrap-datepicker
Requires: python-module-xstatic-d3
Requires: python-module-xstatic-font-awesome
Requires: python-module-xstatic-hogan
Requires: python-module-xstatic-jquery
Requires: python-module-xstatic-jquery-ui
Requires: python-module-xstatic-jquery-migrate
Requires: python-module-xstatic-jquery.quicksearch
Requires: python-module-xstatic-jquery.tablesorter
Requires: python-module-xstatic-jsencrypt
Requires: python-module-xstatic-jasmine
Requires: python-module-xstatic-qunit
Requires: python-module-xstatic-rickshaw
Requires: python-module-xstatic-spin
Requires: python-module-xstatic-smart-table
Requires: python-module-xstatic-term.js
Requires: python-module-xstatic-angular-lrdragndrop
Requires: python-module-xstatic-magic-search

Requires: openssl
Requires: logrotate

BuildRequires: python-module-django
BuildRequires: python-module-django-tests
BuildRequires: python-module-greenlet
BuildRequires: python-module-django-dbbackend-sqlite3
BuildRequires: python-module-django-openstack-auth >= 1.1.7
BuildRequires: python-module-django-compressor >= 1.4
BuildRequires: python-module-django-appconf
BuildRequires: python-module-django-pyscss

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-d2to1
BuildRequires: python-module-pbr >= 0.7.0
BuildRequires: python-module-eventlet
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-django-nose
BuildRequires: python-module-coverage
BuildRequires: python-module-mox
BuildRequires: python-module-nose-exclude
BuildRequires: python-module-nose
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx

BuildRequires: python-module-netaddr
BuildRequires: python-module-kombu
BuildRequires: python-module-anyjson
BuildRequires: python-module-iso8601
BuildRequires: python-module-oslo.concurrency >= 1.4.1
BuildRequires: python-module-oslo.config >= 1.9.0
BuildRequires: python-module-oslo.i18n >= 1.3.0
BuildRequires: python-module-oslo.serialization >= 1.2.0
BuildRequires: python-module-oslo.utils >= 1.2.0

BuildRequires: python-module-glanceclient >= 0.15.0
BuildRequires: python-module-keystoneclient >= 1.1.0
BuildRequires: python-module-novaclient >= 2.18.0
BuildRequires: python-module-neutronclient >= 2.3.11
BuildRequires: python-module-cinderclient >= 1.1.0
BuildRequires: python-module-swiftclient >= 2.2.0
BuildRequires: python-module-heatclient >= 0.3.0
BuildRequires: python-module-ceilometerclient >= 1.0.6
BuildRequires: python-module-troveclient >= 1.0.7
BuildRequires: python-module-saharaclient >= 0.7.6

BuildRequires: python-module-pytz
BuildRequires: python-module-pint

BuildRequires: python-module-xstatic
BuildRequires: python-module-xstatic-angular
BuildRequires: python-module-xstatic-angular-bootstrap
BuildRequires: python-module-xstatic-irdragndrop
BuildRequires: python-module-xstatic-bootstrap-scss
BuildRequires: python-module-xstatic-bootstrap-datepicker
BuildRequires: python-module-xstatic-d3
BuildRequires: python-module-xstatic-font-awesome
BuildRequires: python-module-xstatic-hogan
BuildRequires: python-module-xstatic-jquery
BuildRequires: python-module-xstatic-jquery-ui
BuildRequires: python-module-xstatic-jquery-migrate
BuildRequires: python-module-xstatic-jquery.quicksearch
BuildRequires: python-module-xstatic-jquery.tablesorter
BuildRequires: python-module-xstatic-jsencrypt
BuildRequires: python-module-xstatic-jasmine
BuildRequires: python-module-xstatic-qunit
BuildRequires: python-module-xstatic-rickshaw
BuildRequires: python-module-xstatic-spin
BuildRequires: python-module-xstatic-smart-table
BuildRequires: python-module-xstatic-term.js
BuildRequires: python-module-xstatic-angular-lrdragndrop
BuildRequires: python-module-xstatic-magic-search

BuildRequires: git

%description
Horizon is a Django application for providing Openstack UI components.
It allows performing site administrator (viewing account resource usage,
configuring users, accounts, quotas, flavors, etc.) and end user
operations (start/stop/delete instances, create/restore snapshots, view
instance VNC console, etc.)

%package -n openstack-dashboard
Summary: Openstack web user interface reference implementation
Group: System/Servers

%py_provides openstack_dashboard

Provides: openstack-dashboard-branding-upstream = %version-%release
Provides: openstack-dashboard-theme = %version-%release
Obsoletes: openstack-dashboard-theme < %version-%release

Requires: apache2-base
Requires: apache2-mod_wsgi
Requires: python-module-django-horizon = %version-%release


%description -n openstack-dashboard
Openstack Dashboard is a web user interface for Openstack. The package
provides a reference implementation using the Django Horizon project,
mostly consisting of JavaScript and CSS to tie it altogether as a standalone
site.

%package doc
Summary: Documentation for Django Horizon
Group: Development/Documentation

%description doc
Documentation for the Django Horizon application for talking with Openstack

%prep
%setup

%patch0001 -p1
%patch0002 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1
%patch0009 -p1
%patch1011 -p1

# remove precompiled egg-info
rm -rf horizon.egg-info

git init
git config user.email "python-django-horizon-owner@fedoraproject.org"
git config user.name "python-django-horizon"
git add .
git commit -a -q -m "%{version} baseline"

# remove unnecessary .mo files
# they will be generated later during package build
find . -name "django*.mo" -exec rm -f '{}' \;

sed -i s/REDHATVERSION/%version/ horizon/version.py
sed -i s/REDHATRELEASE/%release/ horizon/version.py

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

# drop config snippet
cp -p %SOURCE4 .

%if 0%{?with_compression} > 0
# set COMPRESS_OFFLINE=True
sed -i 's:COMPRESS_OFFLINE.=.False:COMPRESS_OFFLINE = True:' openstack_dashboard/settings.py
%else
# set COMPRESS_OFFLINE=False
sed -i 's:COMPRESS_OFFLINE = True:COMPRESS_OFFLINE = False:' openstack_dashboard/settings.py
%endif

%build
# compile message strings
cd horizon && django-admin compilemessages && cd ..
cd openstack_dashboard && django-admin compilemessages && cd ..
%python_build

# compress css, js etc.
cp openstack_dashboard/local/local_settings.py.example openstack_dashboard/local/local_settings.py
# get it ready for compressing later in puppet-horizon
python manage.py collectstatic --noinput
python manage.py compress --force

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
install -m 0644 -D -p %SOURCE1 %buildroot%_sysconfdir/httpd2/conf/extra-available/openstack-dashboard.conf
install -d -m 755 %buildroot%_sysconfdir/httpd2/conf/extra-enabled
ln -s %_sysconfdir/httpd2/conf/extra-available/openstack-dashboard.conf %buildroot%_sysconfdir/httpd2/conf/extra-enabled/openstack-dashboard.conf

# httpd-2.4 changed the syntax
# install -m 0644 -D -p %SOURCE2 %buildroot%_sysconfdir/httpd/conf.d/openstack-dashboard.conf

install -d -m 755 %buildroot%_datadir/openstack-dashboard
install -d -m 755 %buildroot%_sharedstatedir/openstack-dashboard
install -d -m 755 %buildroot%_sysconfdir/openstack-dashboard

# create directory for systemd snippet
mkdir -p %buildroot%_unitdir/httpd.service.d/
cp %SOURCE3 %buildroot%_unitdir/httpd.service.d/openstack-dashboard.conf

# Copy everything to /usr/share
mv %buildroot%python_sitelibdir/openstack_dashboard \
   %buildroot%_datadir/openstack-dashboard
cp manage.py %buildroot%_datadir/openstack-dashboard
rm -rf %buildroot%python_sitelibdir/openstack_dashboard

# remove unnecessary .po files
find %buildroot -name django.po -exec rm '{}' \;
find %buildroot -name djangojs.po -exec rm '{}' \;

# Move config to /etc, symlink it back to /usr/share
mv %buildroot%_datadir/openstack-dashboard/openstack_dashboard/local/local_settings.py.example %buildroot%_sysconfdir/openstack-dashboard/local_settings
ln -s ../../../../../%_sysconfdir/openstack-dashboard/local_settings %buildroot%_datadir/openstack-dashboard/openstack_dashboard/local/local_settings.py

mv %buildroot%_datadir/openstack-dashboard/openstack_dashboard/conf/*.json %buildroot%_sysconfdir/openstack-dashboard

%find_lang django
%find_lang djangojs

grep "\/usr\/share\/openstack-dashboard" django.lang > dashboard.lang
grep "\/site-packages\/horizon" django.lang > horizon.lang

cat djangojs.lang >> horizon.lang

# copy static files to %_datadir/openstack-dashboard/static
mkdir -p %buildroot%_datadir/openstack-dashboard/static
cp -a openstack_dashboard/static/* %buildroot%_datadir/openstack-dashboard/static
cp -a horizon/static/* %buildroot%_datadir/openstack-dashboard/static
cp -a static/* %buildroot%_datadir/openstack-dashboard/static

# create /var/run/openstack-dashboard/ and own it
mkdir -p %buildroot%_sharedstatedir/openstack-dashboard

# create /var/log/horizon and own it
mkdir -p %buildroot%_var/log/horizon

# place logrotate config:
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
cp -a %{SOURCE5} %{buildroot}%{_sysconfdir}/logrotate.d/openstack-dashboard

%post -n openstack-dashboard
# ugly hack to set a unique SECRET_KEY
sed -i "/^from horizon.utils import secret_key$/d" /etc/openstack-dashboard/local_settings
sed -i "/^SECRET_KEY.*$/{N;s/^.*$/SECRET_KEY='`openssl rand -hex 10`'/}" /etc/openstack-dashboard/local_settings

%files -f horizon.lang
%doc LICENSE README.rst openstack-dashboard-httpd-logging.conf
%python_sitelibdir/horizon
%python_sitelibdir/*.egg-info

%files -n openstack-dashboard -f dashboard.lang
%dir %_datadir/openstack-dashboard
%{_datadir}/openstack-dashboard/*.py*
%{_datadir}/openstack-dashboard/static
%{_datadir}/openstack-dashboard/openstack_dashboard/*.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/api
%dir %{_datadir}/openstack-dashboard/openstack_dashboard/dashboards/
%{_datadir}/openstack-dashboard/openstack_dashboard/dashboards/admin
%{_datadir}/openstack-dashboard/openstack_dashboard/dashboards/identity
%{_datadir}/openstack-dashboard/openstack_dashboard/dashboards/project
%{_datadir}/openstack-dashboard/openstack_dashboard/dashboards/router
%{_datadir}/openstack-dashboard/openstack_dashboard/dashboards/settings
%{_datadir}/openstack-dashboard/openstack_dashboard/dashboards/__init__.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/django_pyscss_fix
%{_datadir}/openstack-dashboard/openstack_dashboard/enabled
%{_datadir}/openstack-dashboard/openstack_dashboard/local
%{_datadir}/openstack-dashboard/openstack_dashboard/management
%{_datadir}/openstack-dashboard/openstack_dashboard/openstack
%{_datadir}/openstack-dashboard/openstack_dashboard/static
%{_datadir}/openstack-dashboard/openstack_dashboard/templates
%{_datadir}/openstack-dashboard/openstack_dashboard/templatetags
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

%dir %attr(0750, root, apache2) %_sysconfdir/openstack-dashboard
%dir %attr(0750, apache2, apache2) %_sharedstatedir/openstack-dashboard
%dir %attr(0750, apache2, apache2) %_var/log/horizon
%config(noreplace) %_sysconfdir/httpd2/conf/extra-available/openstack-dashboard.conf
%config(noreplace) %_sysconfdir/httpd2/conf/extra-enabled/openstack-dashboard.conf
%config(noreplace) %attr(0640, root, apache2) %_sysconfdir/openstack-dashboard/local_settings
%config(noreplace) %attr(0640, root, apache2) %_sysconfdir/openstack-dashboard/ceilometer_policy.json
%config(noreplace) %attr(0640, root, apache2) %_sysconfdir/openstack-dashboard/cinder_policy.json
%config(noreplace) %attr(0640, root, apache2) %_sysconfdir/openstack-dashboard/keystone_policy.json
%config(noreplace) %attr(0640, root, apache2) %_sysconfdir/openstack-dashboard/nova_policy.json
%config(noreplace) %attr(0640, root, apache2) %_sysconfdir/openstack-dashboard/glance_policy.json
%config(noreplace) %attr(0640, root, apache2) %_sysconfdir/openstack-dashboard/neutron_policy.json
%config(noreplace) %attr(0640, root, apache2) %_sysconfdir/openstack-dashboard/heat_policy.json
%_sysconfdir/logrotate.d/openstack-dashboard
%attr(755,root,root) %dir %_unitdir/httpd.service.d
%config(noreplace) %_unitdir/httpd.service.d/openstack-dashboard.conf

%files doc
%doc html

%changelog
* Wed Sep 09 2015 Lenar Shakirov <snejok@altlinux.ru> 2015.1.1-alt1
- 2015.1.1-alt1

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b3.0
- 2015.1.0b3

* Tue Mar 17 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b2.0
- 2015.1.0b2

* Sun Sep 07 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.2-alt2
- Tests disabled temporary
- 0101-Add-ru-locale-horizon.patch updated
- 0102-CVE-2014-3594.patch added
- AutoReq: yes, nopython for theme subpackage

* Mon Aug 25 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.2-alt1
- 2014.1.2

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt3
- 0101-Add-ru-locale-horizon.patch added

* Wed Aug 06 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt2
- openstack-dashboard.conf: allow /usr/share/openstack-dashboard/static

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt1
- New version (based on Fedora 2014.1.1-1.fc20.src)

* Mon Aug 26 2013 Vitaly Lipatov <lav@altlinux.ru> 2012.2.3-alt2
- cleanup spec, fix groups
- build with django 1.4.x

* Mon Jul 15 2013 Pavel Shilovsky <piastry@altlinux.org> 2012.2.3-alt1
- Initial release for Sisyphus (based on Fedora)
