%define rname kpartsplugin

Name:    mozilla-plugin-kparts
Version: 20120723
Release: alt1
Summary: Use Kparts technology as a plugin for Netscape-compatible browsers

Group:   Graphical desktop/KDE
License: GPLv3+
Url:     http://www.unix-ag.uni-kl.de/~fischer/kpartsplugin/index.html
Source:  https://www.unix-ag.uni-kl.de/~fischer/kpartsplugin/%rname-%version.tar.bz2

BuildRequires(pre): browser-plugins-npapi-devel

# Automatically added by buildreq on Fri Aug 31 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ kde4libs-devel libicu libqt4-sql-mysql
BuildRequires: gcc-c++ kde4libs-devel

%description
This software implements a plugin for Netscape-compatible browsers
in a Unix environment. This plugin uses KDE's KParts technology
to embed file viewers (e.g. for PDF files) into non-KDE browsers.
Tested browsers include both Mozilla Firefox and Opera, and is know
to work with Chrome and Arora.

With this plugin, you can e.g. view PDF files in Firefox using
Okular as an embedded plugin.

%prep
%setup -n %rname-%version -q

%build
%K4build -DNSPLUGIN_INSTALL_DIR=%browser_plugins_path

%install
%K4install

%files
%doc README.txt ChangeLog
%browser_plugins_path/lib%rname.so
%_K4lib/kcm_%rname.so
%_K4srv/kcm_%rname.desktop


%changelog

* Fri Aug 31 2012 Denis G. Samsonenko <ogion@altlinux.org> 20120723-alt1
- first build for ALTLinux
