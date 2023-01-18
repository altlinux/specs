%define rname markdownpart

Name: kde5-%rname
Version: 22.12.1
Release: alt1
%K5init no_appdata

Group: Graphical desktop/KDE
Summary: KPart for rendering Markdown content
Url: https://apps.kde.org/ru/markdownpart/
Vcs: https://invent.kde.org/utilities/markdownpart.git
License: LGPL-2.1-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: qt5-base-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-ktextwidgets-devel

%description
The Markdown Viewer KPart allows KParts-using software to display files in
Markdown format in a rendered view.
Extends: Ark, Kate, KDevelop, Konqueror, Krusader.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc README* LICENSES/*
%_K5plug/kf5/parts/markdownpart.so
%_K5srv/markdownpart.desktop

%changelog
* Wed Jan 18 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.1-alt1
- new version

* Mon Dec 12 2022 Anton Golubev <golubevan@altlinux.org> 22.12.0-alt1
- initial build
