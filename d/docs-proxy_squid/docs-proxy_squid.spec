# Generated File.
%setup_docs_module proxy_squid ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Caching proxy-server Squid
Summary(ru_RU.KOI8-R): Кеширующий прокси-сервер Squid
License: %fdl
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-proxy_squid-kirill
Provides: docs-proxy_squid-kirill = 050321-alt2
Obsoletes: docs-proxy_squid-kirill <= 050321-alt2

Source: %name-%version.tar

%description
Document describes proxy-server setup with Squid.

%description -l ru_RU.KOI8-R
В документе описано, как организовать прокси-сервер при помощи Squid.

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "squid.xml"

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
- replaces docs-proxy_squid-kirill
  + added Provides/Obsoletes

* Mon Jan 14 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-proxy_squid-kirill package

* Fri May 18 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 050321-alt2
- New version from heap

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 050321-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 14 2005 Kirill Maslinsky <kirill@altlinux.ru> 050321-alt1
- Auto build with new version.

