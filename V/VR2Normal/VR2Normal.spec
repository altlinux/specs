Name:    VR2Normal
Version: 3.6
Release: alt1

Summary: Program that converts virtual reality videos into normal videos for viewing on any screen
License: GPL-3.0-or-later
Group:   Video
URL:     https://vongoob9.gitlab.io/vr2normal
VCS:     https://gitlab.com/vongooB9/vr2normal.git

Source: %name-%version.tar
Patch:  VR2Normal-3.6-fix-icons-path.patch

BuildRequires(pre): rpm-macros-qt6
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel

%description
This program allows you to convert a 3D VR video into a normal video, using a virtual
camera to select the most relevant parts of the video at different times. It also
allows you to create screenshots and small webp and gif animations.
The program is basically a GUI for ffmpeg using the v360 and sendcmd plugins.
It generates the ffmpeg command and the sendcmd file needed to convert the video.

%prep
%setup
%patch -p1

%build
%qmake_qt6 USR_DIR=%_prefix
%make_build

%install
%install_qt6_base

%files
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/scalable/mimetypes/VR2NormalFile.svg
%_datadir/mime/packages/vr2normal.xml

%changelog
* Sun Jun 14 2026 Sergey Palcheh <minergenon@altlinux.org> 3.6-alt1
- Initial build for Sisyphus
