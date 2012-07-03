Name: simplemon
Version: 0.2
Release: alt1

Summary: Simple script for monitoring param
Summary(ru_RU.UTF-8): Простой скрипт для мониторинга параметра
License: BSD
Group: Shells
Url: http://spo.tyumen.ru

Source: %name-%version.tar

%description
Simple script for monitoring some param. It may generage graph, run 
commands if value over maximum or less minimum. It may run post command 
after measure. For example it may be used for monitor temperature 
in server room with alerts to jabber and transfer graph to webserver.

%description -l ru_RU.UTF-8
Простой скрипт для мониторинга какого-либо параметра, позволяет
геренировать график, выполнять действия при выхода за пределы
заданных минимума и максимума. Также можно задать команду
выполняемую после измерения. Примером использования может служить
измерение температуры в серверной через digitemp, оповещение через
jabber и отправка графика на web-сервер.
   
%prep
%setup

%install
install -pD get_temp %buildroot%_datadir/%name/get_temp
install -pD simplemon.conf %buildroot%_sysconfdir/simplemon.conf
install -pD %name %buildroot%_bindir/%name

%files
%doc README
%_bindir/*
%_datadir/%name
%config(noreplace) %_sysconfdir/%name.conf

%changelog
* Wed Jan 27 2010 Denis Klimov <zver@altlinux.org> 0.2-alt1
- new version

* Sat Dec 26 2009 Denis Klimov <zver@altlinux.org> 0.1-alt1
- Initial build for ALT Linux

