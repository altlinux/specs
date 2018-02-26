Name:		refal-plus
Version:	2412
Release:	alt1
Summary:	A modern dialect of Refal programming language
Summary(ru_RU.KOI8-R): Современный диалект языка программирования Рефал
Source:		refal-r%{version}-src.zip
Source1:	http://wiki.botik.ru/twiki/pub/Refaldevel/Download/RefalPlusReferenceManual.pdf
Patch:		refal-r2412.patch
License:	GPLv2
Group:		Development/Functional
URL:		http://rfp.botik.ru/

# Automatically added by buildreq on Tue Sep 28 2010
BuildRequires: gcc-c++ libgmp-devel unzip

%description
Refal Plus is a modern dialect of Refal programming language.

Refal (REcursive Functions Algorithmic Language) was originally
developed in the middle of 1960s by V.F.Turchin as a tool for describing
the semantics of other algorithmic languages. Later, when reasonably
efficient Refal implementations had been created, Refal was used as
a symbol manipulation language in such fields as computer algebra,
compiler and interpreter writing, artificial intelligence, etc.

The principal data type in Refal are arbitrary trees, referred to as
ground expressions. In programs and text files ground expressions are
represented by linear sequences of symbols and parentheses, with
parentheses being properly paired. Symbols represent such elementary
data objects as characters, words, numbers and references to objects.

The principal means of analyzing and accessing ground expressions is
pattern matching. Refal patterns may contain symbols, parentheses, and
variables. If matching a ground expression against a pattern succeeds,
the pattern's variables are bound to the corresponding components of the
ground expression, which can be used later for building new ground
expressions.

Refal Plus has been developed taking into account the experience gained
from the design, implementation and use of such languages as Basic
Refal, Refal-2, Refal-4, Refal-5 and RL.

As compared to the other Refal dialects, Refal Plus provides the
following features:

    * Advanced modules support
    * Static declarations of dynamic objects
    * Significantly improved function declarations
    * Failure and error trapping
    * Input/output of ground expressions
    * Operations on boxes, vectors, and tables
    * "Vector" representation of ground expressions

%description -l ru_RU.KOI8-R
Рефал Плюс представляет собой один из диалектов языка программирования
Рефал.

Рефал (алгоритмический язык рекурсивных функций) был создан В.Ф.Турчиным
в качестве языка, предназначенного для описания семантики других
алгоритмических языков [Тур 66], [Тур 71]. Впоследствии, после появления
достаточно эффективных реализаций [КРТ 72], [Бзр 77], [Ром 87а] Рефал
нашел применения в таких областях как компьютерная алгебра,
конструирование компиляторов и интерпретаторов, искусственный интеллект
и др.

Основным типом данных в Рефале являются объектные выражения, которые
представляют собой произвольные деревья, изображаемые в линейной записи
как последовательности символов и скобок правильно построенные
относительно скобок. Символы представляют собой элементарные объекты
(такие как литеры, слова, числа и ссылки на объекты).

Основным средством для анализа структуры объектных выражений и для
доступа к их компонентам является сопоставление с образцом. Образцы
в Рефале могут содержать символы, скобки и переменные. Если объектное
выражение имеет структуру соответствующую образцу, переменные, входящие
в образец, получают в качестве значений фрагменты объектного выражения.
Значения переменных впоследствии могут использоваться для построения
новых объектных выражений.

Рефал-программа представляет собой набор определений функций. Каждая
функция получает в качестве аргумента некоторое объектное выражение
и вырабатывает в качестве результата некоторое объектное выражение.
Функции могут произвольным образом вызывать друг друга. Основным
средством организации управления в программах является рекурсия, т.е.
такая органиация вызовов функций при которой некоторые функции вызывают
сами себя (либо непосредственно, либо через другие функции).

Рефал Плюс возник в результате обобщения опыта, накопленного при
разработке, реализации и использовании Базисного Рефала [Бзр 77],
Рефала-2 [КлР 86], [КлР 87], [Ром 87а], Рефала-4 [Ром 87б], [Ром 87в],
Рефала-5 [Тур 89], и языков FLAC [Кис 87] и RL [Ром 87г], [Ром 88а],
[Ром 88б].

%package devel
Group:		Development/C
Summary:	Development suite for C/C++ programming with %name

%description devel
Development suite for %name

%package samples
Group:		Development/Functional
Summary:	Sample applications for %name

%description samples
Sample applications for %name

%prep
%setup -n refal-r%{version}-src
%patch -p1
touch c++/rules.mk

%build
cp %SOURCE1 .
# Time in the future bug?
find . -exec touch {} \;
cd c++
./configure -prefix /usr
%make_build

%install
cd c++
%makeinstall INSTALL_DIR=%buildroot%_prefix
%ifarch x86_64
mkdir %buildroot%_libdir
mv %buildroot%_prefix/lib/lib* %buildroot%_libdir/
%endif

%files
%doc doc AUTHORS ChangeLog Developers README *.pdf
%_bindir/*
%dir %_prefix/lib/%name
%_prefix/lib/%name/*

%files devel
%_libdir/lib*
%_includedir/*

%files samples
%doc compiler rfp rfpfilt samples trefal

%changelog
* Tue Sep 28 2010 Fr. Br. George <george@altlinux.ru> 2412-alt1
- Initial build from scratch

