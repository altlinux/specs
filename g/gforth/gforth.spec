%def_enable largefile
%def_enable force_reg
%def_without debug
%def_with doc
#----------------------------------------------------------------------
%define subst_enable_to() %{expand:%%{?_enable_%{1}:--enable-%{2}}} %{expand:%%{?_disable_%{1}:--disable-%{2}}}

Name: gforth
%define Name GNU Forth
Version: 0.6.2
Release: alt10.qa1
License: %gpl2plus
Group: Development/Other
Summary: GNU implementation of the ANS Forth language
Summary(uk_UA.CP1251): GNU-реалізація мови програмування ANS Forth
Summary(ru_RU.CP1251): GNU-реализация языка программирования ANS Forth
URL: http://www.jwdt.com/~paysan/gforth.html
Source0: %name-%version.tar
Source1: %name-16.png
Source2: %name-32.png
Source3: %name-48.png
Patch: %name-%version-%release.patch
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
%{?_with_doc:BuildRequires: tetex-core tetex-dvips tetex-latex}
BuildRequires: %_bindir/emacs

%description
%Name is a fast and portable implementation of the ANS Forth
language. It works nicely with the Emacs editor, offers some nice
features such as input completion and history, backtraces, a decompiler
and a powerful locals facility. Gforth combines traditional
implementation techniques with newer techniques for portability and
performance: its inner intnerpreter is direct threaded with several
optimizations, but you can also use a traditional-style indirect
threaded interpreter.

%description -l uk_UA.CP1251
%Name - швидка і портабельна реалізація мови програмування
ANS Forth. Він добре працює з редактором Emacs, пропонує деякі гарні
особливості, такі як завершення та історію вводу, зворотній хід,
детранслятор і потужний локальні можливості. Для портабельності та
продуктивності Gforth поєднує традиційні засоби реалізації з новими:
його внутрішній інтерпретатор - прямий з деякими оптимізаціями, але
також є можливість використання традиційного непрямого інтерпретатора.

%description -l ru_RU.CP1251
%Name - быстрая и портабельная реализация языка программирования
ANS Forth. Он хорошо работает с редактором Emacs, предлагает некоторые
приятные особенности, такие как завершение и историю ввода, обратный
ход, детранслятор и мощные локальные возможности. Для портабельности и
производительности Gforth сочетает традиционные способы реализации с
новыми: его внутренний интерпретатор - прямой с некоторыми
оптимизациями, но также есть возможность использования традиционного
непрямого интерпретатора.


%if_with doc
%package info
Group: Documentation
Summary: Documentation for the %Name in Info format
BuildArch: noarch

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

%description info -l uk_UA.CP1251
%Name - швидка і портабельна реалізація мови програмування
ANS Forth. Він добре працює з редактором Emacs, пропонує деякі гарні
особливості, такі як завершення та історію вводу, зворотній хід,
детранслятор і потужний локальні можливості. Для портабельності та
продуктивності Gforth поєднує традиційні засоби реалізації з новими:
його внутрішній інтерпретатор - прямий з деякими оптимізаціями, але
також є можливість використання традиційного непрямого інтерпретатора.

Цей пакет містить документацію для %Name в форматі Info.

%description info -l ru_RU.CP1251
%Name - быстрая и портабельная реализация языка программирования
ANS Forth. Он хорошо работает с редактором Emacs, предлагает некоторые
приятные особенности, такие как завершение и историю ввода, обратный
ход, детранслятор и мощные локальные возможности. Для портабельности и
производительности Gforth сочетает традиционные способы реализации с
новыми: его внутренний интерпретатор - прямой с некоторыми
оптимизациями, но также есть возможность использования традиционного
непрямого интерпретатора.

Этот пакет содержит документацию для %Name в формате Info.


%package doc-ps
Group: Documentation
Summary: Documentation for the %Name in Postscript format
BuildArch: noarch

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

%description doc-ps -l uk_UA.CP1251
%Name - швидка і портабельна реалізація мови програмування
ANS Forth. Він добре працює з редактором Emacs, пропонує деякі гарні
особливості, такі як завершення та історію вводу, зворотній хід,
детранслятор і потужний локальні можливості. Для портабельності та
продуктивності Gforth поєднує традиційні засоби реалізації з новими:
його внутрішній інтерпретатор - прямий з деякими оптимізаціями, але
також є можливість використання традиційного непрямого інтерпретатора.

Цей пакет містить документацію для %Name в форматі Postscript.

%description doc-ps -l ru_RU.CP1251
%Name - быстрая и портабельная реализация языка программирования
ANS Forth. Он хорошо работает с редактором Emacs, предлагает некоторые
приятные особенности, такие как завершение и историю ввода, обратный
ход, детранслятор и мощные локальные возможности. Для портабельности и
производительности Gforth сочетает традиционные способы реализации с
новыми: его внутренний интерпретатор - прямой с некоторыми
оптимизациями, но также есть возможность использования традиционного
непрямого интерпретатора.

Этот пакет содержит документацию для %Name в формате Postscript.


%package doc-html
Group: Documentation
Summary: Documentation for the %Name in HTML format
BuildArch: noarch

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

%description doc-html -l uk_UA.CP1251
%Name - швидка і портабельна реалізація мови програмування
ANS Forth. Він добре працює з редактором Emacs, пропонує деякі гарні
особливості, такі як завершення та історію вводу, зворотній хід,
детранслятор і потужний локальні можливості. Для портабельності та
продуктивності Gforth поєднує традиційні засоби реалізації з новими:
його внутрішній інтерпретатор - прямий з деякими оптимізаціями, але
також є можливість використання традиційного непрямого інтерпретатора.

Цей пакет містить документацію для %Name в форматі HTML.

%description doc-html -l ru_RU.CP1251
%Name - быстрая и портабельная реализация языка программирования
ANS Forth. Он хорошо работает с редактором Emacs, предлагает некоторые
приятные особенности, такие как завершение и историю ввода, обратный
ход, детранслятор и мощные локальные возможности. Для портабельности и
производительности Gforth сочетает традиционные способы реализации с
новыми: его внутренний интерпретатор - прямой с некоторыми
оптимизациями, но также есть возможность использования традиционного
непрямого интерпретатора.

Этот пакет содержит документацию для %Name в формате HTML.


%package doc-txt
Group: Documentation
Summary: Documentation for the %Name in HTML format
BuildArch: noarch

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

%description doc-txt -l uk_UA.CP1251
%Name - швидка і портабельна реалізація мови програмування
ANS Forth. Він добре працює з редактором Emacs, пропонує деякі гарні
особливості, такі як завершення та історію вводу, зворотній хід,
детранслятор і потужний локальні можливості. Для портабельності та
продуктивності Gforth поєднує традиційні засоби реалізації з новими:
його внутрішній інтерпретатор - прямий з деякими оптимізаціями, але
також є можливість використання традиційного непрямого інтерпретатора.

Цей пакет містить документацію для %Name в тестовому ASCII форматі.

%description doc-txt -l ru_RU.CP1251
%Name - быстрая и портабельная реализация языка программирования
ANS Forth. Он хорошо работает с редактором Emacs, предлагает некоторые
приятные особенности, такие как завершение и историю ввода, обратный
ход, детранслятор и мощные локальные возможности. Для портабельности и
производительности Gforth сочетает традиционные способы реализации с
новыми: его внутренний интерпретатор - прямой с некоторыми
оптимизациями, но также есть возможность использования традиционного
непрямого интерпретатора.

Этот пакет содержит документацию для %Name в текстовом ASCII формате.


%package doc-pdf
Group: Documentation
Summary: Documentation for the %Name in PDF format
BuildArch: noarch

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

%description doc-pdf -l uk_UA.CP1251
%Name - швидка і портабельна реалізація мови програмування
ANS Forth. Він добре працює з редактором Emacs, пропонує деякі гарні
особливості, такі як завершення та історію вводу, зворотній хід,
детранслятор і потужний локальні можливості. Для портабельності та
продуктивності Gforth поєднує традиційні засоби реалізації з новими:
його внутрішній інтерпретатор - прямий з деякими оптимізаціями, але
також є можливість використання традиційного непрямого інтерпретатора.

Цей пакет містить документацію для %Name в форматі PDF.

%description doc-pdf -l ru_RU.CP1251
%Name - быстрая и портабельная реализация языка программирования
ANS Forth. Он хорошо работает с редактором Emacs, предлагает некоторые
приятные особенности, такие как завершение и историю ввода, обратный
ход, детранслятор и мощные локальные возможности. Для портабельности и
производительности Gforth сочетает традиционные способы реализации с
новыми: его внутренний интерпретатор - прямой с некоторыми
оптимизациями, но также есть возможность использования традиционного
непрямого интерпретатора.

Этот пакет содержит документацию для %Name в формате PDF.
%endif


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


%prep
%setup
%patch -p1


%build
# -mtune=pentium4 lead to compile error, using -mtune=pentium3 instead
%remove_optflags -mtune=pentium4
%add_optflags -fno-reorder-blocks
#add_optflags -mtune=pentium3
%autoreconf
%configure \
    --libdir=%_libexecdir \
    %{subst_enable largefile} \
    %{subst_with debug} \
    %{subst_enable_to force_reg force-reg}
%make
%make info TAGS %{?_with_doc:html ps pdf txt}
emacs -q --no-site-file -batch -f batch-byte-compile %name.el
bzip2 --force --best --keep ChangeLog


%install
%define docdir %_docdir/%name-%version
install -d %buildroot{%_datadir/emacs/site-lisp,%docdir}
install -m 0644 %name.el* %buildroot%_datadir/emacs/site-lisp/
%makeinstall libdir=%buildroot%_libexecdir
rm -f %buildroot%_infodir/dir
ln -sf %name.1 %buildroot%_man1dir/%name-fast.1
ln -sf %name.1 %buildroot%_man1dir/%{name}mi.1
install -m 0644 AUTHORS BUGS Benchres ChangeLog.* NEWS* README* ToDo %buildroot%docdir/
%{?_with_doc:install -m 0644 doc/*.{ps,html,txt,pdf} %buildroot%docdir/}

# fixing pathes
mv %buildroot%_datadir/%name/%version/arch/{,i}386

cat > %buildroot%_datadir/%name/site-forth/siteinit.fs <<__EOF__
\ If you change this file, you need to recompile gforth.fi
__EOF__
chmod 0755 %buildroot%_datadir/%name/%version/{httpd,filedump,sieve}.fs

# icons
install -d %buildroot{%_niconsdir,%_miconsdir,%_liconsdir}
install -m 0644 %SOURCE1 %buildroot/%_miconsdir/%name.png
install -m 0644 %SOURCE2 %buildroot/%_niconsdir/%name.png
install -m 0644 %SOURCE3 %buildroot/%_liconsdir/%name.png

#menu
install -d %buildroot%_desktopdir
iconv -f cp1251 -t utf-8 > %buildroot%_desktopdir/%name.desktop <<__MENU__
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


%files
%dir %docdir
%docdir/AUTHORS
%docdir/BUGS
%docdir/Benchres
%docdir/ChangeLog*
%docdir/NEWS*
%docdir/README*
%docdir/ToDo
%_bindir/*
%_libexecdir/%name
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


%files info
%_infodir/*


%if_with doc
%files doc-ps
%dir %docdir
%docdir/*.ps


%files doc-html
%dir %docdir
%docdir/*.html


%files doc-txt
%dir %docdir
%docdir/*.txt


%files doc-pdf
%dir %docdir
%docdir/*.pdf
%endif


%files -n emacs-mode-%name
%_emacslispdir/*.elc


%files -n emacs-mode-%name-el
%_emacslispdir/*.el


%changelog
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
