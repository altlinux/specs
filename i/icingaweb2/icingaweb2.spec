# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2023 BaseALT Ltd
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

%define _unpackaged_files_terminate_build 1

%define icinga_user icinga
%define icinga_group icinga
%define icingacmd_group icingacmd
%define icingaweb_group icingaweb2
%define webdir %_var/www/vhosts/%name

Name:           icingaweb2
Version:        2.12.1
Release:        alt4

Summary:        Icinga Web
License:        GPL-2.0-or-later
Group:          Monitoring

URL:            https://icinga.com

Source0:        https://github.com/Icinga/icingaweb2/archive/v%version/%name-%version.tar
Patch0:         icingaweb2-skip-etc-open.patch

Requires:       icinga-l10n >= 1.1.0
Requires:       icinga2-common

BuildRequires(pre): rpm-build-php-version

BuildRequires:  php-devel
BuildRequires:  icinga-php-library >= 0.13.0

Provides:       icinga2-web

Requires:       %name-cli = %version-%release
Requires:       %name-common = %version-%release
Requires:       %name-php = %version-%release
Requires:       %name-style
Requires:       webserver-common

BuildArch:      noarch

%description
Lightweight and extensible web interface to tackle your monitoring challenge.

%package common
Summary:        Common files for Icinga Web and the Icinga CLI
Group:          Monitoring

%description common
Manages common files for Icinga Web and the Icinga CLI.

%package cli
Summary:        Icinga CLI
Group:          Monitoring
Requires:       bash-completion
Requires:       icinga-l10n >= 1.1.0
Requires:       %name-common = %version-%release
Requires:       %name-php = %version-%release
Requires:       php%_php_major.%_php_minor

%description cli
Icinga command line interface.

%package php-fpm
Summary:        PHP-FPM configuration for %name
Group:          System/Configuration/Other

%description php-fpm
This package contains the PHP FPM configuration file to run %name with php-fpm (fpm-fcgi).

%package php
Summary:        Icinga Web PHP library
Group:          Development/Other
Requires:       icinga-php-library >= 0.13.0
Requires:       icinga-php-thirdparty >= 0.12.0
Requires:       php%_php_major.%_php_minor-openssl
Requires:       %name-php-sql = %version-%release
Requires:       php%_php_major.%_php_minor-ldap
Requires:       php%_php_major.%_php_minor-mbstring
Requires:       php%_php_major.%_php_minor-gd
Requires:       php%_php_major.%_php_minor-imagick
Requires:       php%_php_major.%_php_minor-curl
Requires:       php%_php_major.%_php_minor-fileinfo

%description php
Icinga Web PHP and vendor libraries.

%package php-mysql
Summary:        MySQL PDO bindings for Icinga Web PHP library
Group:          Development/Other
Requires:       php%_php_major.%_php_minor-pdo_mysql
Provides:       %name-php-sql = %version-%release

%description php-mysql
Selects MySQL PDO module to be used with Icinga Web PHP library.

%package php-pgsql
Summary:        PostgreSQL PDO bindings for Icinga Web PHP library
Group:          Development/Other
Requires:       php%_php_major.%_php_minor-pdo_pgsql
Requires:       php%_php_major.%_php_minor-pgsql
Provides:       %name-php-sql = %version-%release

%description php-pgsql
Selects PostgreSQL PDO module to be used with Icinga Web PHP library.

%package nginx
Summary:        Run Icinga Web with Nginx web server
Group:          System/Configuration/Other
Requires:       php%_php_major.%_php_minor-fpm-fcgi
Requires:       %name-php-fpm = %version-%release
Requires:       %name = %version-%release
Requires:       nginx

%description nginx
Dependenices and configuration files to run Icinga Web with Nginx
web server.

%package style-classic
Summary:        Classic styles for Icinga Web 2
Group:          System/Configuration/Other
Provides:       %name-style = %version-%release
Conflicts:      %name-style

%description style-classic
Classic styles (branding) for Icinga Web 2.

%prep
%setup
%patch0 -p2

%build
cat <<EOF >%name-php-fpm.conf
[%name]
user = %icinga_user
group = %icingaweb_group
listen = %_var/run/php%_php_major.%_php_minor-fpm/%name.socket
listen.owner = root
listen.group = _webserver
listen.mode = 0660
pm = dynamic
pm.max_children = 5
pm.start_servers = 1
pm.min_spare_servers = 1
pm.max_spare_servers = 3
chdir = %webdir
env[PATH]=%_bindir:/bin
env[TMPDIR] = /run/%name
env[TMP] = /run/%name
php_value[include_path] = ./
php_admin_value[display_errors] = Off
php_admin_value[open_basedir] = %_datadir/%name:%_sysconfdir/%name:%_var/log/%name:%_datadir/icinga-php:%_localstatedir/%name:%webdir/sessions:%webdir/tmp:%_datadir/icinga-L10n/locale:/run/%name:%_sysconfdir/%name
php_admin_value[upload_tmp_dir] = %webdir/tmp
php_admin_value[session.save_path] = %webdir/sessions
php_admin_value[upload_max_filesize]=10G
php_admin_value[post_max_size]=10G
EOF

cat <<EOF >%name-php-fpm.tmpfiles.conf
d /run/%name 0750 %icinga_user %icingaweb_group
EOF

cat <<EOF >nginx-%name.conf
server {
    listen  127.0.0.1:81;
    listen  [::1]:81;
    server_name localhost localhost.localdomain;
EOF
bin/icingacli setup config webserver nginx \
			  --document-root %_datadir/%name/public \
			  --config %_sysconfdir/%name \
			  --fpm-uri 'unix:%_var/run/php%_php_major.%_php_minor-fpm/%name.socket' | \
	sed -e 's/^.\+$/    &/' \
	    >>nginx-%name.conf
cat <<EOF >>nginx-%name.conf
}
EOF

# patch icingacli
sed -e "s,dirname(__DIR__),'%_datadir/%name',g" \
	-e "s,\\\\Cli::start(),\\\\Cli::start('%_datadir/%name'),g" \
	bin/icingacli >bin/icingacli.patched

%install
install -d %buildroot%_datadir/%name
cp -pr application doc library modules public schema %buildroot%_datadir/%name
install -dm 0770 %buildroot%_sysconfdir/%name
install -dm 2770 %buildroot%_sysconfdir/%name/enabledModules
install -dm 0770 %buildroot%_sysconfdir/%name/modules
install -Dpm 0644 etc/bash_completion.d/icingacli %buildroot%_datadir/bash-completion/completions/icingacli
#cp -p additions/index.php %buildroot%_datadir/%name/public
install -dm 770 %buildroot%_var/cache/%name %buildroot%_localstatedir/%name
install -dm 775 %buildroot%_var/log/%name
#install -Dpm 0644 additions/icingaweb2.conf %buildroot%_sysconfdir/apache2/conf.d/icingaweb2.conf
#install -Dpm 0755 additions/icingacli %buildroot%_bindir/icingacli
install -Dpm 0755 bin/icingacli.patched %buildroot%_bindir/icingacli
mkdir -p %buildroot%webdir
mkdir %buildroot%webdir/sessions %buildroot%webdir/tmp
install -D -m0644 %name-php-fpm.conf %buildroot%_sysconfdir/fpm%_php_major.%_php_minor/php-fpm.d/%name.conf
mkdir -p %buildroot%_datadir/icinga-php
install -D -m0644 nginx-%name.conf %buildroot%_sysconfdir/nginx/sites-available.d/%name.conf
install -D -m0644 %name-php-fpm.tmpfiles.conf %buildroot%_sysconfdir/tmpfiles.d/%name.conf

# for %%ghost
mkdir -p %buildroot%_sysconfdir/nginx/sites-enabled.d
ln -sr %buildroot%_sysconfdir/nginx/sites-available.d/%name.conf \
       %buildroot%_sysconfdir/nginx/sites-enabled.d/
mkdir -p %buildroot/run/%name

%pre
getent group %icingacmd_group >/dev/null || groupadd -r %icingacmd_group
usermod -a -G %icingacmd_group,%icingaweb_group %icinga_user

%pre common
getent group %icingaweb_group  >/dev/null || groupadd -r %icingaweb_group

%post nginx
if [ $1 -eq 1 ]; then
	ln -sr %_sysconfdir/nginx/sites-available.d/%name.conf \
	   %_sysconfdir/nginx/sites-enabled.d/
fi

%files
%doc CHANGELOG.md
%doc README.md
%docdir %_datadir/%name/doc
%dir %_datadir/%name
%dir %_datadir/%name/application
%_datadir/%name/application/controllers
%_datadir/%name/application/fonts
%_datadir/%name/application/forms
%_datadir/%name/application/layouts
%_datadir/%name/application/views
%_datadir/%name/application/VERSION
%_datadir/%name/doc
%_datadir/%name/modules
%_datadir/%name/public
%exclude %_datadir/%name/public/img
%exclude %_datadir/%name/application/fonts
%exclude %_datadir/%name/modules/doc/public/css
%exclude %_datadir/%name/modules/monitoring/public/css
%exclude %_datadir/%name/public/css
%_datadir/%name/schema
%dir %webdir
%dir %webdir/tmp
%attr(0770, %icinga_user, %icingaweb_group) %dir %webdir/sessions
#%config(noreplace) %_sysconfdir/apache2/conf.d/icingaweb2.conf

%files common
%attr(0770, root, %icingaweb_group) %dir %_var/cache/%name
%attr(0775, root, %icingaweb_group) %dir %_var/log/%name
%attr(0770, root, %icingaweb_group) %dir %_localstatedir/%name
%attr(0770, root, %icingaweb_group) %config(noreplace) %dir %_sysconfdir/%name
%attr(0770, root, %icingaweb_group) %config(noreplace) %dir %_sysconfdir/%name/modules
%attr(2770, root, %icingaweb_group) %dir %_sysconfdir/%name/enabledModules

%files cli
%_datadir/%name/application/clicommands
%_datadir/bash-completion/completions/icingacli
%_bindir/icingacli

%files php-fpm
%config(noreplace) %_sysconfdir/fpm%_php_major.%_php_minor/php-fpm.d/%name.conf
%config(noreplace) %_sysconfdir/tmpfiles.d/%name.conf
%ghost %dir /run/%name

%files php
%_datadir/%name/library
%dir %_datadir/icinga-php

%files php-mysql
%files php-pgsql

%files nginx
%config(noreplace) %_sysconfdir/nginx/sites-available.d/%name.conf
%ghost %_sysconfdir/nginx/sites-enabled.d/%name.conf

%files style-classic
%_datadir/%name/public/img
%_datadir/%name/application/fonts
%_datadir/%name/modules/doc/public/css
%_datadir/%name/modules/monitoring/public/css
%_datadir/%name/public/css

%changelog
* Tue Jun 18 2024 Paul Wolneykien <manowar@altlinux.org> 2.12.1-alt4
- Extract CSS and fonts to "icingaweb2-style-classic".
- Extract images to the separate "icingaweb2-style-classic" package.

* Tue Feb 13 2024 Paul Wolneykien <manowar@altlinux.org> 2.12.1-alt3
- Make icingaweb2-php-pgsql depend on php-pgsql (thx Elena Mishina).

* Mon Feb 12 2024 Paul Wolneykien <manowar@altlinux.org> 2.12.1-alt2
- Fix: Require php-fileinfo (thx Elena Mishina).

* Wed Dec 06 2023 Andrey Limachko <liannnix@altlinux.org> 2.12.1-alt1
- New version 2.12.1.

* Thu Nov 23 2023 Paul Wolneykien <manowar@altlinux.org> 2.12.0-alt4
- Rename all subpackages to icingaweb2-*.

* Thu Nov 23 2023 Paul Wolneykien <manowar@altlinux.org> 2.12.0-alt3
- Allow to open /etc/icingaweb2 dir and skip to open "/etc/" (patch).
- Add PHP dependencies (openssl, sql, ldap and others).
- Change group name to "icingaweb2" (hardcoded in docs!).
- Save git remotes.

* Thu Nov 16 2023 Paul Wolneykien <manowar@altlinux.org> 2.12.0-alt2
- Fix: Require icinga2-common (for icigna user and groups).

* Wed Nov 15 2023 Paul Wolneykien <manowar@altlinux.org> 2.12.0-alt1
- Initial build for Sisyphus.
