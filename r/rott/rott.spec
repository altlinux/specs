Name: rott
Version: 1.1.1
Release: alt1.qa1
Summary: Rise of the Triad
Group: Games/Arcade
License: GPLv2+
Url: http://icculus.org/rott/
Source0: http://icculus.org/rott/releases/rott-%version.tar.gz
Source1: rott-shareware.sh
Source2: rott-registered.sh
Source3: rott.autodlrc
Source4: rott-shareware.desktop
Source5: rott-registered.desktop
# Notice this is made from an edited screenshot and thus derived from the non-
# free datafiles. I believe this constitues fair-use. If anyone disagrees let
# me know and I'll remove it
Source6: rott.png
# Note: this gets applied during build, not during prep!
Patch99: rott-1.0-registered.patch

Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Sun Jul 20 2008
BuildRequires: libSDL-devel libSDL_mixer-devel

BuildRequires: libSDL_mixer-devel desktop-file-utils

%description
This is the icculus.org Linux port of Apogee's classic 3d shooter Rise of the
Triad, which has been released under the GPL by Apogee. This version is
enhanced with the "high" resolution rendering from the winrott port.

%package shareware
Summary: Rise of the Triad shareware version
Group: Games/Arcade
Requires: autodownloader

%description shareware
This is the icculus.org Linux port of Apogee's classic 3d shooter Rise of the
Triad (RotT), which has been released under the GPL by Apogee. This version is
enhanced with the "high" resolution rendering from the winrott port.

This package contains the engine for the shareware version of RotT. In order to
play the shareware version, you will need the shareware datafiles. Which can
be freely downloaded from Apogee/3DRealms, but cannot be distributed as a part
of Fedora. When you start RotT for the first time it will offer to download
the datafiles for you.

%package registered
Summary: Rise of the Triad registered version
Group: Games/Arcade
Requires: zenity

%description registered
This is the icculus.org Linux port of Apogee's classic 3d shooter Rise of the
Triad (RotT), which has been released under the GPL by Apogee. This version is
enhanced with the "high" resolution rendering from the winrott port.

This package contains the engine for the registered version of RotT. If you own
the registered version, this allows you to play the registered version under
Linux. Place the registered RotT datafiles in a dir and start rott-registered
from this dir.

%prep
%setup -q

%build
pushd rott
make %{?_smp_mflags} EXTRACFLAGS="$RPM_OPT_FLAGS -Wno-unused -Wno-pointer-sign"
mv rott rott-shareware.bin

patch -p2 < %PATCH99
make clean
make %{?_smp_mflags} EXTRACFLAGS="$RPM_OPT_FLAGS -Wno-unused -Wno-pointer-sign"
mv rott rott-registered.bin
popd

%install
#no make install target, DIY
mkdir -p $RPM_BUILD_ROOT%_bindir
mkdir -p $RPM_BUILD_ROOT%_datadir/%name
install -m 755 rott/rott-* $RPM_BUILD_ROOT%_bindir
install -p -m 755 %SOURCE1 $RPM_BUILD_ROOT%_bindir/%name-shareware
install -p -m 755 %SOURCE2 $RPM_BUILD_ROOT%_bindir/%name-registered
install -p -m 644 %SOURCE3 $RPM_BUILD_ROOT%_datadir/%name

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%_datadir/applications
desktop-file-install --vendor fedora            \
  --dir $RPM_BUILD_ROOT%_datadir/applications \
  %SOURCE4
mkdir -p $RPM_BUILD_ROOT%_datadir/applications
desktop-file-install --vendor fedora            \
  --dir $RPM_BUILD_ROOT%_datadir/applications \
  %SOURCE5
mkdir -p $RPM_BUILD_ROOT%_datadir/icons/hicolor/64x64/apps
install -p -m 644 %SOURCE6 \
  $RPM_BUILD_ROOT%_datadir/icons/hicolor/64x64/apps/

%files shareware
%doc README doc/*
%_bindir/rott-shareware*
%_datadir/%name
%_datadir/applications/fedora-%name-shareware.desktop
%_datadir/icons/hicolor/64x64/apps/%name.png

%files registered
%doc README doc/*
%_bindir/rott-registered*
%_datadir/%name
%_datadir/applications/fedora-%name-registered.desktop
%_datadir/icons/hicolor/64x64/apps/%name.png

%changelog
* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.1.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-gtk-update-icon-cache for rott-registered
  * obsolete-call-in-post-gtk-update-icon-cache for rott-shareware
  * postclean-05-filetriggers for spec file

* Wed Sep 02 2009 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Version up

* Sun Jul 20 2008 Fr. Br. George <george@altlinux.ru> 1.1-alt1
- Version up (all patches are upstream applied)

* Sun Jul 20 2008 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Initial build from FC

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0-5
- Autorebuild for GCC 4.3

* Fri Aug  3 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-4
- Update License tag for new Licensing Guidelines compliance
- Fix 2 calls of memset with the 2nd and 3th argument swaped,
  reported by Dave Jones

* Fri May 11 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-3
- Add missing autodownloader Requires to rott-shareware

* Fri May 11 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-2
- Add desktop entry and userfriendly launcher script for registered package
- Add a patch fixing crashes with "long" usernames

* Fri May 11 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-1
- Initial Fedora Extras package
