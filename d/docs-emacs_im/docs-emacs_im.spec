# Generated File.
%setup_docs_module emacs_im ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Emacs and instant messaging tools
Summary(ru_RU.KOI8-R): Emacs и средства интерактивного общения
License: %fdl
Url: http://xtalk.msk.su/~ott/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-emacs-im-kirill
Provides: docs-emacs-im-kirill
Obsoletes: docs-emacs-im-kirill

Source: %name-%version.tar

%description
Manual on using Emacs for instant messaging: ICQ, Yahoo! Chat, AIM, Jabber, IRC.

%description -l ru_RU.KOI8-R
Руководство по использованию Emacs для интерактивного общения: ICQ, Yahoo! Chat, AIM, Jabber, IRC.

%prep
%setup

%build
%docs_module_build "DocBook/XML" "emacs-im.ru.xml"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Tue Apr 15 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-emacs-im-kirill
  + added Provides/Obsolete

* Tue Apr 15 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-emacs-im-kirill package

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 051010-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 14 2005 Kirill Maslinsky <kirill@altlinux.ru> 051010-alt1
- Auto build with new version.

