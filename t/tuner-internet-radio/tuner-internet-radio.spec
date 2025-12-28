%define _unpackaged_files_terminate_build 1

%define appname com.github.louis77.tuner

Name: tuner-internet-radio
Version: 2.0.0
Release: alt1

Summary: Minimalist internet radio station player
License: GPL-3.0-or-later
Group: Sound
Url: https://github.com/tuner-labs/tuner

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-player-1.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: vapi(granite)

%description
Discover and Listen to your favourite internet radio stations.

%prep
%setup
sed -i "s|docs/logo_01.png|%_iconsdir/hicolor/64x64/apps/com.github.louis77.tuner.svg|" README.md
sed -i "s|docs/Tuner_2.0_discover.png?raw=true|Tuner_2.0_discover.png|" README.md
sed -i "s|^meson.add_install_script|#meson.add_install_script|" data/meson.build

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc LICENSE NOTES.md README.md docs/Tuner_2.0_discover.png
%_bindir/%{appname}
%_desktopdir/%{appname}.desktop
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_iconsdir/hicolor/*/apps/%{appname}.svg
%exclude %_datadir/locale/de/LC_MESSAGES/de.mo
%exclude %_datadir/locale/es/LC_MESSAGES/es.mo
%exclude %_datadir/locale/fr/LC_MESSAGES/fr.mo
%exclude %_datadir/locale/it/LC_MESSAGES/it.mo
%exclude %_datadir/locale/ja/LC_MESSAGES/ja.mo
%exclude %_datadir/locale/nb_NO/LC_MESSAGES/nb_NO.mo
%exclude %_datadir/locale/nl/LC_MESSAGES/nl.mo
%exclude %_datadir/locale/pt_BR/LC_MESSAGES/pt_BR.mo
%exclude %_datadir/locale/ru/LC_MESSAGES/ru.mo
%exclude %_datadir/locale/tr/LC_MESSAGES/tr.mo
%_datadir/metainfo/%{appname}.appdata.xml

%changelog
* Sun Dec 28 2025 Nikolay Strelkov <snk@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus
