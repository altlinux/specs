Name:		python-module-django-horizon
Version:	2012.2.3
Release:	alt2

Summary:	Django application for talking to Openstack

Group:		System/Servers
# Code in horizon/horizon/utils taken from django which is BSD
License:	ASL 2.0 and BSD
URL:		http://horizon.openstack.org/
BuildArch:	noarch

Source0:	%name-%version.tar
Source1:	openstack-dashboard.conf

#
# patches_base=2012.2.3+1
#
Patch0001:	0001-disable-debug-move-web-root.patch
Patch0002:	0002-take-variables-out-of-compressed-output.patch

Requires:	python-module-django1.4

Requires:	python-module-dateutil
Requires:	python-module-glanceclient
Requires:	python-module-keystoneclient
Requires:	python-module-novaclient
Requires:	python-module-quantumclient
Requires:	python-module-cinderclient
Requires:	python-module-swiftclient
Requires:	python-module-netaddr
Requires:	python-module-pytz

BuildRequires:	python-devel
BuildRequires:	python-module-distribute

# additional provides to be consistent with other django packages
Provides:	django-horizon = %version-%release

%description
Horizon is a Django application for providing Openstack UI components.
It allows performing site administrator (viewing account resource usage,
configuring users, accounts, quotas, flavors, etc.) and end user
operations (start/stop/delete instances, create/restore snapshots, view
instance VNC console, etc.)

%package -n openstack-dashboard
Summary:	Openstack web user interface reference implementation
Group:		System/Servers

Requires:	apache2-base
Requires:	apache2-mod_wsgi
Requires:	python-module-django-horizon >= %version
Requires:	python-module-django-openstack-auth
Requires:	python-module-django-compressor

BuildRequires:	python-devel
# required for building compressed css, js
BuildRequires:	node
BuildRequires:	lessjs
BuildRequires:	python-module-django1.4
BuildRequires:	python-module-django-openstack-auth
BuildRequires:	python-module-django-compressor

Provides:	python2.7(openstack_dashboard)

%description -n openstack-dashboard
Openstack Dashboard is a web user interface for Openstack. The package
provides a reference implementation using the Django Horizon project,
mostly consisting of JavaScript and CSS to tie it altogether as a
standalone site.

%package doc
Summary:	Documentation for Django Horizon
Group:		Documentation

Requires:	%name = %version-%release
BuildRequires:	python-module-sphinx >= 1.1.3

# Doc building basically means we have to mirror Requires:
BuildRequires:	python-module-dateutil
BuildRequires:	python-module-glanceclient
BuildRequires:	python-module-keystoneclient
BuildRequires:	python-module-novaclient
BuildRequires:	python-module-quantumclient
BuildRequires:	python-module-cinderclient
BuildRequires:	python-module-swiftclient
BuildRequires:	python-module-objects.inv

%description doc
Documentation for the Django Horizon application for talking with
Openstack.

%prep
%setup

%patch0001 -p1
%patch0002 -p1
# remove unnecessary .po files
find . -name "django*.po" -exec rm -f '{}' \;

# patch settings
# disable debug also in local_settings.py

# correct compressed output

# move dashboard login/logout to /dashboard

%build
%python_build

%install
%python_install

# do not include tests due to their dependence of python selenium module with precompiled binaries
rm -rf %buildroot%python_sitelibdir/horizon/test*

install -m 0644 -D -p %SOURCE1 %buildroot%_sysconfdir/httpd2/conf/extra-available/openstack-dashboard.conf
install -d -m 755 %buildroot%_sysconfdir/httpd2/conf/extra-enabled
ln -s %_sysconfdir/httpd2/conf/extra-available/openstack-dashboard.conf %buildroot%_sysconfdir/httpd2/conf/extra-enabled/openstack-dashboard.conf

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

install -d -m 755 %buildroot%_datadir/openstack-dashboard
install -d -m 755 %buildroot%_sharedstatedir/openstack-dashboard
install -d -m 755 %buildroot%_sysconfdir/openstack-dashboard

# Copy everything to /usr/share
mv %buildroot%python_sitelibdir/openstack_dashboard \
%buildroot%_datadir/openstack-dashboard
mv manage.py %buildroot%_datadir/openstack-dashboard
rm -rf %buildroot%python_sitelibdir/openstack_dashboard

# Move config to /etc, symlink it back to /usr/share
mv %buildroot%_datadir/openstack-dashboard/openstack_dashboard/local/local_settings.py.example %buildroot%_sysconfdir/openstack-dashboard/local_settings
ln -s %_sysconfdir/openstack-dashboard/local_settings %buildroot%_datadir/openstack-dashboard/openstack_dashboard/local/local_settings.py

%find_lang django
%find_lang djangojs

grep "\/usr\/share\/openstack-dashboard" django.lang > dashboard.lang
grep "\/site-packages\/horizon" django.lang > horizon.lang

cat djangojs.lang >> horizon.lang

# copy static files to %_datadir/openstack-dashboard/static
mkdir -p %buildroot%_datadir/openstack-dashboard/static
cp -a openstack_dashboard/static/* %buildroot%_datadir/openstack-dashboard/static
cp -a horizon/static/* %buildroot%_datadir/openstack-dashboard/static

# finally put compressed js, css to the right place, and also manifest.json
cd %buildroot%_datadir/openstack-dashboard
%__python manage.py collectstatic --noinput --pythonpath=../../lib/python2.7/site-packages/
%__python manage.py compress --pythonpath=../../lib/python2.7/site-packages/

%files -f horizon.lang
%dir %python_sitelibdir/horizon/
%python_sitelibdir/horizon/*.py*
%python_sitelibdir/horizon/api
%python_sitelibdir/horizon/browsers
%python_sitelibdir/horizon/conf
%python_sitelibdir/horizon/dashboards
%python_sitelibdir/horizon/forms
%python_sitelibdir/horizon/management
%python_sitelibdir/horizon/openstack
%python_sitelibdir/horizon/static
%python_sitelibdir/horizon/tables
%python_sitelibdir/horizon/tabs
%python_sitelibdir/horizon/templates
%python_sitelibdir/horizon/templatetags
%python_sitelibdir/horizon/usage
%python_sitelibdir/horizon/utils
%python_sitelibdir/horizon/views
%python_sitelibdir/horizon/workflows
%dir %python_sitelibdir/horizon/locale/
%dir %python_sitelibdir/horizon/locale/*/
%dir %python_sitelibdir/horizon/locale/*/LC_MESSAGES/
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/bin

%files -n openstack-dashboard -f dashboard.lang
%dir %_datadir/openstack-dashboard/
%_datadir/openstack-dashboard/*.py*
%_datadir/openstack-dashboard/static/
%dir %_datadir/openstack-dashboard/openstack_dashboard/
%_datadir/openstack-dashboard/openstack_dashboard/*.py*
%_datadir/openstack-dashboard/openstack_dashboard/local/
%_datadir/openstack-dashboard/openstack_dashboard/static/
%_datadir/openstack-dashboard/openstack_dashboard/templates/
%_datadir/openstack-dashboard/openstack_dashboard/test/
%_datadir/openstack-dashboard/openstack_dashboard/wsgi/
%dir %_datadir/openstack-dashboard/openstack_dashboard/locale/
%dir %_datadir/openstack-dashboard/openstack_dashboard/locale/*/
%dir %_datadir/openstack-dashboard/openstack_dashboard/locale/*/LC_MESSAGES/
%_sharedstatedir/openstack-dashboard/
%dir %attr(0750, root, apache2) %_sysconfdir/openstack-dashboard
%config(noreplace) %attr(0640, root, apache2) %_sysconfdir/openstack-dashboard/local_settings
%config(noreplace) %_sysconfdir/httpd2/conf/extra-available/openstack-dashboard.conf
%config(noreplace) %_sysconfdir/httpd2/conf/extra-enabled/openstack-dashboard.conf

%files doc
%doc html

%changelog
* Mon Aug 26 2013 Vitaly Lipatov <lav@altlinux.ru> 2012.2.3-alt2
- cleanup spec, fix groups
- build with django 1.4.x

* Mon Jul 15 2013 Pavel Shilovsky <piastry@altlinux.org> 2012.2.3-alt1
- Initial release for Sisyphus (based on Fedora)
