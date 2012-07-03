# Generated File.
%setup_docs_module firewall ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Network security
Summary(ru_RU.KOI8-R): Сетевая безопасность
License: %fdl
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-firewall-kirill
Provides: docs-firewall-kirill
Obsoletes: docs-firewall-kirill

Source: %name-%version.tar

%description
Short description of iptables 

%description -l ru_RU.KOI8-R
Краткое описание принципов работы iptables

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "firewall.xml"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Sat Apr 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-firewall-kirill
  + added Provides/Obsoletes

* Sat Apr 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-firewall-kirill package

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 051121-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 051121-alt1
- Auto rebuild with new version.

* Tue Nov 15 2005 Kirill Maslinsky <kirill@altlinux.ru> 051115-alt1
- Auto rebuild with new version.

* Mon Nov 14 2005 Kirill Maslinsky <kirill@altlinux.ru> 051114-alt1
- Auto build with new version.

