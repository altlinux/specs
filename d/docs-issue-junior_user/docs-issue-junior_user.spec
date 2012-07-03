%setup_docs_issue junior_user

Name: %packagename
Version: 0.3
Release: alt1

Summary: ALT Linux 4.0 Junior user guide
License: %fdl

Buildarch: noarch
BuildRequires(pre): rpm-build-docs-experimental >= 0.4
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%docs_issue_requires

%description
ALT Linux 4.0 Junior user guide.

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
* Mon May 19 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.3-alt1
- added description:
  + Clam AntiVirus
  + Eclipse
  + Ark
  + Xarchiver
  + Audacity
  + Scilab
  + Maxima
  + KTurtle
  + Lazarus
  + KDevelop
  + Mozilla Thunderbird
  + Claws Mail
  + Quanta Plus
  + Bluefish

* Mon Jan 28 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- depends on modules without commiter_id
- added more sections (as placeholders)

* Thu Dec 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus

