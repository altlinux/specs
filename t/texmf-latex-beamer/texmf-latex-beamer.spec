Name:    texmf-latex-beamer
Version: 3.10
Release: alt0.1
Summary: A LaTeX class that allows create pdf-presentations
Summary(ru_RU.UTF-8): LaTeX класс для подготовки презентаций в pdf-формате
License: GPL
Group:   Publishing
URL:     http://latex-beamer.sourceforge.net

BuildArchitectures: noarch
BuildRequires(pre): rpm-build-texmf
Conflicts: tetex-latex-beamer

Packager: Andrey Bergman <vkni@altlinux.org>

Source: %name-%version.tar

%package -n emacs-latex-beamer-el
Summary: Emacs support for beamer LaTeX class
Group: Editors
Requires: %name = %version-%release

%description 
The beamer class is a LaTeX class that allows you to create 
a beamer presentation. It can also be used to create slides. 
It behaves similarly to other packages like Prosper, 
but has the advantage that it works together directly with pdflatex, 
but also with dvis.

%description -l ru_RU.UTF-8
Beamer - это макропакет LaTeX для создания презентаций
для проектора и слайдов. Использование пакета аналогично
использованию других пакетов для создания презентаций,
например, Prosper'а. Однако, в отличие от них, Beamer
напрямую работает с pdflatex. Впрочем его можно использовать
и для dvi.

%description -n emacs-latex-beamer-el
emacs support for beamer LaTeX class

%prep
%setup -q -n %name-%version

%build
%__mv base/emulation/examples doc/emulation

%install
# Основные каталоги
%__mkdir_p %buildroot%_texmfmain/tex/latex/beamer/base/{emulation,multimedia,themes/{color,font,inner,outer,theme/compatibility}}

%__mkdir_p %buildroot%_texmfmain/tex/latex/beamer/base/translator/dicts/{translator-basic-dictionary,translator-bibliography-dictionary,translator-environment-dictionary,translator-months-dictionary,translator-numbers-dictionary,translator-theorem-dictionary}

# Пакет для Emacs
%__mkdir_p %buildroot%_emacslispdir

# Документация
%__mkdir_p %buildroot%_texmfdoc/tex/latex/beamer/{themes,emulation,examples/{a-conference-talk,a-lecture,lyx-based-presentation},solutions/{conference-talks,generic-talks,short-talks}}

install -pD -m644 base/*.sty %buildroot%_texmfmain/tex/latex/beamer/base/
install -pD -m644 base/*.cls %buildroot%_texmfmain/tex/latex/beamer/base/

install -pD -m644 base/emulation/*.sty %buildroot%_texmfmain/tex/latex/beamer/base/emulation/

install -pD -m644 base/multimedia/* %buildroot%_texmfmain/tex/latex/beamer/base/multimedia/

install -pD -m644 base/themes/color/*.sty %buildroot%_texmfmain/tex/latex/beamer/base/themes/color/
install -pD -m644 base/themes/font/*.sty %buildroot%_texmfmain/tex/latex/beamer/base/themes/font/
install -pD -m644 base/themes/inner/*.sty %buildroot%_texmfmain/tex/latex/beamer/base/themes/inner/
install -pD -m644 base/themes/outer/*.sty %buildroot%_texmfmain/tex/latex/beamer/base/themes/outer/
install -pD -m644 base/themes/theme/*.sty %buildroot%_texmfmain/tex/latex/beamer/base/themes/theme/
install -pD -m644 base/themes/theme/compatibility/*.sty %buildroot%_texmfmain/tex/latex/beamer/base/themes/theme/compatibility/

install -pD -m644 base/translator/*.sty %buildroot%_texmfmain/tex/latex/beamer/base/translator/
install -pD -m644 base/translator/*.tex %buildroot%_texmfmain/tex/latex/beamer/base/translator/

install -pD -m644 base/translator/dicts/translator-basic-dictionary/* %buildroot%_texmfmain/tex/latex/beamer/base/translator/dicts/translator-basic-dictionary

install -pD -m644 base/translator/dicts/translator-bibliography-dictionary/* %buildroot%_texmfmain/tex/latex/beamer/base/translator/dicts/translator-bibliography-dictionary

install -pD -m644 base/translator/dicts/translator-environment-dictionary/* %buildroot%_texmfmain/tex/latex/beamer/base/translator/dicts/translator-environment-dictionary

install -pD -m644 base/translator/dicts/translator-months-dictionary/* %buildroot%_texmfmain/tex/latex/beamer/base/translator/dicts/translator-months-dictionary

install -pD -m644 base/translator/dicts/translator-numbers-dictionary/* %buildroot%_texmfmain/tex/latex/beamer/base/translator/dicts/translator-numbers-dictionary

install -pD -m644 base/translator/dicts/translator-theorem-dictionary/* %buildroot%_texmfmain/tex/latex/beamer/base/translator/dicts/translator-theorem-dictionary

# Документация
install -pD -m644 {AUTHORS,ChangeLog,FILES,INSTALL,README,TODO} %buildroot%_texmfdoc/tex/latex/beamer/
install -pD -m644 doc/beameruserguide.pdf %buildroot%_texmfdoc/tex/latex/beamer/
install -pD -m644 doc/emulation/* %buildroot%_texmfdoc/tex/latex/beamer/emulation/

# Примеры
install -pD -m644 examples/a-conference-talk/* %buildroot%_texmfdoc/tex/latex/beamer/examples/a-conference-talk
install -pD -m644 examples/a-lecture/* %buildroot%_texmfdoc/tex/latex/beamer/examples/a-lecture
install -pD -m644 examples/lyx-based-presentation/* %buildroot%_texmfdoc/tex/latex/beamer/examples/lyx-based-presentation
install -pD -m644 examples/*.pdf %buildroot%_texmfdoc/tex/latex/beamer/examples/

# Решения
install -pD -m644 solutions/conference-talks/* %buildroot%_texmfdoc/tex/latex/beamer/solutions/conference-talks
install -pD -m644 solutions/generic-talks/* %buildroot%_texmfdoc/tex/latex/beamer/solutions/generic-talks
install -pD -m644 solutions/short-talks/* %buildroot%_texmfdoc/tex/latex/beamer/solutions/short-talks

# Пакет для emacs
install -pD -m644 emacs/beamer.el %buildroot%_emacslispdir/

%files
%dir %_texmfmain/tex/latex/beamer
%dir %_texmfmain/tex/latex/beamer/base
%dir %_texmfmain/tex/latex/beamer/base/emulation
%dir %_texmfmain/tex/latex/beamer/base/multimedia
%dir %_texmfmain/tex/latex/beamer/base/themes
%dir %_texmfmain/tex/latex/beamer/base/translator
%dir %_texmfmain/tex/latex/beamer/base/translator/dicts/translator-basic-dictionary
%dir %_texmfmain/tex/latex/beamer/base/translator/dicts/translator-bibliography-dictionary
%dir %_texmfmain/tex/latex/beamer/base/translator/dicts/translator-environment-dictionary
%dir %_texmfmain/tex/latex/beamer/base/translator/dicts/translator-months-dictionary
%dir %_texmfmain/tex/latex/beamer/base/translator/dicts/translator-numbers-dictionary
%dir %_texmfmain/tex/latex/beamer/base/translator/dicts/translator-theorem-dictionary

%dir %_texmfdoc/tex/latex/beamer

%_texmfmain/tex/latex/beamer/base/*
#%%_texmfmain/tex/latex/beamer/base/emulation/*
#%%_texmfmain/tex/latex/beamer/base/multimedia/*
#%%_texmfmain/tex/latex/beamer/base/themes/*
#%%_texmfmain/tex/latex/beamer/base/translator/*
%_texmfdoc/tex/latex/beamer/*
#%%_texmfdoc/latex/beamer/base/art/*

%files -n emacs-latex-beamer-el
%_emacslispdir/beamer.el

%changelog
* Thu Dec 09 2010 Andrey Bergman <vkni@altlinux.org> 3.10-alt0.1
- Update to version 3.10.

* Sun Nov 15 2009 Andrey Bergman <vkni@altlinux.org> 3.07-alt1
- Removed obsolete lyx style package.

* Sat Sep 05 2009 Andrey Bergman <vkni@altlinux.org> 3.07-alt0.5
- Removed references on translator LaTeX package.

* Thu Jul 02 2009 Andrey Bergman <vkni@altlinux.org> 3.07-alt0.3
- Added missing directories ownership.

* Tue Jun 30 2009 Andrey Bergman <vkni@altlinux.org> 3.07-alt0.2
- Directories update.

* Sun Jun 28 2009 Andrey Bergman <vkni@altlinux.org> 3.07-alt0.1
- initial release. Inherited from tetex-latex-beamer.

* Mon Nov 07 2005 Constantin (Const) Mikhaylenko <const@altlinux.ru> 3.06-alt2
- fix dependencies

* Sat Oct 29 2005 Constantin (Const) Mikhaylenko <const@altlinux.ru> 3.06-alt1
- cumulative changes

* Thu Nov 11 2004 Constantin (Const) Mikhaylenko <const@altlinux.ru> 3.01-alt1
- Added:
  * Option "fragile" that allows the use of overlays together with verbatims. 
    *Extremely* useful.
  * Added option "T" to columns command/environment for alignment of
    top of first lines instead of baselines of first lines.
  * Added a color theme (dolphin) and a presentation theme
    (Boadilla) due to Manuel Carro.
  Bugfixes.

* Wed Oct 27 2004 Constantin (Const) Mikhaylenko <const@altlinux.ru> 3.00-alt1
- initial release for Sisyphus
