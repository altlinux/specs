Name: kumir2
Version: 2.1.0
Release: alt0.beta4

Summary: New version of Kumir - simple programming language and IDE for teaching programming
Summary(ru_RU.UTF-8): Новая версия системы Кумир - простого учебного языка программирования и среды разработки

License: GPL
Group: Education
Url: http://lpm.org.ru/kumir
Packager: Denis Kirienko <dk@altlinux.ru>

BuildPreReq: libqt4-devel gcc-c++ cmake python-modules python-modules-json boost-devel
Requires: libqt4-core

Source: kumir2-2.1.0-beta4.tar

%description
Implementation of Kumir programming language, designed by academician
Ershov. It has very simple syntax, also known as "Russian algorithmical
language". Includes compiler, runtime, IDE and  modules "Robot", "Draw",
"Turtle" and some others.

This is a second generation of well-known Kumir system.

%description -l ru_RU.UTF-8
Кумир - это учебный язык программирования, описанный в учебнике
А.Г.Кушниренко, и среда разработки. Он имеет простой синтаксис,
известный также как "русский алгоритмический язык". В состав среды также
входят канонические исполнители Робот, Чертежник, Черепаха и другие,
что делает Кумир очень удобным для начального обучения программированию.

Пакет kumir2 содержит новую реализацию системы Кумир.

%prep
%setup -n kumir2-2.1.0-beta4
sed -i "s/^Categories=.*$/Categories=Education;Qt;ComputerScience;/" *.desktop

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
make

%install
cd build
# make install
%make_install DESTDIR=%buildroot install

%files
%_bindir/*
%_libdir/%name
%_datadir/%name
%_datadir/mime/packages/*.xml
%_desktopdir/*
%_iconsdir/*/*/*/*

%changelog
* Thu Jan 09 2014 Denis Kirienko <dk@altlinux.org> 2.1.0-alt0.beta4
- Version 2.1.0-beta4

* Tue Nov 05 2013 Denis Kirienko <dk@altlinux.org> 2.0.99-alt1
- Version 2.1.0-beta1

* Tue Mar 20 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.99.0.alpha7-alt2
- rebuilt with optflags

* Sat Aug 20 2011 Denis Kirienko <dk@altlinux.ru> 1.99.0.alpha7-alt1
- Initial build for Sisyphus - alpha-version, only for testing.
