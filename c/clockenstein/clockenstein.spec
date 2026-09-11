%define _unpackaged_files_terminate_build 1

%def_with check

Name: clockenstein
Version: 1.0.0
Release: alt1

Summary: Calendar application for Linux Desktops
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://github.com/xapp-project/clockenstein

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): meson
BuildRequires(pre): rpm-macros-systemd
BuildRequires(pre): rpm-build-python3

BuildRequires: cmake
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: /usr/bin/gtk4-update-icon-cache

%filter_from_requires /python3(backends.google)/d
%filter_from_requires /python3(main_window)/d
%filter_from_requires /python3(store)/d

Requires: python3-module-pygobject3
Requires: python3(cairo)
Requires: python3(httplib2)
Requires: python3(google)
Requires: python3(google.oauth2)
Requires: python3(google_auth_httplib2)
Requires: python3(google_auth_oauthlib)
Requires: python3(googleapiclient)
Requires: python3(xapp)
Requires: python3(icalendar)
Requires: python3(setproctitle)
Requires: python3(caldav)
Requires: libgsound-gir

%if_with check
BuildRequires: python3(httplib2)
BuildRequires: python3(google)
BuildRequires: python3(google.oauth2)
BuildRequires: python3(google_auth_httplib2)
BuildRequires: python3(google_auth_oauthlib)
BuildRequires: python3(googleapiclient)
BuildRequires: python3(xapp)
BuildRequires: python3(icalendar)
BuildRequires: python3(setproctitle)
BuildRequires: python3(caldav)
BuildRequires: libgsound-gir
%endif

%description
Calendar application for Linux desktops.
Supported Calendars:

* Local calendars.
* Google calendars
* CalDAV calendars (Nextcloud, Memotoo, etc)

Remote calendars are read-only when disconnected or offline.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%check
%meson_test

%files -f %{name}.lang
%doc README.md
%_sysconfdir/xdg/autostart/clockenstein-daemon.desktop
%_sysconfdir/xdg/autostart/clockenstein-notification-agent.desktop
%_bindir/clockenstein-calendar
%_bindir/clockenstein-daemon
%_bindir/clockenstein-notification-agent
%_userunitdir/clockenstein-daemon.service
%_userunitdir/clockenstein-notification-agent.service
%_desktopdir/org.x.clockenstein.Calendar.desktop
%dir %_datadir/clockenstein
%dir %_datadir/clockenstein/agent
%_datadir/clockenstein/agent/main.py
%_datadir/clockenstein/agent/notification.oga
%dir %_datadir/clockenstein/calendar
%dir %_datadir/clockenstein/calendar/backends
%_datadir/clockenstein/calendar/backends/caldav.py
%_datadir/clockenstein/calendar/backends/google.py
%_datadir/clockenstein/calendar/dbus.py
%_datadir/clockenstein/calendar/event_dialog.py
%_datadir/clockenstein/calendar/formatting.py
%_datadir/clockenstein/calendar/main.py
%_datadir/clockenstein/calendar/main_window.py
%_datadir/clockenstein/calendar/store.py
%_datadir/clockenstein/calendar/style.css
%dir %_datadir/clockenstein/calendar/views
%_datadir/clockenstein/calendar/views/__init__.py
%_datadir/clockenstein/calendar/views/colors.py
%_datadir/clockenstein/calendar/views/day_view.py
%_datadir/clockenstein/calendar/views/month_view.py
%_datadir/clockenstein/calendar/views/week_view.py
%dir %_datadir/clockenstein/calendar/widgets
%_datadir/clockenstein/calendar/widgets/mini_calendar.py
%dir %_datadir/clockenstein/daemon
%_datadir/clockenstein/daemon/main.py
%_datadir/dbus-1/services/org.x.clockenstein.Calendar.Service.service
%_datadir/glib-2.0/schemas/org.x.clockenstein.calendar.gschema.xml
%_datadir/glib-2.0/schemas/org.x.clockenstein.daemon.gschema.xml
%_iconsdir/hicolor/scalable/apps/clockenstein-calendar.svg
%_iconsdir/hicolor/scalable/apps/clockenstein-clock.svg

%changelog
* Fri Sep 11 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
