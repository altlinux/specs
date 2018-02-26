# Generated File.
%setup_docs_module linux_processes ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Processes and job control
Summary(ru_RU.KOI8-R): Процессы и управление заданиями
License: %gpl2plus
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses

# replace docs-linux_processes-kirill
Provides: docs-linux_processes-kirill
Obsoletes: docs-linux_processes-kirill

Source: %name-%version.tar

%description
Section fromm introductory textbook in Linux: main utilities for process management and job control in shell.

%description -l ru_RU.KOI8-R
Раздел вводного учебника по Linux: основные утилиты управления процессами и управление заданиями в shell.

%prep
%setup

%build
%docs_module_build "DocBook/XML" "processes.xml"

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
- replaces docs-linux_processes-kirill
  + added Provides/Obsoletes

* Mon Apr 07 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-linux_processes-kirill package

* Mon Mar 13 2006 Kirill Maslinsky <kirill@altlinux.ru> 060313-alt1
- Auto rebuild with new version.

* Mon Feb 06 2006 Kirill Maslinsky <kirill@altlinux.ru> 060202-alt1
- Auto build with new version.

