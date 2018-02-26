Name: paman
Version: 0.9.4
Release: alt4.qa1

Summary: PulseAudio Manager
License: GPL
Group: Sound
Url: http://0pointer.de/lennart/projects/paman/

Source0: %name-%version.tar.gz

Patch0: paman-0.9.4-alt-desktop-file.patch

Packager: Igor Zubkov <icesik@altlinux.org>

Requires: pulseaudio >= 0.9.5

# Automatically added by buildreq on Tue Dec 02 2008
BuildRequires: gcc-c++ libglademm-devel libpulseaudio-devel lynx
BuildRequires: desktop-file-utils

%description
PulseAudio Manager (paman) is a simple GTK frontend for the
PulseAudio sound server.

%prep
%setup -q
%patch0 -p1

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Mixer \
	%buildroot%_desktopdir/paman.desktop

%files
%doc README doc/README.html doc/style.css
%_bindir/paman
%dir %_datadir/paman/
%_datadir/paman/paman.glade
%_datadir/applications/paman.desktop

%changelog
* Tue May 17 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.4-alt4.qa1
- NMU (by repocop): the following fixes applied:
  * freedesktop-desktop-file-proposed-patch for paman

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 0.9.4-alt4
- apply patch from repocop

* Sat Jul 12 2008 Igor Zubkov <icesik@altlinux.org> 0.9.4-alt3
- re-fix desktop file

* Fri Jul 11 2008 Igor Zubkov <icesik@altlinux.org> 0.9.4-alt2
- fix desktop file

* Wed Mar 05 2008 Igor Zubkov <icesik@altlinux.org> 0.9.4-alt1
- 0.9.3 -> 0.9.4
- buildreq

* Tue Sep 05 2006 Igor Zubkov <icesik@altlinux.org> 0.9.3-alt1
- 0.9.2 -> 0.9.3
- buildreq

* Fri Jul 21 2006 Igor Zubkov <icesik@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Sun Jun 25 2006 Igor Zubkov <icesik@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Mon May 29 2006 Igor Zubkov <icesik@altlinux.ru> 0.9.0-alt1
- 0.9.0
- patch1 merged in upstream
- add docs
- add url

* Wed Apr 26 2006 Igor Zubkov <icesik@altlinux.ru> 0.8-alt1
- Initial build for Sisyphus
