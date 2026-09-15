Name: speedofsound
Version: 0.14.0
Release: alt1

Summary: Voice typing for the GNOME and KDE
License: MIT
Group: Accessibility
URL: https://www.speedofsound.io
VCS: https://github.com/zugaldia/speedofsound.git

Source0: %name-%version.tar
Source1: gradle-cache.tar
Source2: models-onnx.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: rpm-build-ninja
BuildRequires: rpm-build-java
BuildRequires: /proc

BuildRequires: meson
BuildRequires: glib2-devel
BuildRequires: gtk4-update-icon-cache
BuildRequires: java-25-openjdk-devel

Requires: java

ExcludeArch: %ix86

%description
Offline, on-device transcription using models like Whisper, Parakeet, and
Canary, with no data leaving your machine. Activate via in-app button, global
shortcut, or system tray. Types results directly into any focused app
(X11/Wayland). Supports multi-language switching, built-in
multilingual Whisper models, and optional LLM-based text polishing (Anthropic,
Google, OpenAI, or self-hosted services like vLLM, Ollama, and llama.cpp).

%prep
%setup -a2
%autopatch -p1
tar xf %SOURCE1 -C ~

%build
%meson
%meson_build

%install
%meson_install
install -pm 0755 scripts/trigger.sh %buildroot%_libexecdir/%name
sed -i 's|^CLASSPATH=$APP_HOME/.*|CLASSPATH=%_libexecdir/%name/%name.jar|' %buildroot%_bindir/%name

%files
%_bindir/%name
%_libexecdir/%name
%_desktopdir/io.speedofsound.SpeedOfSound.desktop
%_datadir/dbus-1/services/io.speedofsound.SpeedOfSound.service
%_datadir/glib-2.0/schemas/io.speedofsound.SpeedOfSound.gschema.xml
%_iconsdir/hicolor/scalable/apps/io.speedofsound.SpeedOfSound.svg
%_metainfodir/io.speedofsound.SpeedOfSound.metainfo.xml

%changelog
* Tue Sep 15 2026 Ulysses Apokin <ulysses@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus.
