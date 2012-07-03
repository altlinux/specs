%define rname kmid
%define libname libkmidbackend1

Name: kde4-kmid
Version: 2.4.0
Release: alt2

Group: Sound
Summary: A MIDI/karaoke player for KDE
# code under GPLv2+ for the code, examples under CC-BY-SA
License: GPLv2+ / CC-BY-SA
Url: http://userbase.kde.org/KMid2

Requires: TiMidity++ fluidsynth
Requires: %libname >= %version
Conflicts: kdemultimedia-kmid < 3.5.12-alt2

Source0: http://downloads.sourceforge.net/project/%name/%name/%version/kmid-%version.tar.bz2
Patch1: kmid-2.3.0-alt-start-timidity.patch

# Automatically added by buildreq on Wed Apr 28 2010 (-bi)
#BuildRequires: desktop-file-utils gcc-c++ glib2-devel glibc-devel-static kde4libs-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libalsa-devel libqt3-devel libxkbfile-devel qt4-assistant qt4-designer rpm-build-ruby
BuildRequires(pre): kde4libs-devel
BuildRequires: desktop-file-utils gcc-c++ glib2-devel glibc-devel
BuildRequires: libalsa-devel

%description
KMid2 is a MIDI/karaoke file player, with configurable midi mapper, real
Session Management, drag & drop, customizable fonts, etc. It has a very
nice interface which let you easily follow the tune while changing the
color of the lyrics.
It supports output through external synthesizers, AWE, FM and GUS cards.
It also has a keyboard view to see the notes played by each instrument.

%package -n %libname
Group: System/Libraries
Summary: %name library package
Requires: kde4libs >= %{get_version kde4libs}
%description -n %libname
%summary

%package devel
Group: Sound
Summary: %name developement files
%description devel
This package contains header files needed when building
applications based on %name


%prep
%setup -qn %rname-%version
%patch1 -p1

%build
%K4build

%install
%K4install

# install desktop-file
desktop-file-install \
		--vendor="" \
		--add-category="AudioVideo" \
		--add-category="Audio" \
		--remove-category="Music" \
		--dir %buildroot/%_K4xdg_apps %buildroot/%_K4xdg_apps/%rname.desktop

%K4find_lang --with-kde %rname


%files -f %rname.lang
%doc ChangeLog README TODO
%_K4bindir/%rname
%_K4lib/kmid_*.so
%_K4apps/%rname
%_K4apps/%{rname}_part
%_K4xdg_apps/%rname.desktop
%_K4cfg/%rname.kcfg
%_K4srv/*
%_K4srvtyp/*
%_K4iconsdir/hicolor/*/*/*.*

%files -n %libname
%_libdir/libkmidbackend.so.*

%files devel
%_K4dbus_interfaces/org.kde.KMid*
%_K4includedir/%rname
%_K4link/libkmidbackend.so

%changelog
* Thu Apr 21 2011 Sergey V Turchin <zerg@altlinux.org> 2.4.0-alt2
- move to standart place

* Tue Oct 26 2010 Sergey V Turchin <zerg@altlinux.org> 2.4.0-alt0.M51.1
- built for M51

* Tue Oct 26 2010 Sergey V Turchin <zerg@altlinux.org> 2.4.0-alt1
- new version

* Wed Apr 28 2010 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.M51.1
- build for M51

* Wed Apr 28 2010 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt1
- initial specfile
