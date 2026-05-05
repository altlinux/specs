%define _unpackaged_files_terminate_build 1

Name: reco
Version: 5.2.0
Release: alt1

Summary: An audio recorder focused on being concise and simple to use
License: GPL-3.0
Group: Sound
Url: https://github.com/ryonakano/reco

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(livechart-2)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(ryokucha)

%description
Reco is an audio recorder focused on being concise and simple to use.

You can use it to record and remember spoken words, system audio,
improvized melodies, and anything else you can do with a microphone,
speaker, or both.

Features include:

* Recording sounds from both your microphone and system at the same
  time. This is useful for recording calls or streaming videos on
  the Internet.
* Saving in many commonly used formats. It supports ALAC, FLAC, MP3,
  Ogg Vorbis, Opus, and WAV.
* Timed recording. You can set a delay before recording up to 15
  seconds, and set the length of recording up to 600 seconds.
* Choosing where to save recordings. You can select whether the app
  saves recordings into a directory of your choosing automatically
  or manually.
* Saving recordings when the app quits. Even if you happen to quit
  the app while recording, the recording is either saved
  automatically, or the file chooser dialog is shown - depending on
  your preferences.

%prep
%setup
sed -i 's|^Categories=Audio;AudioVideo;Utility;Recorder;|Categories=GNOME;GTK;AudioVideo;Recorder;|' data/reco.desktop.in.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --all-name

%check
%meson_test

%files -f %{name}.lang
%doc CONTRIBUTING.md LICENSE README.md RELEASE_HOWTO.md
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/scalable/apps/*.svg
%_datadir/glib-2.0/schemas/*.gschema.xml
%_datadir/metainfo/*.metainfo.xml

%changelog
* Tue May 05 2026 Nikolay Strelkov <snk@altlinux.org> 5.2.0-alt1
- New version 5.2.0.

* Sun Oct 26 2025 Nikolay Strelkov <snk@altlinux.org> 5.1.1-alt1
- Initial build for Sisyphus
