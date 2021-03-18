%global repo dde-device-formatter

Name: deepin-device-formatter
Version: 0.0.1.6
Release: alt1
Summary: Device formatter for Deepin Desktop Environment
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-device-formatter
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires: gcc-c++ qt5-base-devel qt5-tools deepin-gettext-tools udisks2-qt5-devel dtk5-widget-devel qt5-x11extras-devel
#Requires: icon-theme-hicolor

%description
%summary.

%prep
%setup -n %repo-%version
sed -i 's|lrelease|lrelease-qt5|' \
	generate_translations.sh
sed -i 's|lupdate|lupdate-qt5|' \
	update_trabslations.sh

%build
%qmake_qt5 \
	DEFINES+="VERSION=%version" \
	CONFIG+=nostrip \
	VERSION=%version \
	LIB_INSTALL_DIR=%_libdir \
	#
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot
%find_lang %repo

%files -f %repo.lang
%doc README.md LICENSE
%_bindir/%repo
%_datadir/%repo/

%changelog
* Thu Mar 18 2021 Leontiy Volodin <lvol@altlinux.org> 0.0.1.6-alt1
- Initial build for ALT Sisyphus.
