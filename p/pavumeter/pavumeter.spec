Name: pavumeter
Version: 0.9.3
Release: alt3.qa3

Summary: PulseAudio Volume Meter
Group: Sound
License: GPL
Url: http://0pointer.de/lennart/projects/pavumeter/

Source0: %name-%version.tar.gz
Patch0: pavumeter-0.9.3-alt-fix-desktop-file.patch

Packager: Igor Zubkov <icesik@altlinux.org>

Requires: pulseaudio >= 0.9.2

# Automatically added by buildreq on Wed Mar 05 2008
BuildRequires: gcc-c++ libgtkmm2-devel libpulseaudio-devel lynx
BuildRequires: desktop-file-utils

%description
PulseAudio Volume Meter (pavumeter) is a simple GTK volume meter for
the PulseAudio sound server.

%prep
%setup -q
%patch0 -p1

%build
%add_optflags -std=gnu++11
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Mixer \
	%buildroot%_desktopdir/pavumeter.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Mixer \
	%buildroot%_desktopdir/pavumeter-record.desktop

%files
%doc README doc/README.html doc/style.css
%_bindir/*
%_datadir/applications/pavumeter.desktop
%_datadir/applications/pavumeter-record.desktop

%changelog
* Tue Oct 13 2015 Andrey Cherepanov <cas@altlinux.org> 0.9.3-alt3.qa3
- Fix build with gcc5

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.9.3-alt3.qa2
- NMU: rebuilt for updated dependencies.

* Tue May 17 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.3-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * freedesktop-desktop-file-proposed-patch for pavumeter

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 0.9.3-alt3
- apply patch from repocop

* Fri Jul 11 2008 Igor Zubkov <icesik@altlinux.org> 0.9.3-alt2
- fix desktop file

* Wed Mar 05 2008 Igor Zubkov <icesik@altlinux.org> 0.9.3-alt1
- 0.9.2 -> 0.9.3
- buildreq

* Sat Jul 22 2006 Igor Zubkov <icesik@altlinux.ru> 0.9.2-alt1
- 0.9.2
- buildreq

* Mon May 29 2006 Igor Zubkov <icesik@altlinux.ru> 0.9.0-alt1
- 0.9.0
- add docs
- add url

* Sat Apr 22 2006 Igor Zubkov <icesik@altlinux.ru> 0.8-alt1
- Initial build for Sisyphus
