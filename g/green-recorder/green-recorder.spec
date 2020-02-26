Name: green-recorder
Version: 3.2.2
Release: alt2

Summary: A simple yet functional desktop recorder for Linux systems
License: GPLv3
Group: Video
Url: https://github.com/foss-project/%name
Packager: Anton Midyukov <antohami@altlinux.org>

BuildArch: noarch

Source: %name-%version.tar
Patch0: port-to-python3.patch
Patch1: fix-using-undeclared-var.patch

BuildRequires(pre): rpm-build-python3 rpm-build-gir


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
%patch0 -p1
%patch1 -p1

%build
%python3_build_debug

%install
%python3_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%python3_sitelibdir/*
%_datadir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png


%changelog
* Tue Feb 25 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.2.2-alt2
- Porting to python3.

* Fri Jul 05 2019 Anton Midyukov <antohami@altlinux.org> 3.2.2-alt1
- new version 3.2.2

* Thu Apr 12 2018 Anton Midyukov <antohami@altlinux.org> 3.1-alt1
- new version 3.1

* Fri Oct 06 2017 Anton Midyukov <antohami@altlinux.org> 3.0.4-alt1
- new version 3.0.4

* Tue Aug 08 2017 Anton Midyukov <antohami@altlinux.org> 3.0.3-alt1
- Initial build for ALT Sisyphus.
