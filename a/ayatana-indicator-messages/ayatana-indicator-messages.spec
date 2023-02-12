%define _unpackaged_files_terminate_build 1

%define libname libmessaging-menu
%define typelib %libname-gir
%define sover   0
Name: ayatana-indicator-messages
Version: 22.9.0
Release: alt1

Summary: Ayatana Indicator for collecting messages that need a response
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-indicator-messages

Packager: Nikolay Strelkov <snk@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-macros-systemd rpm-build-vala

BuildRequires: ayatana-cmake-modules cmake gcc-c++ gtk-doc intltool libaccountsservice-devel vala vala-tools
BuildRequires: ayatana-indicator-common
BuildRequires: gobject-introspection-devel
BuildRequires: hicolor-icon-theme
BuildRequires: libblkid-devel
BuildRequires: libffi-devel
BuildRequires: libmount-devel
BuildRequires: libpcre2-devel
BuildRequires: libpcre-devel
BuildRequires: libpolkit-devel
BuildRequires: libselinux-devel
BuildRequires: libsystemd-devel
BuildRequires: pkg-config
BuildRequires: zlib-devel

Requires: ayatana-indicator-common
Requires: gobject-introspection
Requires: typelib(MessagingMenu)
Requires: %libname%sover

%description
A place on the user's desktop that collects messages that need a
response. This menu provides a condensed and collected view of all
of those messages for quick access, but without making them
annoying in times that you want to ignore them.

%package -n %libname%sover
Summary: Shared library for providing status information to the messaging indicator
Group: System/Libraries

%description -n %libname%sover
A place on the user's desktop that collects messages that need a
response. This menu provides a condensed and collected view of all
of those messages for quick access, but without making them
annoying in times that you want to ignore them.

%package -n %libname-devel
Summary: Development files for Ayatana Messaging Menu
Group: Development/C
Requires: %libname%sover = %version

%description -n %libname-devel
A place on the user's desktop that collects messages that need a
response. This menu provides a condensed and collected view of all
of those messages for quick access, but without making them
annoying in times that you want to ignore them.

%package -n %libname-doc
Group: Documentation
Summary: HTML documentation for the Ayatana Messaging Indicator shared library
BuildArch: noarch

%description -n %libname-doc
This package installs documentation for the Ayatana Messaging
Indicator shared library.

%package -n %typelib
Summary: Ayatana Messaging indicators library
Group: System/Libraries

%description -n %typelib
This package contains the GObject Introspection bindings for the
Ayatana Messaging Menu library.

%prep
%setup

%build
%cmake \
  -DCMAKE_INSTALL_LIBEXECDIR=%_libexecdir \
  -Denable_tests=Off
%cmake_build

%install
%cmake_install
find %buildroot -type f -name "*.la" -delete -print

%post
%systemd_user_post %name.service

%preun
%systemd_user_preun %name.service

%postun
%systemd_user_postun %name.service

%files
%doc COPYING NEWS
%config %_sysconfdir/xdg/autostart/%name.desktop
%_libexecdir/%name/
%_datadir/ayatana/indicators/org.ayatana.indicator.messages
%_datadir/glib-2.0/schemas/org.ayatana.indicator.messages.gschema.xml
%dir %_iconsdir/hicolor/16x16/categories/
%dir %_iconsdir/hicolor/16x16/status/
%dir %_iconsdir/hicolor/22x22/categories/
%dir %_iconsdir/hicolor/22x22
%dir %_iconsdir/hicolor/22x22/status/
%dir %_iconsdir/hicolor/24x24/status/
%dir %_iconsdir/hicolor/24x24
%dir %_iconsdir/hicolor/32x32/categories/
%dir %_iconsdir/hicolor/32x32/status/
%dir %_iconsdir/hicolor/48x48/status/
%dir %_iconsdir/hicolor/scalable/
%dir %_iconsdir/hicolor/scalable/categories/
%dir %_iconsdir/hicolor/scalable/status/
%_iconsdir/hicolor/*/*/*
%_userunitdir/%name.service
%_datadir/locale/*/LC_MESSAGES/*.mo

%files -n %libname%sover
%_libdir/libmessaging-menu.so.%{sover}*

%files -n %libname-devel
%_includedir/messaging-menu/
%_datadir/gir-1.0/MessagingMenu-1.0.gir
%_vapidir/MessagingMenu-1.0.vapi
%_libdir/libmessaging-menu.so
%_pkgconfigdir/messaging-menu.pc

%files -n %libname-doc
%dir %_datadir/gtk-doc
%dir %_datadir/gtk-doc/html
%dir %_datadir/gtk-doc/html/messaging-menu
%_datadir/gtk-doc/html/messaging-menu/*

%files -n %typelib
%_libdir/girepository-1.0/MessagingMenu-1.0.typelib

%changelog
* Sun Nov 06 2022 Nikolay Strelkov <snk@altlinux.org> 22.9.0-alt1
- Initial build for Sisyphus

