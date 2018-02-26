%setup_docs_module whatis-office-server ru

%define _altdocsdir %_defaultdocdir/alt-docs

Name: docs-whatis-office-server
Version: 5.0
Release: alt2

Summary: What is ALT Linux Server
Summary(ru_RU.UTF-8): Что такое Альт Линукс Сервер
License: %fdl
Url: http://git.altlinux.org/people/azol/packages/docs-whatis-office-server.git

Buildarch: noarch
BuildRequires: cmake
BuildRequires: asciidoc
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%description
Description of ALT Linux Server distribution for customers.
No technical details.

%description -l ru_RU.UTF-8
Описание дистрибутива Альт Линукс Сервер.
Без технических подробностей, для пользователей/заказчиков.

%prep
%setup

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DDOC_DIR=%_altdocsdir/%modulename
%make_build
mkdir doc/
ln index.html doc/index.html
ln COPYING License
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
* Sun Mar 22 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt2
- fix Summary: (#19281)
- fix %%build cmake call

* Tue Feb 17 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt1
- initial build for Sisyphus
  + based on docs-whatis_school_server package

