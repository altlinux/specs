# Generated File.
%setup_docs_module script_story ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: A story of one script
Summary(ru_RU.KOI8-R): История одного скрипта
License: %fdl
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-script_story-boyarsh
Provides: docs-script_story-boyarsh
Obsoletes: docs-script_story-boyarsh

Source: %name-%version.tar

%description
A history of writing  a script for photo collection management.

%description -l ru_RU.KOI8-R
Описание истории написания скрипта для поддержки коллекции фотографий

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
* Fri Apr 25 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-script_story-boyarsh
  + added Provides/Obsoletes

* Mon Apr 07 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-script_story-boyarsh package

* Fri Mar 24 2006 Kirill Maslinsky <kirill@altlinux.ru> 060322-alt2
- Auto rebuild with new version.

* Wed Mar 22 2006 Kirill Maslinsky <kirill@altlinux.ru> 060322-alt1
- Auto rebuild with new version.

* Tue Feb 21 2006 Kirill Maslinsky <kirill@altlinux.ru> 060221-alt1
- Initial build for Sisyphus

