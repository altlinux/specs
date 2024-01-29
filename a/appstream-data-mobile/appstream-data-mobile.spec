%define _unpackaged_files_terminate_build 1

Name:      appstream-data-mobile
Summary:   ALT Linux AppStream metadata
Version:   20240125
Release:   alt1
Group:     System/Configuration/Packaging
BuildArch: noarch
License:   CC0 and CC-BY-SA
URL:       http://www.altlinux.org/SoftwareCenter/Applications
Source:    %name-%version.tar

BuildRequires: appstream-data-generator

%description
This package provides the distribution specific AppStream metadata
required for GNOME Software Center or KDE Discover.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/app-info/xmls
mkdir -p %buildroot%_datadir/app-info/icons

cp -r icons/* %buildroot%_datadir/app-info/icons/
cp -r xmls/* %buildroot%_datadir/app-info/xmls/
#cp -r manual-%version/* %buildroot%_datadir/app-info/xmls/

%files
%_datadir/app-info/xmls/*
%_datadir/app-info/icons/altlinux

%changelog
* Thu Jan 25 2024 Kirill Izmestev <felixz@altlinux.org> 20240125-alt1
- Initial build in Sisyphus.
- Added exclusivelist file for ALT mobile applications.
- Generated appstream-data-mobile for Sisyphus.
