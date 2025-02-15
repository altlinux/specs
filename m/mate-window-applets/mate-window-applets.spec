%define _unpackaged_files_terminate_build 1

Name: mate-window-applets
Version: 21.04.0
Release: alt1

Summary: Window applets for MATE Desktop
License: GPLv3
Group: Other
Url: https://github.com/ubuntu-mate/mate-window-applets

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala-tools
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libwnck-3.0)
BuildRequires: pkgconfig(libmatepanelapplet-4.0)

%description
The MATE Window Applets collection provides various applets to show
window control elements in the MATE Panel:
* WindowButtons applet shows the close,minimize,actions in a panel;
* WindowTitle applet shows the title of the active window;
WindowMenu applet shows you the window menu of the active window.

%package -n mate-window-applets-common
Group: Graphical desktop/MATE
Summary: MATE Window Applets (common files)
BuildArch: noarch

%description -n mate-window-applets-common
This package contains the arch-independent files of the MATE Windows
Applets.

%package -n mate-window-buttons-applet
Group: Graphical desktop/MATE
Summary: MATE Window Applets (WindowButtons Applet)
Requires: mate-window-applets-common == %{version}-%{release}

%description -n mate-window-buttons-applet
This WindowButtons applet shows you the close, minimize and actions
buttons.

%package -n mate-window-menu-applet
Group: Graphical desktop/MATE
Summary: MATE Window Applets (WindowMenu Applet)
Requires: mate-window-applets-common == %{version}-%{release}

%description -n mate-window-menu-applet
This WindowMenu applet shows you the window menu of the active window.

%package -n mate-window-title-applet
Group: Graphical desktop/MATE
Summary: MATE Window Applets (WindowTitle Applet)
Requires: mate-window-applets-common == %{version}-%{release}

%description -n mate-window-title-applet
This WindowTitle applet shows you the class, title, role, xid and pid of
the active window.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
mkdir -p %buildroot/usr/share/pixmaps/mate-window-applets
./install-icons.sh %buildroot/usr/share/ install

%files -n mate-window-applets-common
%doc LICENSE README.md
%_datadir/glib-2.0/schemas/org.mate.window-applets.gschema.xml
%dir %_pixmapsdir/mate-window-applets
%dir %_pixmapsdir/mate-window-applets/Black
%_pixmapsdir/mate-window-applets/Black/*
%dir %_pixmapsdir/mate-window-applets/White
%_pixmapsdir/mate-window-applets/White/*
%dir %_libexecdir/mate-applets/mate-window-applets

%files -n mate-window-buttons-applet
%doc LICENSE README.md
%dir %_libexecdir/mate-applets/mate-window-applets/window-buttons
%_libexecdir/mate-applets/mate-window-applets/window-buttons/dialog.ui
%_libexecdir/mate-applets/mate-window-applets/window-buttons/window-buttons-applet
%_datadir/dbus-1/services/org.mate.panel.applet.WindowButtonsAppletFactory.service
%_datadir/mate-panel/applets/org.mate.panel.WindowButtonsApplet.mate-panel-applet

%files -n mate-window-menu-applet
%doc LICENSE README.md
%dir %_libexecdir/mate-applets/mate-window-applets/window-menu
%_libexecdir/mate-applets/mate-window-applets/window-menu/dialog.ui
%_libexecdir/mate-applets/mate-window-applets/window-menu/window-menu-applet
%_datadir/dbus-1/services/org.mate.panel.applet.WindowMenuAppletFactory.service
%_datadir/mate-panel/applets/org.mate.panel.WindowMenuApplet.mate-panel-applet

%files -n mate-window-title-applet
%doc LICENSE README.md
%dir %_libexecdir/mate-applets/mate-window-applets/window-title
%_libexecdir/mate-applets/mate-window-applets/window-title/dialog.ui
%_libexecdir/mate-applets/mate-window-applets/window-title/window-title-applet
%_datadir/dbus-1/services/org.mate.panel.applet.WindowTitleAppletFactory.service
%_datadir/mate-panel/applets/org.mate.panel.WindowTitleApplet.mate-panel-applet

%changelog
* Sat Feb 15 2025 Nikolay Strelkov <snk@altlinux.org> 21.04.0-alt1
- Initial build for Sisyphus
