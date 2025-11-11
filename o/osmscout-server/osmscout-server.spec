%define _unpackaged_files_terminate_build 1

Name: osmscout-server
Version: 3.1.5
Release: alt2

Summary: Maps server providing tiles, geocoder, and route
License: GPL-3.0-or-later
Group: Sciences/Geosciences
Url: https://rinigus.github.io/osmscout-server/en
Vcs: https://github.com/rinigus/osmscout-server.git

Source0: %name-%version.tar
Source1: %name-%version-server-src-geocoder-nlp.tar
Source2: %name-%version-server-src-geocoder-nlp-thirdparty-sqlite3pp.tar
Patch0: %name-%version-libpostalheader.patch

BuildRequires(pre): rpm-macros-qt5
BuildRequires: gcc-c++
BuildRequires: kf5-kirigami-devel
BuildRequires: libssl-devel
BuildRequires: qt5-base-devel
BuildRequires: libmarisa-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: qt5-location-devel
BuildRequires: qt5-quickcontrols2-devel
BuildRequires: qt5-tools-devel
BuildRequires: libpostal-devel
BuildRequires: libkyotocabinet-devel
BuildRequires: libsqlite3-devel
BuildRequires: libvalhalla-devel
BuildRequires: boost-geometry-devel

%description
OSM Scout server can be used as a drop-in replacement for online map services
providing map tiles, search, and routing. As a result, an offline operation is
possible if the device has a server and map client programs installed and
running.

%package gui
Summary: Graphical interface for osmscout-server
Group: Graphical desktop/Other
Requires: osmscout-server = %EVR
Requires: qt5-sql
Requires: qt5-quickcontrols2
Requires: kf5-kirigami

%description gui
Provides a graphical interface for managing OSM Scout Server. The package
includes an application for convenient configuration and interaction with the
server, enabling access to offline maps and geodata. It includes a desktop file
for desktop environment integration, an application icon, and styles for the
user interface.

%prep
%setup -a1 -a2
%autopatch -p1

%build
%qmake_qt5 \
  VERSION=%version \
  PREFIX=%prefix \
  CONFIG+=disable_osmscout \
  CONFIG+=disable_mapnik \
  CONFIG+=disable_systemd \
  SCOUT_FLAVOR=kirigami \
  CONFIG+=use_dbusactivation \
  #

%make

%install
%install_qt5

%check
%make check

%files
%_bindir/osmscout-server
%_datadir/dbus-1/services/io.github.rinigus.OSMScoutServer.service
%_datadir/osmscout-server/data/

%files gui
%_bindir/osmscout-server-gui
%_desktopdir/osmscout-server-gui.desktop
%_iconsdir/hicolor/*/apps/osmscout-server.png
%_datadir/osmscout-server/styles/

%changelog
* Tue Nov 11 2025 Ivan Khanas <xeno@altlinux.org> 3.1.5-alt2
- Remove requires on libprocps(closes: 55994).

* Sun Jun 08 2025 Ivan Khanas <xeno@altlinux.org> 3.1.5-alt1
- First build for ALT.
