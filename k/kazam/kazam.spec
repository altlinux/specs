%define _unpackaged_files_terminate_build 1

Name: kazam
Version: 2.0.0
Release: alt1

Summary: Kazam - Linux Screen Recorder, Broadcaster, Capture and OCR with AI in mind
License: GPL-3.0 and LGPL-3.0
Group: Video
URL: https://github.com/henrywoo/kazam

BuildRequires(pre): rpm-build-gir
BuildRequires: python3-devel
BuildRequires: python3-module-distutils-extra
BuildRequires: intltool
BuildRequires: python3(hiq)

Requires: typelib(AyatanaAppIndicator3)
Requires: python3(PIL)
Requires: python3(pytesseract)
Requires: /usr/bin/tesseract
Requires: /usr/bin/xdotool
Requires: /usr/bin/canberra-gtk-play
Requires: /usr/bin/xdg-open

%filter_from_requires /python3(rapidocr_onnxruntime)/d

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
Kazam 2.0 is a versatile tool for screen recording, broadcasting,
capturing and optical character recognition(OCR).

Main Features:
* Screen Recording: Kazam allows you to capture everything displayed on
  your screen and save it as a video file. The recorded video is saved in
  a format compatible with any media player that supports H264, VP8 codec
  and WebM video format.
* Broadcasting: Kazam offers the ability to broadcast your screen content
  live over the internet, making it suitable for live streaming sessions.
  It supports Twitch and Youtube live broadcasting at the time of this
  writing.
* Optical Character Recognition (OCR): Kazam includes OCR functionality,
  enabling it to detect and extract text from the captured screen
  content, which can then be edited or saved.
* Audio Recording: In addition to screen content, Kazam can record audio
  from any sound input device that is recognized and supported by the
  PulseAudio sound system. This allows you to capture both the screen
  and accompanying audio, such as voice narration or system sounds,
  in your recordings.
* Web Camera: Kazam support web camera recording and users can drag and
  drop webcam window anywhere in the screen to suit the recording need.
* Full Screen, Window and Area Mode: Kazam support full screen, window
  and area modes.

%prep
%setup -n %name-%version
%patch -p1

sed -i s,"DISTRO = 'Ubuntu'","DISTRO = '%vendor'",g kazam/version.py
sed -i s,"RELEASE = '.*'","RELEASE = '$(rpm --eval %%_priority_distbranch)'",g kazam/version.py

ln -s ../data kazam/data

%build
%python3_build
%__python3 setup.py build_icons
%__python3 setup.py build_i18n

%install
%python3_install

# icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/
cp -rva data/icons/*x* %{buildroot}%{_iconsdir}/hicolor/

# desktop file
sed -i s,"^_","",g data/kazam.desktop.in
mkdir -p "%buildroot%_datadir/applications/"
cp -vfa data/kazam.desktop.in %{buildroot}%{_datadir}/applications/kazam.desktop

# locales
mkdir -p %buildroot%_datadir/locale
cp -rva build/mo/* %buildroot%_datadir/locale

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING COPYING.LGPL NEWS README.md TODO
%_bindir/%name
%_desktopdir/%{name}.desktop
%dir %python3_sitelibdir/%name/
%python3_sitelibdir/%name/*
%dir %python3_sitelibdir/%{name}*info/
%python3_sitelibdir/%{name}*info/*
%_datadir/icons/gnome/*/apps/*
%_datadir/icons/hicolor/*/apps/*
%_datadir/icons/hicolor/*/status/*
%_datadir/icons/hicolor/*/icons/*
%_datadir/icons/hicolor/*/%{name}.*
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Sun Mar 16 2025 Nikolay Strelkov <snk@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus with support of Ayatana Indicator
