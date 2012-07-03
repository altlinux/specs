Name: rumor
Version: 1.0.3
Release: alt1.beta

Summary: Really Unintelligent Music transcriptOR
License: %gpl2only
Url: http://www.volny.cz/smilauer/rumor/
Group: Sound

Packager: Artem Zolochevskiy <azol@altlinux.ru>

# http://www.volny.cz/smilauer/rumor/src/rumor-1.0.3b.tar.bz2
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Sep 27 2009
BuildRequires: gcc-c++ guile18-devel libalsa-devel

%description
Rumor is a realtime monophonic (with chords) MIDI keyboard to Lilypond
converter. It receives MIDI events, quantizes them according to its
metronome on the fly and outputs handwritten-like corresponding Lilypond
notation. Tempo, meter, key and other parameters can be set via
command-line options.

%prep
%setup
%patch -p1

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/*
%_infodir/*

%changelog
* Sun Sep 27 2009 Artem Zolochevskiy <azol@altlinux.ru> 1.0.3-alt1.beta
- initial build for Sisyphus
