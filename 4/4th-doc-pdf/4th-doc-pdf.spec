%define Name 4tH
%define bname 4th
Name: %bname-doc-pdf
Version: 3.5c3
Release: alt3
Summary: %Name manual in PDF format
Summary(uk_UA.CP1251): Посібник для %Name у форматі PDF
Summary(ru_RU.CP1251): Руководство для %Name в формате PDF
License: %gpl2plus
Group: Development/Documentation
URL: http://hansoft.come.to/
Source: http://www.xs4all.nl/~thebeez/%Name/%{Name}manual.pdf
BuildArch: noarch
Provides: %bname-doc = %version-%release
Provides: %bname-manual = %version-%release
Provides: %bname-manual-pdf = %version-%release
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses

%description
%Name is basic framework for creating application specific scripting
languages. It is a library of functions centered around a virtual
machine, which guarantees high performance, ease of use and low
overhead. But in the meanwhile %Name has acquired a reputation as an
educational tool. Its simplicity makes it perfectly suited to learn
Forth, from which it has been derived.

This package contains %Name manual in PDF format.

%description -l uk_UA.CP1251
%Name - це базова оболонка для створення специфічних для програм мов
сценаріїв. А саме - бібліотека функцій навколо віртуальної машини, яка
гарантує високу продуктивність, легкість використання при незначних
накладних витратах. Всі його базові вбудовані блоки (транслятор,
інтерпретатор, детранслятор, завантажувач та зберігач) можуть бути
викликані одним рядком в C, потреби в ініціалізації немає.

В цьому пакеті знаходиться посібник для %Name у форматі PDF.

%description -l ru_RU.CP1251
%Name - это базовая оболочка для создания специфических для програм
языков сценариев. А именно - библиотека функций вокруг виртуальной
машины, которая гарантирует высокую производительность, лёгкость
использования при незначительных накладных расходах. Все его базовые
встроенные блоки (транслятор, интерпретатор, детранслятор, загрузчик и
хранитель) могут быть вызваны одной строкой в C, необходимости в
нициализации нет.

В этом пакете находится руководство для %Name в формате PDF.


%install
install -D -m 0644 %SOURCE0 %buildroot%_docdir/%bname-%version/manual.pdf


%files
%dir %_docdir/%bname-%version
%_docdir/%bname-%version/*


%changelog
* Fri Jan 23 2009 Led <led@altlinux.ru> 3.5c3-alt3
- fixed spec

* Wed Jun 18 2008 Led <led@altlinux.ru> 3.5c3-alt2
- separate %name-doc-pdf package

* Tue Jun 03 2008 Led <led@altlinux.ru> 3.5c3-alt1
- 3.5c3

* Mon Jan 28 2008 Led <led@altlinux.ru> 3.5c2-alt1
- 3.5c2

* Thu Jan 10 2008 Led <led@altlinux.ru> 3.5c-alt1
- initial build
