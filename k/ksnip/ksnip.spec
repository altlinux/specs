%global optflags %optflags -I%_includedir/KF5 -L%_libdir/kf5/devel

Name:		ksnip
Version:	1.10.0
Release:	alt1

Summary:	Window Snipping Tool

License:	GPLv2+
Group:		Graphics
Url:		https://github.com/ksnip/ksnip

# Source-url: https://github.com/ksnip/ksnip/archive/refs/tags/v%version.tar.gz
Source:	%name-%version.tar

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: libX11-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: zlib-devel
BuildRequires: bzlib-devel
BuildRequires: kde5-kimageannotator-devel
BuildRequires: kde5-kcolorpicker-devel
BuildRequires: qt5-tools-devel
BuildRequires: libpng-devel
BuildRequires: libpcre-devel
BuildRequires: libuuid-devel
BuildRequires: libexpat-devel
BuildRequires: libbrotli-devel

BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

Requires:       icon-theme-hicolor

%description
Screenshot tool inspired by Windows Snipping Tool and made with Qt5 for Linux.

%prep
%setup -q -n %name-%version

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
%find_lang %name --with-qt

%check
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/*.appdata.xml
desktop-file-validate %buildroot%_datadir/applications/*.desktop

%files -f ksnip.lang
%doc README.md CHANGELOG.md
%_bindir/ksnip
%dir %_datadir/ksnip
%dir %_datadir/ksnip/translations
%_datadir/applications/org.ksnip.ksnip.desktop
%_datadir/icons/hicolor/*/apps/ksnip.svg
%_datadir/metainfo/org.ksnip.ksnip.appdata.xml

%changelog
* Mon Aug 01 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.10.0-alt1
- new version (1.10.0) with rpmgs script
- Remove patches merged to upstream

* Wed Dec 08 2021 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.9.2-alt1
- new version (1.9.2) with rpmgs script
- Update russian translation
- Add russian translation for desktop file

* Sun Nov 28 2021 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.9.1-alt2
- Add BR

* Tue Nov 23 2021 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.9.1-alt1
- new version (1.9.1) with rpmgs script

* Fri May 14 2021 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.8.2-alt1
- new version

* Fri Mar 12 2021 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.8.0-alt1
- Initial build in Sisyphus
