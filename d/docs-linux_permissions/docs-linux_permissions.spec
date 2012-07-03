# Generated File.
%setup_docs_module linux_permissions ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Permissions in Linux
Summary(ru_RU.KOI8-R): Права доступа в системе Linux
License: %gpl2plus

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses

# replace docs-linux_permissions-kirill
Provides: docs-linux_permissions-kirill
Obsoletes: docs-linux_permissions-kirill

Source: %name-%version.tar

%description
Introduction into the Linux permissions for the user (with examples).

%description -l ru_RU.KOI8-R
Введение в систему прав доступа Linux для пользователя с примерами.

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "permissions.xml"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Tue Apr 15 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-linux_permissions-kirill
  + added Provides/Obsoletes
- used macro for License tag (rpm-build-licenses)

* Sun Jan 13 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-linux_permissions-kirill package

* Mon Mar 13 2006 Kirill Maslinsky <kirill@altlinux.ru> 060313-alt1
- Auto rebuild with new version.

* Wed Jan 25 2006 Kirill Maslinsky <kirill@altlinux.ru> 060124-alt1
- Auto rebuild with new version.

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 051121-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 051121-alt1
- Auto rebuild with new version.

* Tue Oct 04 2005 Kirill Maslinsky <kirill@altlinux.ru> 050921-alt1.1
- Auto rebuild with new version.

* Wed Sep 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 050921-alt1
- Auto rebuild with new version.

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050325-alt5
- rebuilt with rpm-build-docs-0.4.2-alt3

* Sun Jul 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 050325-alt4
- rebuilt with rpm-build-docs-0.4.2-alt2

* Tue Jun 14 2005 Alexey Gladkov <legion@altlinux.ru> 050325-alt3
- Requires bugfix;

* Mon Jun 06 2005 Alexey Gladkov <legion@altlinux.ru> 050325-alt2
- rebuild with new rpm-build-docs.

* Mon Apr 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050325-alt1
- initial build
