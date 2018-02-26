Packager: Repocop Q. A. Robot <repocop@altlinux.org>
Version: 1.1
Release: alt2.1
#Epoch: %(date +%%Y%%m%%d)
Name: emacs-xtla
License: GPL
Group: Editors
Url: https://gna.org/projects/xtla-el
Summary: %name is an Emacs interface for GNU Arch (tla).
Summary(ru_RU.KOI8-R): %name это пакет для интеграции Emacs с системой контроля версий GNU Arch (tla).
Requires: emacs-common tla
Source: xtla-%version.tar.gz
Source1: xtla-emacs.el

Provides: xtla
BuildArch: noarch


# Automatically added by buildreq on Thu Jan 06 2005
BuildRequires: emacs-common tla emacs-gnus

%description
%name is an Emacs interface for GNU Arch (tla). It is similar to PCL-CVS 
for CVS or PSVN to Subversion. The interface should give the user full 
access to the functionality of tla within Emacs. 

All Emacs Lisp code is byte-copmpiled, install %name-el for sources.

%description -l ru_RU.KOI8-R
Пакет %name для интергации Emacs с системой контроля версий GNU Arch (tla).
По набору команд данный пакет схож с PCL-CVS для CVS или PSVN для Subversion.
Данный пакет предоставляет пользователю полный спектр команд для работы 
с репозиториями GNU Arch из Emacs.

Весь код на Emacs Lisp откомпилирован, для получения исходных текстов установите
пакет %name-el

%package el
Summary: The Emacs Lisp sources for bytecode included in %name
Group: Development/Other
Requires: %name = %version-%release

%description el
%name-el contains the Emacs Lisp sources for the bytecode
included in the %name package, that extends the Emacs editor.

You need to install %name-el only if you intend to modify any of the
%name code or see some Lisp examples.

%description el -l ru_RU.KOI8-R
Пакет %name-el содержит исходные тексты для пакета %name, который
является дополнением к редактору Emacs.

%name-el необходим вам только, если вы собираетесь изменять файлы
входящие в %name, или хотите посмотреть некоторые примеры.

%prep
%setup -n xtla-%version

%build
%configure --prefix=%prefix --with-lispdir=%_emacslispdir/xtla --with-emacs=emacs 
%make_build

%install
%__mkdir -p %buildroot%_emacslispdir/xtla
%__install -m 644 lisp/*.el* %buildroot%_emacslispdir/xtla

%__mkdir -p %buildroot%_infodir
%__install -m 644 texinfo/*.info %buildroot%_infodir

%__mkdir -p %buildroot/etc/emacs/site-start.d
%__install -m 644 %SOURCE1 %buildroot/etc/emacs/site-start.d/xtla.el

%files
%doc ChangeLog COPYING docs/*
%_infodir/*
%_emacslispdir/xtla/*.elc
%config(noreplace) /etc/emacs/site-start.d/*

%files el
%_emacslispdir/xtla/*.el

%changelog
* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2.1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for emacs-xtla

* Tue Mar 14 2006 Maxim Tyurin <mrkooll@altlinux.ru> 1.1-alt2
- Fix requires

* Wed Aug 10 2005 Maxim Tyurin <mrkooll@altlinux.ru> 1.1-alt1
- New version

* Thu Jan 06 2005 Maxim Tyurin <mrkooll@altlinux.ru> 0.9-alt1
- Initial build

