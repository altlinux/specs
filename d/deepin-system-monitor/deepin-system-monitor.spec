%def_disable clang

Name: deepin-system-monitor
Version: 5.8.0.7
Release: alt1
Summary: A more user-friendly system monitor
License: GPL-3.0+
Group: Monitoring
Url: https://github.com/linuxdeepin/deepin-system-monitor
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang11.0-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja
BuildRequires(pre): desktop-file-utils
BuildRequires: cmake
BuildRequires: dtk5-widget-devel
BuildRequires: dtk5-wm-devel
BuildRequires: libprocps-devel
BuildRequires: libxcb-devel
BuildRequires: libxcbutil-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXtst-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-linguist
BuildRequires: libpcap-devel
BuildRequires: libcap-devel
BuildRequires: libncurses-devel
BuildRequires: qt5-tools-devel
BuildRequires: libicu-devel
BuildRequires: deepin-gettext-tools
BuildRequires: libxcbutil-icccm-devel
Requires: icon-theme-hicolor
#Recommends:     deepin-manual

%description
%summary.

%prep
%setup
# Upstream likes to refactor code while ignoring pull requests
sed -i '20i#include <QMap>\n#include <QHash>\n#include <QPainterPath>' src/compact_memory_monitor.cpp
sed -i '1i#include <QPainterPath>' src/memory_monitor.cpp src/compact_network_monitor.h \
                                   src/network_monitor.h src/utils.cpp \
                                   src/gui/system_service_page_widget.cpp \
                                   src/gui/process_page_widget.cpp \
                                   src/gui/base_header_view.cpp src/disk_monitor.h \
                                   src/cpu_monitor.h src/compact_disk_monitor.h \
                                   src/compact_cpu_monitor.cpp
# Fixed paths
sed -i 's|/usr/lib/virtualbox/VirtualBox|%_libdir/virtualbox/VirtualBox|' src/utils.cpp
# Workaround build failure with GCC 10
sed -e 's|print_err|print_err_system|g' -i src/process/system_stat.cpp
sed -e 's|print_err|print_err_process|g' -i src/process/process_stat.cpp
sed -e 's|print_err|print_err_desktop|g' -i src/process/desktop_entry_stat.cpp

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif
%cmake \
    -GNinja \
    -DLIB_INSTALL_DIR=%_libdir \
    -DAPP_VERSION=%version
%ninja_build -C BUILD

%install
%ninja_install -C BUILD

%find_lang %name

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop ||:

%files -f %name.lang
%doc README.md
%doc LICENSE
%_bindir/%name
%_datadir/polkit-1/actions/com.deepin.pkexec.deepin-system-monitor.policy
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/%name/

%changelog
* Fri Dec 04 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.7-alt1
- New version (5.8.0.7) with rpmgs script.
- Fixed build with gcc10.

* Tue Nov 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.4-alt1
- New version (5.8.0.4) with rpmgs script.

* Fri Oct 09 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.1-alt1
- New version (5.8.0.1) with rpmgs script.

* Fri Jul 31 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.12-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
