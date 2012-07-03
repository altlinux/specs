Version: 20.7
Release: alt1.qa1
Name: emacs-manual-ru
Copyright: GPL
Group: Editors
Url: http://www.gnu.org.ru
Summary: Emacs Manual (Russian Translation) 
Summary(ru_RU.CP1251): Руководство по Emacs (Перевод на русский)
Requires: emacs-common
Source: %{name}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Jul 26 2002
BuildRequires: texinfo

%description
This package contain full description of Emacs version %{version}

%description -l ru_RU.CP1251
Это пакет содержит полное описание редактора Emacs версии %{version}.

%prep
%setup

%build
makeinfo emacs.texi

%install
mkdir -p $RPM_BUILD_ROOT%{_infodir}

install -m 644 *.info* $RPM_BUILD_ROOT%{_infodir}

%post
cd %{_infodir}

%preun
cd %{_infodir}

%files
%defattr(-, root, root)
%{_infodir}/*

%changelog
* Wed Dec 02 2009 Igor Vlasenko <viy@altlinux.ru> 20.7-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for emacs-manual-ru
  * postclean-05-filetriggers for spec file

* Mon Oct 28 2002 Ott Alex <ott@altlinux.ru> 20.7-alt1
- Initial build


