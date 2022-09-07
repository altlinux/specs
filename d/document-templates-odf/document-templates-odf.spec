Name:    document-templates-odf
Version: 0.1
Release: alt2

Group:   Graphical desktop/Other
Summary: ODF templates
Summary(ru_RU.UTF-8): Шаблоны документов OD
License: GPL-3.0-only
Url:     http://git.osmesh.ru/KOMETA/kde5-menu-new-odf-files

BuildArch: noarch

Provides: kde5-menu-new-odf-files = %EVR
Obsoletes: kde5-menu-new-odf-files < %EVR
#Requires: menu-icons-default

# Source-url: http://git.osmesh.ru/KOMETA/kde5-menu-new-odf-files/archive/v%version.tar.gz
Source: %name-%version.tar
Patch1: alt-fix-icons-paths.patch

%description
Templates to create a document, table and presentation in ODF format.
%description -l ru_RU.UTF-8
Шаблоны для для создания документа, таблицы и презентации в формате ODF.

%prep
%setup
%patch1 -p1

%install
%define templdir %_datadir/templates
mkdir -p %buildroot/%templdir/.source/

install -pm644 kde5-menu-new-odf-files-*/*.desktop %buildroot/%templdir/
install -pm644 kde5-menu-new-odf-files-*/*.od* %buildroot/%templdir/.source/

%files
%dir %templdir/
%dir %templdir/.source/
%templdir/*.desktop
%templdir/.source/*.od*

%changelog
* Wed Sep 07 2022 Sergey V Turchin <zerg@altlinux.org> 0.1-alt2
- rename package (closes: 43695)
- obsolete kde5-menu-new-odf-files
- fix desktop-files

* Mon Dec 13 2021 Evgeniy Kukhtinov <neurofreak@altlinux.org> 0.1-alt1
- new version
