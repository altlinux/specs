Name:           peek
Version:        1.5.1
Release:        alt2

Summary:        Simple animated GIF screen recorder with an easy to use interface

License:        GPLv3
Group:          Video
Url:            https://github.com/phw/peek

# Source-url: https://github.com/phw/peek/archive/refs/tags/%version.tar.gz
Source:	%name-%version.tar

Patch1: peek-1.5.1-alt-fix-meson-build-python-requires.patch

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  libgtk+3-devel
BuildRequires:  libkeybinder3-devel

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  txt2man

Requires: ffmpeg
Requires: icon-theme-hicolor

%description
Peek makes it easy to create short screencasts of a screen area. It was built
for the specific use case of recording screen areas, e.g. for easily showing UI
features of your own apps or for showing a bug in bug reports. With Peek, you
simply place the Peek window over the area you want to record and press
"Record". Peek is optimized for generating animated GIFs, but you can also
directly record to WebM or MP4 if you prefer.

Peek is not a general purpose screencast app with extended features but rather
focuses on the single task of creating small, silent screencasts of an area of
the screen for creating GIF animations or silent WebM or MP4 videos.

%prep
%setup -q -n %name-%version
%patch1 -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/com.uploadedlobster.peek.appdata.xml
desktop-file-validate %buildroot%_desktopdir/com.uploadedlobster.peek.desktop

%files -f peek.lang
%doc README.md CHANGES.md AUTHORS
%_man1dir/peek.1
%_bindir/peek
%_desktopdir/com.uploadedlobster.peek.desktop
%_datadir/metainfo/com.uploadedlobster.peek.appdata.xml
%_datadir/glib-2.0/schemas/com.uploadedlobster.peek.gschema.xml
%_iconsdir/hicolor/*/apps/com.uploadedlobster.peek*.svg
%_datadir/dbus-1/services/com.uploadedlobster.peek.service

%changelog
* Fri Dec 03 2021 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.5.1-alt2
- Change patch to fix python command for meson.build

* Wed Dec 01 2021 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.5.1-alt1
- new version (1.5.1) with rpmgs script
- Add patch to fix python command for meson.build
