%define ccomp gcc
%def_enable shared
%def_enable static
%def_disable debug

%define Name 4tH
Name: 4th
%define lname lib%name
%define ver 3.5c3
%define subver %nil
Version: %ver%subver
Release: alt4
Summary: Basic framework for creating application specific scripting languages
Summary(uk_UA.CP1251): Базова оболонка для створення специфічних для програм мов сценаріїв
Summary(ru_RU.CP1251): Базовая оболочка для создания специфических для программ языков сценариев
License: %gpl2plus
Group: Development/Other
URL: http://hansoft.come.to/
Source: http://www.xs4all.nl/~thebeez/%Name/%name-%version-unix.tar
Patch0: %name-%version-%release.patch
Patch1: %name-%version-shared.patch
%{?_enable_shared:Requires: %lname = %version-%release}
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
%if %ccomp == tcc
BuildRequires: tcc >= 0.9.23-alt3
%endif

%description
%Name is basic framework for creating application specific scripting
languages. It is a library of functions centered around a virtual
machine, which guarantees high performance, ease of use and low
overhead. But in the meanwhile %Name has acquired a reputation as an
educational tool. Its simplicity makes it perfectly suited to learn
Forth, from which it has been derived.
This package is an attempt to suit both audiences. It contains
instructions how to modify the package in order to fit your own
requirements. %Name in its current form is a calculator for simple
teletype applications.

%description -l uk_UA.CP1251
%Name - це базова оболонка для створення специфічних для програм мов
сценаріїв. А саме - бібліотека функцій навколо віртуальної машини, яка
гарантує високу продуктивність, легкість використання та незначні
накладні витрати. Але, в той же час, %Name набув репутацію як навчальний
інструмент. Завдяки своїй простоті він відмінно підходить для навчання
Forth'у (з чого все і починалося). Даний пакет намагається бути
корисним обом аудиторіям. Він включає в себе інструкції з модифікації
пакета за особистими вимогами. %Name в його сучасній формі - це
обчислювач для простих телетайпних програм.

%description -l ru_RU.CP1251
%Name - это базовая оболочка для создания специфических для програм
языков сценариев. А именно - библиотека функций вокруг виртуальной
машины, которая гарантирует высокую производительность, лёгкость
использования при незначительных накладных расходах. Но, в то же время,
%Name приобрёл репутацию обучающего инструмента. Благодаря своей простоте
он отлично подходит для обучения Forth'у (с чего всё и начиналось).
Данный пакет пытается быть полезным обоим аудиториям. Он включает в
себя инструкции по модификации пакета согласно личных требований. %Name
в его современной форме - это вычислитель для простых телетайпных
программ.


%package examples
Group: Development/Other
Summary: Examples for the %Name
Summary(uk_UA.CP1251): Приклади для %Name
Summary(ru_RU.CP1251): Примеры для %Name
BuildArch: noarch
Requires: %name = %version

%description examples
%Name is basic framework for creating application specific scripting
languages. It is a library of functions centered around a virtual
machine, which guarantees high performance, ease of use and low
overhead. But in the meanwhile %Name has acquired a reputation as an
educational tool. Its simplicity makes it perfectly suited to learn
Forth, from which it has been derived.

This package contains examples for the %Name.

%description -l uk_UA.CP1251 examples
%Name - це базова оболонка для створення специфічних для програм мов
сценаріїв. А саме - бібліотека функцій навколо віртуальної машини, яка
гарантує високу продуктивність, легкість використання та незначні
накладні витрати. Але, в той же час, %Name набув репутацію як навчальний
інструмент. Завдяки своїй простоті він відмінно підходить для навчання
Forth'у (з чого все і починалося).

В цьому пакеті знаходяться приклади для %Name.

%description -l ru_RU.CP1251 examples
%Name - это базовая оболочка для создания специфических для програм
языков сценариев. А именно - библиотека функций вокруг виртуальной
машины, которая гарантирует высокую производительность, лёгкость
использования при незначительных накладных расходах. Но, в то же время,
%Name приобрёл репутацию обучающего инструмента. Благодаря своей простоте
он отлично подходит для обучения Forth'у (с чего всё и начиналось).

В этом пакете находятся примеры для %Name.


%if_enabled shared
%package -n %lname
Group: System/Libraries
Summary: %Name shared library
Summary(uk_UA.CP1251): Бібліотека %Name
Summary(ru_RU.CP1251): Библиотека %Name

%description -n %lname
%Name is basic framework for creating application specific scripting
languages. It is a library of functions centered around a virtual
machine, which guarantees high performance, ease of use and low
overhead. All its basic building blocks (compiler, interpreter,
decompiler, loader and saver) can be called with a single line of C. No
initialization necessary.

This package contains %Name shared library.

%description -n %lname -l uk_UA.CP1251
%Name - це базова оболонка для створення специфічних для програм мов
сценаріїв. А саме - бібліотека функцій навколо віртуальної машини, яка
гарантує високу продуктивність, легкість використання та незначні
накладні витрати. Всі його базові вбудовані блоки (транслятор, інтерпретатор,
детранслятор, завантажувач та зберігач) можуть бути викликані одним
рядком в C, потреби в ініціалізації немає.

В цьому пакеті знаходиться бібліотека %Name.

%description -n %lname -l ru_RU.CP1251
%Name - это базовая оболочка для создания специфических для програм
языков сценариев. А именно - библиотека функций вокруг виртуальной
машины, которая гарантирует высокую производительность, лёгкость
использования при незначительных накладных расходах. Все его базовые
встроенные блоки (транслятор, интерпретатор, детранслятор, загрузчик и
хранитель) могут быть вызваны одной строкой в C, необходимости в
нициализации нет.

В этом пакете находится библиотека %Name.
%endif

%package -n %lname-devel
Group: Development/C
Summary: Files required to link software that uses %lname
Summary(uk_UA.CP1251): Файли, необхідні для лінкування програм, що використовують %lname
Summary(ru_RU.CP1251): Файлы, необходимые для линкования программ, которые используют %lname
Requires: %lname%{!?_enable_shared:-devel-static} = %version-%release

%description -n %lname-devel
%Name is basic framework for creating application specific scripting
languages. It is a library of functions centered around a virtual
machine, which guarantees high performance, ease of use and low
overhead. All its basic building blocks (compiler, interpreter,
decompiler, loader and saver) can be called with a single line of C. No
initialization necessary.

This package contains headers for development whith %Name.

%description -n %lname-devel -l uk_UA.CP1251
%Name - це базова оболонка для створення специфічних для програм мов
сценаріїв. А саме - бібліотека функцій навколо віртуальної машини, яка
гарантує високу продуктивність, легкість використання та незначні
накладні витрати. Всі його базові вбудовані блоки (транслятор, інтерпретатор,
детранслятор, завантажувач та зберігач) можуть бути викликані одним
рядком в C, потреби в ініціалізації немає.

В цьому пакеті знаходяться заголовки для розробки з %Name.

%description -n %lname-devel -l ru_RU.CP1251
%Name - это базовая оболочка для создания специфических для програм
языков сценариев. А именно - библиотека функций вокруг виртуальной
машины, которая гарантирует высокую производительность, лёгкость
использования при незначительных накладных расходах. Все его базовые
встроенные блоки (транслятор, интерпретатор, детранслятор, загрузчик и
хранитель) могут быть вызваны одной строкой в C, необходимости в
нициализации нет.

В этом пакете находятся заголовки для розработки с %Name.


%if_enabled static
%package -n %lname-devel-static
Group: Development/C
Summary: Static %Name library
Summary(uk_UA.CP1251): Статична бібліотека %Name
Summary(ru_RU.CP1251): Статическая библиотека %Name
Requires: %lname-devel = %version-%release

%description -n %lname-devel-static
%Name is basic framework for creating application specific scripting
languages. It is a library of functions centered around a virtual
machine, which guarantees high performance, ease of use and low
overhead. All its basic building blocks (compiler, interpreter,
decompiler, loader and saver) can be called with a single line of C. No
initialization necessary.

This package contains static %Name library.

%description -n %lname-devel-static -l uk_UA.CP1251
%Name - це базова оболонка для створення специфічних для програм мов
сценаріїв. А саме - бібліотека функцій навколо віртуальної машини, яка
гарантує високу продуктивність, легкість використання та незначні
накладні витрати. Всі його базові вбудовані блоки (транслятор, інтерпретатор,
детранслятор, завантажувач та зберігач) можуть бути викликані одним
рядком в C, потреби в ініціалізації немає.

В цьому пакеті знаходиться статична бібліотека %Name.

%description -n %lname-devel-static -l ru_RU.CP1251
%Name - это базовая оболочка для создания специфических для програм
языков сценариев. А именно - библиотека функций вокруг виртуальной
машины, которая гарантирует высокую производительность, лёгкость
использования при незначительных накладных расходах. Все его базовые
встроенные блоки (транслятор, интерпретатор, детранслятор, загрузчик и
хранитель) могут быть вызваны одной строкой в C, необходимости в
нициализации нет.

В этом пакете находится статическая библиотека %Name.
%endif

%package doc-txt
Summary: %Name manual in plain text format
Summary(uk_UA.CP1251): Посібник для %Name у текстовому форматі
Summary(ru_RU.CP1251): Руководство для %Name в текстовом формате
Group: Development/Documentation
BuildArch: noarch
Provides: %name-doc = %version-%release
Provides: %name-manual = %version-%release
Provides: %name-manual-txt = %version-%release

%description doc-txt
%Name is basic framework for creating application specific scripting
languages. It is a library of functions centered around a virtual
machine, which guarantees high performance, ease of use and low
overhead. But in the meanwhile %Name has acquired a reputation as an
educational tool. Its simplicity makes it perfectly suited to learn
Forth, from which it has been derived.

This package contains %Name manual in plain text format.

%description doc-txt -l uk_UA.CP1251
%Name - це базова оболонка для створення специфічних для програм мов
сценаріїв. А саме - бібліотека функцій навколо віртуальної машини, яка
гарантує високу продуктивність, легкість використання та незначні
накладні витрати. Всі його базові вбудовані блоки (транслятор, інтерпретатор,
детранслятор, завантажувач та зберігач) можуть бути викликані одним
рядком в C, потреби в ініціалізації немає.

В цьому пакеті знаходиться посібник для %Name у текстовому форматі.

%description doc-txt -l ru_RU.CP1251
%Name - это базовая оболочка для создания специфических для програм
языков сценариев. А именно - библиотека функций вокруг виртуальной
машины, которая гарантирует высокую производительность, лёгкость
использования при незначительных накладных расходах. Все его базовые
встроенные блоки (транслятор, интерпретатор, детранслятор, загрузчик и
хранитель) могут быть вызваны одной строкой в C, необходимости в
нициализации нет.

В этом пакете находится руководство для %Name в текстовом формате.



%prep
%setup -n %name-%ver-unix
%patch0 -p1
%patch1 -p1


%build
%define _optlevel 3
%add_optflags %{?_enable_shared:%optflags_shared} -DUNIX
%make_build -C sources \
    BINARIES=%_bindir LIBRARIES=%_libdir INCLUDES=%_includedir \
    %{?_enable_shared:SHARED=1} %{?_enable_static:STATIC=1} \
    CFLAGS="%optflags" %{?ccomp:CC=%ccomp}

sed 's/\r$//' documentation/%{Name}manual.txt > documentation/manual.txt


%install
install -d -m 0755 %buildroot{%_bindir,%_libdir,%_libexecdir/%name,%_includedir/%name,%_docdir/%name-%version/examples}
%make_install -C sources \
    %{?_enable_shared:SHARED=1} %{?_enable_static:STATIC=1} \
    BINARIES=%buildroot%_bindir \
    LIBRARIES=%buildroot%_libdir \
    install
install -pD -m 0644 documentation/%name.1 %buildroot%_man1dir/%name.1
ln -s %name.1 %buildroot%_man1dir/%{name}x.1
ln -s %name %buildroot%_bindir/%{name}x
install -m 0644 sources/*%name.h %buildroot%_includedir/%name/
install -m 0644 lib/* %buildroot%_libexecdir/%name/
find examples -type f -exec install -pD -m 0644 \{} %buildroot%_docdir/%name-%version/\{} \;
install -m 0644 documentation/euro.txt %buildroot%_docdir/%name-%version/examples/
install -m 0644 README documentation/manual.txt %buildroot%_docdir/%name-%version/

# menu
install -d %buildroot%_desktopdir
iconv -f cp1251 -t utf-8 > %buildroot%_desktopdir/%name.desktop <<__MENU__
[Desktop Entry]
GenericName=%Name
Name=%Name System
Name[uk]=%Name-система
Name[ru]=%Name-система
Exec=%name
Icon=shells_section
Type=Application
Terminal=true
Categories=Development;IDE;ConsoleOnly;
__MENU__


%files
%dir %_docdir/%name-%version
%_docdir/%name-%version/README
%_bindir/*
%dir %_libexecdir/%name
%_libexecdir/%name/*
%_man1dir/*
%_desktopdir/*


%if_enabled shared
%files -n %lname
%_libdir/*.so.*
%endif


%files -n %lname-devel
%_includedir/%name
%{?_enable_shared:%_libdir/*.so}


%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif


%files examples
%dir %_docdir/%name-%version
%_docdir/%name-%version/examples


%files doc-txt
%dir %_docdir/%name-%version
%_docdir/%name-%version/manual.txt


%changelog
* Sat Dec 27 2008 Led <led@altlinux.ru> 3.5c3-alt4
- cleaned up spec

* Fri Aug 08 2008 Led <led@altlinux.ru> 3.5c3-alt3
- fixed %name.desktop

* Wed Jun 18 2008 Led <led@altlinux.ru> 3.5c3-alt2
- added %name-doc-txt subpackage

* Tue Jun 03 2008 Led <led@altlinux.ru> 3.5c3-alt1
- 3.5c3
- build with shared library

* Tue Mar 04 2008 Led <led@altlinux.ru> 3.5c2-alt2
- fixed %name.desktop

* Mon Jan 28 2008 Led <led@altlinux.ru> 3.5c2-alt1
- 3.5c2
- updated %name-3.5c2-alt.patch

* Thu Jan 10 2008 Led <led@altlinux.ru> 3.5c-alt1
- 3.5c
- fixed License
- cleaned up spec
- fixed %%description
- fixed x86_64 build (added %name-3.5c-alt.patch)

* Sat Dec 22 2007 Led <led@altlinux.ru> 3.5b2-alt1
- 3.5b2
- fixed License

* Mon May 21 2007 Led <led@altlinux.ru> 3.5b-alt1
- 3.5b
- cleaned up spec

* Thu Nov 23 2006 Led <led@altlinux.ru> 3.5a2-alt1
- 3.5a2

* Mon Nov 13 2006 Led <led@altlinux.ru> 3.5a-alt1
- 3.5a release

* Mon Oct 16 2006 Led <led@altlinux.ru> 3.5a-alt0.2
- fixed descriptions

* Thu Oct 12 2006 Led <led@altlinux.ru> 3.5a-alt0.1
- fixed %%version
- fixed %%changelog
- made ability compile with tcc

* Sun Sep 24 2006 Led <led@altlinux.ru> 3.5-alt0.1
- 3.5a-pre3
- remade spec
- added docs from 3.3d2

* Sun Sep 24 2006 Led <led@altlinux.ru> 3.3d2-alt4
- fixed spec

* Tue Feb 14 2006 Led <led@altlinux.ru> 3.3d2-alt3
- fixed spec

* Tue Feb 14 2006 Led <led@altlinux.ru> 3.3d2-alt2
- added menu icon
- fixed spec

* Wed Jan 25 2006 Led <led@altlinux.ru> 3.3d2-alt1
- 3.3d2
- added uk and ru menu, description and Summary
- moved examples to separate package
- added headers
- moved %lname.a and headers to separate package

* Sun Jan 22 2006 Led <led@altlinux.ru> 3.3d-alt1
- Initial build
