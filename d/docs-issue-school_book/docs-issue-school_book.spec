%setup_docs_issue school_book

Name: docs-issue-school_book
Version: 4.0
Release: alt3

Summary: School Linux guide
License: %fdl

Buildarch: noarch
BuildRequires(pre): rpm-build-docs-experimental >= 0.4
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

# replace old separate school issues
Provides: docs-issue-school_install = %version
Provides: docs-issue-school_admin = %version
Provides: docs-issue-school_user = %version
Obsoletes: docs-issue-school_install < %version
Obsoletes: docs-issue-school_admin < %version
Obsoletes: docs-issue-school_user < %version


%docs_issue_requires

%description
School Linux guide (pdf version).

%prep
%setup

%build
%docs_issue_build

%install
mkdir -p %buildroot%_defaultdocdir/alt-docs/school_book/
cp block.pdf %buildroot%_defaultdocdir/alt-docs/school_book/
%docs_issue_install

%post
%docs_issue_postin

%postun
%docs_issue_postun

%files
%docs_issue_files

%changelog
* Mon Apr 20 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.0-alt3
- change link to school terminal install guide

* Sun Mar 29 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.0-alt2
- add link to school master install guide

* Fri Mar 27 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.0-alt1
- replace old separate school issues:
  + docs-issue-school_install
  + docs-issue-school_admin
  + docs-issue-school_user
- new version scheme: version = branch

* Fri Mar 27 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- add separate install guides

* Mon Jun 23 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus

