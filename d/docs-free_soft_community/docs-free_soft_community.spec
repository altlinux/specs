# Generated File.
%setup_docs_module free_soft_community ru

Name: %packagename
Version: 0.1.1
Release: alt1

Summary: Free Software and Community
Summary(ru_RU.KOI8-R): Свободные программы и сообщества
License: %fdl
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-FreeSoftCommunity-george
Provides: docs-FreeSoftCommunity-george
Obsoletes: docs-FreeSoftCommunity-george

Source: %name-%version.tar

%description
Community around a free source product: causes, conditions, merits and demerits.

%description -l ru_RU.KOI8-R
Сообщество вокруг свободного программного продукта: причины появления, условия существования, достоинства и недостатки

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
* Tue Sep 09 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- fixed typo in docinfo / spec (#17066)

* Sun Jun 01 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-FreeSoftCommunity-george
  + added Provides/Obsoletes

* Wed Jan 16 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-FreeSoftCommunity-george package

* Mon Mar 20 2006 Kirill Maslinsky <kirill@altlinux.ru> 1.009-alt1
- Auto rebuild with new version.

* Mon Feb 20 2006 Kirill Maslinsky <kirill@altlinux.ru> 1.006-alt1
- Initial build for Sisyphus.

