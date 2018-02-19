Group: Graphical desktop/MATE
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/xsltproc libXext-devel libgio-devel libwrap-devel pkgconfig(glib-2.0) pkgconfig(ice) pkgconfig(x11) pkgconfig(xau) pkgconfig(xrender)
# END SourceDeps(oneline)
BuildRequires(pre): browser-plugins-npapi-devel
%define _libexecdir %_prefix/libexec
%define oldname mate-session-manager
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%oldname and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mate-session-manager
%define version 1.20.0
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.20

# Settings used for build from snapshots.
%{!?rel_build:%global commit af58c2ecd98fe68360635f0e566b81e4b8c7be4d}
%{!?rel_build:%global commit_date 20151006}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{oldname}-%{version}-%{git_ver}.tar.xz}

Name:           mate-session
Summary:        MATE Desktop session manager
License:        GPLv2+
Version:        %{branch}.0
%if 0%{?rel_build}
Release:        alt1_1
%else
Release:        alt1_1
%endif
URL:            http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R mate-session-manager.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{oldname}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{oldname}/snapshot/%{oldname}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires:  libdbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-demo libgail3-devel libgtk+3 libgtk+3-devel libgtk+3-gir-devel
BuildRequires:  libSM-devel
BuildRequires:  mate-common
BuildRequires:  libpangox-compat-devel
BuildRequires:  libsystemd-devel libudev-devel
BuildRequires:  xmlto
BuildRequires:  libXtst-devel
BuildRequires:  xorg-xtrans-devel

# Needed for mate-settings-daemon
Requires: mate-control-center
# we need an authentication agent in the session
Requires: mate-polkit
# and we want good defaults
Requires: polkit
# for gsettings shemas
Requires: libmate-desktop
# for /bin/dbus-launch
Requires: dbus-tools-gui
Source44: import.info
Patch33: mate-session-manager-cflags.patch
Provides: mate-session-manager = %version-%release
Provides: mate-session-xsession = %version-%release
Requires: mate-desktop
Source45: MATE64.png

%description
This package contains a session that can be started from a display
manager such as MDM. It will load all necessary applications for a
full-featured user session.

%prep
%if 0%{?rel_build}
%setup -n %{oldname}-%{version} -q

%else
%setup -q -n %{oldname}-%{commit}

%endif

%if 0%{?rel_build}
# for releases
#NOCONFIGURE=1 ./autogen.sh
%else
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif
%patch33 -p1

%build
%configure                    \
    --disable-static          \
    --enable-ipv6             \
    --with-default-wm=marco   \
    --with-systemd            \
    --enable-docbook-docs     \
    --disable-schemas-compile

%make_build V=1

%install
%{makeinstall_std}

desktop-file-install                               \
        --delete-original                          \
        --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/mate-session-properties.desktop

%find_lang %{oldname} --with-gnome --all-name

cat <<__START_MATE__ >startmate
#!/bin/sh

# turn on fonts antialiasing
export GDK_USE_XFT=1

# TODO
# set default browser to whatever MATE user likes
#export BROWSER=mate-open

# does not work; see https://bugzilla.altlinux.org/28134
# tell restored browsers where plugins are
# export MOZ_PLUGIN_PATH="\${MOZ_PLUGIN_PATH:+"\$MOZ_PLUGIN_PATH:"}\${HOME:+"\$HOME/.mozilla/plugins:"}%_libdir/mozilla/plugins:%_libdir/netscape/plugins:%browser_plugins_path"

# TODO
# export HELP_BROWSER=yelp

# use prefixed .menu files
#export XDG_MENU_PREFIX="mate-"

# Since shared-mime-info-0.90-alt3 XDG_DATA_DIRS not exported. We need to define
# the set of base directories explicitly.

export XDG_DATA_DIRS="%_datadir/mate:%_datadir:/usr/local/share"

exec %_bindir/mate-session "\$@"
__START_MATE__

install -pD -m755 startmate %buildroot%_bindir/startmate

mkdir -p %buildroot%_sysconfdir/X11/wmsession.d/
cat << __EOF__ > %buildroot%_sysconfdir/X11/wmsession.d/02Mate
NAME=Mate
ICON=%_iconsdir/hicolor/64x64/apps/mate.png
DESC=Mate (Gnome 2) Environment
EXEC=%_bindir/startmate
SCRIPT:
exec %_bindir/startmate
__EOF__

install -pD -m644 %SOURCE45 %buildroot%_iconsdir/hicolor/64x64/apps/mate.png
sed -i -e s,Exec=mate-session,Exec=%_bindir/startmate, %buildroot%_datadir/xsessions/mate.desktop



%files -f %{oldname}.lang
%doc AUTHORS COPYING README
%{_mandir}/man1/*
%{_bindir}/mate-session
%{_bindir}/mate-session-inhibit
%{_bindir}/mate-session-properties
%{_bindir}/mate-session-save
%{_bindir}/mate-wm
%{_datadir}/applications/mate-session-properties.desktop
%{_datadir}/mate-session-manager
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/mate-session-properties.svg
%{_datadir}/glib-2.0/schemas/org.mate.session.gschema.xml
%{_datadir}/xsessions/mate.desktop
%if 0%{?fedora} > 22 || 0%{?rhel}
%{_docdir}/mate-session-manager/dbus/mate-session.html
%endif

%_bindir/*
%_iconsdir/hicolor/64x64/apps/mate.png
%config %_sysconfdir/X11/wmsession.d/*Mate*
#exclude %_datadir/xsessions/mate.desktop
#exclude %_bindir/mate-wm



%changelog
* Tue Feb 20 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

* Wed Sep 06 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.0-alt1_3
- new fc release

* Tue Oct 25 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.16.0-alt2_1
- fix the value of 'Exec' field in mate.desktop (closes: #32656)

* Thu Oct 06 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.16.0-alt1_1
- update to mate 1.16

* Tue Apr 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt1_1
- new fc release

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt1_2
- new version

* Mon Mar 31 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt2_1
- disabled upower support (not compatible with upower 0.99)

* Thu Mar 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt1_1
- new fc release

* Fri Feb 21 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.1-alt2
- disable direct upower support (use logind instead)

* Sat Sep 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_3
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_1
- new fc release

* Tue Jun 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt2_3
- new fc release

* Tue Apr 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt2_1
- added Requires: mate-desktop (closes: 28825)

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_1
- new fc release

* Sun Feb 17 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_0
- new version

* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_2
- new fc release

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_1
- no toying with MOZ_PLUGIN_PATH in startmate (closes: 28134)

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

* Thu Oct 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_5.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_5
- adapted alt patches

* Sun Aug 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_5
- new release

* Wed May 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

