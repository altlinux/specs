Name: gforth
%define Name GNU Forth
Version: 0.7.3
Release: alt2
License: %gpl3plus
Group: Development/Other
Summary: GNU implementation of the ANS Forth language
Summary(uk_UA.UTF-8): GNU-реалізація мови програмування ANS Forth
Summary(ru_RU.UTF-8): GNU-реализация языка программирования ANS Forth
Url: http://www.gnu.org/software/gforth/
Source0: %name-%version.tar
Source1: %name-16.png
Source2: %name-32.png
Source3: %name-48.png

Patch01: 01-script-hashbang.patch
Patch02: 02-skip-install.patch
Patch03: 03-hppa-build.patch
Patch04: 04-minus-number.patch
Patch05: 05-distclean.patch
Patch06: 06-configure-assumptions.patch
Patch07: 07-manpage.patch
Patch08: 08-qrnnd-build.patch
Patch09: 09-alt-elisp-auto-mode.patch
Patch10: 10-engine-subst.patch
Patch11: 11-static-newline.patch

BuildRequires(pre): rpm-build-licenses
Requires: %name-doc-txt

# Automatically added by buildreq on Wed Jan 20 2016
# optimized out: emacs-base emacs-common gnu-config libX11-locales libp11-kit perl-Encode perl-Text-Unidecode perl-Unicode-EastAsianWidth perl-Unicode-Normalize perl-libintl perl-unicore tex-common texlive-base texlive-base-bin texlive-common texlive-generic-recommended texlive-latex-base texlive-latex-recommended
BuildRequires: emacs-nox emacs24-speedbar libffi-devel libltdl7-devel makeinfo openssh-clients texi2dvi

BuildRequires: texlive-latex-recommended

%description
%Name is a fast and portable implementation of the ANS Forth
language. It works nicely with the Emacs editor, offers some nice
features such as input completion and history, backtraces, a decompiler
and a powerful locals facility. Gforth combines traditional
implementation techniques with newer techniques for portability and
performance: its inner intnerpreter is direct threaded with several
optimizations, but you can also use a traditional-style indirect
threaded interpreter.

%description -l uk_UA.UTF-8
%Name - швидка і портабельна реалізація мови програмування
ANS Forth. Він добре працює з редактором Emacs, пропонує деякі гарні
особливості, такі як завершення та історію вводу, зворотній хід,
детранслятор і потужний локальні можливості. Для портабельності та
продуктивності Gforth поєднує традиційні засоби реалізації з новими:
його внутрішній інтерпретатор - прямий з деякими оптимізаціями, але
також є можливість використання традиційного непрямого інтерпретатора.

%description -l ru_RU.UTF-8
%Name - быстрая и портабельная реализация языка программирования
ANS Forth. Он хорошо работает с редактором Emacs, предлагает некоторые
приятные особенности, такие как завершение и историю ввода, обратный
ход, детранслятор и мощные локальные возможности. Для портабельности и
производительности Gforth сочетает традиционные способы реализации с
новыми: его внутренний интерпретатор - прямой с некоторыми
оптимизациями, но также есть возможность использования традиционного
непрямого интерпретатора.

%package info
Group: Documentation
Summary: Documentation for the %Name in Info format
BuildArch: noarch
License: %fdl

%description info
%Name is a fast and portable implementation of the ANS Forth
language. It works nicely with the Emacs editor, offers some nice
features such as input completion and history, backtraces, a decompiler
and a powerful locals facility. Gforth combines traditional
implementation techniques with newer techniques for portability and
performance: its inner intnerpreter is direct threaded with several
optimizations, but you can also use a traditional-style indirect
threaded interpreter.

This package contains documentation for the %Name in Info format.

%description info -l uk_UA.UTF-8
%Name - швидка і портабельна реалізація мови програмування
ANS Forth. Він добре працює з редактором Emacs, пропонує деякі гарні
особливості, такі як завершення та історію вводу, зворотній хід,
детранслятор і потужний локальні можливості. Для портабельності та
продуктивності Gforth поєднує традиційні засоби реалізації з новими:
його внутрішній інтерпретатор - прямий з деякими оптимізаціями, але
також є можливість використання традиційного непрямого інтерпретатора.

%description info -l ru_RU.UTF-8
%Name - быстрая и портабельная реализация языка программирования
ANS Forth. Он хорошо работает с редактором Emacs, предлагает некоторые
приятные особенности, такие как завершение и историю ввода, обратный
ход, детранслятор и мощные локальные возможности. Для портабельности и
производительности Gforth сочетает традиционные способы реализации с
новыми: его внутренний интерпретатор - прямой с некоторыми
оптимизациями, но также есть возможность использования традиционного
непрямого интерпретатора.

%package doc-ps
Group: Documentation
Summary: Documentation for the %Name in Postscript format
BuildArch: noarch
License: %fdl

%description doc-ps
%Name is a fast and portable implementation of the ANS Forth
language. It works nicely with the Emacs editor, offers some nice
features such as input completion and history, backtraces, a decompiler
and a powerful locals facility. Gforth combines traditional
implementation techniques with newer techniques for portability and
performance: its inner intnerpreter is direct threaded with several
optimizations, but you can also use a traditional-style indirect
threaded interpreter.

This package contains documentation for the %Name in Postscript format.

%description doc-ps -l uk_UA.UTF-8
%Name - швидка і портабельна реалізація мови програмування
ANS Forth. Він добре працює з редактором Emacs, пропонує деякі гарні
особливості, такі як завершення та історію вводу, зворотній хід,
детранслятор і потужний локальні можливості. Для портабельності та
продуктивності Gforth поєднує традиційні засоби реалізації з новими:
його внутрішній інтерпретатор - прямий з деякими оптимізаціями, але
також є можливість використання традиційного непрямого інтерпретатора.

%description doc-ps -l ru_RU.UTF-8
%Name - быстрая и портабельная реализация языка программирования
ANS Forth. Он хорошо работает с редактором Emacs, предлагает некоторые
приятные особенности, такие как завершение и историю ввода, обратный
ход, детранслятор и мощные локальные возможности. Для портабельности и
производительности Gforth сочетает традиционные способы реализации с
новыми: его внутренний интерпретатор - прямой с некоторыми
оптимизациями, но также есть возможность использования традиционного
непрямого интерпретатора.

%package doc-html
Group: Documentation
Summary: Documentation for the %Name in HTML format
BuildArch: noarch
License: %fdl

%description doc-html
%Name is a fast and portable implementation of the ANS Forth
language. It works nicely with the Emacs editor, offers some nice
features such as input completion and history, backtraces, a decompiler
and a powerful locals facility. Gforth combines traditional
implementation techniques with newer techniques for portability and
performance: its inner intnerpreter is direct threaded with several
optimizations, but you can also use a traditional-style indirect
threaded interpreter.

This package contains documentation for the %Name in HTML format.

%description doc-html -l uk_UA.UTF-8
%Name - швидка і портабельна реалізація мови програмування
ANS Forth. Він добре працює з редактором Emacs, пропонує деякі гарні
особливості, такі як завершення та історію вводу, зворотній хід,
детранслятор і потужний локальні можливості. Для портабельності та
продуктивності Gforth поєднує традиційні засоби реалізації з новими:
його внутрішній інтерпретатор - прямий з деякими оптимізаціями, але
також є можливість використання традиційного непрямого інтерпретатора.

%description doc-html -l ru_RU.UTF-8
%Name - быстрая и портабельная реализация языка программирования
ANS Forth. Он хорошо работает с редактором Emacs, предлагает некоторые
приятные особенности, такие как завершение и историю ввода, обратный
ход, детранслятор и мощные локальные возможности. Для портабельности и
производительности Gforth сочетает традиционные способы реализации с
новыми: его внутренний интерпретатор - прямой с некоторыми
оптимизациями, но также есть возможность использования традиционного
непрямого интерпретатора.

%package doc-txt
Group: Documentation
Summary: Documentation for the %Name in HTML format
BuildArch: noarch
License: %fdl

%description doc-txt
%Name is a fast and portable implementation of the ANS Forth
language. It works nicely with the Emacs editor, offers some nice
features such as input completion and history, backtraces, a decompiler
and a powerful locals facility. Gforth combines traditional
implementation techniques with newer techniques for portability and
performance: its inner intnerpreter is direct threaded with several
optimizations, but you can also use a traditional-style indirect
threaded interpreter.

This package contains documentation for the %Name in ASCII text format.

%description doc-txt -l uk_UA.UTF-8
%Name - швидка і портабельна реалізація мови програмування
ANS Forth. Він добре працює з редактором Emacs, пропонує деякі гарні
особливості, такі як завершення та історію вводу, зворотній хід,
детранслятор і потужний локальні можливості. Для портабельності та
продуктивності Gforth поєднує традиційні засоби реалізації з новими:
його внутрішній інтерпретатор - прямий з деякими оптимізаціями, але
також є можливість використання традиційного непрямого інтерпретатора.

%description doc-txt -l ru_RU.UTF-8
%Name - быстрая и портабельная реализация языка программирования
ANS Forth. Он хорошо работает с редактором Emacs, предлагает некоторые
приятные особенности, такие как завершение и историю ввода, обратный
ход, детранслятор и мощные локальные возможности. Для портабельности и
производительности Gforth сочетает традиционные способы реализации с
новыми: его внутренний интерпретатор - прямой с некоторыми
оптимизациями, но также есть возможность использования традиционного
непрямого интерпретатора.

%package doc-pdf
Group: Documentation
Summary: Documentation for the %Name in PDF format
BuildArch: noarch
License: %fdl

%description doc-pdf
%Name is a fast and portable implementation of the ANS Forth
language. It works nicely with the Emacs editor, offers some nice
features such as input completion and history, backtraces, a decompiler
and a powerful locals facility. Gforth combines traditional
implementation techniques with newer techniques for portability and
performance: its inner intnerpreter is direct threaded with several
optimizations, but you can also use a traditional-style indirect
threaded interpreter.

This package contains documentation for the %Name in PDF format.

%description doc-pdf -l uk_UA.UTF-8
%Name - швидка і портабельна реалізація мови програмування
ANS Forth. Він добре працює з редактором Emacs, пропонує деякі гарні
особливості, такі як завершення та історію вводу, зворотній хід,
детранслятор і потужний локальні можливості. Для портабельності та
продуктивності Gforth поєднує традиційні засоби реалізації з новими:
його внутрішній інтерпретатор - прямий з деякими оптимізаціями, але
також є можливість використання традиційного непрямого інтерпретатора.

%description doc-pdf -l ru_RU.UTF-8
%Name - быстрая и портабельная реализация языка программирования
ANS Forth. Он хорошо работает с редактором Emacs, предлагает некоторые
приятные особенности, такие как завершение и историю ввода, обратный
ход, детранслятор и мощные локальные возможности. Для портабельности и
производительности Gforth сочетает традиционные способы реализации с
новыми: его внутренний интерпретатор - прямой с некоторыми
оптимизациями, но также есть возможность использования традиционного
непрямого интерпретатора.

%package -n emacs-mode-%name
Summary: %Name mode for GNU Emacs
Group: Editors
BuildArch: noarch
Requires: emacs-base

%description -n emacs-mode-%name
%Name mode for GNU Emacs.

%package -n emacs-mode-%name-el
Summary: The Emacs Lisp sources for bytecode included in emacs-mode-%name
Group: Editors
BuildArch: noarch
Requires: emacs-base

%description -n emacs-mode-%name-el
The Emacs Lisp sources for bytecode included in emacs-mode-%name.

%define docdir %_defaultdocdir/%name-%version

%prep
%setup
%patch01 -p1
%patch04 -p1
# ?? 06-configure-assumptions.patch
%patch07 -p1
%patch09

cat > %name.desktop <<__MENU__
[Desktop Entry]
GenericName=Gforth
Name=%Name shell
Name[uk]=%Name оболонка
Name[ru]=%Name оболочка
Exec=%name
Icon=%name
Type=Application
Terminal=true
Categories=Development;IDE;ConsoleOnly;
__MENU__

%ifarch x86_64
sed -i '/^#!/s@.*@%_datadir/%name/%version/kernl64l.fi@' filedump.fs
%else
%ifarch %ix86
sed -i '/^#!/s@.*@%_datadir/%name/%version/kernl32l.fi@' filedump.fs
%else
sed -i '/^#!/s@.*@%_datadir/%name/%version/kernel.fi@' filedump.fs
%endif
%endif

%build
#add_optflags -fno-reorder-blocks
%autoreconf
%configure
%make
%make TAGS
%make info doc pdf

cat << EOF > path.el
(setq load-path (cons "." load-path) byte-compile-warnings nil)
EOF
emacs --no-site-file -q -batch -l path.el -f batch-byte-compile gforth.el

%install
%makeinstall
# fixing pathes
mv %buildroot%_datadir/%name/%version/arch/{,i}386

cat > %buildroot%_datadir/%name/site-forth/siteinit.fs <<__EOF__
\ If you change this file, you need to recompile gforth.fi
__EOF__
chmod 0755 %buildroot%_datadir/%name/%version/{httpd,filedump,sieve}.fs

# icons
install -D -m 0644 %SOURCE1 %buildroot/%_miconsdir/%name.png
install -D -m 0644 %SOURCE2 %buildroot/%_niconsdir/%name.png
install -D -m 0644 %SOURCE3 %buildroot/%_liconsdir/%name.png

#menu
install -D %name.desktop %buildroot%_desktopdir/%name.desktop

install -Dm 0644 %name.el %buildroot%_datadir/emacs/site-lisp/%name.el
install -Dm 0644 %name.elc %buildroot%_datadir/emacs/site-lisp/%name.elc

mkdir -p %buildroot%docdir
cp [ABCINRT]* %buildroot%docdir/
cd doc
cp -a *.ps *.txt *.doc *.pdf gforth vmgen %buildroot%docdir
cd %buildroot%_datadir/%name/%version

%files
%doc %docdir/[ABCINRT]*
%_bindir/*
%_libdir/%name
%dir %_datadir/%name
%dir %_datadir/%name/%version
%_datadir/%name/%version/*
%dir %_datadir/%name/site-forth
%_datadir/%name/site-forth/*
%_man1dir/*
%_niconsdir/*
%_liconsdir/*
%_miconsdir/*
%_desktopdir/*
%_includedir/gforth/%version

%files info
%_infodir/*

%files doc-ps
%docdir/*.ps

%files doc-html
%docdir/gforth
%docdir/vmgen

%files doc-txt
%docdir/*.txt
%docdir/*.doc

%files doc-pdf
%docdir/*.pdf

%files -n emacs-mode-%name
%_emacslispdir/*.elc

%files -n emacs-mode-%name-el
%_emacslispdir/*.el

%changelog
* Wed Jan 20 2016 Fr. Br. George <george@altlinux.ru> 0.7.3-alt2
- Fix build

* Wed Aug 20 2014 Fr. Br. George <george@altlinux.ru> 0.7.3-alt1
- Autobuild version bump to 0.7.3
- Fix patch
- Fix spec typo

* Thu Apr 04 2013 Fr. Br. George <george@altlinux.ru> 0.7.2-alt1
- Autobuild version bump to 0.7.2
- Siplify build
- Fix patches

* Tue Dec 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt10.qa2
- Disabled build docs (broken)

* Fri Nov 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.6.2-alt10.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for gforth-info
  * postclean-05-filetriggers for spec file

* Sun Feb 01 2009 Led <led@altlinux.ru> 0.6.2-alt10
- cleaned up spec

* Mon Nov 10 2008 Led <led@altlinux.ru> 0.6.2-alt9
- fixed build with gcc 4.3

* Mon Aug 11 2008 Led <led@altlinux.ru> 0.6.2-alt8
- fixed %name.desktop
- added %name-0.6.2-emacs.patch
- moved emacs mode files to subpackages

* Tue Mar 04 2008 Led <led@altlinux.ru> 0.6.2-alt7
- fixed %name.desktop

* Thu Jun 07 2007 Led <led@altlinux.ru> 0.6.2-alt6
- updated %name-0.6.2-doc.patch
- cleaned up spec
- added patches from Fedora 7:
  + %name-shebang.patch
  + %name-0.6.2-buildpath.patch
  + %name.patch
- removed %name-doc-dvi subpackage

* Thu Mar 30 2006 Led <led@altlinux.ru> 0.6.2-alt5
- fixed %%changelog

* Mon Mar 27 2006 Led <led@altlinux.ru> 0.6.2-alt4
- fixed spec
- removed -mtune=pentium4 from %%optflags

* Fri Feb 17 2006 Led <led@altlinux.ru> 0.6.2-alt3
- apdeted %name-0.6.2-doc.patch

* Fri Feb 03 2006 Led <led@altlinux.ru> 0.6.2-alt2
- added 0.6.2-debug.diff

* Mon Jan 30 2006 Led <led@altlinux.ru> 0.6.2-alt1
- initial build
