Name: dbview
Version: 1.0.4
Release: alt5

Summary: Dbview - view dBase files
Group: Databases
License: GPL-2.0+
Url: ftp://metalab.unc.edu/pub/Linux/apps/database/proprietary/
Source: %name-%version.tar.gz
Packager: Ilya Mashkin <oddity@altlinux.ru>

Summary(ru_RU.UTF-8): Dbview - программа для просмотра dBase файлов

%description
dbview is a little tool that will display dBase III and IV files.
You can also use it to convert your old .dbf files for further use with Unix.

%description -l ru_RU.UTF-8
dbview - это маленькая утилита, которая отображает содержимое dBase-файлов
версии III и IV.  Также вы можете использовать её для преобразования ваших
старых .dbf-файлов в целях дальнейшего использования на Unix-системах.

%prep
%setup
sed -i 's,-O6,-O3,' Makefile

%build
%make_build

%install
install -pDm755 %name %buildroot%_bindir/%name
install -pDm644 %name.1 %buildroot%_man1dir/%name.1

%files
%doc README dBASE
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Wed Sep 06 2023 Ilya Mashkin <oddity@altlinux.ru> 1.0.4-alt5
- Fix summary and description encoding (Closes: #46943)
- Update License tag to GPL-2.0+

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt4
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 01 2019 Michael Shigorin <mike@altlinux.org> 1.0.4-alt3
- minor spec cleanup
- converted spec to UTF-8
- dropped %%ubt
- avoid superfluous (fake) optimization level

* Wed Jun 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.4-alt2%ubt
- Updated spec to include man files with any compression

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.4-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Sep 26 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.4-alt1
- 1.0.4 (Closes: #16975)

* Fri Oct 11 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.0.3-alt2
- rebuilded with gcc-3.2
- removed Summary & description in KOI8-R encoding

* Mon Feb 18 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.0.3-alt1
- first build for Sisyphus
- dbview-fixes.patch taken from PDL Linux Distribution
