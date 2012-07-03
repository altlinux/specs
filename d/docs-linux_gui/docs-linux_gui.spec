# Generated File.
%setup_docs_module linux_gui ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Graphical user interface in Linux
Summary(ru_RU.KOI8-R): Графический интерфейс в Linux
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-linux_gui-kirill
Provides: docs-linux_gui-kirill
Obsoletes: docs-linux_gui-kirill

Source: %name-%version.tar

%description
Description of Linux graphical system architecture: X, window managers,
integrated graphical environments (KDE, GNOME). With screenshots.

%description -l ru_RU.KOI8-R
Описание устройства графической подсистемы Linux: X, оконные менеджеры, интегрированные графические среды (KDE, GNOME). Со скриншотами.

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "gui.xml"

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
- replaces docs-linux_gui-kirill
  + added Provides/Obsoletes

* Wed Jan 16 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-linux_gui-kirill package

* Tue Mar 14 2006 Kirill Maslinsky <kirill@altlinux.ru> 060314-alt1
- Auto rebuild with new version.

* Tue Jan 24 2006 Kirill Maslinsky <kirill@altlinux.ru> 060123-alt1
- Auto rebuild with new version.

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 051010-alt2.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 051010-alt2
- Auto rebuild with new version.

* Mon Oct 10 2005 Kirill Maslinsky <kirill@altlinux.ru> 051010-alt1
- Auto rebuild with new version.

* Wed Oct 05 2005 Kirill Maslinsky <kirill@altlinux.ru> 050315-alt5.1.1
- Auto rebuild with new version.

* Wed Sep 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 050315-alt5.1
- Auto rebuild with new version.

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050315-alt5
- rebuilt with rpm-build-docs-0.4.2-alt3

* Sun Jul 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 050315-alt4
- rebuilt with rpm-build-docs-0.4.2-alt2

* Tue Jun 14 2005 Alexey Gladkov <legion@altlinux.ru> 050315-alt3
- Requires bugfix;

* Mon Jun 06 2005 Alexey Gladkov <legion@altlinux.ru> 050315-alt2
- rebuild with new rpm-build-docs.

* Mon Apr 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050315-alt1
- initial build
