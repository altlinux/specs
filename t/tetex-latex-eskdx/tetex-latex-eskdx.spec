%define texpackname eskdx
%define texmf_dir %_datadir/texmf/tex/latex/%texpackname

Name: tetex-latex-eskdx
Version: 0.97
Release: alt1.qa1

Summary: Collection of LaTeX classes and packages to typeset textual and graphical documents in accordance with russian (and probably post USSR) standards for designers
Summary(ru_RU.KOI8-R): набор пакетов и классов для LaTeX предназначенный для верстки как текстовой, так и графической документации в соответствии с требованиями Единой системы конструкторской документации.
License: LPPL
Group: Publishing

Url: http://lostclus.linux.kiev.ua/eskdx/index-ru.html
Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Source: http://lostclus.linux.kiev.ua/eskdx/eskdx-%version.tar.bz2
Source1: chngpage.sty

PreReq: tetex-core >= 2.0-alt0.8

#BuildRequires: tetex-latex >= 2.0-alt0.8

%package doc
Summary: Documentation for usage of %name
Summary(ru_RU.KOI8-R): Документация по использованию %name
Group: Publishing
Requires: %name = %version-%release

%description
eskdx is a collection of LaTeX classes and packages to typeset textual
and graphical documents in accordance with russian (and probably post
USSR) standards for designers.
Basic Features:
 - Stamp and additional columns to fit GOST 2.104-68 
 - Supported paper formats: A0, A1, A2, A3, A4 
 - Support for Two side printing 
 - Text parameters tuning to fit GOST 2.105-95 
 - Title page and approving sheet to fit GOST 2.105-95 
 - Specification sheet to fit GOST 2.106-96 form 1, 1a, 2, 2a 
 - Changes registration sheet to fit GOST 2.503-90 
 - Support for multiple languages (at this time Russian and Ukrainian is supported)


%description -l ru_RU.KOI8-R
eskdx - это набор пакетов и классов для LaTeX предназначенный для
верстки как текстовой, так и графической документации в соответствии с
требованиями Единой системы конструкторской документации.
Основные возможности:
 - основная надпись и дополнительные графы по ГОСТ 2.104-68, форма 1, 2, 2а, 2б; 
 - поддерживаемые форматы листов: А0, А1, А2, А3, А4; 
 - поддержка двусторонней печати; 
 - настройка элементов текста (абзацы, перечисления, и т.п.)
   и рубрикации (разделы, подразделы, пункты, подпункты, приложения) по ГОСТ 2.105-95; 
 - титульный лист и лист утверждения по ГОСТ 2.105-95; 
 - спецификация по ГОСТ 2.106-96, форма 1, 1а, 2, 2а; 
 - лист регистрации изменений по ГОСТ 2.503-90; 
 - поддержка множества языков (на данный момент русский и украинский). 
eskdx еще находится в ранней стадии разработки, так что возможно некоторые
стандарты поддерживаются не полностью.
 
%description doc
Documentation for usage of %name

%description doc -l ru_RU.KOI8-R
Документация по использованию %name

%prep
%setup -n %texpackname-%version

%build

%install
mkdir -p %buildroot%texmf_dir
cp -fa unpacked/*.* %buildroot%texmf_dir
cp %SOURCE1 %buildroot%texmf_dir

%files
%doc ChangeLog FAQ NEWS README
%doc manual/eskdx.pdf
%dir %texmf_dir/
%texmf_dir/*.sty
%texmf_dir/*.def
%texmf_dir/*.cls

%changelog
* Sun Dec 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.97-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * altlinux-policy-tex-obsolete-util-calls-in-post for tetex-latex-eskdx
  * postclean-05-filetriggers for spec file

* Fri May 11 2007 Vitaly Lipatov <lav@altlinux.ru> 0.97-alt1
- fix summary
- add chngpage.sty (requires by the package)

* Sun Dec 24 2006 Vitaly Lipatov <lav@altlinux.ru> 0.97-alt0.1
- new version 0.97 (with rpmrb script)

* Mon Dec 11 2006 Vitaly Lipatov <lav@altlinux.ru> 0.96-alt0.1
- inital build for ALT Linux Sisyphus
