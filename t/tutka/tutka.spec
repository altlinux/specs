Name: tutka
Version: 0.12.4
Release: alt1

Summary: tracker style MIDI sequencer
License: %gpl2plus
Group: Sound
Url: http://www.nongnu.org/tutka/

Packager: Timur Batyrshin <erthad@altlinux.org>
Source0: %name-%version.tar.bz2

BuildPreReq: rpm-build-licenses
BuildRequires: gcc-c++ libalsa-devel libgtk+2-devel libgnomeui-devel libxml2-devel libglade-devel

%description
Tutka is a free (as in freedom) tracker style MIDI sequencer for GNU/Linux (and
other systems; only GNU/Linux is supported at this time though). It is similar
to programs like SoundTracker, ProTracker and FastTracker except that it does
not support samples and is meant for MIDI use only. Tutka is licensed under the
GNU GPL.
   
%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std
mkdir -p %buildroot/%_liconsdir/
mv %buildroot%_pixmapsdir/* %buildroot/%_liconsdir/
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README TODO 
%_bindir/*
%_sysconfdir/gconf/schemas/*.schemas
%_desktopdir/*
%_liconsdir/*
%_datadir/%name

%changelog
* Sun Sep 13 2009 Timur Batyrshin <erthad@altlinux.org> 0.12.4-alt1
- initial build for sisyphus

