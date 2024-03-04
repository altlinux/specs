%define _unpackaged_files_terminate_build 1

Name: alt-welcome-k
Version: 1.0
Release: alt1

Summary: Greeting to Alt Linux for plasma5-welcome
License: GPL-2.0-or-later
Group: Graphical desktop/KDE

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: kf5-kdeclarative-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kpackage-devel
BuildRequires: qt5-tools-devel

Requires: plasma5-welcome

%description
Greeting to Alt Linux for plasma5-welcome.

%prep
%setup

%build
%K5build \
    -DPLASMA_WELCOME_EXTRA_PAGES:PATH="%_datadir/plasma-welcome-extra-pages-pre"

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%_K5qml/org/kde/plasma/private/*/
%_datadir/plasma-welcome-extra-pages-pre/*.qml

%changelog
* Fri Mar 01 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 1.0-alt1
- Initial build for ALT Linux
