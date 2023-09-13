%define _unpackaged_files_terminate_build 1

Name:     bottles
Version:  51.9
Release:  alt1
Epoch:    1

Summary:  Easily manage wine prefixes in a new way. Run Windows software and games on Linux
License:  GPL-3.0
Group:    Other
Url:      https://github.com/bottlesdevs/Bottles

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   Bottles-%version.tar

BuildArch: noarch

BuildRequires(pre): meson
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-gir
BuildRequires: libhandy1-devel
BuildRequires: libappstream-glib
BuildRequires: blueprint-compiler
BuildRequires: libadwaita-gir-devel

Requires: typelib(WebKit2) = 4.0
Requires: typelib(GtkSource) = 5

%add_python3_path %_datadir/%name

%description
Easily manage wineprefix using environments.

%prep
%setup -n Bottles-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name
echo %_datadir/locale/zh_Hans/LC_MESSAGES/bottles.mo >> %name.lang
echo %_datadir/locale/zh_Hant/LC_MESSAGES/bottles.mo >> %name.lang

%files -f %name.lang
%doc *.md
%_bindir/%name
%_bindir/%name-cli
%_datadir/%name
%_datadir/glib-2.0/schemas/*.gschema.xml
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/apps/*.svg
%_iconsdir/hicolor/symbolic/apps/*.svg
%_datadir/metainfo/*.metainfo.xml

%changelog
* Wed Sep 13 2023 Andrey Cherepanov <cas@altlinux.org> 1:51.9-alt1
- New version.

* Sat Oct 22 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 2022.5.28-alt2.trento.3
- NMU: Added needed Requires (ALT #44023).

* Sun Jun 05 2022 Andrey Cherepanov <cas@altlinux.org> 2022.5.28-alt1.trento.3
- Initial build for Sisyphus (ALT #42935).
