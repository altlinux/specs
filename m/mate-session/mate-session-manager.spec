# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/xmlto /usr/bin/xsltproc libICE-devel libSM-devel libXau-devel libXext-devel libwrap-devel pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gtk+-3.0) pkgconfig(ice) pkgconfig(xau) pkgconfig(xext) pkgconfig(xrender) pkgconfig(xtst) xorg-xtrans-devel
# END SourceDeps(oneline)
Group: Graphical desktop/Other
%define _libexecdir %_prefix/libexec
%define oldname mate-session-manager
Name:           mate-session
Version:        1.5.0
Release:        alt2_1
Summary:        MATE Desktop session manager
License:        GPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{oldname}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  mate-common
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(polkit-gtk-mate-1)
BuildRequires:  mate-icon-theme
BuildRequires:  icon-naming-utils
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)

Requires:       gsettings-desktop-schemas
Source44: import.info
Provides: mate-session-manager = %version-%release
Provides: mate-session-xsession = %version-%release
Patch33: mate-session-manager-cflags.patch
Source45: MATE64.png

%description
MATE Desktop session manager

%prep
%setup -q -n %{oldname}-%{version}
NOCONFIGURE=1 ./autogen.sh
%patch33 -p1

%build
%configure --disable-static \
           --enable-ipv6 \
           --with-gtk=2.0 \
           --with-gnu-ld \
           --with-default-wm=marco \
           --with-x
make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}


desktop-file-install                               \
        --remove-category="MATE"                   \
        --add-category="X-Mate"                    \
        --delete-original                          \
        --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/mate-session-properties.desktop


%find_lang %{oldname}

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




%files -f %{oldname}.lang
%doc AUTHORS COPYING README
%{_mandir}/man1/*
%{_bindir}/mate-session
%{_bindir}/mate-session-properties
%{_bindir}/mate-session-save
%{_bindir}/mate-wm
%{_datadir}/applications/mate-session-properties.desktop
%{_datadir}/mate-session/
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/mate-session-properties.svg
%{_datadir}/glib-2.0/schemas/org.mate.session.gschema.xml
%{_datadir}/xsessions/mate.desktop

%_bindir/*
%_iconsdir/hicolor/64x64/apps/mate.png
%config %_sysconfdir/X11/wmsession.d/*Mate*
#exclude %_datadir/xsessions/mate.desktop
#exclude %_bindir/mate-wm


%changelog
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

