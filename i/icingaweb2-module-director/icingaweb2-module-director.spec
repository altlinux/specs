# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2024 BaseALT Ltd
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
%define icingadirector_user icingadirector

%define basedir	%_datadir/icingaweb2

Name:           icingaweb2-module-director
Version:        1.11.0
Release:        alt1

Summary:        Config module for Icinga 2
License:        GPL-2.0-or-later
Group:          Monitoring

URL:            https://icinga.com

Source0:        https://github.com/Icinga/%name/archive/v%version/%name-%version.tar

BuildRequires(pre): rpm-build-php-version
BuildRequires:  php-devel

Requires:       icinga2 >= 2.8.0
Requires:       icingaweb2 >= 2.8.0
Requires:       icingaweb2-common >= 2.8.0
Requires:       icingaweb2-module-incubator >= 0.20.0
Requires:       icingaweb2-module-ipl >= 0.5.0
Requires:       icingaweb2-module-reactbundle >= 0.9.0
Requires:       php%_php_major.%_php_minor >= 7.3
Requires:       php%_php_major.%_php_minor-curl
Requires:       php%_php_major.%_php_minor-iconv
Requires:       php%_php_major.%_php_minor-pcntl
Requires:       php%_php_major.%_php_minor-posix
Requires:       php%_php_major.%_php_minor-sockets

BuildArch:      noarch

%description
Director is a config module for Icinga 2.

%prep
%setup

%build

%install
mkdir -p %buildroot%basedir/modules/director
mkdir -p %buildroot%basedir/modules/director/{application,contrib,doc,library,public,schema,test}
cp -prv application contrib doc library public schema test %buildroot%basedir/modules/director/
cp -pv *.md *.php *.info %buildroot%basedir/modules/director/

# not needed
rm %buildroot%basedir/modules/director/contrib/docker-test.sh

# systemd
install -D -m0644 %buildroot%basedir/modules/director/contrib/systemd/icinga-director.service %buildroot%_unitdir/icinga-director.service
rm -r %buildroot%basedir/modules/director/contrib/systemd

mkdir -p %buildroot%_localstatedir/%name

# l10n
%find_lang --output=%name.lang director

%pre
getent passwd %icingadirector_user >/dev/null || useradd -c "Icinga2 director" -s /sbin/nologin -r -d %_localstatedir/%name -g %icingaweb_group %icingadirector_user

%post
%post_service icinga-director

%preun
%preun_service icinga-director

%filter_from_requires /^\/etc\/default\/icinga2/d
%filter_from_requires /^\/etc\/icinga2\/icinga2\.sysconfig/d

%files -f %name.lang
%doc README.md
%docdir %basedir/modules/director/doc
%dir %basedir
%dir %basedir/modules
%dir %basedir/modules/director
%dir %attr(0750,%icingadirector_user,%icingaweb_group) %_localstatedir/%name
%basedir/modules/director/*
%_unitdir/icinga-director.service

%changelog
* Tue Jan 09 2024 Paul Wolneykien <manowar@altlinux.org> 1.11.0-alt1
- Initial build for Sisyphus.
