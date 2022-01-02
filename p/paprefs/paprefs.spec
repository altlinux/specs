Name: paprefs
Version: 1.2
Release: alt1

Summary: PulseAudio Preferences
License: GPLv2+
Group: Sound

Url: http://freedesktop.org/software/pulseaudio/%name
Source0: http://freedesktop.org/software/pulseaudio/%name/%name-%version.tar.xz
Source1: %name.desktop
Patch2: %name-0.9.10-module-combine-sink.patch
Packager: Ilya Mashkin <oddity@altlinux.ru>

Requires: pulseaudio >= 0.9.5

# Automatically added by buildreq on Mon Apr 19 2021
BuildRequires: gcc-c++ libgtkmm3-devel libpulseaudio-devel
BuildRequires: meson ninja-build

%description
PulseAudio Preferences (paprefs) is a simple GTK based configuration dialog for
the PulseAudio sound server.

Please note that this program can only configure local servers, and requires
that a special module module-gconf is loaded in the sound server. (Since
PulseAudio 0.9.5 this modules is loaded by default.)

%prep
%setup
#patch2 -p1 -b .module-combine-sink

%build
%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.12
%add_optflags -std=c++11
%endif
%meson
%meson_build

%install
%meson_install
install -pDm644 %SOURCE1 %buildroot%_datadir/applications/%name.desktop
%find_lang %name

%files -f %name.lang
%_bindir/paprefs
%_datadir/applications/paprefs.desktop
%_datadir/paprefs/paprefs.glade

%changelog
* Sun Jan 02 2022 Ilya Mashkin <oddity@altlinux.ru> 1.2-alt1
- 1.2
- Update License tag to GPLv2+

* Mon Apr 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- NMU: new version 1.1 (with rpmrb script)
- switch to meson and gtkmm3

* Sun Jun 30 2019 Michael Shigorin <mike@altlinux.org> 0.9.10-alt2
- E2K: explicit -std=c++11
- minor spec cleanup

* Sat Jun 13 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.10-alt1.1
- Rebuilt for gcc5 C++11 ABI.

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
