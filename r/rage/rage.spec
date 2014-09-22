Name: rage
Version: 0.1.0
Release: alt2

Summary: EFL Video Player
License: BSD
Group: Video

Url: http://www.enlightenment.org/
Source: http://download.enlightenment.org/releases/%name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: efl-libs-devel >= 1.11.0
BuildRequires: libelementary-devel >= 1.11.0

%description
Rage is a video and audio player written with Enlightenment
Foundation Libraries with some extra bells and whistles.

It is a simple video and audio player intended to be slick yet
simplistic, much like Mplayer. You can provide 1 or more files to
play on the command-line or just DND files onto the rage window
to insert them into the playlist. You can get a visual
representation of everything on the playlist by hitting the /
key, or just hovering your mouse over the right side of the
window. Mouse back over the left side of the window ti dismiss it
or press the key again. It has a full complement of key controls
if you see the README for the full list. It will automatically
search for album art for music files, if not already cached, and
display that. It even generates thumbnails for the timeline of a
video and allows you to preview the position on mouseover of the
position bar at the bottom of the window.

Here is a list of all the things it can do:

* Play video and audio files
* Support a playlist via command-line
* Insert to playlist via DND
* Controls hide on mouse idle, and appear on mouse movement
* Fullscreen mode support with automatic "no blank" support
* Playlist visual previews and controls
* Subtitle file support
* Supports Gstreamer 0.10, Gstreamer 1.x, Xine and VLC
  as media engines via Emotion modules
* Selection of media back-end via command-line
* Album art fetch and caching
* Video thumbnail timeline generation and caching
* Works with any Evas engine (OpenGL acceleration, pure software etc.)
* Works in X11, Wayland and Framebuffer direct support
* Accelerated seek on keyboard fowrard/reverse
* Drag gestures for seeking
* Special different UI modes for pure audio and video

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING README
%_bindir/%name
%_libdir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%_iconsdir/%name.png

%changelog
* Mon Sep 22 2014 Michael Shigorin <mike@altlinux.org> 0.1.0-alt2
- built for sisyphus (rebased upon ge1184db)

* Wed Aug 27 2014 Michael Shigorin <mike@altlinux.org> 0.1.0-alt1
- built for ALT Linux

