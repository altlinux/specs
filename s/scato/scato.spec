Name:       scato
Version:    0.3.7
Release:    alt2

Summary:    Scalable Tortoise is a programming language to drive the tortoise, that can draw lines with different width and colors
Summary(ru_RU.KOI8-R): Язык для создания рисунков, посредством программирования действий воображаемой черепашки

License:    BSD
Group:      Education
Url:        http://code.google.com/p/scato
BuildArch:  noarch

Source:     %name-%version.tar.gz
Source1:    doc.tar
Patch0:     port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

Requires: python3-module-%name = %version


%description
Scato (Scalable Tortoise) is a programming language to drive the
tortoise, that can draw lines with different width and colors. Scato is
designed to plot iterated function system (IFS), L-systems, Penrose
tile, and similar kinds of fractal objects. It's arm to make easy to
scale and rotate parts of plots, produce loops and recursions, and
create pretty self-similar colored curves.

Moreover, Scato is environment. You can execute your programs, debug
them, view results and export pictures in PostScript format. Also Scato
equipped with helpful build-in examples and demos.

%description -l ru_RU.KOI8-R
Scato -- развитый черепаший язык (язык для создания рисунков,
посредством программирования действий воображаемой черепашки). Язык
позволяет продемонстрировать основные доктрины императивного
программирования: ветвления, циклы, подпрограммы, контексты. Язык
разрабатывался таким образом, чтобы, с одной стороны, быть максимально
простым, а с другой стороны, подготовить ученика к изучения Pascal
(Pascal используется в ЕГЭ). Интерпретатор языка не только визуализирует
результат работы программы, но и позволяет выполнять программу пошагово,
просматривать текущие значения переменных и параметры черепашки. Scato
развивается с учётом пожеланий преподавателей и уже был представлен на
нескольких педагогических конференциях.

%package -n python3-module-%name
License: BSD
Group: Development/Python3
Summary: Supplemental module for %name

%description -n python3-module-%name
Supplemental module for %name, %summary

%prep
%setup
tar xvf %SOURCE1
%patch0 -p2

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%doc README doc/*
%_bindir/*

%files -n python3-module-%name
%python3_sitelibdir/*


%changelog
* Thu Jan 30 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.3.7-alt2
- Porting on Python3.

* Sun Dec 23 2012 Fr. Br. George <george@altlinux.ru> 0.3.7-alt1
- Autobuild version bump to 0.3.7

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.6-alt1.1
- Rebuild with Python-2.7

* Fri Jan 21 2011 Fr. Br. George <george@altlinux.ru> 0.3.6-alt1
- Version up

* Fri Nov 05 2010 Fr. Br. George <george@altlinux.ru> 0.3.5-alt2
- Documentation update

* Tue Jul 27 2010 Fr. Br. George <george@altlinux.ru> 0.3.5-alt1
- Version up

* Thu Jul 08 2010 Fr. Br. George <george@altlinux.ru> 0.3.0-alt1
- Initial build for ALT

