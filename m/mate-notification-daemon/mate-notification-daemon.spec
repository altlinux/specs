Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtk-update-icon-cache libgio-devel pkgconfig(dbus-1) pkgconfig(gdk-2.0) pkgconfig(gdk-3.0) pkgconfig(gdk-pixbuf-2.0) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(libcanberra-gtk) pkgconfig(libcanberra-gtk3) pkgconfig(libwnck-3.0) pkgconfig(x11)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mate-notification-daemon
%define version 1.8.0
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.8

# Settings used for build from snapshots.
%{!?rel_build:%global commit 0280831e27ff5dc2d7c7473cd3bf9041f805299e}
%{!?rel_build:%global commit_date 20131227}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:           mate-notification-daemon
Version:        %{branch}.0
#Release:        0.2%{?git_rel}%{?dist}
Release:        alt1_1
Summary:        Notification daemon for MATE Desktop
License:        GPLv2+
URL:            http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R mate-notification-daemon.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%%{name}-%%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires:  libdbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libcanberra-devel
BuildRequires:  libnotify-devel
BuildRequires:  libwnck-devel
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel

Provides:       desktop-notification-daemon
Source44: import.info

%description
Notification daemon for MATE Desktop

%prep
%setup -q%{!?rel_build:n %{name}-%{commit}}

# needed for git snapshots
#NOCONFIGURE=1 ./autogen.sh

%build
%configure --disable-schemas-compile   \
           --with-gtk=2.0

make %{?_smp_mflags} V=1

%install
%{makeinstall_std}

desktop-file-install                               \
        --delete-original                          \
        --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}/%{_datadir}/applications/mate-notification-properties.desktop

# remove needless gsettings convert file
rm -f  %{buildroot}%{_datadir}/MateConf/gsettings/mate-notification-daemon.convert

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/mate-notification-properties
%{_datadir}/applications/mate-notification-properties.desktop
%{_datadir}/dbus-1/services/org.freedesktop.mate.Notifications.service
%{_datadir}/mate-notification-daemon/mate-notification-properties.ui
%{_libexecdir}/mate-notification-daemon
%{_datadir}/icons/hicolor/*/apps/mate-notification-properties.*
%{_datadir}/glib-2.0/schemas/org.mate.NotificationDaemon.gschema.xml
%{_mandir}/man1/mate-notification-properties.1*
%{_libdir}/mate-notification-daemon


%changelog
* Thu Mar 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_3
- new fc release

* Mon Jul 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_2
- new fc release

* Tue Apr 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Wed Mar 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_1
- new fc release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_2
- new fc release

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_1
- new fc release

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_1
- 20120622 mate snapshot

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

