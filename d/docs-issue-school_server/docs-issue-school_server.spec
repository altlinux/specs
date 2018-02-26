%setup_docs_issue school_server

Name: %packagename
Version: 4.1
Release: alt4
Group: Books/Other

Summary: School Server guide
License: %fdl

Buildarch: noarch
BuildRequires(pre): rpm-build-docs-experimental >= 0.4
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%docs_issue_requires

%description
School Server guide.

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
* Fri Jan 23 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt4
- add hidden docs-raid_install module link

* Tue Jan 13 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt3
- add docs-tips_school_server module link

* Sat Dec 06 2008 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt2
- rename mediawiki/moodle user guide links

* Thu Nov 20 2008 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt1
- initial build for Sisyphus

