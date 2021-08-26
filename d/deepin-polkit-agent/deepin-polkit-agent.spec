%define repo dde-polkit-agent

%def_disable clang

Name: deepin-polkit-agent
Version: 5.4.12
Release: alt1
Summary: Deepin Polkit Agent
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-polkit-agent
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang12.0-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires: dtk5-widget-devel deepin-qt-dbus-factory-devel libpolkitqt5-qt5-devel qt5-base-devel qt5-linguist qt5-tools gsettings-qt-devel qt5-multimedia-devel qt5-x11extras-devel

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
sed -i 's|lrelease|lrelease-qt5|' translate_generation.sh
sed -i 's|lupdate|lupdate-qt5|' lupdate.sh
# sed -i 's|/usr/lib|/usr/libexec|' dde-polkit-agent.pro polkit-dde-authentication-agent-1.desktop \
#     pluginmanager.cpp
# https://github.com/linuxdeepin/developer-center/issues/1721
sed -i 's/bool is_deepin = true/bool is_deepin = false/' policykitlistener.cpp
# https://github.com/linuxdeepin/dde-polkit-agent/issues/26
sed -i '/setCancel/d' policykitlistener.cpp

%build
%qmake_qt5 \
%if_enabled clang
    QMAKE_STRIP= -spec linux-clang \
%endif
    CONFIG+=nostrip \
    PREFIX=%prefix
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
%dir %_includedir/dpa/
%_includedir/dpa/agent-extension-proxy.h
%_includedir/dpa/agent-extension.h

%changelog
* Fri Aug 20 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.12-alt1
- New version (5.4.12).

* Thu Jul 01 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.7-alt1
- New version (5.4.7).

* Tue Apr 27 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.0.3-alt2
- Changed location of the libraries.

* Wed Nov 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.3-alt1
- New version (5.3.0.3) with rpmgs script.

* Wed Oct 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.2-alt1
- New version (5.3.0.2) with rpmgs script.

* Mon Aug 03 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.7-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

