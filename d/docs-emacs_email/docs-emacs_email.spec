# Generated File.
%setup_docs_module emacs_email ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Using Emacs for mail and Usenet news reading
Summary(ru_RU.KOI8-R): Использование Emacs для работы с электронной почтой и новостями Usenet
License: distributable
Url: http://xtalk.msk.su/~ott/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3

# replace docs-EmacsEmail-kirill
Provides: docs-EmacsEmail-kirill
Obsoletes: docs-EmacsEmail-kirill

Source: %name-%version.tar

%description
Short description of Emacs usage for mail and Usenet news reading.

%description -l ru_RU.KOI8-R
Краткое описание использования Emacs для работы с почтой и новостями Usenet

%prep
%setup

%build
%docs_module_build "DocBook/XML" "altlinux-gnus.xml"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Sat Apr 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-EmacsEmail-kirill
  + added Provides/Obsoletes

* Sat Apr 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-EmacsEmail-kirill package

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 051114-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 14 2005 Kirill Maslinsky <kirill@altlinux.ru> 051114-alt1
- Auto build with new version.

