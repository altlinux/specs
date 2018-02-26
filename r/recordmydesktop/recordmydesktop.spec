Name: recordmydesktop
Version: 0.3.8.1
Release: alt2

Summary: Captures audio-video data of a linux desktop session (screencasting)
Group: Video
License: GPLv2+

Url: http://sourceforge.net/projects/recordmydesktop/
Source: %name-%version.tar.gz

Patch1: %name-0.3.8.1-alt-headers.patch
Patch2: %name-sane-theora-defaults.patch

# Automatically added by buildreq on Sun Sep 21 2008
BuildRequires: jackit-devel libX11-devel libXext-devel libSM-devel libXdamage-devel libXext-devel libalsa-devel libtheora-devel libvorbis-devel xorg-cf-files zlib-devel

%description 
recordMyDesktop is a command line screencasting program
that captures audio-video data of a linux desktop session,
producing an ogg-encapsulated theora-vorbis file.
recordMyDesktop tries to be as unobstrusive as possible
by proccessing only regions of the screen
that have changed.

%prep
%setup -q -n %name-%version
%patch1 -p1
%patch2 -p1

%build
%configure
%make_build

%install
%makeinstall

%files
%doc AUTHORS ChangeLog NEWS README TODO INSTALL
%_bindir/*
%_man1dir/*

%changelog
* Tue Aug 23 2011 Sergey Kurakin <kurakin@altlinux.org> 0.3.8.1-alt2
- encoding with libtheora 1.1 fixed (patch from Fedora)

* Sun Apr 11 2010 Sergey Kurakin <kurakin@altlinux.org> 0.3.8.1-alt1
- 0.3.8.1 (maintenance release)
- fixed build with new xorg

* Thu Dec  4 2008 Sergey Kurakin <kurakin@altlinux.org> 0.3.8-alt1
- 0.3.8 (mostly bugfix release)

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.3.7.3-alt2.1
- NMU:
  * updated build dependencies

* Tue Dec  2 2008 Sergey Kurakin <kurakin@altlinux.ru> 0.3.7.3-alt2
- build fixed (BuildRequires)

* Sun Sep 21 2008 Sergey Kurakin <kurakin@altlinux.ru> 0.3.7.3-alt1
- initial build for AltLinux Sisyphus
