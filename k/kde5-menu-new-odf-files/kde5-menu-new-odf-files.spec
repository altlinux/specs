Name:    kde5-menu-new-odf-files
Version: 0.1
Release: alt1 

Summary: ODF files to KDE5 pop-up menu
Summary(ru_RU.UTF-8): Файлы ODF для меню KDE5

License: GPLv3
Group:   Graphical desktop/Other
Url:     http://git.osmesh.ru/KOMETA/kde5-menu-new-odf-files

# Source-url: http://git.osmesh.ru/KOMETA/kde5-menu-new-odf-files/archive/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

Requires: menu-icons-default

%description
Adding elements to the KDE5 pop-up menu to create a document,
table and presentation in ODF format

%description -l ru_RU.UTF-8
Добавление пунктов меню в KDE5 для создания документа,
таблицы и презентации в формате ODF

%prep
%setup -q -n %name-%version

%install
%define templdir %_datadir/templates
mkdir -p %buildroot%templdir

install -pm644 %name-%version/*.desktop %buildroot%templdir
install -pm644 %name-%version/*.od* %buildroot%templdir

%files
%templdir/document.desktop
%templdir/document.odt
%templdir/presentation.desktop
%templdir/presentation.odp
%templdir/sheet.desktop
%templdir/sheet.ods

%changelog
* Mon Dec 13 2021 Evgeniy Kukhtinov <neurofreak@altlinux.org> 0.1-alt1
- new version
