%setup_docs_module tips_school_server ru

Name: %packagename
Version: 4.1
Release: alt6

Summary: Tips for School Server
Summary(ru_RU.UTF-8): Советы по использованию дистрибутива Школьный Сервер
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires: asciidoc
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%description
Tips for School Server.

%description -l ru_RU.UTF-8
Советы по использованию дистрибутива Школьный Сервер.

%prep
%setup

%build
asciidoc -b html4 -f doc/html4.conf doc/index.txt
rm -f doc/html4.conf doc/index.txt
%docs_module_build "html" "index.html"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Fri Mar 20 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt6
- fix version in docinfo file

* Sun Feb 15 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt5
- add local repo mirror section

* Fri Jan 30 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt4
- add email client settings subsection (thx Vladimir Zhukov)
- proofreading of new sections (thx Vladimir Zhukov)

* Thu Jan 29 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt3
- add users section
- add OpenLDAP to autostart list

* Thu Jan 29 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt2
- add services state section
- fix typo

* Mon Jan 12 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt1
- initial build for Sisyphus
