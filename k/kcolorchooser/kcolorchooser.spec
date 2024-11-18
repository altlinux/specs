%define rname kcolorchooser

Name: %rname
Version: 24.08.3
Release: alt1
%K6init

Group: Graphics
Summary: Color Chooser
Url: http://www.kde.org
License: MIT

Provides:  kde5-kcolorchooser = %EVR
Obsoletes: kde5-kcolorchooser < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel qt6-wayland-devel
BuildRequires: kf6-kcoreaddons-devel kf6-ki18n-devel kf6-kxmlgui-devel kf6-kcolorscheme-devel

%description
Color selector and palette editor.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K6bin/kcolorchooser
%_K6xdgapp/*kcolorchooser*.desktop
%_K6icon/*/*/apps/*kcolorchooser*
%_datadir/metainfo/*.xml


%changelog
* Mon Nov 18 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

