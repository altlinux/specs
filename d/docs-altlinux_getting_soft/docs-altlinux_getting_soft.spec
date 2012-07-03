# Generated File.
%setup_docs_module altlinux_getting_soft ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: How to get a Linux program
Summary(ru_RU.KOI8-R): Как получить нужную программу
License: %fdl
Url: http://heap.altlinux.ru/kirill/altlinux_getting_soft/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-altlinux_getting_soft-kirill
Provides: docs-altlinux_getting_soft-kirill
Obsoletes: docs-altlinux_getting_soft-kirill

Source: %name-%version.tar

%description
Procedure to find a required Linux program descripbed: from installed packages to distribution, to contrib, to unstable repository (Sisyphus). 

%description -l ru_RU.KOI8-R
Описана последовательность поиска нужного пакета в дистрибутиве, contrib, backports, Sisyphus.

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
- replaces docs-altlinux_getting_soft-kirill
  + added Provides/Obsoletes

* Sun Jan 13 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-altlinux_getting_soft-kirill package

* Mon Mar 13 2006 Kirill Maslinsky <kirill@altlinux.ru> 060313-alt1
- Initial build for Sisyphus

