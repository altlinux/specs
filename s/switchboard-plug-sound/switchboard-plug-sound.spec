%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.settings.sound

Name: switchboard-plug-sound
Version: 8.0.3
Release: alt1

Summary: Switchboard Sound Plug
License: LGPL-2.1-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/settings-sound

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(switchboard-3)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: vapi(libcanberra)

%description
Sound plug for Switchboard.
This plug allows the user to set the audio and microphone volume and several
sound-related settings.

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
%_libdir/switchboard-3/system/libio.elementary.settings.sound.so
%_datadir/glib-2.0/schemas/sound.gschema.xml
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Tue May 05 2026 Nikolay Strelkov <snk@altlinux.org> 8.0.3-alt1
- New version 8.0.3.

* Fri Nov 14 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.2-alt1
- New version 8.0.2.

* Sun Sep 21 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.1-alt1
- Initial build for Sisyphus
