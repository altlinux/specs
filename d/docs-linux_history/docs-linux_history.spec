# Generated File.
%setup_docs_module linux_history ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Linux history: From kernel to distributions
Summary(ru_RU.KOI8-R): История Linux: от ядра к дистрибутивам
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-linux_history-kirill
Provides: docs-linux_history-kirill = 051012-alt1.1
Obsoletes: docs-linux_history-kirill <= 051012-alt1.1

Source: %name-%version.tar

%description
Concise Linux history since the beginning of kernel development,
history of distributions and localization (Russian).

%description -l ru_RU.KOI8-R
Кратко изложена история разработки ядра Linux, появления и развития дистрибутивов, русификации Linux.

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
* Sat Mar 29 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-linux_history-kirill
  + added Provides/Obsoletes

* Wed Jan 16 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-linux_history-kirill package

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 051012-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Wed Oct 12 2005 Kirill Maslinsky <kirill@altlinux.ru> 051012-alt1
- Auto rebuild with new version.

* Tue Oct 04 2005 Kirill Maslinsky <kirill@altlinux.ru> 050830-alt1.1
- Auto rebuild with new version.

* Wed Sep 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 050830-alt1
- Auto rebuild with new version.

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050717-alt2
-rebuilt with rpm-build-docs-0.4.2-alt3

* Sun Jul 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 050717-alt1
- initial build

