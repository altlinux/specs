%define setupdir egroupware

Name: egroupware-epl
Version: 14.2
Release: alt1.qa1

Summary: Multi-user, web-based groupware suite
Summary(ru_RU.UTF-8): Многопользовательский, web-ориентированный пакет для коллективной работы

Group: Networking/WWW
License: GPL
Url: http://sourceforge.net/projects/egroupware

Source: %name-%version.tar

BuildRequires: perl-Text-Iconv perl-CGI perl-DBI
AutoReq: yes, noshell

BuildArch: noarch
Packager: Pavel Isopenko <pauli@altlinux.org>
%description
EGroupware is a multi-user, web-based groupware suite. Currently available modules include: email, addressbook, calendar, infolog (notes, to-do's, phone calls), content management, wiki, project management, tracker, timesheet, knowledge base, CalDAV/CardDAV
%description -l ru_RU.UTF-8
EGroupware - многопользовательский, web-ориентированный комплект ПО групповой работы. Доступные модули включают: электронную почту, адресные книги, календарь, инфожурнал (заметки, задачи, звонки), управление контентом, вики, управление проектами, трекер, табель, базу знаний, CalDAV/CardDAV

%prep
%setup

%install
mkdir -p %buildroot%_datadir/%setupdir
cp -aRf egroupware/* %buildroot%_datadir/%setupdir

# It is the file in the package named Thumbs.db or Thumbs.db.gz, 
# which is normally a Windows image thumbnail database. 
# Such databases are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete

%files
%_datadir/%setupdir

%changelog
* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 14.2-alt1.qa1
- NMU: applied repocop patch

* Sun Feb 23 2015 Pavel Isopenko <pauli@altlinux.org> 14.2-alt1
- initial build for Sisyphus
- based on version 14.2.20150218



