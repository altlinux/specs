Version: 0.4.8
Release: alt2
Name: emacs-mmm-mode
Copyright: GPL
Group: Editors
Url: http://mmm-mode.sourceforge.net/
Summary: Multiple Major Modes in Emacs
Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>
Requires: emacs-common 
Source: mmm-mode-%{version}.tar.gz
Source1: mmm-emacs.el

BuildArch: noarch

# Automatically added by buildreq on Thu Jul 18 2002
BuildRequires: emacs-common 

%description
MMM Mode is a minor mode for Emacs that allows Multiple Major Modes
(hence the name) to coexist in one buffer.  It is particularly
well-suited to editing embedded code, such as Mason server-side
Perl, or HTML output in CGI scripts.

%description -l ru_RU.CP1251
Режим MMM является вспомогательным режимом для Emacs, позволяющим использовать 
несколько основных режимов в одном буфере. В частности он удобен для редактирования
встроенного кода, такого как код на Perl в Mason или другого.

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

%description el -l ru_RU.CP1251
Пакет %name-el содержит исходные тексты для пакета %name, который 
является дополнением к редактору Emacs.

%name-el необходим вам только, если вы собираетесь изменять файлы
входящие в %name, или хотите посмотреть некоторые примеры.

%prep
%setup -n mmm-mode-%{version}

%build
./configure --prefix=%{_prefix} --infodir=%{_infodir} --with-emacs
make 

%install
mkdir -p $RPM_BUILD_ROOT%{_emacslispdir}/mmm
install -m 644 *.el* $RPM_BUILD_ROOT%{_emacslispdir}/mmm

mkdir -p $RPM_BUILD_ROOT%{_infodir}
install -m 644 *.info* $RPM_BUILD_ROOT%{_infodir}

mkdir -p $RPM_BUILD_ROOT/etc/emacs/site-start.d
install -m 644 %SOURCE1 $RPM_BUILD_ROOT/etc/emacs/site-start.d/mmm.el

%files
%defattr(-, root, root)
%doc AUTHORS FAQ INSTALL README* TODO NEWS
%dir %{_emacslispdir}/mmm/
%{_emacslispdir}/mmm/*.elc
/etc/emacs/site-start.d/*
%{_infodir}/*

%files el
%{_emacslispdir}/mmm/*.el

%changelog
* Sat Oct 24 2009 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt2
- applied repocop patch: removed obsolete (un)install_info macros

* Wed Jan 11 2006 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt1
- updated url; now maintained by Emacs Maintainers Team
- new version

* Mon Feb 17 2003 Ott Alex <ott@altlinux.ru> 0.4.7-alt5
- Fixing spec file

* Sat Feb 08 2003 Ott Alex <ott@altlinux.ru> 0.4.7-alt4
- fixing spec

* Wed Oct 09 2002 Ott Alex <ott@altlinux.ru> 0.4.7-alt2
- Fixing patch

* Fri Sep 20 2002 Ott Alex <ott@altlinux.ru> 0.4.7-alt1
- Initial build


