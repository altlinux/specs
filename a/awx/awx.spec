%def_without check

Name: awx
Version: 24.6.1
Release: alt7

Summary: The official command line interface for Ansible AWX
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/ansible/awx

#ExclusiveArch: x86_64
BuildArch: noarch

Source: %name-%version.tar
Source1: node_modules.tar
Source2: awx.conf
Source3: 0196_oauth2_toolkit_v3_fields.py
Source4: supervisord.conf
Source5: receptor.conf
Source6: awx.service
Source7: redis_settings.py
Patch0: reimplementation_of_strtobool_function.patch
Patch1: replace_distutils_version.patch
Patch2: awx-disable-aioredis.patch
Patch3: awx-disable-asciichartpy.patch
Patch4: awx-remove-hardcoded-pg_version-check.patch
Patch5: awx-use-chunk_size.patch
Patch6: awx-default-settings.patch
Patch7: remove-old-django-attribute.patch
Patch8: fix-migrations-for-sqlite.patch
Patch9: new-attribute-for-psycopg.patch
Patch10: replace-old-python-attribute.patch
Patch11: redis-py-with-unix-socket.patch


BuildRequires(pre): rpm-macros-webserver-common
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-apache2
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
BuildRequires: npm

Requires: python3-module-logutils
Requires: python3-module-colorama
Requires: python3-module-django-extensions
Requires: python3-module-django-cors-headers
Requires: python3-module-django-debug-toolbar
Requires: python3-module-django-dbbackend-postgresql
Requires: python3-module-python-tss-sdk
Requires: redis
Requires: python3-module-channels_redis
Requires: supervisor
Requires: receptor
Requires: python3-module-receptorctl
Requires: uwsgi
Requires: apache2-mod_wsgi-py3

%add_python3_req_skip defaults development

%description
AWX provides a web-based user interface, REST API, and task engine built on top
of Ansible. It is one of the upstream projects for Red Hat Ansible Automation
Platform.

%package apache2
Summary: AWX configuration for Apache2
Group: System/Servers
Requires: %name = %EVR
Requires: apache2-mod_wsgi-py3
Requires: apache2-mod_ssl

%description apache2
AWX configuration for Apache2

%prep
%setup
tar xf %SOURCE1
%autopatch -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build
make ui-release

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install
rm -r %buildroot%python3_sitelibdir/%name/ui/{src,node_modules}
cp -a awx/ui/public %buildroot%python3_sitelibdir/%name/ui

mkdir -p %buildroot%_sharedstatedir/awx/{public/static,projects,job_status,venv}
mkdir -p %buildroot%_logdir/tower

cp -a awx/ui/build/* %buildroot%python3_sitelibdir/%name/
rm -rf %buildroot%python3_sitelibdir/awx/ui/node_modules

# Install default settings
install -Dpm0644 awx/settings/defaults.py %buildroot%_sysconfdir/tower/settings.py

# Remove development environment flag
rm -f %buildroot%python3_sitelibdir/%name/devonly.py

# Apache2 configuration
install -Dm0644 -p %SOURCE2 %buildroot%apache2_sites_available/awx.conf
mkdir -p %buildroot%apache2_sites_enabled
touch %buildroot%apache2_sites_enabled/awx.conf

# Uwsgi configuration
cp tools/ansible/roles/dockerfile/files/uwsgi.ini %buildroot%_sysconfdir/tower/uwsgi.ini

# Secret key generation
openssl rand -base64 32 > %buildroot%_sysconfdir/tower/SECRET_KEY
chmod 600 %buildroot%_sysconfdir/tower/SECRET_KEY

# Migration for the new version of django-tookit
install -Dm0644 -p %SOURCE3 %buildroot%python3_sitelibdir/%name/main/migrations/0196_oauth2_toolkit_v3_fields.py
 
# supervisor.conf
install -Dm0644 -p %SOURCE4 %buildroot%_sysconfdir/supervisord.d/awx.ini

# receptor.conf
install -Dm0644 -p %SOURCE5 %buildroot%_sysconfdir/receptor/receptor.conf

mkdir -p %buildroot%_sysconfdir/tower/conf.d/
touch %buildroot%_sysconfdir/tower/conf.d/database.py
touch %buildroot%_sysconfdir/tower/conf.d/local_settings.py

mkdir -p %buildroot%_sharedstatedir/awx/rsyslog

install -Dm0644 -p %SOURCE6 %buildroot%_unitdir/awx.service

install -Dm0644 -p %SOURCE7 %buildroot%_sysconfdir/tower/conf.d/redis_settings.py

%check
%pyproject_run_pytest

%pre
# Add the "awx" user and group
getent group awx >/dev/null || %_sbindir/groupadd -r awx
getent passwd awx >/dev/null || \
    %_sbindir/useradd -r -g awx -G awx -M -d %_sharedstatedir/awx -s /sbin/nologin -c "AWX" awx
# Add apache into awx group for static files access
getent passwd %apache2_user >/dev/null && \
    %_sbindir/usermod -a -G awx %apache2_user
exit 0

%preun
%preun_service supervisord

%files
%doc README.*
%_bindir/awx-manage
%attr(640,root,awx) %config(noreplace) %_sysconfdir/tower/settings.py
%attr(640,root,awx) %config(noreplace) %_sysconfdir/tower/uwsgi.ini
%attr(640,root,awx) %config(noreplace) %_sysconfdir/tower/conf.d/database.py
%attr(640,root,awx) %config(noreplace) %_sysconfdir/tower/conf.d/local_settings.py
%attr(640,root,awx) %config(noreplace) %_sysconfdir/tower/conf.d/redis_settings.py
%attr(640,root,awx) %config(noreplace) %_sysconfdir/tower/SECRET_KEY
%config(noreplace) %_sysconfdir/supervisord.d/awx.ini
%config(noreplace) %_sysconfdir/receptor/receptor.conf
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}
%dir %_sysconfdir/tower
%dir %_sysconfdir/tower/conf.d
%dir %attr(770,awx,awx) %_sharedstatedir/awx
%dir %_sharedstatedir/awx/public
%dir %attr(755,root,root) %_sharedstatedir/awx/public/static
%dir %attr(770,awx,awx) %_sharedstatedir/awx/projects
%dir %attr(770,awx,awx) %_sharedstatedir/awx/job_status
%dir %attr(770,awx,awx) %_logdir/tower   
%dir %attr(755,root,root) %_sharedstatedir/awx/venv
%dir %attr(755,root,root) %_sharedstatedir/awx/rsyslog
%_unitdir/awx.service

%files apache2
%config(noreplace) %apache2_sites_available/*.conf
%ghost %apache2_sites_enabled/*.conf

%changelog
* Mon Jun 15 2026 Nikita Panov <nexxy@altlinux.org> 24.6.1-alt7
- Receptor config fixes and improvements.

* Tue Jun 09 2026 Nikita Panov <nexxy@altlinux.org> 24.6.1-alt6
- Automation of deployment and fixes.

* Tue May 19 2026 Nikita Panov <nexxy@altlinux.org> 24.6.1-alt5
- Readme and minor fixes.

* Mon Apr 27 2026 Nikita Panov <nexxy@altlinux.org> 24.6.1-alt4
- Added configs for deployment.

* Tue Apr 07 2026 Nikita Panov <nexxy@altlinux.org> 24.6.1-alt3
- Fixing for new versions of dependencies.

* Mon Jul 29 2024 Andrey Cherepanov <cas@altlinux.org> 24.6.1-alt2
- Packaged %_logdir/tower, %_sharedstatedir/awx and /etc/tower with settings.py

* Sun Jul 21 2024 Anton Vyatkin <toni@altlinux.org> 24.6.1-alt1
- Initial build for Sisyphus.
