%setup_docs_module raid_install ru

Name: %packagename
Version: 0.1
Release: alt1

Summary: Install Linux on RAID
Summary(ru_RU.UTF-8): Установка Linux на RAID
License: Creative Commons - Attribution - Share Alike 3.0
URL: http://www.altlinux.org/Создание_и_установка_на_RAID

Buildarch: noarch
Requires: docs-utils
BuildRequires: asciidoc
BuildRequires(pre): rpm-build-docs-experimental >= 0.3

Source: %name-%version.tar

%description
Install Linux on RAID.

%description -l ru_RU.UTF-8
Установка Linux на RAID.

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
* Thu Jan 22 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
