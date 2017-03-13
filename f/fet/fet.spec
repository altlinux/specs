# $Revision: 1.60 $, $Date: 2011/05/27 11:58:40 $
# TODO:
#	- fet doesn't respect locale settings
#
Summary: FET is open source free software for automatically scheduling the timetable
Summary(hu.UTF-8):	FET egy nyílt forrású órarend-készítő program
Summary(pl.UTF-8):	Narzędzie do automatycznego układania planów dla szkół i uczelni
Summary(ru_RU.UTF-8):	Программа для составления расписаний учебного заведения
Name: fet
Version: 5.31.1
Release: alt1
License: GPL v2
Group: Office
Source0: http://www.lalescu.ro/liviu/fet/download/%name-%version.tar.bz2
# TODO fresh documentation
Source1: http://www.lalescu.ro/liviu/fet/doc/en/faq.html
Source2: http://www.lalescu.ro/liviu/fet/doc/en/instructions.html
Source3: http://www.lalescu.ro/liviu/fet/doc/en/tips.html
Url: http://www.lalescu.ro/liviu/fet

# Automatically added by buildreq on Mon Jul 11 2011
# optimized out: fontconfig libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-qt3support libqt4-sql libqt4-xml libstdc++-devel
BuildRequires: gcc-c++ phonon-devel ImageMagick-tools

%description
FET is open source free software for automatically scheduling the
timetable of a school, high-school or university. It uses a fast and
efficient timetabling algorithm.

%description -l ru_RU.UTF-8
FET — это программа для автоматического составления расписания занятий
в школе, техникуме или ВУЗе, использующая быстрый и эффективный
алгоритм, названный автором «рекурсивным обменом».

%description -l hu.UTF-8
FET egy nyílt forrású szoftver, amely általános iskolák, középiskolák,
egyetemek órarendjét (időbeosztását) készíti el. Egy gyors és hatékony
algoritmust használ.

%description -l pl.UTF-8
FET jest oprogramowaniem o otwartych źródłach służącym do
automatycznego układania planów zajęć szkół i uczelni. Program ten
używa szybkiego i efektywnego algorytmu układającego harmonogramy.

%package examples
Summary: Sample inputs to FET
Summary(hu.UTF-8):	Példafájlok FET-hez
Summary(pl.UTF-8):	Przykładowe pliki wejściowe dla programu FET
Group: Office
Requires: %name = %version-%release

%description examples
Sample input files to FET from all the world.

%description examples -l ru_RU.UTF-8
Прримеры входных файлов для программы составления расписаний FET

%description examples -l hu.UTF-8
Példafájlok FET-hez a világ minden tájáról.

%description examples -l pl.UTF-8
Przykładowe pliki wejściowe dla programu FET.

%package doc
Summary: FET documentation by Volker Dirr
Summary(hu.UTF-8):	FET dokumentáció Volker Dirr "szerkesztésében"
Summary(pl.UTF-8):	Dokumentacja do programu FET autorstwa Volkera Dirra
Summary(ru_RU.UTF-8):	Документация к программе составления расписаний FET
Group: Office

%description doc
FET documentation by Volker Dirr.

%description doc -l ru_RU.UTF-8
Документация к программе составления расписаний FET

%description doc -l hu.UTF-8
FET dokumentáció Volker Dirr tollából.

%description doc -l pl.UTF-8
Dokumentacja do programu FET autorstwa Volkera Dirra.

%prep
%setup
install %SOURCE1 %SOURCE2 %SOURCE3 .

sed -i '/documentation.path *=/s@=.*@= %_defaultdocdir/%name-%version@' fet.pro

cat > %name.desktop <<@@@
[Desktop Entry]
Type=Application
Name=FET
Comment=Automatical scheduling the timetable of a school
Comment[ru]=Автоматическое составлени расписаний в школе
Terminal=false
Exec=%name
Categories=Office;Calendar;
GenericName=Timetable generating
GenericName[hu]=Órarend generáló
GenericName[ru]=Составление распианий
Icon=%name
@@@

for i in 16 32 48 64 92 128; do
	convert icons/fet.png $i.png
done

%build
%qmake_qt4 fet.pro
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

for i in 16 32 48 64 92 128; do
	install -D $i.png %buildroot%_iconsdir/hicolor/${i}x${i}/apps/fet.png
done

%find_lang --with-qt fet

%files -f fet.lang
%doc AUTHORS ChangeLog README REFERENCES THANKS TODO TRANSLATORS doc/*/* faq.html instructions.html tips.html
%_bindir/*
%dir %_datadir/%name
%dir %_datadir/%name/translations
%_datadir/%name/translations/fet_untranslated.qm
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.*
%_pixmapsdir/*
%_man1dir/*

%files examples
%_datadir/%name/examples

%changelog
* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 5.31.1-alt1
- Autobuild version bump to 5.31.1

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 5.30.5-alt1
- Autobuild version bump to 5.30.5

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 5.30.1-alt1
- Autobuild version bump to 5.30.1

* Thu Jul 14 2016 Fr. Br. George <george@altlinux.ru> 5.30.0-alt1
- Autobuild version bump to 5.30.0

* Thu Dec 24 2015 Fr. Br. George <george@altlinux.ru> 5.28.4-alt1
- Autobuild version bump to 5.28.4

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 5.28.3-alt1
- Autobuild version bump to 5.28.3

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 5.27.4-alt1
- Autobuild version bump to 5.27.4

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 5.27.0-alt1
- Autobuild version bump to 5.27.0

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 5.26.0-alt1
- Autobuild version bump to 5.26.0

* Thu Oct 23 2014 Fr. Br. George <george@altlinux.ru> 5.23.3-alt1
- Autobuild version bump to 5.23.3
- Fix spec

* Sat Sep 27 2014 Fr. Br. George <george@altlinux.ru> 5.23.2-alt1
- Autobuild version bump to 5.23.2

* Tue Aug 19 2014 Fr. Br. George <george@altlinux.ru> 5.23.1-alt1
- Autobuild version bump to 5.23.1

* Mon Jun 09 2014 Fr. Br. George <george@altlinux.ru> 5.22.0-alt1
- Autobuild version bump to 5.22.0

* Mon May 12 2014 Fr. Br. George <george@altlinux.ru> 5.21.3-alt1
- Autobuild version bump to 5.21.3

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 5.21.2-alt1
- Autobuild version bump to 5.21.2

* Sun Jan 12 2014 Fr. Br. George <george@altlinux.ru> 5.21.0-alt1
- Autobuild version bump to 5.21.0

* Mon Oct 14 2013 Fr. Br. George <george@altlinux.ru> 5.20.2-alt1
- Autobuild version bump to 5.20.2

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 5.19.3-alt1
- Autobuild version bump to 5.19.3

* Sun Jun 09 2013 Fr. Br. George <george@altlinux.ru> 5.19.2-alt1
- Autobuild version bump to 5.19.2

* Thu Feb 14 2013 Fr. Br. George <george@altlinux.ru> 5.19.0-alt1
- Autobuild version bump to 5.19.0

* Mon Oct 22 2012 Fr. Br. George <george@altlinux.ru> 5.18.2-alt1
- Autobuild version bump to 5.18.2

* Mon Jun 18 2012 Fr. Br. George <george@altlinux.ru> 5.18.0-alt1
- Autobuild version bump to 5.18.0

* Wed Mar 21 2012 Fr. Br. George <george@altlinux.ru> 5.16.1-alt1
- Autobuild version bump to 5.16.1

* Tue Jan 10 2012 Fr. Br. George <george@altlinux.ru> 5.16.0-alt1
- Autobuild version bump to 5.16.0

* Mon Aug 22 2011 Fr. Br. George <george@altlinux.ru> 5.14.5-alt1
- Autobuild version bump to 5.14.5

* Mon Jul 11 2011 Fr. Br. George <george@altlinux.ru> 5.14.4-alt1
- Initial build from PLD

