Name: prescanic
Version: 0.8
Release: alt2

Summary: IP Scanner that catalogs all information
Summary(ru_RU.UTF-8): Сканер IP адресов, упорядочивающий все сведения
License: GPL
Group: Monitoring
Url: http://www.presonico.com/prescanic/
Packager: Malo Skryleve <malo@altlinux.org>

Source: %name-%version.tar.bz2
Patch: %name-0.8-alt-makefile.patch

Requires: libmysqlclient16 libpcap
BuildRequires: libmysqlclient-devel libpcap-devel

%description
Prescanic's goal was to an attempt to obtain as much information about
a single host as possible. From tcp fingerprintging, banner grabbing,
anonymous ftp detection, telnet banner parsing, and more.

%description -l ru_RU.UTF-8
Цель Пресканика попытаться получить все возможныя сведения о заданном
хосте, например, как чтения сведений "пальца" finger и снимка баннера,
определение анонимного ftp, обработка приглашения telnet, и т.д.
Полученныя данныя Пресканик упорядочивает и сохраняет в базе данных.

%prep
%setup
%patch -p1

%build
%make

%install
mkdir -p %buildroot%_bindir
%make_install DESTDIR=%buildroot%_bindir install

%files
%doc PROJECT README TODO
%_bindir/*

%changelog
* Thu Aug 18 2011 Malo Skryleve <malo@altlinux.org> 0.8-alt2
Fixed require dependency libmysqlclient16

* Sat Feb 19 2011 Malo Skryleve <malo@altlinux.org> 0.8-alt1
- initial build for ALT Linux Sisyphus

