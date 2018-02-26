%define truename gost

Name: texmf-bibtex8-%truename
Version: 0.20050820
Release: alt2

Summary: GOST cyrillic bibtex styles and extended cyrillic support for BibTeX8
Summary(ru_RU.CP1251): кириллические BibTeX стили ГОСТ
License: GPL
Group: Publishing
Url: http://tug.ctan.org/tex-archive/biblio/bibtex/contrib/gost/
Packager: Igor Vlasenko <viy@altlinux.ru>

Obsoletes: tetex-bibtex8-gost <= 0.00000001

Source: ftp://tug.ctan.org/pub/tex-archive/biblio/bibtex/contrib/gost/gost.zip
BuildArch: noarch

# Automatically added by buildreq on Sat Dec 31 2005
BuildRequires: /usr/bin/latex unzip

BuildRequires(pre): rpm-build-texmf

#TODO: bibtex8 does not support kpathsea

%description
USSR GOST 7.1-84 and Russian GOST 7.80-00 cyrillic BibTeX styles 
with russian, ukrainian and (partially) belarussian languages support.
ruscii, cp1251 and koi8-u code pages for BibTeX8 --- 
an 8-bit Implementation of BibTeX 0.99 with multilanguage support.

%description -l ru_RU.CP1251
стили BiBTeX для оформления библиографии 
на английском, русском, украинском, беларусском языках 
согласно ГОСТ СССР 7.1-84 и ГОСТ России 7.80-00
а также расширенная поддержка кириллицы для BibTeX8.
Содержит ruscii, cp1251 and koi8-u code pages.

Для правильной сортировки рекомендуется использовать BiBTeX8.

%prep
%setup -q -n %truename

%build
latex %truename.ins

%install
install -d %buildroot/usr/share/texmf/bibtex/csf
install -m644 *.csf %buildroot/usr/share/texmf/bibtex/csf/
#bibtex8 does not support kpathsea :( note: might not be true for texlive: check...
#install -d %buildroot/usr/share/texmf/bibtex/bst/%truename
#install -m644 *.bst %buildroot/usr/share/texmf/bibtex/bst/%truename/
install -d %buildroot/usr/share/texmf/bibtex/bst/
install -m644 *.bst %buildroot/usr/share/texmf/bibtex/bst/

%files
%doc README gost780.pdf gost71.pdf
/usr/share/texmf/bibtex/csf/*.csf
#/usr/share/texmf/bibtex/bst/%truename/*.bst
/usr/share/texmf/bibtex/bst/*.bst

%changelog
* Fri Nov 13 2009 Igor Vlasenko <viy@altlinux.ru> 0.20050820-alt2
- fixed buildreqs

* Thu Nov 12 2009 Igor Vlasenko <viy@altlinux.ru> 0.20050820-alt1
- renamed to texmf-bibtex8-gost

* Sat Dec 31 2005 Igor Vlasenko <viy@altlinux.ru> 0-alt1.20050820
- initial build
