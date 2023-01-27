%define _unpackaged_files_terminate_build 1
%define mname bonito
%define _jobrunner_group corpadm

Name: bonito-open
Version: 5.58.1
Release: alt1

Summary: Bonito is an API interface for the Manatee corpus management system. 
License: GPLv2+
Group: Text tools
Url: http://nlp.fi.muni.cz/trac/noske/wiki/Downloads
Packager: Kirill Maslinsky <kirill@altlinux.org>
BuildRequires(pre): rpm-macros-apache2 rpm-build-python3
BuildRequires: python3-module-setuptools time python3-dev
Provides: bonito2-open = %version
Obsoletes: bonito2-open
BuildArch: noarch

Source: %name-%version.tar
Source100: bonito.conf
Patch: %name-%version-%release.patch

%py3_provides %mname

%description
Bonito is a python API to corpora mantained by Manatee.

%prep
%setup
%patch -p1

%pre
/usr/sbin/groupadd -r -f %_jobrunner_group ||:

%build
#export 
%configure MANATEE_REGISTRY=%_localstatedir/manatee PYTHON=python3
%make_build 

%install
%makeinstall_std
touch %buildroot/%python3_sitelibdir/%mname/__init__.py
# httpd config and cgi script
mkdir -p %buildroot/%_sysconfdir/httpd2/conf/sites-available
install %SOURCE100 %buildroot/%_sysconfdir/httpd2/conf/sites-available/bonito.conf
mkdir -p %buildroot/%_var/www/%mname
mkdir -p %buildroot/%_localstatedir/%mname
mkdir -p %buildroot/%_localstatedir/ske/jobs
sed -e "s,@MANATEE_REGISTRY\@,%_localstatedir/manatee,g" \
        -e "s,@datapath\@,%_localstatedir/bonito,g" run.cgi > %buildroot/%_var/www/%mname/run.cgi
chmod a+x %buildroot/%python3_sitelibdir/%mname/jobrunner.py

# systemd skejodserver service
mkdir -p %buildroot/%_sysconfdir
mkdir -p %buildroot/%systemd_unitdir
install misc/skejobserver.service %buildroot/%systemd_unitdir
sed 's|/var/lib/ske|/var/lib/bonito|' misc/skejobserver.conf > %buildroot/%_sysconfdir/skejobserver

# clear_cache cronjob
mkdir -p %buildroot/%_sysconfdir/cron.d
mkdir -p %buildroot/%_bindir
mv misc/bonito_clear_cache.cron %buildroot/%_sysconfdir/cron.d/bonito_clear_cache
sed 's|/usr/bin/bonito_clear_cache|%{_bindir}/bonito_clear_cache|' bonito_clear_cache > %buildroot/%_bindir/bonito_clear_cache
chmod a+x %buildroot/%{_bindir}/bonito_clear_cache


%post
%post_service skejobserver

%preun
%preun_service skejobserver

%files 
%python3_sitelibdir/%mname
%_datadir/%mname
%_bindir/*
%_sysconfdir/httpd2/conf/sites-available/bonito.conf
%_sysconfdir/cron.d/bonito_clear_cache
%_sysconfdir/skejobserver
%systemd_unitdir/skejobserver.service
%dir %attr(0775,root,%apache2_user) %_localstatedir/bonito
%dir %attr(0770,root,%_jobrunner_group) %_localstatedir/ske
%dir %attr(0770,%apache2_user,%_jobrunner_group) %_localstatedir/ske/jobs
%_var/www/bonito
%doc README.md


%changelog
* Wed Jan 04 2023 Kirill Maslinsky <kirill@altlinux.org> 5.58.1-alt1
- 5.58.1
- add corpadm group for jobrunner.py

* Wed Dec 29 2021 Kirill Maslinsky <kirill@altlinux.org> 4.24.6-alt3
- remove dependency on python3-module-signalfd

* Fri Apr 02 2021 Kirill Maslinsky <kirill@altlinux.org> 4.24.6-alt2
- fix python3 syntax errors

* Thu Mar 12 2020 Kirill Maslinsky <kirill@altlinux.org> 4.24.6-alt1
- 4.24.6
- package renamed to bonito-open
- ported to python3

* Sat Dec 05 2015 Kirill Maslinsky <kirill@altlinux.org> 3.80.5-alt1
- 3.80.5

* Wed Mar 18 2015 Kirill Maslinsky <kirill@altlinux.org> 3.48.9-alt1
- 3.48.9

* Wed Oct 02 2013 Kirill Maslinsky <kirill@altlinux.org> 2.91.13-alt1
- 2.91.13

* Tue Apr 10 2012 Kirill Maslinsky <kirill@altlinux.org> 2.68-alt1
- Initial build for Sisyphus

