%setup_docs_module whatis_school_server ru

Name: %packagename
Version: 4.1
Release: alt4

Summary: What is School Server
Summary(ru_RU.UTF-8): Что такое Школьный Сервер
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires: asciidoc
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%description
Description of School Server distribution for customers.
No technical details.

%description -l ru_RU.UTF-8
Описание дистрибутива Школьный Сервер.
Без технических подробностей, для пользователей/заказчиков.

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
* Tue Feb 17 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt4
- proofreading (thx Vladimir Zhukov)

* Mon Feb 16 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt3
- fix typos

* Sat Dec 06 2008 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt2
- add system requirements for moodle/mediawiki

* Thu Nov 20 2008 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt1
- initial build for Sisyphus
