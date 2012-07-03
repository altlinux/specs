%setup_docs_module tips-office-server ru

%define _altdocsdir %_defaultdocdir/alt-docs

Name: docs-tips-office-server
Version: 5.0
Release: alt2

Summary: Tips for ALT Linux Server
Summary(ru_RU.UTF-8): Советы по использованию дистрибутива Альт Линукс Сервер
License: %fdl
Url: http://git.altlinux.org/people/azol/packages/docs-tips-office-server.git

Buildarch: noarch
BuildRequires: cmake
BuildRequires: asciidoc
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%description
Tips for ALT Linux Server.

%description -l ru_RU.UTF-8
Советы по использованию дистрибутива Альт Линукс Сервер.

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
* Fri Mar 20 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt2
- CMake driven build

* Fri Mar 20 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt1
- initial build for Sisyphus
  + based on docs-tips_school_server package

