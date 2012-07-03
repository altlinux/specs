# Stolen from docs-alterator_apt-kirill.spec
%setup_docs_module vsftpd ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: FTP service
Summary(ru_RU.KOI8-R): Служба FTP
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-vsftpd-kirill
Provides: docs-vsftpd-kirill = 1.0-alt2
Obsoletes: docs-vsftpd-kirill <= 1.0-alt2

Source: %name-%version.tar

%description
Recommendations for ftp-server adjustment and secure running maintenance (vsftpd)

%description -l ru_RU.KOI8-R
Рекомендации по настройке и обеспечению безопасной работы FTP-сервера (vsftpd)

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "ftpd.xml"

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
- replaces docs-vsftpd-kirill
  + added Provides/Obsoletes

* Mon Jan 14 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-vsftpd-kirill package

* Fri May 25 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 1.0-alt2
- Build with updated version from branch heap

* Fri May 18 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 1.0-alt1
- First build for Sisyphus
