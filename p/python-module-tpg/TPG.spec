Version: 3.2.1
Release: alt1

%setup_python_module tpg

Summary: Toy Parser Generator is syntax analyzer under Python
Summary(ru_RU.UTF-8): Простой, но мощный синтаксический анализатор Toy Parser Generator
%define nameUC TPG
Name: %packagename
Source: TPG-%version.tar.gz
License: BSD
Group: Development/Python
Url: http://cdsoft.fr/tpg
Buildarch: noarch

# Automatically added by buildreq on Thu Feb 23 2012
# optimized out: ImageMagick-tools fontconfig ghostscript-classic ghostscript-common python-base python-modules python-modules-compiler python-modules-email tex-common texlive-base texlive-base-bin texlive-common texlive-generic-recommended texlive-latex-base texlive-latex-recommended texlive-xetex texmf-tex4ht
BuildRequires: python-devel tex4ht texlive-latex-recommended

%description
Toy Parser Generator is a lexical and syntactic parser generator for Python.
This generator was born from a simple statement: YACC is to complex to use in
simple cases (calculators, configuration files, small programming languages, ...).

This module is built for python %__python_version

%description -l ru_RU.UTF-8
Toy Parser Generator -- это лексический и синтаксический анализатор,
порождающий код на Python. Идея автора была в том, чтобы в простых случаях
(калькуляторы, анализаторы конфигурационных файлов, встроенные языки
программирования) заменить YACC более простым и высокоуровневым инструментом.

Этот модуль собран для Python версии %__python_version

%prep
%setup -n %nameUC-%version

%build
python setup.py build
(
	cd doc
	pdflatex tpg
	htlatex tpg
)

%install
python setup.py install --root=%buildroot

%files
%doc doc/*.{png,pdf,html,css}
%doc examples
%_bindir/*
%python_sitelibdir/tpg*

%changelog
* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 3.2.1-alt1
- Autobuild version bump to 3.2.1

* Fri Feb 24 2012 Fr. Br. George <george@altlinux.ru> 3.1.4-alt1
- Autobuild version bump to 3.1.4

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.2-alt1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt1.1
- Rebuilt with python 2.6

* Sun Jun 08 2008 Fr. Br. George <george@altlinux.ru> 3.1.2-alt1
- Version up

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 3.1.0-alt1.1.1
- Rebuilt with python-2.5.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 3.1.0-alt1.1
- Rebuilt using rpm-build-python-0.29-alt4.

* Sun Aug 20 2006 Fr. Br. George <george@altlinux.ru> 3.1.0-alt1
- New version

* Tue Apr 12 2005 Fr. Br. George <george@altlinux.ru> 3.0.5-alt2
- Minor version uupping, obsoleted dependency removed

* Mon Nov 22 2004 Fr. Br. George <george@altlinux.ru> 3.0.4-alt1
- Minor version uupping

* Tue Oct 05 2004 Fr. Br. George <george@altlinux.ru> 3.0.3-alt1
- Initial ALT build

