%define origname mpDris2
Name: mpdris2
Summary: provides MPRIS 2 support to mpd (Music Play Daemon)
Version: 0.1
Release: alt1.git.gc29014
License: GPL3
Group: Sound
Url: https://github.com/eonpatapon/%origname
Packager: Ildar Mulyukov <ildar@altlinux.ru>
BuildArch: noarch

Source: %name.tar

Requires: mpd
# Automatically added by buildreq on Tue Mar 27 2012 (-bi)
# optimized out: perl-XML-Parser python-base python-devel python-modules
BuildRequires: intltool python-module-distribute

%description
Useful for MPRIS2-aware agents

%prep
%setup -n %name
subst 's|^Name=.*|Name=MPD MPRIS2 agent|' src/%origname.desktop

%build
./autogen.sh
%configure
make

%install
%makeinstall_std

%find_lang %origname

%files -f %origname.lang
%exclude %_docdir/mpdris2/*
%doc AUTHORS README* src/%origname.conf
%_sysconfdir/xdg/autostart/*.desktop
%_bindir/*
%_desktopdir/*.desktop
%_datadir/dbus-1/services/*.service

%changelog
* Tue Mar 27 2012 Ildar Mulyukov <ildar@altlinux.ru> 0.1-alt1.git.gc29014
- initial build for ALT Linux Sisyphus
