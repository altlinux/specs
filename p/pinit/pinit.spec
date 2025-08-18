%define _unpackaged_files_terminate_build 1

Name: pinit
Version: 2.2.0
Release: alt1

Summary: Pin portable apps to the launcher
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/ryonakano/pinit

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-vala
BuildRequires: meson
BuildRequires: vala
BuildRequires: vala-tools
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)

%description
Pin shortcuts for portable apps like raw executable files, AppImage
files, etc. to the app launcher on your desktop.

Other features include:

- Edit or delete created app entries without opening the file manager
- Automatically add execution permission to the file you select

%prep
%setup
sed -i "s|Categories=.*|Categories=Utility;FileTools|" data/pinit.desktop.in.in

%build
%meson
%meson_build

%install
%meson_install

# this translation is ignored by %%find_lang
rm -fv %buildroot%_datadir/locale/zh_Hans/LC_MESSAGES/*.mo

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc CONTRIBUTING.md LICENSE README.md data/screenshots/gnome
%_bindir/*
%_desktopdir/*
%_iconsdir/*/*/apps/*
%_datadir/glib-2.0/schemas/*.xml
%_datadir/metainfo/*.xml

%changelog
* Mon Aug 18 2025 Nikolay Strelkov <snk@altlinux.org> 2.2.0-alt1
- New version 2.2.0.

* Wed Jul 02 2025 Nikolay Strelkov <snk@altlinux.org> 2.1.1-alt1
- Initial build for Sisyphus
