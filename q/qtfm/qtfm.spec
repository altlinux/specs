Name:		qtfm
Version:	6.2.1
Release:	alt1
Summary:	qtFM is a small, lightweight file manager
License:	GPLv2+
Group:		File tools
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://www.qtfm.org/
Source0:	http://www.qtfm.org/%name-%version.tar.gz

BuildRequires: /usr/bin/convert gcc-c++ libmagic-devel 

Patch0:         0001-iconview-Fix-QPainterPath-path-has-incomplete-type.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(Magick++)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
Requires:     icon-theme-adwaita
Requires:     udisks2



%description
qtFM is a small, lightweight file manager for Linux desktops based on pure Qt
and works great with minimal desktop environments like Openbox.

Features:

 - lightweight, pure Qt, no kde libraries or other dependencies
 - full theme and mime filetype icon integration
 - tree, bookmarks, list, icon, detail and thumbnail views
 - customizable interface, rearrange views and toolbars to suit
 - powerful custom command system for user defined actions
 - customizable key bindings for built-in and custom actions
 - drag & drop functionality
 - tabs

%prep
%setup
%patch0 -p1

%build

%qmake_qt5 PREFIX=%{_prefix} CONFIG+=with_magick CONFIG+=magick7 CONFIG+=with_ffmpeg
%make_build



%install

%makeinstall_std INSTALL_ROOT=%buildroot
fdupes %{buildroot}/%{_datadir}


%files

%doc AUTHORS ChangeLog README.md
%{_bindir}/qtfm
%{_bindir}/qtfm-tray
%{_datadir}/applications/qtfm.desktop
#dir %{_datadir}/icons/hicolor/160x160/{,apps}
#dir %{_datadir}/icons/hicolor/20x20/{,apps}
%{_datadir}/icons/hicolor/*/apps/qtfm.??g
%{_sysconfdir}/xdg/autostart/qtfm-tray.desktop
%{_man1dir}/qtfm*


%changelog
* Fri Oct 29 2021 Ilya Mashkin <oddity@altlinux.ru> 6.2.1-alt1
- 6.2.1
- Build with qt5
- Update License and URL tags

* Mon Jun 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.5-alt2
- Fix build with gcc-6

* Sun Jun 17 2012 Motsyo Gennadi <drool@altlinux.ru> 5.5-alt1
- 5.5

* Fri Dec 16 2011 Motsyo Gennadi <drool@altlinux.ru> 5.3-alt1
- 5.3

* Fri Dec 09 2011 Motsyo Gennadi <drool@altlinux.ru> 5.2-alt1
- initial build for ALT Linux
