Name:		scato
Version:	0.3.6
Release:	alt1.1
Group:		Education
Summary:	Scalable Tortoise is a programming language to drive the tortoise, that can draw lines with different width and colors
Summary(ru_RU.KOI8-R): Язык для создания рисунков, посредством программирования действий воображаемой черепашки
License:	BSD
URL:		http://code.google.com/p/scato
Source:		http://%name.googlecode.com/files/%name-%version.tar.gz
# wget -P doc -E -H -k -K -p http://code.google.com/p/scato/wiki/{language_manual_ru,menu_overview_ru,examples,menu_overview,BNF_ru,BNF}
Source1:	doc.tar
BuildArch:	noarch
%setup_python_module %name
Requires:	%packagename = %version

# Automatically added by buildreq on Thu Jul 08 2010
BuildRequires: python-devel

%description
Scato (Scalable Tortoise) is a programming language to drive the tortoise, that can draw lines with different width and colors. Scato is designed to plot iterated function system (IFS), L-systems, Penrose tile, and similar kinds of fractal objects. It's arm to make easy to scale and rotate parts of plots, produce loops and recursions, and create pretty self-similar colored curves.

Moreover, Scato is environment. You can execute your programs, debug them, view results and export pictures in PostScript format. Also Scato equipped with helpful build-in examples and demos.

%description -l ru_RU.KOI8-R
Scato -- развитый черепаший язык (язык для создания рисунков, посредством программирования действий воображаемой черепашки). Язык позволяет продемонстрировать основные доктрины императивного программирования: ветвления, циклы, подпрограммы, контексты. Язык разрабатывался таким образом, чтобы, с одной стороны, быть максимально простым, а с другой стороны, подготовить ученика к изучения Pascal (Pascal используется в ЕГЭ). Интерпретатор языка не только визуализирует результат работы программы, но и позволяет выполнять программу пошагово, просматривать текущие значения переменных и параметры черепашки. Scato развивается с учётом пожеланий преподавателей и уже был представлен на нескольких педагогических конференциях.

%package -n %packagename
License:	BSD
Group:		Development/Python
Summary:	Supplemental module for %name

%description -n %packagename
Supplemental module for %name, %summary

%prep
%setup
tar xvf %SOURCE1

%build
%python_build

%install
%python_install

# TODO documentation
%files
%doc README doc/*
%_bindir/*

%files -n %packagename
%python_sitelibdir/*

%changelog
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

