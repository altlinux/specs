%global repo dde-polkit-agent

Name: deepin-polkit-agent
Version: 5.2.0.7
Release: alt1
Summary: Deepin Polkit Agent
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-polkit-agent
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires: gcc-c++ dtk5-widget-devel deepin-qt-dbus-factory-devel libpolkitqt5-qt5-devel qt5-base-devel qt5-linguist qt5-tools gsettings-qt-devel qt5-multimedia-devel qt5-x11extras-devel

%description
DDE Polkit Agent is the polkit agent used in Deepin Desktop Environment.

%package devel
Summary: Development package for %name
Group: Graphical desktop/Other
BuildArch: noarch

%description devel
Header files and libraries for %name.

%prep
%setup -n %repo-%version
%__subst 's|lrelease|lrelease-qt5|' translate_generation.sh
%__subst 's|lupdate|lupdate-qt5|' lupdate.sh
# https://github.com/linuxdeepin/developer-center/issues/1721
%__subst 's/bool is_deepin = true/bool is_deepin = false/' policykitlistener.cpp

%build
%qmake_qt5 PREFIX=%prefix
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc README.md
%doc LICENSE
%dir %_libexecdir/polkit-1-dde
%_libexecdir/polkit-1-dde/%repo
%_datadir/%repo/

%files devel
%_includedir/dpa/agent-extension-proxy.h
%_includedir/dpa/agent-extension.h

%changelog
* Mon Aug 03 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.7-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

