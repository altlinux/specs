Name: mpdtoys
Version: 0.20
Release: alt1.1

Summary: Small command line tools and toys for MPD
License: GPLv2+
Group: Sound

Url: http://kitenet.net/~joey/code/mpdtoys/

Packager: Andrey Rahmatullin <wrar@altlinux.ru>
BuildArch: noarch

# git://git.kitenet.net/mpdtoys
Source: %name-%version.tar

%define _unpackaged_files_terminate_build 1

BuildPreReq: perl-Audio-MPD perl-Term-ReadKey
BuildRequires: perl-podlators

%description
This is a collection of small toys and tools for doing various things to
MPD (Music Player Daemon) from the command line. Some of them are very
useful, while others are only amusing.
Some examples of things the mpdtoys can do include moving the playing
song between different mpd daemons on different machines, storing the
state of a mpd daemon and loading it back later, reversing the playlist,
slowly fading volume up or down, stopping playback after the current
song finishes, emulating a skipping record, and editing the playlist in
a text editor.

%prep
%setup

%install
%makeinstall_std

%files
%doc TODO debian/changelog
%_bindir/*
%perl_vendor_privlib/*.pm
%_man1dir/*

%changelog
* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Oct 26 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.20-alt1
- 0.20

* Sun Mar 08 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.12-alt1
- 0.12

* Sun Oct 12 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.8-alt1
- initial build
