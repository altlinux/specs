# Generated File.
%setup_docs_module linux_navigation ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Work with files
Summary(ru_RU.KOI8-R): Работа с файлами
License: %fdl
Url: http://heap.altlinux.ru/kirill/linux_navigation/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-linux_navigation-kirill
Provides: docs-linux_navigation-kirill
Obsoletes: docs-linux_navigation-kirill

Source: %name-%version.tar

%description
Short introduction into work with files in Linux shell.

%description -l ru_RU.KOI8-R
Краткое введение по ``навигации'' в командной оболочке Linux: основы работы с файлами и каталогами.

%prep
%setup

%build
%docs_module_build "m-k" "index.m-k"

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
- replaces docs-linux_navigation-kirill
  + added Provides/Obsoletes

* Mon Apr 07 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-linux_navigation-kirill package

* Fri Mar 24 2006 Kirill Maslinsky <kirill@altlinux.ru> 060324-alt1
- Auto rebuild with new version.

* Mon Mar 13 2006 Kirill Maslinsky <kirill@altlinux.ru> 060313-alt1
- Initial build for Sisyphus

