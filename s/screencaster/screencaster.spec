Name: screencaster
Version: 0.5
Release: alt1

Summary: Screencaster
Packager: Dmitry Derjavin <dd@altlinux.org> 
License: GPLv3+
Group: Video
Url: http://git.altlinux.org/people/dd/packages/screencaster.git

Source: %name-%version.tar

BuildArch: noarch

Requires: ffmpeg

%description
ffmpeg based screencaster

%prep
%setup

%install
mkdir -p -m755 %buildroot%_bindir
cp -a recstart %buildroot%_bindir
cp -a recstop %buildroot%_bindir

%files
%doc screencasterrc article.*
%_bindir/*

%changelog
* Fri Feb 11 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.5-alt1
- avconv/ffmpeg switch back. Note: avconv is obsolete.
- fix recstop command with signal -2 due error with file save.

* Fri Sep 21 2012 Dmitry Derjavin <dd@altlinux.org> 0.4-alt1
- Check for data directory availability;
- simple check for Pulse Audio, else fall back to ALSA;
- current directory is now default data directory;
- ffmpeg/avconv configuration switch.

* Tue Sep 04 2012 Dmitry Derjavin <dd@altlinux.org> 0.3-alt1
- Example configuration file errors fixed;
- OSS@highschool conference abstract added as a doc.

* Fri Jul 27 2012 Ildar Mulyukov <ildar@altlinux.ru> 0.2-alt1
- new snapshot

* Sun Jan 30 2011 Dmitry Derjavin <dd@altlinux.org> 0.1-alt1
- Initial release. Spec file by sin@altlinux.org.
