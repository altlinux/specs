Name: paprefs
Version: 0.9.8
Release: alt1.1

Summary: PulseAudio Preferences
License: GPL
Group: Sound
Url: http://0pointer.de/lennart/projects/paprefs/

Source0: %name-%version.tar.gz
Source1: %name.desktop

Patch0: paprefs-0.9.6-alt-desktop-file.patch

Packager: Ilya Mashkin <oddity@altlinux.ru>

Requires: pulseaudio >= 0.9.5

# Automatically added by buildreq on Tue Dec 02 2008
BuildRequires: gcc-c++ intltool libgconfmm2-devel libglademm-devel lynx libpulseaudio-devel

%description
PulseAudio Preferences (paprefs) is a simple GTK based configuration dialog for
the PulseAudio sound server.

Please note that this program can only configure local servers, and requires
that a special module module-gconf is loaded in the sound server. (Since
PulseAudio 0.9.5 this modules is loaded by default.)

%prep
%setup -q
%patch0 -p1

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
%__install -p -m644 -D %SOURCE1 $RPM_BUILD_ROOT%_datadir/applications/%name.desktop

%find_lang %name

%files -f %name.lang
%_bindir/paprefs
%_datadir/applications/paprefs.desktop
%_datadir/paprefs/paprefs.glade

%changelog
* Sun Aug 09 2009 Ilya Mashkin <oddity@altlinux.ru> 0.9.8-alt1.1
- fix .desktop file (Closes: #20896)

* Sun May 31 2009 Ilya Mashkin <oddity@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 0.9.7-alt1
- 0.9.6 -> 0.9.7
- buildreq

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 0.9.6-alt3
- apply patch from repocop

* Fri Jul 11 2008 Igor Zubkov <icesik@altlinux.org> 0.9.6-alt2
- fix desktop file

* Wed Mar 05 2008 Igor Zubkov <icesik@altlinux.org> 0.9.6-alt1
- 0.9.5 -> 0.9.6
- buildreq

* Tue Sep 05 2006 Igor Zubkov <icesik@altlinux.org> 0.9.5-alt1
- Initial build for Sisyphus
