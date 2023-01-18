%define _unpackaged_files_terminate_build 1

Name: kde5-markdownpart
Version: 22.12.0
Release: alt1
%K5init

Summary: KPart for rendering Markdown content
License: LGPL-2.1-or-later
Group: Graphical desktop/KDE
Url: https://apps.kde.org/ru/markdownpart/
Vcs: https://invent.kde.org/utilities/markdownpart.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: qt5-base-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: libappstream-devel
BuildRequires: gettext-tools

%description
The Markdown Viewer KPart allows KParts-using software to display files in
Markdown format in a rendered view.
Extends: Ark, Kate, KDevelop, Konqueror, Krusader.

%prep
%setup

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc README.md
%_K5plug/kf5/parts/markdownpart.so
%_K5srv/markdownpart.desktop
%_datadir/metainfo/org.kde.markdownpart.metainfo.xml

%changelog
* Mon Dec 12 2022 Anton Golubev <golubevan@altlinux.org> 22.12.0-alt1
- initial build
