Name: unzoo
Version: 4.4
Release: alt1

Summary: unZOO - extract, test and view ZOO archives
Summary(pl): unZOO - rozpakowuje, testuje i przegląda archiwa ZOO.
Summary(ru_RU.UTF-8): unZOO - распаковка, проверка и просмотр соедржимого архивов ZOO
License: Public Domain
Group: Archiving/Compression
Url: ftp://ftp.math.rwth-aachen.de/pub/gap/gap4/util/unzoo.c
Source: unzoo.c.gz

%description
The unzoo utility is a Public Domain program, distributed with source code and
developed for extracting, testing and viewing the contents of archives created
with the ZOO archiver.

%description -l pl
Unzoo jest programem freeware, rozpowszechnianym wraz z kodem źródłowym,
przeznaczonym do rozpakowywania, testowania oraz przeglądania zawartości
archiwów stworzonych przez program ZOO.

%description -l ru_RU.UTF-8
Программа unzoo является общественным достоянием, распространяется с исходным кодом
и позволяет распаковывать файлы, проверять и просматривать содержимое архивов, созданных
архиватором ZOO.

%prep
%setup -q -c -T
%__gzip -dc %SOURCE0 > unzoo.c

%build
gcc $RPM_OPT_FLAGS -DSYS_IS_UNIX unzoo.c -o unzoo

%install
install -d $RPM_BUILD_ROOT%_bindir
install -s unzoo $RPM_BUILD_ROOT%_bindir

%files
%_bindir/unzoo

%changelog
* Wed Nov 24 2004 Vyacheslav Dikonov <slava@altlinux.ru> 4.4-alt1
- ALTLinux build
