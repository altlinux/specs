%define _unpackaged_files_terminate_build 1

Name:      appstream-data-1-mobile
Summary:   ALT Linux AppStream metadata
Version:   20240710
Release:   alt1
Group:     System/Configuration/Packaging
BuildArch: noarch
License:   CC0 and CC-BY-SA
URL:       http://www.altlinux.org/SoftwareCenter/Applications
Source:    %name-%version.tar

Conflicts: appstream-data-desktop
Provides:  appstream-data
Provides:  appstream-data-mobile

BuildRequires: appstream-data-generator

%description
This package provides the distribution specific AppStream metadata
required for GNOME Software Center or KDE Discover in ALT mobile

%prep
%setup

%install
mkdir -p %buildroot%_datadir/app-info/xmls
mkdir -p %buildroot%_datadir/app-info/icons

cp -r icons/* %buildroot%_datadir/app-info/icons/
cp -r xmls/* %buildroot%_datadir/app-info/xmls/

%files
%_datadir/app-info/xmls/*
%_datadir/app-info/icons/altlinux

%changelog
* Wed Jul 10 2024 Kirill Izmestev <felixz@altlinux.org> 20240710-alt1
- Added applications to exclusivelist and updated database.

* Fri May 31 2024 Kirill Izmestev <felixz@altlinux.org> 20240531-alt1
- Added/removed applications to exclusivelist and updated database.

* Fri Apr 19 2024 Kirill Izmestev <felixz@altlinux.org> 20240419-alt1
- Added applications to exclusivelist and updated database.

* Thu Apr 05 2024 Kirill Izmestev <felixz@altlinux.org> 20240405-alt1
- Added application to exclusive list and updated database.

* Thu Mar 21 2024 Kirill Izmestev <felixz@altlinux.org> 20240321-alt1
- Added applications to exclusive list and updated database.

* Mon Feb 26 2024 Kirill Izmestev <felixz@altlinux.org> 20240226-alt1
- Added application to exclusive list and updated database.
- Changed conflicts to appstream-data-desktop.
- Added provides for package appstream-data.
- Renamed package to appstream-data-1-mobile (thanks antohami@).

* Thu Feb 08 2024 Kirill Izmestev <felixz@altlinux.org> 20240208-alt1
- Improved package description.
- Added conflicts for package appstream-data.

* Thu Jan 25 2024 Kirill Izmestev <felixz@altlinux.org> 20240125-alt1
- Initial build in Sisyphus.
- Added exclusivelist file for ALT mobile applications.
- Generated appstream-data-mobile for Sisyphus.
