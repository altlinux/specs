%define  doc_version 1.1

Name: 	 plasma-applet-stackfolder
Summary: Browse the stack of folders
Version: 2.4
Release: alt1

Group: 	 Graphical desktop/KDE
License: GPL
URL: 	 http://www.rosalab.ru

Packager: Andrey Cherepanov <cas@altlinux.org>

Source0: %name-%version.tar.gz
Source1: %name-doc-%{doc_version}.tar.gz

BuildRequires(pre): kde4libs-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: kde4base-devel

%description
Browse the stack of folders.

%prep
%setup -q
tar xvf %SOURCE1

%build
%K4build

%install
%K4install
%K4find_lang --with-kde %name

%files -f %name.lang
%doc welcome-en.pdf welcome-ru.pdf
%_K4lib/plasma_applet_stackfolder.so
%_K4srv/%name.desktop
%_K4apps/plasma/packages/org.kde.stackfolder/*

%changelog
* Tue Sep 30 2014 Andrey Cherepanov <cas@altlinux.org> 2.4-alt1
- Build for Sisyphus from ROSA (ALT #27489)

