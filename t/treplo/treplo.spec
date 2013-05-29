Name:		treplo
Version:	0.01
Release:	alt2
Group:		Games/Other
Summary:	Meaningless period generator in russian
Summary(ru_RU.UTF-8):	Генератор бессмысленных русских фраз
Source:		%name-%version.tar
Source1:	index.html
# http://shade.msu.ru/~taras/Grinchuk/treplo/treplo.zip
# URL:		http://shade.msu.ru/~taras/Grinchuk/
License:	Distributable
Requires:	iconv

%description
Treplo ("prater" in russian) is random meaningless russian period
generator authored by Mikhail Grinchuk.

%description -l ru_RU.UTF-8
Трепло -- программа, генерирующая бесконечную последовательность
бессмысленных, но синтаксически верных фраз на русском.
Автор -- Михаил Гринчук.

%prep
%setup

cat > %name.sh <<@@@
#!/bin/sh
cd %_datadir/%name
%_bindir/%name.bin "\$@"| while read d; do echo "\$d" | iconv -f koi8-r; done
@@@

%build
%make

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
* Wed May 29 2013 Fr. Br. George <george@altlinux.ru> 0.01-alt2
- Convert output to UTF (Closes: 21426)

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.01-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Feb 10 2009 Fr. Br. George <george@altlinux.ru> 0.01-alt1
- Initial build from DOS sources

