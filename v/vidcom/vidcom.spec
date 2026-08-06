%define _unpackaged_files_terminate_build 1
%define oname io.github.seja_arctic_fox.vidcom

Name: vidcom
Version: 0.83
Release: alt1

Summary: Archive your videos easily
License: GPL-3.0-only
Group: Video

Url: https://seja-arctic-fox.github.io
Vcs: https://github.com/seja-arctic-fox/vidcom

Source: %name-%version.tar

Requires: ffmpeg

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++ pkgconfig(gtkmm-4.0)
BuildRequires: cmake pkgconfig(libadwaita-1) jsoncpp-devel

%description
VidCom (short for Video Compression) is a simple utility for archiving
videos. It offers both GUI and CLI interface and utilises ffmpeg for
the video encoding.

For screenshots and basic information, visit the project website.

VidCom features two modes; Archive mode and Compress mode:

Archive mode compresses a video as much as possible without losing
target image quality.

Compress mode compresses a video to a specified target size.

There are also other options for quick setup, such as reducing resolution
and frame rate, choosing an output directory and a trimming function. More
advanced users can set the codec used for encoding and tweak some parameters
of chosen codec to trade time for better compression and vice versa.

You can process as many videos as you want by adding them to a queue (GUI)
or specifying their paths in the command (CLI).

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc *.md
%_bindir/%name
%_desktopdir/%oname.desktop
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%oname.metainfo.xml
%_datadir/glib-2.0/schemas/%oname.gschema.xml

%changelog
* Fri Aug 07 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.83-alt1
- 0.82 -> 0.83

* Fri Jun 19 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.82-alt1
- Initial build for ALT Linux.

