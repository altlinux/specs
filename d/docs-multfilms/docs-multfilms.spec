# Generated File.
%setup_docs_module multfilms ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Self-made animation
Summary(ru_RU.KOI8-R): Самодельные мультфильмы
License: %fdl
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-multfilms-boyarsh
Provides: docs-multfilms-boyarsh
Obsoletes: docs-multfilms-boyarsh

Source: %name-%version.tar

%description
Short description of technology of making animations with objects.

%description -l ru_RU.KOI8-R
Краткое описание технологии самостоятельного изготовления кукольных мультфильмов

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
- replaces docs-multfilms-boyarsh
  + added Provides/Obsoletes

* Mon Apr 07 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-multfilms-boyarsh package

* Wed Mar 22 2006 Kirill Maslinsky <kirill@altlinux.ru> 060322-alt1
- Auto rebuild with new version.

* Tue Feb 21 2006 Kirill Maslinsky <kirill@altlinux.ru> 060221-alt1
- Initial build for Sisyphus.

