%define _unpackaged_files_terminate_build 1
%define php_version 8.2

Name: nextcloud
Version: 30.0.0
Release: alt1

%define installdir %webserver_webappsdir/%name

Summary: Cloud platform
Group: Networking/WWW
License: AGPL-3.0
Url: https://nextcloud.com/

BuildArch: noarch

BuildRequires(pre): rpm-macros-webserver-common
BuildRequires: python3-base
Requires(pre): webserver-common

# https://docs.nextcloud.com/server/13/admin_manual/installation/source_installation.html#ubuntu-installation-label
Requires: php%php_version
Requires: php%php_version-libs
Requires: php%php_version-dom
Requires: php%php_version-gd2
Requires: php%php_version-mbstring
Requires: php%php_version-xmlreader
Requires: php%php_version-zip
# Highly recommended:
Requires: php%php_version-curl
Requires: php%php_version-fileinfo
Requires: php%php_version-openssl
# For SQL DBs
Requires: php%php_version-pdo-driver
Requires: php%php_version-pcntl
Requires: php%php_version-intl
# Recommended
Requires: php%php_version-memcached
Requires: php%php_version-gmp
Requires: php%php_version-imagick
Requires: php%php_version-exif

Source0: %name-%version.tar
Source1: %name.watch
Patch1: nextcloud-simple-check-unicode-locale.patch
Patch2: nextcloud-fix-openssl-config.patch

# Automatically added by buildreq on Mon Oct 03 2016
# optimized out: python-base python-modules python3
BuildRequires: python3-base

%filter_from_requires /^composer$/d

%description
Nextcloud gives you easy and universal access to all of your files.
It also provides a platform to easily view, sync and share your contacts
calendars, bookmarks and files across all your devices.

%package apache2
Summary: Apache 2.x web-server default configuration for %name
Group: Networking/WWW
Requires: %name = %EVR
Requires: apache2-mod_php%php_version
Requires: apache2-mod_ssl
Requires(post): cert-sh-functions

%description apache2
Apache 2.x web-server default configuration for %name.

%package nginx
Summary: nginx web-server default configuration for %name
Group: Networking/WWW
Requires: %name = %EVR nginx
Requires: php%php_version-fpm-fcgi
Requires(post): cert-sh-functions

%description nginx
nginx web-server default configuration for %name.

%prep
%setup
%patch1 -p1
%patch2 -p1

%install
mkdir -p %buildroot%installdir
cp -rp %name/* %buildroot%installdir/
cp %name/.htaccess %buildroot%installdir/
cp %name/.user.ini %buildroot%installdir/

find %buildroot%installdir/ -name tests -type d | xargs rm -fr
rm -f %buildroot%installdir/l10n/l10n.pl

mkdir -p %buildroot%_sysconfdir/%name
mv %buildroot%installdir/config/ %buildroot%_sysconfdir/%name/.
ln -s %_sysconfdir/%name/config %buildroot%installdir/config

mkdir -p %buildroot%_localstatedir/%name
ln -s %_localstatedir/%name %buildroot%installdir/data

# Install apache2
install -pD -m0644 apache2/default.conf %buildroot%_sysconfdir/httpd2/conf/sites-available/%name.conf

# Install nginx
subst 's/php[0-9.]\+-fpm/php%php_version-fpm/g' nginx/default.conf
install -pD -m0644 nginx/default.conf %buildroot%_sysconfdir/nginx/sites-available.d/%name.conf

# Remove distribution
#rm -rf %buildroot%installdir/dist

%post apache2
a2ensite %name
a2enmod ssl
a2enport https
a2enmod rewrite
a2enmod env
a2enmod headers
a2enmod dir
a2enmod mime
# Generate SSL key
. cert-sh-functions
ssl_generate "nextcloud"
# Disable mod_php7 if it is enabled
/usr/sbin/apachectl2 -M | grep -q php7_module && ( a2dismod mod_php7 &>/dev/null ) ||:
%_initdir/httpd2 condreload

%postun apache2
%_initdir/httpd2 condreload

%post nginx
# Generate SSL key
. cert-sh-functions
ssl_generate "nextcloud"

%files
%dir %installdir
%installdir/3rdparty
%dir %attr(0775,root,_webserver) %installdir/apps
%attr(0775,root,_webserver) %installdir/apps/*
%installdir/core
%installdir/dist
%installdir/lib
%installdir/oc*
%installdir/resources
%installdir/themes
%installdir/updater
%dir %attr(0770,root,_webserver) %_sysconfdir/%name/config/
%_sysconfdir/%name
%installdir/config
%dir %attr(0770,root,_webserver) %_localstatedir/%name
%installdir/data
%installdir/*.php
%installdir/*.json
%installdir/*.lock
%installdir/.htaccess
%installdir/.user.ini
%doc %installdir/AUTHORS
%doc %installdir/COPYING
%installdir/index.html
%installdir/robots.txt
%installdir/LICENSES

%files apache2
%config(noreplace) %attr(0644,root,root) %_sysconfdir/httpd2/conf/sites-available/%name.conf

%files nginx
%config(noreplace) %attr(0644,root,root) %_sysconfdir/nginx/sites-available.d/%name.conf

%changelog
* Thu Oct 10 2024 Andrey Cherepanov <cas@altlinux.org> 30.0.0-alt1
- New version (fixes: CVE-2024-37887, CVE-2024-37884, CVE-2024-37882,
  CVE-2024-37315, CVE-2024-37313, CVE-2024-22403, CVE-2023-49792,
  CVE-2023-49791).

* Sun Jun 09 2024 Andrey Cherepanov <cas@altlinux.org> 29.0.2-alt1
- New version.

* Wed May 01 2024 Andrey Cherepanov <cas@altlinux.org> 29.0.0-alt1
- New version.

* Tue Apr 30 2024 Andrey Cherepanov <cas@altlinux.org> 28.0.5-alt1
- New version.

* Mon Dec 04 2023 Andrey Cherepanov <cas@altlinux.org> 27.1.4-alt1
- New version (fixes: CVE-2023-48306, CVE-2023-48305, CVE-2023-48304,
  CVE-2023-48303, CVE-2023-48302, CVE-2023-48301, CVE-2023-48239,
  CVE-2023-45148).

* Tue Oct 24 2023 Andrey Cherepanov <cas@altlinux.org> 27.1.2-alt1
- New version.
- Used PHP 8.2.

* Sun Jul 30 2023 Andrey Cherepanov <cas@altlinux.org> 27.0.1-alt1
- New version.

* Fri Jun 16 2023 Andrey Cherepanov <cas@altlinux.org> 27.0.0-alt1
- New version.
- Used PHP 8.1.
- nexcloud-nginx supported php8.1-fpm-fcgi.
- Added recommended exif module.
- Fixed permissions for apps directories.

* Mon Mar 27 2023 Andrey Cherepanov <cas@altlinux.org> 26.0.0-alt1
- New version.

* Mon Feb 13 2023 Andrey Cherepanov <cas@altlinux.org> 25.0.3-alt2
- Removed composer requirement (ALT #43336).

* Mon Jan 23 2023 Andrey Cherepanov <cas@altlinux.org> 25.0.3-alt1
- New version.

* Fri Jan 13 2023 Andrey Cherepanov <cas@altlinux.org> 25.0.2-alt1
- New version.

* Wed Oct 26 2022 Andrey Cherepanov <cas@altlinux.org> 25.0.0-alt1
- New version.

* Thu Sep 01 2022 Andrey Cherepanov <cas@altlinux.org> 24.0.4-alt2
- Disable mod_php7 if it is enabled.

* Tue Aug 23 2022 Andrey Cherepanov <cas@altlinux.org> 24.0.4-alt1
- New version.
- Use PHP 8.0.

* Mon Nov 15 2021 Andrey Cherepanov <cas@altlinux.org> 22.2.0-alt2
- Add recommended requirements.

* Mon Oct 25 2021 Andrey Cherepanov <cas@altlinux.org> 22.2.0-alt1
- New version (ALT #41211).

* Thu Oct 15 2020 Evgeniy Korneechev <ekorneechev@altlinux.org> 20.0.0-alt1
- version 20.0.0 / Oct 3 2020 (closes: #39028)
- Add requirement to php7-intl (closes: #36902)

* Wed Aug 28 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 16.0.0-alt4
- fixed nginx configuration to use php7

* Sun Aug 25 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 16.0.0-alt3
- avoid gdb requirement

* Wed Jun 05 2019 Andrey Cherepanov <cas@altlinux.org> 16.0.0-alt2
- Fix Apache2 configuration (ALT #36755) according to
  https://docs.nextcloud.com/server/16/admin_manual/installation/source_installation.html#apache-web-server-configuration
- Add requirement to php7-pcntl.

* Tue May 07 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 16.0.0-alt1
- version 16.0.0 (Apr 25 2019)
- fix requires (closes: #36713)

* Wed Mar 13 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 15.0.5-alt1
- version 15.0.5 (Feb 28 2019)
- NMU: Generate SSL key diring package installation (by cas@) 

* Wed Dec 05 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 13.0.8-alt1
- version 13.0.8 (Nov 22 2018)

* Thu Oct 25 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 13.0.7-alt1
- version 13.0.7 (Oct 11 2018)
- update requires for apache2 (php5 -> php7)

* Mon Sep 03 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 13.0.6-alt1
- version 13.0.6 (Aug 30 2018)
- update requires for SQL DBs

* Tue Jun 19 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 13.0.4-alt1
- version 13.0.4 (Jun 11 2018)
- update requires: php5 > php7
  (php5-xmlreader there is not for aarch64)

* Mon May 28 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 13.0.2-alt1
- version 13.0.2 (Apr 26 2018)

* Wed Mar 21 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 13.0.1-alt1
- version 13.0.1 (Mar 15 2018)

* Wed Feb 28 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 13.0.0-alt1
- version 13.0.0 (Feb 6 2018)

* Tue Jan 30 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 12.0.5-alt1
- version 12.0.5 (Jan 24 2018)

* Wed Dec 06 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 12.0.4-alt1
- version 12.0.4 (Dec 4 2017)

* Thu Sep 21 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 12.0.3-alt1
- version 12.0.3 (Sep 20 2017)
- fixed unowned files

* Mon Aug 21 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 12.0.2-alt1
- version 12.0.2 (Aug 14 2017)

* Wed Aug 09 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 12.0.1-alt1
- version 12.0.1 (Aug 7 2017)
- update requires (PHP >= 5.6)

* Thu Jul 13 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 12.0.0-alt4
- fixed permissions - addition to previous release

* Thu Jul 13 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 12.0.0-alt3
- [major] fixed permissions for installdir

* Fri Jun 16 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 12.0.0-alt2
- added missing files
- fixed requires for subpackages

* Thu Jun 15 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 12.0.0-alt1
- version 12.0.0 (May 22 2017)
- initial build
