%def_disable static
%define username _prelude

Summary:        Prelude Hybrid Intrusion Detection System Manager
Name:           prelude-manager
Version:        1.0.1
Release:        alt1
License:        GPLv2
Group:          System/Servers
URL:            http://www.prelude-ids.org/

Source:		http://www.prelude-ids.org/download/releases/%name-%version.tar.gz
Source99:	%name-initd
Patch: %name-%version-alt-changes.patch

Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

%{?_enable_static:BuildPreReq: glibc-devel-static}

BuildRequires: gcc-c++ libgnutls-devel libpreludedb-devel libwrap-devel libxml2-devel libgcrypt-devel

%description
Prelude Manager is the main program of the Prelude Hybrid IDS suite.
It is a multithreaded server which handles connections from the Prelude
sensors. It is able to register local or remote sensors, let the operator
configure them remotely, receive alerts, and store alerts in a database or any
format supported by reporting plugins, thus providing centralized logging and
analysis.
It also provides relaying capabilities for failover and replication.
The IDMEF standard is used for alert representation. Support for filtering
plugins allows you to hook in different places in the Manager to define custom
criteria for alert relaying and logging. 

%description -l uk_UA.UTF-8
Менеджер Prelude -- основна програма комплекту Prelude Hybrid IDS. Він
являє собою мультитредовий сервер який приймає з'єднання від сенсорів
Prelude. За допомогою менеджера реєструються локальні та віддалені
сенсори, виконується віддалене налаштування оператором, приймаються
тривожні повідомлення та записуються в базу даних або в будь-якому
іншому форматі, що підтримуються плагінами звітності, таким чином
забезпечуючи централізоване ведення журналу та аналіз подій.
Менеджер також забезпечує можливість надійної ретрансляції повідомлень
та реплікацію.
Для репрезентації тривожних повідомлень використовується стандарт
IDMEF. Підтримка плагінами фільтрування дозволяє Вам визначати та
описувати власні критерії для ведення журналу та відображення
тривожних повідомлень в різних місцях в менеджері.


%description -l ru_RU.UTF-8
Менеджер Prelude -- основная программа комплекта Prelude Hybrid
IDS. Он представляет собой мультитредовый сервер, который принимает
соединения от сенсоров Prelude. С помощью менеджера регистрируются
локальные и удалённые сенсоры, выполняется удалённое конфигурирование
оператором, принимаются тревожные сообщения и записываются в базу
данных или в любом другом формате, которые поддерживаются плагинами
отчётов, таким образом обеспечивая централизованное ведение журнала и
анализ событий.
Менеджер также обеспечивает гарантированную ретрансляцию сообщений и
их репликацию.
Для репрезентации тревожных сообщений используется стандарт
IDMEF. Поддержка плагинами фильтров позволяет Вам определять и
описывать собственные критерии для ведения журналов и отображения
тревожных сообщений в разных местах в менеджере.

%package devel
Summary: Libraries, includes, etc. to develop Prelude IDS Manager plugins
Group: Development/C
Requires: %name = %version-%release

%description devel
Prelude Manager is the main program of the Prelude Hybrid IDS suite.
It is a multithreaded server which handles connections from the Prelude
sensors. It is able to register local or remote sensors, let the operator
configure them remotely, receive alerts, and store alerts in a database or any
format supported by reporting plugins, thus providing centralized logging and
analysis.
It also provides relaying capabilities for failover and replication.
The IDMEF standard is used for alert representation. Support for filtering
plugins allows you to hook in different places in the Manager to define custom
criteria for alert relaying and logging. 

Install this package if you want to build Prelude IDS Manager Plugins.

%description -l uk_UA.UTF-8 devel
Менеджер Prelude -- основна програма комплекту Prelude Hybrid IDS. Він
являє собою мультитредовий сервер який приймає з'єднання від сенсорів
Prelude. За допомогою менеджера реєструються локальні та віддалені
сенсори, виконується віддалене налаштування оператором, приймаються
тривожні повідомлення та записуються в базу даних або в будь-якому
іншому форматі, що підтримуються плагінами звітності, таким чином
забезпечуючи централізоване ведення журналу та аналіз подій.

Встановіть даний пакет, якщо Ви хочете збирати власні плагіни до
менеджера Prelude.

%description -l ru_RU.UTF-8 devel
Менеджер Prelude -- основная программа комплекта Prelude Hybrid
IDS. Он представляет собой мультитредовый сервер, который принимает
соединения от сенсоров Prelude. С помощью менеджера регистрируются
локальные и удалённые сенсоры, выполняется удалённое конфигурирование
оператором, принимаются тревожные сообщения и записываются в базу
данных или в любом другом формате, которые поддерживаются плагинами
отчётов, таким образом обеспечивая централизованное ведение журнала и
анализ событий.

Установите данный пакет, если Вы хотите создавать свои плагины к
менеджеру Prelude.

%if_enabled static
%package devel-static
Summary: Libraries, includes, etc. to develop Prelude IDS Manager plugins
Group: Development/C
Requires: %name = %version-%release
Requires: %name-devel

%description devel-static
Prelude Manager is the main program of the Prelude Hybrid IDS suite.
It is a multithreaded server which handles connections from the Prelude
sensors. It is able to register local or remote sensors, let the operator
configure them remotely, receive alerts, and store alerts in a database or any
format supported by reporting plugins, thus providing centralized logging and
analysis.
It also provides relaying capabilities for failover and replication.
The IDMEF standard is used for alert representation. Support for filtering
plugins allows you to hook in different places in the Manager to define custom
criteria for alert relaying and logging. 

This package contains statically builded libraries for Prelude IDS Manager.

%description -l uk_UA.UTF-8 devel-static
Менеджер Prelude -- основна програма комплекту Prelude Hybrid IDS. Він
являє собою мультитредовий сервер який приймає з'єднання від сенсорів
Prelude. За допомогою менеджера реєструються локальні та віддалені
сенсори, виконується віддалене налаштування оператором, приймаються
тривожні повідомлення та записуються в базу даних або в будь-якому
іншому форматі, що підтримуються плагінами звітності, таким чином
забезпечуючи централізоване ведення журналу та аналіз подій.

Даний пакет містить в собі статичні файли бібліотек менеджера Prelude.

%description -l ru_RU.UTF-8 devel-static
Менеджер Prelude -- основная программа комплекта Prelude Hybrid
IDS. Он представляет собой мультитредовый сервер, который принимает
соединения от сенсоров Prelude. С помощью менеджера регистрируются
локальные и удалённые сенсоры, выполняется удалённое конфигурирование
оператором, принимаются тревожные сообщения и записываются в базу
данных или в любом другом формате, которые поддерживаются плагинами
отчётов, таким образом обеспечивая централизованное ведение журнала и
анализ событий.

Данный пакет содержит статические файлы библиотек менеджера Prelude.
%endif

%package xml-plugin
Summary: XML report plugin for Prelude IDS Manager
Group: System/Servers
Requires: %name = %version-%release

%description xml-plugin
Prelude Manager is the main program of the Prelude Hybrid IDS suite. It is a
multithreaded server which handles connections from the Prelude sensors. It is
able to register local or remote sensors, let the operator configure them
remotely, receive alerts, and store alerts in a database or any format
supported by reporting plugins, thus providing centralized logging and
analysis. It also provides relaying capabilities for failover and replication.
The IDMEF standard is used for alert representation. Support for filtering
plugins allows you to hook in different places in the Manager to define custom
criteria for alert relaying and logging.

This plugin adds XML logging capabilities to the Prelude IDS Manager.

%description -l uk_UA.UTF-8 xml-plugin
Менеджер Prelude -- основна програма комплекту Prelude Hybrid IDS. Він
являє собою мультитредовий сервер який приймає з'єднання від сенсорів
Prelude. За допомогою менеджера реєструються локальні та віддалені
сенсори, виконується віддалене налаштування оператором, приймаються
тривожні повідомлення та записуються в базу даних або в будь-якому
іншому форматі, що підтримуються плагінами звітності, таким чином
забезпечуючи централізоване ведення журналу та аналіз подій.

Даний плагін додає можливість ведення журналів у форматі XML.

%description -l ru_RU.UTF-8 xml-plugin
Менеджер Prelude -- основная программа комплекта Prelude Hybrid
IDS. Он представляет собой мультитредовый сервер, который принимает
соединения от сенсоров Prelude. С помощью менеджера регистрируются
локальные и удалённые сенсоры, выполняется удалённое конфигурирование
оператором, принимаются тревожные сообщения и записываются в базу
данных или в любом другом формате, которые поддерживаются плагинами
отчётов, таким образом обеспечивая централизованное ведение журнала и
анализ событий.

Данный плагин дает возможность ведения журналов в формате XML.

%package db-plugin
Summary: Database report plugin for Prelude IDS Manager
Group: System/Servers
Requires: %name = %version-%release
Requires: libprelude-db

%description db-plugin
Prelude Manager is the main program of the Prelude Hybrid IDS
suite. It is a multithreaded server which handles connections from
the Prelude sensors. It is able to register local or remote
sensors, let the operator configure them remotely, receive alerts,
and store alerts in a database or any format supported by
reporting plugins, thus providing centralized logging and
analysis. It also provides relaying capabilities for failover and
replication. The IDMEF standard is used for alert representation.
Support for filtering plugins allows you to hook in different
places in the Manager to define custom criteria for alert relaying
and logging.

This plugin authorize prelude-manager to write to database.

%description -l uk_UA.UTF-8 db-plugin
Менеджер Prelude -- основна програма комплекту Prelude Hybrid IDS. Він
являє собою мультитредовий сервер який приймає з'єднання від сенсорів
Prelude. За допомогою менеджера реєструються локальні та віддалені
сенсори, виконується віддалене налаштування оператором, приймаються
тривожні повідомлення та записуються в базу даних або в будь-якому
іншому форматі, що підтримуються плагінами звітності, таким чином
забезпечуючи централізоване ведення журналу та аналіз подій.

Даний плагін додає можливість ведення журналів у базi даних.

%description -l ru_RU.UTF-8 db-plugin
Менеджер Prelude -- основная программа комплекта Prelude Hybrid
IDS. Он представляет собой мультитредовый сервер, который принимает
соединения от сенсоров Prelude. С помощью менеджера регистрируются
локальные и удалённые сенсоры, выполняется удалённое конфигурирование
оператором, принимаются тревожные сообщения и записываются в базу
данных или в любом другом формате, которые поддерживаются плагинами
отчётов, таким образом обеспечивая централизованное ведение журнала и
анализ событий.

Данный плагин дает возможность ведения журналов в базе данных.

%prep
%setup -q
%patch -p1

%build
%autoreconf
# Fix undefined symbol
find ./plugins -type f -print0 -name Makefile | xargs -r0 %__subst "s|(LDFLAGS)|(LDFLAGS) \$(LIBPRELUDEDB_LIBS) |g"

%configure %{subst_enable static} \
	--localstatedir=%_var \
	--docdir=%_defaultdocdir/%name-%version \
	--sysconfdir=%_sysconfdir/prelude


%make

%install
%make DESTDIR=%buildroot install
%__mkdir_p %buildroot%_logdir/prelude

##%__subst 's/\/var\/log\/prelude/\/var\/log\/prelude\/prelude/i' $RPM_BUILD_ROOT/%_sysconfdir/prelude/%name/%name.conf
%__mkdir_p %buildroot%_initdir
%__install -m 755 %SOURCE99 %buildroot%_initdir/%name
%__mkdir_p %buildroot%_sysconfdir/sysconfig
%__cat > %buildroot%_sysconfdir/sysconfig/%name <<EOF
# Additional command line parameters for %name:
#
OPTIONS=""
EOF

%__subst 's/# user = prelude/user = _prelude/g' %buildroot%_sysconfdir/prelude/%name/%name.conf
%__subst 's/# group = prelude/group = _prelude/g' %buildroot%_sysconfdir/prelude/%name/%name.conf
%__subst 's|/your/path/to/your/db/idmef-db.sql|%_var/lib/preludedb/idmef-db.sqlite|g' %buildroot%_sysconfdir/prelude/%name/%name.conf

%pre
/usr/sbin/groupadd -r -f %username &> /dev/null ||:
/usr/sbin/useradd -r -g %username -d %_datadir/%name -c 'Prelude Hybrid Intrusion Detection System Manager' -s /dev/null -n %username &> /dev/null ||:

%files
%doc AUTHORS ChangeLog README INSTALL NEWS HACKING.README
%doc plugins/reports/smtp/template.example

%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_initdir/%name
%config %dir %_sysconfdir/prelude/%name
%config(noreplace) %attr(0640,root,%username) %_sysconfdir/prelude/%name/*

%_bindir/*
%_libdir/%name/*/*.so
%_man1dir/*
%dir %_libdir/%name/
%dir %_libdir/%name/decodes
%dir %_libdir/%name/filters
%dir %_libdir/%name/reports

%dir %_datadir/%name
%dir %attr(3770,root,%username) %_logdir/prelude
%dir %attr(0770,root,%username) %_var/spool/%name
%dir %attr(0770,root,%username) %_var/spool/%name/scheduler
%dir %attr(0770,root,%username) %_var/spool/%name/failover
%dir %attr(0770,root,%username) %_var/run/%name/

%if_enabled static
%_libdir/%name/*/*.a
%endif

%exclude %_libdir/%name/reports/xmlmod.*
%exclude %_libdir/%name/reports/db.*

%files devel
%_includedir/%name/*.h
##%_datadir/gtk-doc/html/*

%if_enabled static
%files devel-static
%_libdir/%name/*/*.la
%endif

%files xml-plugin
%_libdir/%name/reports/xmlmod.so
%_datadir/%name/xmlmod

%if_enabled static
%_libdir/%name/reports/xmlmod.a
%endif

%files db-plugin
%_libdir/%name/reports/db.so

%if_enabled static
%_libdir/%name/reports/db.a
%endif

%changelog
* Wed Mar 30 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.1-alt1
- New version
- Add libgcrypt-devel to BuildRequires

* Tue Jul 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt1
- New version

* Mon Jul 13 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.15-alt1
- New version
- Migrate to git

* Mon Jan 12 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.14.2-alt3
- Fix path to sqlite database in config

* Tue Dec 23 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.14.2-alt2
- Add Patch1: %name-0.9.12-pie.patch

* Sun Oct 19 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.14.2-alt1
- New version

* Sun Jun 29 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.13-alt1
- Recovery from orfaned
- Update to new version 0.9.13
- Update BuildRequires
- Remove all patches
- Update /etc/init.d/%name
- Update spec

* Mon Dec 20 2004 Serge A. Volkov <vserge at altlinux.ru> 0.8.10-alt5
- Update to new version 0.8.10
- Rebuild with libprelude-0.8.10
- Update BuildRequires

* Thu Feb 13 2004 Serge A. Volkov <vserge@altlinux.ru> 0.8.9-alt4.1
- Rebuild with openssl-0.9.7d
- Remove configure option "--enable-gtk-doc"

* Mon Feb  2 2004 Serhii Hlodin <hlodin@altlinux.ru> 0.8.9-alt3
- Minor fixes for Sisyphus
- Add initscript
- Add additional sysconfig file

* Thu Nov  6 2003 Serhii Hlodin <hlodin@altlinux.ru> 0.8.9-alt2
- Minor fixes in dependencies

* Wed Nov  5 2003 Serhii Hlodin <hlodin@altlinux.ru> 0.8.9-alt1
- New release

* Sun Oct 12 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.8.8-alt2
- Minor fixes in spec

* Wed Oct 08 2003 Serhii Hlodin <hlodin@altlinux.ru> 0.8.8-alt1
- New release

* Sun May 18 2003 Serhii Hlodin <hlodin@altlinux.ru> 0.8.7-alt1
- Initial build based on original spec-file

