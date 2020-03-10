%define setupdir egroupware

Name: egroupware
Version: 19.1
Release: alt1

Summary: Multi-user, web-based groupware suite
Summary(ru_RU.UTF-8): Многопользовательский web-ориентированный пакет для коллективной работы

Group: Networking/WWW
License: GPLv2
Url: https://github.com/EGroupware/egroupware

Source: %name-%version.tar
Requires: apache2-mod_php7 php7 php7-mysqli php7-pgsql php7-mbstring php7-ldap php7-pdo php7-zip php7-tidy php7-xsl php7-xmlreader php7-gd2 php7-openssl
Requires: php7-pdo_mysql php7-pdo_pgsql git composer

# BuildRequires: perl-Text-Iconv perl-CGI perl-DBI
# AutoReq: yes, noshell

BuildArch: noarch
Packager: Pavel Isopenko <pauli@altlinux.org>
%description
EGroupware is a multi-user, web-based groupware suite. Currently available modules include: email, addressbook, calendar, infolog (notes, to-do's, phone calls), content management, wiki, project management, tracker, timesheet, knowledge base, CalDAV/CardDAV. CE (Community Edition) version
%description -l ru_RU.UTF-8
EGroupware - многопользовательская, web-ориентированная система групповой работы. Доступные модули включают: электронную почту, адресные книги, календарь, инфожурнал (заметки, задачи, звонки), управление контентом, вики, управление проектами, трекер, табель, базу знаний, CalDAV/CardDAV. CE (Community Edition) версия

%prep
%setup

%install
mkdir -p %buildroot%_datadir/%setupdir
cp *.php %buildroot%_datadir/%setupdir
cp *.json %buildroot%_datadir/%setupdir
cp *.js %buildroot%_datadir/%setupdir
cp *.lock %buildroot%_datadir/%setupdir
cp *.template %buildroot%_datadir/%setupdir
cp -aRf api %buildroot%_datadir/%setupdir
cp -aRf setup %buildroot%_datadir/%setupdir
cp -aRf timesheet %buildroot%_datadir/%setupdir
cp -aRf resources %buildroot%_datadir/%setupdir
cp -aRf preferences %buildroot%_datadir/%setupdir
cp -aRf pixelegg %buildroot%_datadir/%setupdir
cp -aRf notifications %buildroot%_datadir/%setupdir
cp -aRf mail %buildroot%_datadir/%setupdir
cp -aRf infolog %buildroot%_datadir/%setupdir
cp -aRf importexport %buildroot%_datadir/%setupdir
cp -aRf home %buildroot%_datadir/%setupdir
cp -aRf files %buildroot%_datadir/%setupdir
cp -aRf filemanager %buildroot%_datadir/%setupdir
cp -aRf emailadmin %buildroot%_datadir/%setupdir
cp -aRf calendar %buildroot%_datadir/%setupdir
cp -aRf admin %buildroot%_datadir/%setupdir
cp -aRf addressbook %buildroot%_datadir/%setupdir
cp -aRf ViewerJS %buildroot%_datadir/%setupdir

mkdir -p %buildroot%_localstatedir/%setupdir/default/files
mkdir -p %buildroot%_localstatedir/%setupdir/default/backup

%files
# каталог файлов установки
%_datadir/%setupdir
# каталог рабочих файлов
%dir %_localstatedir/%setupdir
# каталоги файлов домена по умолчанию
%attr(0755,apache2,apache2) %_localstatedir/%setupdir/default

%post
composer install --no-plugins --no-scripts --working-dir=%_datadir/%setupdir
find %_datadir/%setupdir -type f -exec chmod 644 {} \;

%postun
rm -rf %_datadir/%setupdir

%changelog
* Tue Mar 10 2020 Pavel Isopenko <pauli@altlinux.org> 19.1-alt1
- initial build for Sisyphus




