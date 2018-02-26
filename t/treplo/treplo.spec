Name:		treplo
Version:	0.01
Release:	alt1
Group:		Games/Other
Summary:	Meaningless period generator in russian
Summary(ru_RU.KOI8-R):	Генератор бессмысленных русских фраз
Source:		%name-%version.tar
Source1:	index.html
# http://shade.msu.ru/~taras/Grinchuk/treplo/treplo.zip
URL:		http://shade.msu.ru/~taras/Grinchuk/
License:	Unknown/Distributable
Packager: Fr. Br. George <george@altlinux.ru>

%description
Treplo ("prater" in russian) is random meaningless russian period generator authored by Mikhail Grinchuk.

%description -l ru_RU.KOI8-R
Трепло -- программа, генерирующая бесконечную последовательность бессмысленных, но синтаксически верных фраз на русском. Автор -- Михаил Гринчук.

%prep
%setup

%build
%make
cat > %name.sh <<@@@
#!/bin/sh
cd %_datadir/%name
%_bindir/%name.bin
@@@
cp %SOURCE1 README.alex.tarasov.html

%install
install -D %name %buildroot%_bindir/%name.bin
install -D -m755 %name.sh %buildroot%_bindir/%name
mkdir -p %buildroot%_datadir/%name
install *.dat %buildroot%_datadir/%name/

%files
%doc *.dsc *.html
%_bindir/%{name}*
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Tue Feb 10 2009 Fr. Br. George <george@altlinux.ru> 0.01-alt1
- Initial build from DOS sources

