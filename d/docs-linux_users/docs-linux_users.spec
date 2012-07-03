# Generated File.
%setup_docs_module linux_users ru

Name: %packagename
Version: 0.1
Release: alt3

Summary: Users in Linux
Summary(ru_RU.KOI8-R): Пользователи в Linux
License: %fdl
Url: http://heap.altlinux.ru/kirill/linux_users/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-linux_users-kirill, obsolete docs-users_in_linux-kirill
Provides: docs-linux_users-kirill
Obsoletes: docs-linux_users-kirill, docs-users_in_linux-kirill

Source: %name-%version.tar

%description
Short description into user accounts in Linux, comments on system configuration files for users and groups, utilities for managing users and group.

%description -l ru_RU.KOI8-R
Краткое введение в учётные записи Linux, пояснения по соответствующим файлам.

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
* Mon Apr 21 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt3
- obsoletes docs-users_in_linux-kirill
- fixed docinfo (Abstract)

* Sat Apr 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-linux_users-kirill
  + added Provides/Obsoletes

* Sun Jan 13 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-linux_users-kirill package

* Mon Mar 13 2006 Kirill Maslinsky <kirill@altlinux.ru> 060313-alt1
- Initial build for Sisyphus

