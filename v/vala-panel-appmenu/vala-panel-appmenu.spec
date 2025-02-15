%define _unpackaged_files_terminate_build 1

Name: vala-panel-appmenu
Version: 24.05
Release: alt1

Summary: AppMenu plugin for xfce4-panel, mate-panel and vala-panel
License: LGPLv3
Group: Other
Url: https://gitlab.com/vala-panel-project/vala-panel-appmenu

Source: %name-%version.tar
Source1: %name.sh

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-systemd
BuildRequires: cmake
BuildRequires: meson
BuildRequires: vala-tools
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libwnck-3.0)
BuildRequires: pkgconfig(vala-panel)
BuildRequires: pkgconfig(libmatepanelapplet-4.0)
BuildRequires: pkgconfig(libxfce4panel-2.0)
BuildRequires: pkgconfig(libxfconf-0)
#BuildRequires: pkgconfig(budgie-1.0)
BuildRequires: pkgconfig(systemd)

%description
This is Global Menu plugin for using with Xfce Panel, MATE Panel and
Vala Panel.

%package -n xfce4-vala-panel-appmenu-plugin
Group: Graphical desktop/XFce
Summary: Application Menu plugin for xfce4-panel
Requires: xfce4-panel
Requires: vala-panel-appmenu-gtk-module == %{version}-%{release}

%description -n xfce4-vala-panel-appmenu-plugin
Xfce4 desktop plugin for %{name}.


%package -n mate-vala-panel-appmenu-plugin
Group: Graphical desktop/MATE
Summary: Application Menu plugin for xfce4-panel
Requires: mate-panel
Requires: vala-panel-appmenu-gtk-module == %{version}-%{release}

%description -n mate-vala-panel-appmenu-plugin
Mate desktop plugin for %{name}.

%package devel
Group: Development/Other
Summary: Development package for budgie-desktop
Requires: vala-panel-appmenu-gtk-module = %{version}-%{release}

%description devel
Header files, libraries, and other files for developing %{name}.

%package -n vala-panel-appmenu-gtk-module
Group: Graphical desktop/GNOME
Summary: Gtk3MenuShell D-Bus exporter

%description -n vala-panel-appmenu-gtk-module
GTK (2, 3) module that exports GtkMenuShells over D-Bus.

%prep
%setup

%build
%meson \
       -Dxfce=enabled \
       -Dvalapanel=enabled \
       -Dmate=enabled
#      -Djayatana=enabled -Dbudgie=enabled
%meson_build

%install
%meson_install

mkdir -p %buildroot%_sysconfdir/profile.d
install -p -m 755 %SOURCE1 %buildroot%_sysconfdir/profile.d/

rm -fv %{buildroot}%{_datadir}/licenses/appmenu-gtk-module/LICENSE
rm -fv %{buildroot}%{_datadir}/licenses/vala-panel-appmenu/LICENSE
rm -rfv %{buildroot}%{_datadir}/doc/vala-panel-appmenu

%find_lang vala-panel-appmenu

%files -f vala-panel-appmenu.lang
%doc README.md LICENSE
%dir %_libdir/vala-panel
%dir %_libdir/vala-panel/applets
%_libdir/vala-panel/applets/libappmenu.so
%dir %_libexecdir/vala-panel
%_libexecdir/vala-panel/appmenu-registrar
%_docdir/appmenu-gtk-module/
%_datadir/dbus-1/services/com.canonical.AppMenu.Registrar.service
%_datadir/glib-2.0/schemas/org.valapanel.appmenu.gschema.xml
%_datadir/vala-panel/applets/org.valapanel.appmenu.plugin
%_datadir/vala/vapi/appmenu-glib-translator.*
%_datadir/gir-1.0/AppmenuGLibTranslator-*.gir
%dir %_includedir/appmenu-glib-translator
%_includedir/appmenu-glib-translator/importer.h
%_libdir/girepository-1.0/AppmenuGLibTranslator-*.typelib
%_libdir/libappmenu-glib-translator.*

%files -n vala-panel-appmenu-gtk-module
%doc README.md LICENSE
%_sysconfdir/profile.d/%name.sh
%_userunitdir/appmenu-gtk-module.service
%_libdir/libappmenu-gtk2-parser.so.*
%_libdir/libappmenu-gtk3-parser.so.*
%_libdir/gtk-2.0/modules/libappmenu-gtk-module.so
%_libdir/gtk-3.0/modules/libappmenu-gtk-module.so
%_datadir/glib-2.0/schemas/org.appmenu.gtk-module.gschema.xml

%files -n xfce4-vala-panel-appmenu-plugin
%doc README.md LICENSE
%_libdir/xfce4/panel/plugins/libappmenu-xfce.so
%_datadir/xfce4/panel/plugins/appmenu.desktop

%files -n mate-vala-panel-appmenu-plugin
%doc README.md LICENSE
%_libdir/mate-panel/libappmenu-mate.so
%_datadir/mate-panel/applets/org.vala-panel.appmenu.mate-panel-applet

%files devel
%doc README.md LICENSE
%dir %_includedir/appmenu-gtk-parser
%_includedir/appmenu-gtk-parser/*.h
%_libdir/libappmenu-gtk2-parser.so
%_libdir/libappmenu-gtk3-parser.so
%_libdir/pkgconfig/*.pc

%changelog
* Sat Feb 15 2025 Nikolay Strelkov <snk@altlinux.org> 24.05-alt1
- Initial build for Sisyphus
