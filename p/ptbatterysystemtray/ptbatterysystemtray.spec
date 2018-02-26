Name: ptbatterysystemtray
Version: 0.8.0
Release: alt1

Summary: A simple battery monitor in the system tray, in Qt
License: GPLv3
Group: Graphical desktop/Other

# http://gitorious.org/ptbatterysystemtray/ptbatterysystemtray
# http://sourceforge.net/projects/batterysystem/
Url: http://www.pyrotools.org/
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++
BuildRequires: qt4-devel qt4-designer

%description
%summary.
It allows to handle power management and CPU frequency.

%prep
%setup

%build
qmake-qt4 INSTALL_PREFIX=%prefix
%make

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc LICENCE NEWS README ChangeLog
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Tue Feb 14 2012 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- initial build for ALT Linux Sisyphus (based on Mageia spec)

