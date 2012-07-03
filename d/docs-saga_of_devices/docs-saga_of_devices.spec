%setup_docs_module saga_of_devices ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Devices in Linux (Saga of drivers)
Summary(ru_RU.KOI8-R): Работа с устройствами в Linux (Сага о Драйверах)
License: distributable
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3

# replace docs-Saga_of_Devices-george
Provides: docs-Saga_of_Devices-george
Obsoletes: docs-Saga_of_Devices-george

Source: %name-%version.tar

%description
How external devices are represented in Linux system and what is covered by "driver" notion.

%description -l ru_RU.KOI8-R
Как внешние устройства представляются в системе и что скрвыается за понятием "драйвер" в Linux

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
- replaces docs-Saga_of_Devices-george
  + added Provides/Obsoletes

* Mon Jul 30 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-Saga_of_Devices-george package

* Fri Mar 10 2006 Kirill Maslinsky <kirill@altlinux.ru> 0.002-alt1
- Auto rebuild with new version.

* Thu Feb 02 2006 Kirill Maslinsky <kirill@altlinux.ru> 0.001-alt1
- Auto build with new version.

