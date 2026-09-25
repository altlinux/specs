
%define priority_min 1
%define priority_max 300

Name: webclient-dummy
Version: 0.1
Release: alt1

Summary: Dummy webclient
License: GPL-3.0-or-later
Group: System/Configuration/Other
Url: https://www.altlinux.org/

%description
A fake web client designed to simplify user package management.

%package -n 00-webclient-dummy
Group: System/Configuration/Other
Summary: Dummy webclient
Provides: webclient x-www-browser
Requires: %_bindir/xdg-open
%description -n 00-webclient-dummy
%{description}

%package -n zz-webclient-dummy
Group: System/Configuration/Other
Summary: Dummy webclient
Provides: webclient x-www-browser
Requires: %_bindir/firefox
%description -n zz-webclient-dummy
%{description}

%install
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/00-webclient-dummy <<__EOF__
%_bindir/xbrowser       %_bindir/xdg-open      %priority_min
%_bindir/x-www-browser  %_bindir/xdg-open      %priority_min
__EOF__
cat > %buildroot/%_sysconfdir/alternatives/packages.d/zz-webclient-dummy <<__EOF__
%_bindir/xbrowser       %_bindir/firefox      %priority_max
%_bindir/x-www-browser  %_bindir/firefox      %priority_max
__EOF__

%files -n 00-webclient-dummy
%config /%_sysconfdir/alternatives/packages.d/00-webclient-dummy

%files -n zz-webclient-dummy
%config /%_sysconfdir/alternatives/packages.d/zz-webclient-dummy

%changelog
* Fri Sep 25 2026 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
