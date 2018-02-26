# Generated File.
%setup_docs_module wifi_short ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: WiFi setup
Summary(ru_RU.KOI8-R): Настройка беспроводной сети
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-wifi_short-kirill
Provides: docs-wifi_short-kirill = 050321-alt4.1
Obsoletes: docs-wifi_short-kirill <= 050321-alt4.1

Source: %name-%version.tar

%description
Some hints on WiFi configuration

%description -l ru_RU.KOI8-R
Очень краткие рекомендации по настройке беспроводной сети

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "wifi.xml"

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
- replaces docs-wifi_short-kirill
  + added Provides/Obsoletes

* Thu Feb 07 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-wifi_short-kirill package

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 050321-alt4.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 14 2005 Kirill Maslinsky <kirill@altlinux.ru> 050321-alt4
- Auto rebuild with new rpm-build-docs.

* Tue Jun 14 2005 Alexey Gladkov <legion@altlinux.ru> 050321-alt3
- Requires bugfix;

* Mon Jun 06 2005 Alexey Gladkov <legion@altlinux.ru> 050321-alt2
- rebuild with new rpm-build-docs.

* Mon Apr 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050321-alt1
- initial build
