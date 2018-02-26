%setup_docs_issue junior_install

Name: %packagename
Version: 0.1
Release: alt2
Packager: ALT Docs Team <docs@packages.altlinux.org>

Summary: ALT Linux 4.0 Junior user guide
License: %fdl

Buildarch: noarch
BuildRequires(pre): rpm-build-docs-experimental >= 0.4
BuildRequires(pre): rpm-build-licenses >= 0.6


Source: %name-%version.tar

%docs_issue_requires

%description
ALT Linux 4.0 Junior user guide

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
* Thu Jan 17 2008 Vladimir Zhukov <bertis@altlinux.ru> 0.1-alt2
- Package rebuilt
	added missing references in index.html

* Fri Dec 14 2007 Kirill Maslinsky <kirill@altlinux.org> 0.1-alt1
- Initial build 
	based on package docs-issue-desktop_lite

