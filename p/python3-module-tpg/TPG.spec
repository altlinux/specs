Version: 3.2.4
Release: alt1

%def_enable doc

Summary: Toy Parser Generator is syntax analyzer under Python
Summary(ru_RU.UTF-8): Простой, но мощный синтаксический анализатор Toy Parser Generator
%define nameUC TPG
Name: python3-module-tpg
Source: TPG-%version.tar.gz
License: LGPL-2.1
Group: Development/Python3
Url: http://christophe.delord.free.fr/tpg/index.html
Buildarch: noarch

# Automatically added by buildreq on Wed Feb 02 2022
# optimized out: fontconfig libgpg-error libx265-199 python-modules python2-base python3 python3-base python3-dev python3-module-pkg_resources sh4 tex-common texlive texlive-collection-basic texlive-dist
BuildRequires: python3-module-setuptools

%if_enabled doc
BuildRequires: tex4ht texlive-collection-latexrecommended tex(a4wide.sty)
%endif

%description
Toy Parser Generator is a lexical and syntactic parser generator for Python.
This generator was born from a simple statement: YACC is to complex to use in
simple cases (calculators, configuration files, small programming languages, ...).

%description -l ru_RU.UTF-8
Toy Parser Generator -- это лексический и синтаксический анализатор,
порождающий код на Python. Идея автора была в том, чтобы в простых случаях
(калькуляторы, анализаторы конфигурационных файлов, встроенные языки
программирования) заменить YACC более простым и высокоуровневым инструментом.

%prep
%setup -n TPG-%version

%build
%python3_build

%if_enabled doc
	cd doc
	pdflatex tpg
	htlatex tpg
    cd ..
%endif

%install
%python3_install

%files
%if_enabled doc
%doc doc/*.{png,pdf,html,css}
%endif
%doc examples
%_bindir/*
%python3_sitelibdir/*

%changelog
* Wed Feb 02 2022 Fr. Br. George <george@altlinux.ru> 3.2.4-alt1
- Autobuild version bump to 3.2.4
- Drop python2 support
- Actualize License

* Sat Oct 17 2020 Fr. Br. George <george@altlinux.ru> 3.2.3-alt1
- Autobuild version bump to 3.2.3

* Mon Mar 12 2018 Igor Vlasenko <viy@altlinux.ru> 3.2.2-alt3.1
- NMU: fixed BR: for texlive 2017

* Tue Feb 27 2018 Michael Shigorin <mike@altlinux.org> 3.2.2-alt3
- doc knob: "enable" instead of "with" (imz@)

* Mon Feb 26 2018 Michael Shigorin <mike@altlinux.org> 3.2.2-alt2
- Added doc knob (on by default)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.2.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Aug 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.2-alt1
- Version 3.2.2
- Added module for Python 3

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

