# Stolen from docs-alterator_apt-kirill.spec
%setup_docs_module ve_management ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Management of virtual servers
Summary(ru_RU.KOI8-R): Развертывание виртуальных серверов
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-ve_management-kirill
Provides: docs-ve_management-kirill = 1.0-alt1
Obsoletes: docs-ve_management-kirill <= 1.0-alt1

Source: %name-%version.tar

%description
Description of virtual server management by use of web-interface

%description -l ru_RU.KOI8-R
Описание управления виртуальными серверами при помогщи веб-интерфейса

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
- replaces docs-ve_management-kirill
  + added Provides/Obsoletes

* Thu Feb 07 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-ve_management-kirill package

* Fri May 18 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 1.0-alt1
- First build for Sisyphus
