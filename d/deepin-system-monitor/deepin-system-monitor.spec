Name: deepin-system-monitor
Version: 5.6.12
Release: alt1
Summary: A more user-friendly system monitor
License: GPL-3.0+
Group: Monitoring
Url: https://github.com/linuxdeepin/deepin-system-monitor
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Source1: %name-appdata.xml

BuildRequires(pre): rpm-build-ninja desktop-file-utils libappstream-glib
BuildRequires: gcc-c++ cmake dtk5-widget-devel dtk5-wm-devel libprocps-devel libxcb-devel libxcbutil-devel libX11-devel libXext-devel libXtst-devel qt5-base-devel qt5-x11extras-devel qt5-linguist libpcap-devel libcap-devel libncurses-devel qt5-tools-devel libicu-devel deepin-gettext-tools
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
# Workaround build failure with GCC 10
#   sed -e 's|print_err|print_err_system|g' -i src/process/system_stat.cpp
#   sed -e 's|print_err|print_err_process|g' -i src/process/process_stat.cpp
#   sed -e 's|print_err|print_err_desktop|g' -i src/process/desktop_entry_stat.cpp

%build
%cmake -GNinja
%ninja_build -C BUILD

%install
%ninja_install -C BUILD
install -Dm644 %SOURCE1 %buildroot%_datadir/appdata/%name.appdata.xml

%find_lang %name

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop ||:
appstream-util validate-relax --nonet %buildroot%_datadir/appdata/*.appdata.xml

%files -f %name.lang
%doc README.md
%doc LICENSE
%_bindir/%name
%_datadir/appdata/%name.appdata.xml
%_datadir/polkit-1/actions/com.deepin.pkexec.deepin-system-monitor.policy
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/%name/

%changelog
* Fri Jul 31 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.12-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
