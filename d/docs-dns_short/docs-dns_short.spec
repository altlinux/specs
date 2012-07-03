# Generated File.
%setup_docs_module dns_short ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: DNS service (Bind)
Summary(ru_RU.KOI8-R): Служба DNS (Bind)
License: %fdl
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-dns_short-kirill
Provides: docs-dns_short-kirill = 050321-alt2
Obsoletes: docs-dns_short-kirill <= 050321-alt2

Source: %name-%version.tar

%description
Short description of installation and usage of DNS on Linux-machine.

%description -l ru_RU.KOI8-R
Кратко описано как организовать и использовать DNS на Linux-машине.

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "bind.xml"

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
- replaces docs-dns_short-kirill
  + added Provides/Obsoletes

* Mon Jan 14 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-dns_short-kirill package

* Fri May 18 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 050321-alt2
- New version from heap

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 050321-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 14 2005 Kirill Maslinsky <kirill@altlinux.ru> 050321-alt1
- Auto build with new version.

