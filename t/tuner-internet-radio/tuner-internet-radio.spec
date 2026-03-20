%define _unpackaged_files_terminate_build 1

%define appname io.github.tuner_labs.tuner

Name: tuner-internet-radio
Version: 2.1.0
Release: alt1

Summary: Minimalist internet radio station player
License: GPL-3.0-or-later
Group: Sound
Url: https://github.com/tuner-labs/tuner

Source: %name-%version.tar

Patch: %name-%version-%release.patch

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
sed -i "s|flathub/||g" README.md
%patch -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc LICENSE README.md flathub/logo_01.png flathub/Tuner.210.one.png
%_bindir/%{appname}
%_desktopdir/%{appname}.desktop
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_iconsdir/hicolor/scalable/apps/%{appname}-scalable.svg
%_iconsdir/hicolor/symbolic/apps/%{appname}-symbolic.svg
%exclude %_datadir/locale/es_419/LC_MESSAGES/io.github.tuner_labs.tuner.mo
%exclude %_datadir/locale/zh_Hant/LC_MESSAGES/io.github.tuner_labs.tuner.mo
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Fri Mar 20 2026 Nikolay Strelkov <snk@altlinux.org> 2.1.0-alt1
- New version 2.1.0.

* Sun Dec 28 2025 Nikolay Strelkov <snk@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus
