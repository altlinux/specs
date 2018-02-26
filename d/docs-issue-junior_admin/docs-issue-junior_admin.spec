%setup_docs_issue junior_admin

Name: %packagename
Version: 0.1
Release: alt2

Summary: ALT Linux 4.0 Junior admin guide
License: %fdl

Buildarch: noarch
BuildRequires(pre): rpm-build-docs-experimental >= 0.4
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%docs_issue_requires

%description
ALT Linux 4.0 Junior admin guide.

%prep
%setup

%build
%docs_issue_build

%install
%docs_issue_install

%post
%docs_issue_postin

%postun
%docs_issue_postun

%files
%docs_issue_files

%changelog
* Mon Jan 28 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- depends on modules without commiter_id

* Thu Dec 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus

