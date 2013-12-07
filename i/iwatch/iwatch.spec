Name: iwatch
Version: 0.2.2
Release: alt1
Summary: Realtime filesystem monitor
License: GPLv2
Group: System/Libraries
Source: %name-%version.tgz
Source1: %name.init
Url: http://sourceforge.net/projects/iwatch/

BuildArch: noarch
BuildRequires: perl(Event.pm) perl(Linux/Inotify2.pm) perl(Mail/Sendmail.pm) perl(XML/SimpleObject/LibXML.pm)

%description
iWatch is a realtime filesystem monitoring program. Its purpose is to monitor
any changes in a specific directory or file and send email notification
immediately after the change. This can be very useful to watch a sensible file
or directory against any changes, like files /etc/passwd,/etc/shadow or
directory /bin or to monitor the root directory of a website against
any unwanted changes.

%prep
%setup -q -n %name

%build

%install
install -pD -m755 %name %buildroot%_bindir/%name
install -pD -m755 %SOURCE1 %buildroot%_initdir/%name
install -pD -m644 %name.xml %buildroot%_sysconfdir/%name.xml
install -pD -m644 %name.dtd %buildroot%_sysconfdir/%name.dtd

%post
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS COPYING ChangeLog README iwatch.xml.example
%_bindir/*
%_initdir/*
%config(noreplace) %_sysconfdir/%name.*

%changelog
* Sat Dec 07 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2.2-alt1
- Build for ALTLinux
