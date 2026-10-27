
%define priority_min 1
%define priority_max 300

Name: webclient-dummy
Version: 0.2
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
Provides: /usr/bin/x-www-browser = %priority_min
Provides: /usr/bin/xbrowser = %priority_min
Requires: %_bindir/xdg-open
%description -n 00-webclient-dummy
%{description}

%package -n zz-webclient-dummy
Group: System/Configuration/Other
Summary: Dummy webclient
Provides: webclient x-www-browser
Provides: /usr/bin/x-www-browser = %priority_max
Provides: /usr/bin/xbrowser = %priority_max
Requires: %_bindir/firefox
%description -n zz-webclient-dummy
%{description}

%install
install -d %buildroot/%_bindir/
install -d %buildroot/%_sysconfdir/alternatives/packages.d
# weakest webclient
cat >%buildroot/%_bindir/00-webclient-dummy <<__EOF__
#!/bin/sh
exec %_bindir/xdg-open "\${@}"
__EOF__
chmod 0755 %buildroot/%_bindir/00-webclient-dummy
cat > %buildroot/%_sysconfdir/alternatives/packages.d/00-webclient-dummy <<__EOF__
%_bindir/xbrowser       %_bindir/00-webclient-dummy      %priority_min
%_bindir/x-www-browser  %_bindir/00-webclient-dummy      %priority_min
__EOF__
# strongest webclient
cat >%buildroot/%_bindir/zz-webclient-dummy <<__EOF__
#!/bin/sh
exec %_bindir/firefox "\${@}"
__EOF__
chmod 0755 %buildroot/%_bindir/zz-webclient-dummy
cat > %buildroot/%_sysconfdir/alternatives/packages.d/zz-webclient-dummy <<__EOF__
%_bindir/xbrowser       %_bindir/zz-webclient-dummy      %priority_max
%_bindir/x-www-browser  %_bindir/zz-webclient-dummy      %priority_max
__EOF__

%files -n 00-webclient-dummy
%config /%_sysconfdir/alternatives/packages.d/00-webclient-dummy
%_bindir/00-webclient-dummy

%files -n zz-webclient-dummy
%config /%_sysconfdir/alternatives/packages.d/zz-webclient-dummy
%_bindir/zz-webclient-dummy

%changelog
* Tue Oct 27 2026 Sergey V Turchin <zerg@altlinux.org> 0.2-alt1
- fix provides

* Fri Sep 25 2026 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
