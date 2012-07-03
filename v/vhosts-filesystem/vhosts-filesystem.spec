%define srv_dir           %webserver_datadir
# The word "www" here does not meen http
# It used for compability for now and should be
# changed to something like "inet-services-data" in the future.
# That's why it looks better to move to /svr, - it simplify
# naming :)
%define vhosts_dir             %webserver_vhostdir
# Next is for addons (content), that could be used with both apaches
%define apache_addons_data_dir	%srv_dir/common-addons
# Next three defines are for apachkconfig fs
%define apachk_addon_dir        /etc/httpd-addon
%define apachk_addon_initd      %apachk_addon_dir/init.d
%define apachk_favours_dir      %apachk_addon_dir/favours

Name: vhosts-filesystem
Version: 0.2
Release: alt1.4
License: GPL
Group: System/Servers
Packager: Yury Konovalov <yurix@altlinux.ru>

Summary: Shared content filesystem to be served by HTTP and FTP servers in hosting environment
Summary(ru_RU.KOI8-R): Файловая система разделяемого контента для служб HTTP и FTP в хостинговом применении

Provides: %apache_addons_data_dir
Provides: %apachk_addon_dir
Provides: %apachk_addon_initd
Provides: %apachk_favours_dir

BuildRequires(pre): rpm-build-webserver-common

PreReq: webserver-common

BuildArch: noarch

%description
The basic directory layout for shared content in hosting environment.
The vhosts-filesystem package is the basic package that is needed by
services like HTTP and FTP. The package contains the basic directory
layout for a virtual hosts data, and other shared data. It also provide
the root directory which could be used by corresponding packages
to install sprecific subdirectories, used by thouse services.

%description -l ru_RU.KOI8-R
Базовая структура каталогов для размещения разделяемого контента в хостинговых
примениях. Пакет vhosts-filesystem является базовым пакетом, требуемым такими службами
как HTTP и FTP. Содержит базовую структуру каталогов для размещения данных
виртуальных хостов и др. разделяемых данных. Этот пакет также предоставляет
общий "корень", в котором другие пакеты могут располагать свои специфичные данные.

%package -n rpm-macros-%name
Summary: RPM macroses for packages, serving shared content
Summary(ru_RU.KOI8-R): RPM макросы для пакетов, обслуживающих разделяемый контент
Group: Development/Other

Conflicts: %name-devel <= 0.2-alt1.2
Requires: rpm-macros-webserver-common

%description -n rpm-macros-%name
Contains RPM macroses to be used while building other packages in case them
provide a software that could be used to serve shared content.

%description -n rpm-macros-%name -l ru_RU.KOI8-R
Содержит макросы RPM, предназначенные для использования при сборке других пакетов
в случае если собираемые пакеты содержат программы для обслуживания разделяемого
контента.

%package -n rpm-build-%name
Summary: RPM macroses for build packages, serving shared content
Summary(ru_RU.KOI8-R): RPM макросы сборки для пакетов, обслуживающих разделяемый контент
Group: Development/Other

Provides: %name-devel = %version-%release
Obsoletes: %name-devel <= 0.2-alt1.2
Requires: rpm-macros-%name >= %version
Requires: rpm-build-webserver-common

%description -n rpm-build-%name
Contains RPM macroses to be used while building other packages in case them
provide a software that could be used to serve shared content.

%description -n rpm-build-%name -l ru_RU.KOI8-R
Содержит макросы RPM, предназначенные для использования при сборке других пакетов
в случае если собираемые пакеты содержат программы для обслуживания разделяемого
контента.

%install
mkdir -p %buildroot%srv_dir %buildroot%vhosts_dir \
    %buildroot%apache_addons_data_dir \
    %buildroot%apachk_addon_dir \
    %buildroot%apachk_addon_initd \
    %buildroot%apachk_favours_dir

# Generate macros for rpm
mkdir -p %buildroot%_sysconfdir/rpm/macros.d

echo "#root for data served by inet services
srv_dir                 %srv_dir

#place to hold virtual hosts data
vhosts_dir              %vhosts_dir

# Next is for addons content, that could be served by both apache1/2
apache_addons_data_dir  %apache_addons_data_dir

# Next three defines are for apachkconfig fs
apachk_addon_dir        %apachk_addon_dir
apachk_addon_initd      %apachk_addon_initd
apachk_favours_dir      %apachk_favours_dir
post_addon() [ -x /usr/sbin/apachkconfig ] && /usr/sbin/apachkconfig --add %* ||: %\nil
preun_addon() [ -x /usr/sbin/apachkconfig ] && /usr/sbin/apachkconfig --del %* ||: %\nil
" | sed -e "s/^\([[:alpha:]]\+\)/%\1/" -e "s/\\\//g" > %buildroot%_sysconfdir/rpm/macros.d/%name

mkdir -p %buildroot%_rpmlibdir
cat <<\EOF >%buildroot%_rpmlibdir/%name-files.req.list
# %name dirlist for %_rpmlibdir/files.req
%apache_addons_data_dir	%name
%apachk_addon_dir	%name
%apachk_addon_initd	%name
%apachk_favours_dir	%name
EOF

%files
# uncomment the following, when %srv_dir will not been provided by apache
# this will requre correct regexp in /etc/sisyphus/fhs
#%dir %srv_dir/
#%dir %vhosts_dir/
%attr(2771,root,%webserver_webmaster) %dir %apache_addons_data_dir
%dir %apachk_addon_dir
%dir %apachk_addon_initd
%dir %apachk_favours_dir

%files -n rpm-macros-%name
%attr(0644,root,root) %_sysconfdir/rpm/macros.d/%name

%files -n rpm-build-%name
%_rpmlibdir/%name-files.req.list

%changelog
* Sat Jul 12 2008 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt1.4
- NMU
- Add build subpackage for ALT Linux RPM Packaging Policy:
  + rpm-macros-%%name
  + rpm-build-%%name

* Sat Jun 28 2008 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt1.2
- NMU
- Fix #16163: webserver-common using

* Wed Jun 13 2007 Slava Semushin <php-coder@altlinux.ru> 0.2-alt1.1
- NMU
- Fixed misprint in Summary (#11742) and some typos found by me
- Spec cleanup:
  + Removed many trailing spaces
  + Don't use macros for sed and mkdir commands
  + More strict name in %%files section
  + s/%%attr(0755,root,root) %%dir/%%dir/

* Tue Jun 29 2004 Yury Konovalov <yurix@altlinux.ru> 0.2-alt1
- added apachkconfig directories and macroses

* Tue May 18 2004 Yury Konovalov <yurix@altlinux.ru> 0.1-alt1
- initial build
