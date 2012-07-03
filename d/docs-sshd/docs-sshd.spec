# Stolen from docs-alterator_apt-kirill.spec
%setup_docs_module sshd ru

Name: %packagename
Version: 0.1.1
Release: alt1

Summary: Remote access and remote administration (OpenSSH)
Summary(ru_RU.KOI8-R): Удалённый доступ и удалённое администрирование (OpenSSH)
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-sshd-kirill
Provides: docs-sshd-kirill = 1.0-alt1
Obsoletes: docs-sshd-kirill <= 1.0-alt1

Source: %name-%version.tar

%description
Description of capacity and principles of remote administration by the use of OpenSSH (SSH technology realization)

%description -l ru_RU.KOI8-R
Описание возможностей и принципов удалённого администрирования при момощи OpenSSH - реализации технологии SSH

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
* Thu Sep 04 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- fixed typos
- replaced 'ie' with 'io'

* Sat Mar 29 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-sshd-kirill
  + added Provides/Obsoletes

* Mon Jan 14 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-sshd-kirill package

* Fri May 18 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 1.0-alt1
- First build for Sisyphus
