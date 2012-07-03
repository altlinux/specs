%setup_docs_module install_server ru

Name: docs-install_server
Version: 4.0
Release: alt3

Summary: ALT Linux Server Installation Guide
Summary(ru_RU.UTF-8): Руководство по установке ALT Linux Server
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace old docs-install[0-3]-kirill, docs-install_finish-kirill packages
Provides: docs-install0-kirill = %version
Provides: docs-install2-kirill = %version
Provides: docs-install3-kirill = %version
Provides: docs-install_finish-kirill = %version
Obsoletes: docs-install0-kirill <= %version
Obsoletes: docs-install2-kirill < %version
Obsoletes: docs-install3-kirill < %version
Obsoletes: docs-install_finish-kirill < %version

Source: %name-%version.tar

%description
ALT Linux Server Installation Guide.

%description -l ru_RU.UTF-8
Руководство по установке ALT Linux Server.

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
* Sat Mar 28 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.0-alt3
- update Version in docinfo file

* Sat Mar 28 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.0-alt2
- add docs-install_finish-kirill to Obsolete list

* Sat Mar 28 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.0-alt1
- replace old packages (add Provides/Obsoletes):
  + docs-install0-kirill
  + docs-install2-kirill
  + docs-install3-kirill
- new version scheme: version = branch
- use hardcoded Name: for better gear utilities support

* Tue Mar 25 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.4.1-alt1
- initial build for Sisyphus

