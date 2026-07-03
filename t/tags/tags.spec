%define _unpackaged_files_terminate_build 1

%define appname io.github.phastmike.tags

Name: tags
Version: 2.2
Release: alt1

Summary: A simple text tagger
License: MIT
Group: Text tools
Url: https://github.com/phastmike/tags

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gee-0.8)

%description
A GNOME text tagger inspired by the TextAnalysisTool.NET tool.

The main goal is to aid log analysis by tagging lines with user defined
colors. Tags have a match pattern, description name, visibility toggle,
color scheme and hit counter.

%prep
%setup
sed -i "s|./data/screenshots/||" README.md
sed -i "s|Categories=.*|Categories=GTK;Utility;TextTools;FileTools;|" data/io.github.phastmike.tags.desktop.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --all-name

%check
%meson_test

%files -f %{name}.lang
%doc COPYING README.md data/screenshots/tags-default.png
%_bindir/tags
%_desktopdir/%{appname}.desktop
%_datadir/appdata/%{appname}.appdata.xml
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_iconsdir/hicolor/scalable/apps/%{appname}.svg
%_iconsdir/hicolor/symbolic/apps/%{appname}-symbolic.svg

%changelog
* Fri Jul 03 2026 Nikolay Strelkov <snk@altlinux.org> 2.2-alt1
- New version 2.2.

* Sat Apr 11 2026 Nikolay Strelkov <snk@altlinux.org> 2.1-alt2
- Fix FTBFS.

* Sat Mar 28 2026 Nikolay Strelkov <snk@altlinux.org> 2.1-alt1
- New version 2.1.

* Sun Jan 11 2026 Nikolay Strelkov <snk@altlinux.org> 2.0-alt1
- New version 2.0.

* Sun Dec 28 2025 Nikolay Strelkov <snk@altlinux.org> 1.8-alt1
- Initial build for Sisyphus
