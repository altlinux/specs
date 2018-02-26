Name: kumir-console
Version: 1.7.2
Release: alt1

Summary: Console interpreter of Kumir programming language
Summary(ru_RU.UTF-8): Консольный интерпретатор языка программирования Кумир

License: GPL
Group: Education
Url: http://lpm.org.ru/kumir
Packager: Denis Kirienko <dk@altlinux.ru>

BuildPreReq: libqt4-devel gcc-c++
Requires: libqt4-core

Source: ckumir-20101122.tar.gz

%description
Console interpreter of Kumir programming language. Useful for running
Kumir programs from command line. May be used in programming contest
control system, such as ejudge.

%description -l ru_RU.UTF-8
Консольный интерпретатор языка прогрммирования Кумир.
Позволяет запускать программы на Кумире, не использующие исполнителей,
из командной строки. Консольный интерпретатор можно использовать для
пакетного исполнения программ, например, совместно с тестирующей
системой ejudge.

%prep
%setup -n ckumir
cd src
sed -i "s/-Werror//" *.pro

%build
cd src
qmake-qt4
%make_build

%install
mkdir -p %buildroot%_bindir
install -m 755 bin/ckumir %buildroot%_bindir/
mkdir -p %buildroot%_datadir
cp -r share/kumir %buildroot%_datadir/

%files
%_bindir/*
%_datadir/kumir

%changelog
* Wed Dec 01 2010 Denis Kirienko <dk@altlinux.ru> 1.7.2-alt1
- Initial build for Sisyphus
