%setup_docs_module wine_intro ru

Name: %packagename
Version: 0.1.1
Release: alt1

Summary: Introductory manual to wine technology and usage
Summary(ru_RU.KOI8-R): WINE: среда для запуска win-приложений на платформе Unix
License: %fdl
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-wine_intro-kirill
Provides: docs-wine_intro-kirill = 060307-alt1
Obsoletes: docs-wine_intro-kirill <= 060307-alt1

Source: %name-%version.tar

%description
Introductory manual to wine technology and usage

%description -l ru_RU.KOI8-R
Объясняется, что такое WINE, как и для чего он может использоваться.

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
* Mon Jun 23 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- fixed typos
- used macro for License tag (rpm-build-licenses)

* Sat Mar 29 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-wine_intro-kirill
  + added Provides/Obsoletes

* Mon Jul 30 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-wine_intro-kirill package

* Mon Mar 06 2006 Kirill Maslinsky <kirill@altlinux.ru> 060307-alt1
- Auto rebuild with new version.

* Thu Jan 26 2006 Kirill Maslinsky <kirill@altlinux.ru> 060126-alt1
- Auto build with new version.

