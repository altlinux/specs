%define _unpackaged_files_terminate_build 1

%define appname com.github.hezral.keystrokes

Name: keystrokes
Version: 1.0.2
Release: alt1

Summary: Simple keystrokes on-screen display
License: GPL-3.0-or-later
Group: Graphical desktop/Other
URL: https://github.com/hezral/keystrokes

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-python3

BuildRequires: meson
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

Requires: python3(gi)
Requires: python3-module-xlib
Requires: python3(pynput)
Requires: libgranite-gir-devel

BuildArch: noarch

Source: %name-%version.tar

%description
Simple on-screen keyboard and mouse keystrokes display

%prep
%setup
sed -i "s|data/screenshot-01.png?raw=true|screenshot-01.png|" README.md
sed -i "s|data/screenshot-02.png?raw=true|screenshot-02.png|" README.md
sed -i "s|clips|keystrokes|" README.md
sed -i "s|Categories=.*|Categories=Accessibility;Utility;|" data/com.github.hezral.keystrokes.desktop.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%check
%meson_test

%files -f %{name}.lang
%doc COPYING README.md data/screenshot-01.png data/screenshot-02.png
%_bindir/%name
%_desktopdir/%{appname}.desktop
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_datadir/metainfo/%{appname}.appdata.xml
%dir %_datadir/com.github.hezral.keystrokes
%_datadir/com.github.hezral.keystrokes

%changelog
* Sun Nov 02 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
