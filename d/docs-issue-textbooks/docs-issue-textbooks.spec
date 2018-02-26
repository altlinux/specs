%setup_docs_issue textbooks

Name: %packagename
Version: 0.1
Release: alt2
Group: Books/Other

Summary: Free textbooks on open systems and Linux
Summary(ru_RU.KOI8-R): Учебники и пособия по Linux
License: %fdl

Buildarch: noarch
BuildRequires(pre): rpm-build-docs-experimental >= 0.4
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%docs_issue_requires

%description
Free textbooks on open systems and Linux

%description -l ru_RU.KOI8-R
В этом выпуске собрано несколько свободно распространяемых учебников, в которых широко используется материал открытых операционных систем, в том числе (и зачастую в первую очередь) -- Linux.

%prep
%setup

%build
%docs_issue_build 

%install
%docs_issue_install

%files
%docs_issue_files

%post
%docs_issue_postin

%postun
%docs_issue_postun

%changelog
* Fri Jan 25 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- depends on modules without commiter_id

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.1-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Thu Nov 10 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.1-alt1
- initial release

