%define _unpackaged_files_terminate_build 1

Name: xfce4-indicator-plugin
Version: 2.4.1
Release: alt3

Summary: Plugin to display information from applications in the Xfce panel
License: GPL-2.0-or-later
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/panel-plugins/xfce4-indicator-plugin

Source: %name-%version.tar
Patch: %name-%version-alt-ayatana.patch

BuildRequires(pre): rpm-build-xfce4

BuildRequires: libayatana-indicator3-devel
BuildRequires: libxfce4panel-gtk3-devel
BuildRequires: libxfce4ui-gtk3-devel
BuildRequires: intltool

Requires: xfce4-panel >= 4.11

%description
A small plugin to display information from various applications
consistently in the Xfce panel as described in
Ubuntu's MessagingMenu design specification.

%prep
%setup
%patch -p1

# Don't use git tag in version.
%xfce4_drop_gitvtag indicator_version_tag configure.ac.in

%build
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README.md AUTHORS COPYING* NEWS
%_libdir/xfce4/panel/plugins/libindicator-plugin.so
%exclude %_libdir/xfce4/panel/plugins/libindicator-plugin.la
%_iconsdir/hicolor/*/apps/%name.*
%_datadir/xfce4/panel/plugins/indicator.desktop

%changelog
* Sat Oct 12 2024 Nikolay Strelkov <snk@altlinux.org> 2.4.1-alt3
- fix FTBFS by adding intltool build dependency

* Sun Nov 12 2023 Nikolay Strelkov <snk@altlinux.org> 2.4.1-alt2
- Handle review issues:
  + removed obsolete Packager tag
  + break BuildRequires to multiple lines
  + renamed patch

* Fri Feb 10 2023 Nikolay Strelkov <snk@altlinux.org> 2.4.1-alt1
- initial build for ALT Sisyphus

