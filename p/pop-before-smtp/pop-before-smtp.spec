Name:		pop-before-smtp
Version:	1.36
Release:	alt4
Summary:	POP-before-SMTP daemon
Summary(ru_RU.KOI8-R): почтовый сервис POP-before-SMTP
License:	GPL
Group:		Networking/Mail
URL:		http://popbsmtp.sourceforge.net/
Packager:	Denis Ovsienko <pilot@altlinux.ru>
Source0:	%name-%version.tar.gz
Source1:	%name.init
Patch0:		%name-alt-config.patch
BuildArch:	noarch

BuildRequires: perl-DBM perl-Net-Netmask perl-TimeDate
Requires: perl-DBM perl-Net-Netmask perl-TimeDate

%description
The %name project is a simple daemon written in Perl, to allow email relay
control based on successful POP or IMAP logins. %name requires no mods to the
other daemons, and uses no client-server communication. So it's much, much
simpler to install and maintain, and it fails to address the needs of people
with separate POP/IMAP and smtp servers.

%description -l ru_RU.KOI8-R
Проект %name --- простой демон, написанный на Perl, предназначенный для
управления доступом к пересылке почты на основании успешной попытки входа по
протоколам POP или IMAP. %name не требует внесения изменений в другие демоны и
не использует клиент-серверный подход. Поэтому он намного проще в установке и
сопровождении, но бесполезен в случае с раздельными POP/IMAP и SMTP серверами.

%prep
%setup -q
%patch0

%build

%install
%__install -D -m 755 %name %buildroot%_sbindir/%name
%__install -D -m 755 %SOURCE1 %buildroot%_initdir/%name
%__install -D -m 640 %name-conf.pl %buildroot%_sysconfdir/%name-conf.pl

%post
%post_service %name

%preun
%preun_service %name

%files
%_sbindir/%name
%_initdir/%name
%config %_sysconfdir/%name-conf.pl
%doc README TODO ChangeLog

%changelog
* Wed Apr 06 2005 Denis Ovsienko <pilot@altlinux.ru> 1.36-alt4
- another BuildReq fix

* Tue Apr 05 2005 Denis Ovsienko <pilot@altlinux.ru> 1.36-alt3
- fixing BuildReq...

* Wed Mar 30 2005 Denis Ovsienko <pilot@altlinux.ru> 1.36-alt2
- added config patch
- more information in RPM

* Fri Mar 25 2005 Denis Ovsienko <pilot@altlinux.ru> 1.36-alt1
- initial ALTLinux build
