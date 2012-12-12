Name: sparkleshare
Version: 1.0.0
Release: alt1

Summary: Collaboration and sharing tool based on git repositories
Group: Development/Tools
License: GPLv3+
Url: http://www.sparkleshare.org/

# 26fd9e53f
Source: %name-%version.tar
#Source: https://github.com/downloads/hbons/SparkleShare/%name-linux-%version.tar.gz
# icons are too small for tray icon in gnome-shell-3.6
#https://github.com/hbons/SparkleShare/issues/957
Patch: sparkleshare-0.9.9-trayicon.patch

Requires: git curl
Requires: gvfs-utils

BuildRequires: monodevelop nant libmono-devel
BuildRequires: libnotify-sharp-devel libwebkit-sharp-devel
BuildRequires: ndesk-dbus-devel ndesk-dbus-glib-devel

%description
SparkleShare is a crossplatform collaboration and sharing tool that is
designed to keep things simple and to stay out of your way. It allows to
instantly sync with Git repositories and is available for Linux, Mac and
Windows.

%prep
%setup
%patch -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure --enable-maintainer-mode
%make

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_libdir/%name/
%_datadir/%name/
%_datadir/applications/%name.desktop
%_datadir/applications/%name-invite-opener.desktop
%_iconsdir/gnome/scalable/apps/%name-symbolic.svg
%_iconsdir/hicolor/*x*/*/%name.png
%doc legal/Authors.txt legal/Trademark.txt News.txt README.md

%exclude %_iconsdir/ubuntu-mono*

%changelog
* Tue Dec 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- first build for Sisyphus

