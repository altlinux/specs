Name: sevents
Version: 1.2
Release: alt6.r69

Summary: System of Events programming with random factor
Summary(ru_RU.UTF8): Система событийного программирования с фактором случайности
License: GPL
Group: Education

Url: https://sourceforge.net/projects/sevents
Source: %name-%version.tar.xz
Patch: sevents-distribution.patch
Packager: Rinat Bikov <becase@altlinux.org>

BuildRequires(pre): /proc rpm-build-java
BuildRequires(pre): java-devel >= 1.6.0
BuildRequires(pre): ant ant-optional ant-nodeps junit

Requires: %name-main %name-libloader

%description
SEvents is a System of Event programming with random factor 
designed to accept script file and execute it with using extra 
modules. One module - one object, who relate on changing of some variables.
It can change variables values, manages events activity and draw himself,
using standart interface.

%description -l ru_RU.UTF8
SEvents - система событийного программирования с фактором случайности.
Сценарий для системы пишется на событийном языке, в котором возможно определять
переменные и константы, а также события с обработчиками. Условие выполнения
события может быть любым, включая проверку переменных/констант и проверку
относительно других событий. В этой системе объектами являются динамические
библиотеки (so, dll), которые могут реагировать на изменения системы и
изменять её состояние.

%package -n %name-main
Summary: Main SEvents cross-platform program
Summary(ru_RU.UTF8): Главная, кросс-платфоменная часть программы SEvents
Group: Education
Requires: java >= 1.6
BuildArch: noarch

%description -n %name-main
Main part of SEvents

%description -n %name-main -l ru_RU.UTF8
Основная часть системы событийного программирования SEvents, написанная на Java.

%package -n %name-libloader
Summary: Loader of plugins for SEvents
Summary(ru_RU.UTF8): Загрузчик плагинов для SEvents
Group: Education

%description -n %name-libloader
Loader of plugins for SEvents. Plugins manager.

%description -n %name-libloader -l ru_RU.UTF8
Загрузчик плагинов для SEvents. Управляет загрузкой плагинов и предоставляет
интерфейс взаимодействия плагинов с системой.

%prep
%setup -q
%patch -p1

%build
mkdir bin
mkdir lib
cd src/
./makemodule.sh
./makemodule.sh 1
./makemodule.sh 2
./makemodule.sh 3
./makemodule.sh 4
cd ..
%ant -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 jar
cd src/libloader/
%make
cd ../..

%install
mkdir -p %buildroot/
install -pD -m 644 ./dist/%name.jar  %buildroot/%_javadir/%name-%version.jar
install -pD -m 755 sevents %buildroot/%_bindir/sevents
install -pD -m 755 ./src/libloader/libseventsloader %buildroot/%_bindir/libseventsloader
install -pD -m 644 ./src/libloader/libseventsloader.so.%{version} %buildroot/%_libdir/libseventsloader.so.%{version}
ln -s -f %_javadir/%name-%version.jar %buildroot/%_javadir/%name.jar

%files

%files -n %name-main
%doc resources/BNF resources/readme-eng.txt resources/readme-rus.txt
%_javadir/*
%_bindir/sevents

%files -n %name-libloader
%_libdir/libseventsloader.so*
%_bindir/libseventsloader

%changelog
* Mon Feb 7 2011 Rinat Bikov <becase@altlinux.org> 1.2-alt6.r69
- created second, main noarch package

* Wed Jan 26 2011 Rinat Bikov <becase@altlinux.org> 1.2-alt5.r69
- separated arch-specific and noarch elements

* Fri Dec 24 2010 Rinat Bikov <becase@altlinux.org> 1.2-alt4.r69
- used distribution patch

* Wed Dec 22 2010 Rinat Bikov <becase@altlinux.org> 1.2-alt3.r69
- added distribution patch

* Sat Dec 18 2010 Rinat Bikov <becase@altlinux.org> 1.2-alt3
- avoided deadlock
- fixed interruption of dead looping modules

* Thu Dec 16 2010 Rinat Bikov <becase@altlinux.org> 1.2-alt2.1
- avoided installation of unnecessary libraries

* Thu Dec 16 2010 Rinat Bikov <becase@altlinux.org> 1.2-alt2
- fixed interruption of looping modules
- fixed indifference for wrong function name of modules
- added output of remaining delay for events
- added example of looping module
- added thread-save module execution

* Wed Dec 15 2010 Rinat Bikov <becase@altlinux.org> 1.2-alt1
- new version 1.2

* Fri Dec 25 2008 Rinat Bikov <becase@altlinux.org> 1.1-alt1
- add GUI
- change format of settings file to XML
- add localization

* Sat May 31 2008 Michael Shigorin <mike@altlinux.org> 1.0-alt1.2.M0
- minor spec fixup/cleanup
- comprehensive buildrequires (thanks Rinat Bikov and Eugene Ostapets)

* Fri May 30 2008 Rinat Bikov <bikr@mail.ru> 1.0-alt1
- initial build
