Name: paprefs
Version: 0.9.10
Release: alt1

Summary: PulseAudio Preferences
License: GPL
Group: Sound
Url: http://freedesktop.org/software/pulseaudio/%name
Source0: http://freedesktop.org/software/pulseaudio/%name/%name-%version.tar.xz

Source1: %name.desktop

Patch0: paprefs-0.9.6-alt-desktop-file.patch

Patch1: %name-%version-modules-path.patch
Patch2: %name-%version-module-combine-sink.patch

Packager: Ilya Mashkin <oddity@altlinux.ru>

Requires: pulseaudio >= 0.9.5

# Automatically added by buildreq on Tue Dec 02 2008
BuildRequires: gcc-c++ intltool libgconfmm2-devel libglademm-devel lynx libpulseaudio-devel libdbus-glib-devel

%description
PulseAudio Preferences (paprefs) is a simple GTK based configuration dialog for
the PulseAudio sound server.

Please note that this program can only configure local servers, and requires
that a special module module-gconf is loaded in the sound server. (Since
PulseAudio 0.9.5 this modules is loaded by default.)

%prep
%setup
%patch0 -p1

touch -r configure.ac configure.ac.stamp
%patch1 -p1 -b .modules-path
touch -r configure.ac.stamp configure.ac
%patch2 -p1 -b .module-combine-sink

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
* Mon Apr 07 2014 Ilya Mashkin <oddity@altlinux.ru> 0.9.10-alt1
- 0.9.10
- add patches
- fix url

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.9.8-alt1.1.qa1
- NMU: rebuilt for debuginfo.

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
