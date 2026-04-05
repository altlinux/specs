%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.settings.keyboard

Name: switchboard-plug-keyboard
Version: 8.1.1
Release: alt1

Summary: Switchboard Keyboard Plug
License: GPL-2.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/settings-keyboard

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(xkeyboard-config)
BuildRequires: pkgconfig(switchboard-3)
BuildRequires: pkgconfig(ibus-1.0)
BuildRequires: pkgconfig(libxml-2.0)

%description
%summary

%prep
%setup
sed -i '/var install_button = add_button (_("Install Unlisted Engines…"), Gtk.ResponseType.OK);/d' src/InputMethod/Widgets/AddEngineDialog.vala

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc COPYING README.md
%_libdir/switchboard-3/hardware/libkeyboard.so
%_datadir/glib-2.0/schemas/io.elementary.settings.keyboard.gschema.xml
%_datadir/metainfo/io.elementary.settings.keyboard.metainfo.xml

%changelog
* Sun Apr 05 2026 Nikolay Strelkov <snk@altlinux.org> 8.1.1-alt1
- New version 8.1.1.

* Sun Sep 21 2025 Nikolay Strelkov <snk@altlinux.org> 8.1.0-alt1
- Initial build for Sisyphus
