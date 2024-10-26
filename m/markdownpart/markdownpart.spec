%define rname markdownpart

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KPart for rendering Markdown content
Url: https://apps.kde.org/ru/markdownpart/
Vcs: https://invent.kde.org/utilities/markdownpart.git
License: LGPL-2.1-or-later

Provides:  kde5-markdownpart = %EVR
Obsoletes: kde5-markdownpart < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: qt6-declarative-devel
BuildRequires: kf6-kparts-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-ktextwidgets-devel

%description
The Markdown Viewer KPart allows KParts-using software to display files in
Markdown format in a rendered view.
Extends: Ark, Kate, KDevelop, Konqueror, Krusader.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc README* LICENSES/*
%_K6plug/kf6/parts/markdownpart.so
%_datadir/metainfo/*.xml


%changelog
* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

