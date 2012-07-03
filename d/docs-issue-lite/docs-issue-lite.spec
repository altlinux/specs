%setup_docs_issue lite

Name: %packagename
Version: 4.0
Release: alt1

Summary: ALT Linux 4.0 Lite user guide
License: %fdl

Buildarch: noarch
BuildRequires(pre): rpm-build-docs-experimental >= 0.4
BuildRequires(pre): rpm-build-licenses >= 0.6

Provides: docs-issue-desktop_lite = %version
Obsoletes: docs-issue-desktop_lite < %version

Source: %name-%version.tar

%docs_issue_requires

%description
ALT Linux 4.0 Lite user guide.

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
* Sun Mar 22 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.0-alt1
- new version scheme: version = branch
- fix Provides/Obsoletes list

* Wed Mar 19 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- new version:
  + fixed distro name: ALT Linux 4.0 Lite
  + fixed link to install_lite module
  + removed smc(www) mention
  + fixed russian smc name
  + used modules without commiter_id
- package renamed: docs-issue-desktop_lite -> docs-issue-lite
- spec modifications:
  + fixed distro name: ALT Linux 4.0 Lite
  + removed Packager tag
  + added missig "." in %%description

* Sat Nov 24 2007 Vladimir Zhukov <bertis@altlinux.org> 0.1-alt1
- initial build for Sisyphus
  + spec based on docs-issue-desktop_personal by @azol

