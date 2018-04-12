Name: green-recorder
Summary: A simple yet functional desktop recorder for Linux systems
Group: Video
Url: https://github.com/foss-project/%name
Version: 3.1
Release: alt1
Packager: Anton Midyukov <antohami@altlinux.org>
Source: %name-%version.tar
License: GPLv3
BuildArch: noarch
BuildRequires: python-devel rpm-build-python rpm-build-gir
Requires: ffmpeg
Requires: pulseaudio

%description
A simple desktop recorder for Linux systems. Supports both Xorg
server and Wayland (GNOME).

The following formats are currently supported: mkv, avi, mp4, wmv,
gif and nut (And only WebM for Wayland's GNOME session). You can
stop the recording process easily by right-clicking the icon and
choosing "Stop Record". Or middle-clicking the recording icon in
the notifications area (but doesn't work on all interfaces).

You can choose the audio input source you want from the list. You
can also set the default values you want from the preferences
window. And a lot more.

%prep
%setup

%build
%python_build

%install
%python_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%python_sitelibdir/*
%_datadir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Thu Apr 12 2018 Anton Midyukov <antohami@altlinux.org> 3.1-alt1
- new version 3.1

* Fri Oct 06 2017 Anton Midyukov <antohami@altlinux.org> 3.0.4-alt1
- new version 3.0.4

* Tue Aug 08 2017 Anton Midyukov <antohami@altlinux.org> 3.0.3-alt1
- Initial build for ALT Sisyphus.
