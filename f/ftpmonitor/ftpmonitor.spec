Name:		ftpmonitor
Version:	0.80
Release:	alt2.3
Summary:	A simple panel KDE applet to monitor your ftp server
Summary(ru_RU.UTF8): Простой апплет панели KDE для наблюдения за вашим FTP сервером
Source0:	http://www.cs.toronto.edu/~nilesh/linux/ftpmonitor/%name-%version.tar.gz
Source1:	%name.ru
Patch0:		%name-0.80-alt_link.diff
Patch1:		%name-0.80-alt_messages.diff
Patch2:		%name-0.80-url.diff
Patch3:		%name-0.80-russian.diff
Patch4:		%name-0.80-desktop.diff
Url:		http://queens.db.toronto.edu/~nilesh/linux/ftpmonitor/
Group:		Monitoring
License:	GPLv2
Packager:	Motsyo Gennadi <drool@altlinux.ru>

# Automatically added by buildreq on Sat Oct 20 2007 (-bi)
BuildRequires: gcc-c++ imake kdelibs-devel libXext-devel libXt-devel libqt3-devel xorg-cf-files

%description
Its a simple kde panel applet, which monitors incoming connections to
ftpd(vsftpd/ncftpd/pure-ftpd/proftpd) and generates passive popups.

For pure-ftpd, ncftpd, proftpd it acts as a frontend to pure-ftpwho,
ncftpd_spy and ftpwho respectively. For vsftpd, it looks in output of
ps -fe.

AUTHORS
-------
  Nilesh Bansal <nilesh@iitb.ac.in>

%description -l ru_RU.UTF8
Простой апплет панели KDE, наблюдающий за входящими соединениями к серверам 
ftpd(vsftpd/ncftpd/pure-ftpd/proftpd), и, показывающий всплывающие уведомления.

В случае использования pure-ftpd, ncftpd или proftpd, он работает как интерфейс к
pure-ftpwho, ncftpd_spy и ftpwho соответственно. В случае использования vsftpd,
ftpmonitor просматривает вывод ps -fe.

Авторы
-------
 Nilesh Bansal <nilesh at iitb.ac.in>

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%__install %SOURCE1 po/ru.po
%add_optflags -I%_includedir/tqtinterface
%K3configure --disable-rpath
%make_build

%install
%K3install
%__install -Dp -m 0644 src/%name-icon.png %buildroot%_pixmapsdir/%name-icon.png
%K3find_lang %name --with-kde

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%_libdir/lib%name.so
%_K3datadir/apps/kicker/applets/%name.desktop
%_K3datadir/apps/%name
%_pixmapsdir/%name-icon.png

%changelog
* Tue Mar 08 2011 Motsyo Gennadi <drool@altlinux.ru> 0.80-alt2.3
- move to alternate place

* Sun Nov 22 2009 Motsyo Gennadi <drool@altlinux.ru> 0.80-alt2.2
- fixed russian locale for Summary

* Wed Oct 28 2009 Motsyo Gennadi <drool@altlinux.ru> 0.80-alt2.1
- added russian description and summary (fixed #22075). Thanks to Phantom.

* Sun Dec 09 2007 Motsyo Gennadi <drool@altlinux.ru> 0.80-alt2
- add Url for Source

* Sat Oct 20 2007 Motsyo Gennadi <drool@altlinux.ru> 0.80-alt1
- build for Sisyphus

* Sat Oct 20 2007 Motsyo Gennadi <drool@altlinux.ru> 0.80-alt0.M40.1
- initial build for ALT Linux (M40)
