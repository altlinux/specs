%setup_docs_module openvz_basics ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Short introduction to OpenVZ
Summary(ru_RU.KOI8-R): Краткое введение в OpenVZ
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-openvz_basics-kirill
Provides: docs-openvz_basics-kirill = 1.0-alt2
Obsoletes: docs-openvz_basics-kirill <= 1.0-alt2

Source: %name-%version.tar

%description
Short manual for server infrastructure organisation using virtualization technology (OpenVZ)

%description -l ru_RU.KOI8-R
Краткое руководство по организации инфраструктуры сервера с использованием технологии виртуализации (OpenVZ)

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
- replaces docs-openvz_basics-kirill
  + added Provides/Obsoletes

* Tue Mar 25 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-openvz_basics-kirill package

* Mon Sep 10 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 1.0-alt2
- Fixed typo (#12737)

* Fri May 18 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 1.0-alt1
- First build for Sisyphus
