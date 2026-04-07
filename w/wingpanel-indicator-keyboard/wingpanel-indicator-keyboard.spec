%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.panel.keyboard

Name: wingpanel-indicator-keyboard
Version: 2.4.2
Release: alt1.git.f0403d0

Summary: Wingpanel Keyboard Indicator
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/panel-keyboard

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(xkeyboard-config)
BuildRequires: libwingpanel-devel
BuildRequires: pkgconfig(ibus-1.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: vapi(granite)

%description
Settings plugin for keyboard settings.
This plug can be used to change several keyboard settings, for example
the delay and speed of the key repetition, or the cursor blinking speed.
You can change your keyboard layout, and use multiple layouts at the
same time.
Keyboard shortcuts are also part of this plug.

%prep
%setup

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
%_libdir/wingpanel-9/libkeyboard.so
%_datadir/glib-2.0/schemas/io.elementary.panel.keyboard.gschema.xml
%_datadir/metainfo/io.elementary.panel.keyboard.metainfo.xml

%changelog
* Tue Apr 07 2026 Nikolay Strelkov <snk@altlinux.org> 2.4.2-alt1.git.f0403d0
- Initial build for Sisyphus
