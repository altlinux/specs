%define origname mpDris2
Name: mpdris2
Summary: provides MPRIS 2 support to mpd (Music Play Daemon)
Version: 0.7
Release: alt1.git.40.g19e8783
License: GPL3
Group: Sound
Url: https://github.com/eonpatapon/%origname
BuildArch: noarch

# https://github.com/eonpatapon/mpDris2/
Source: %name.tar

Requires: mpd python3-module-mutagen python3-module-pygobject3 libnotify-gir
# Automatically added by buildreq on Tue Nov 07 2017 (-bi)
# optimized out: perl perl-XML-Parser python-base python3 rpm-build-python3
BuildRequires: intltool python3-base

%description
mpDris2 is run in the user session and monitors a local or distant mpd server.
Useful for MPRIS2-aware agents

%prep
%setup -n %name
subst 's|^Name=.*|Name=MPD MPRIS2 agent|' src/%name.desktop

%build
NOCONFIGURE=1 \
./autogen.sh
%configure
make

%install
%makeinstall_std

%find_lang %origname

%files -f %origname.lang
%exclude %_docdir/mpdris2/*
%doc AUTHORS README* NEWS src/%origname.conf
%_sysconfdir/xdg/autostart/*.desktop
%_bindir/*
%_prefix/lib/systemd/user/mpDris2.service
%_desktopdir/*.desktop
%_datadir/dbus-1/services/*.service

%changelog
* Tue Nov 07 2017 Ildar Mulyukov <ildar@altlinux.ru> 0.7-alt1.git.40.g19e8783
- new git snapshot
- moved to python3

* Wed May 04 2016 Ildar Mulyukov <ildar@altlinux.ru> 0.7-alt1.git.10.ga3af302
- new version

* Tue Mar 27 2012 Ildar Mulyukov <ildar@altlinux.ru> 0.1-alt1.git.gc29014
- initial build for ALT Linux Sisyphus
