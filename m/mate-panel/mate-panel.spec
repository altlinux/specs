Serial: 1
Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/gtkdocize libX11-devel libXau-devel libgio-devel libgtk+2-gir-devel libgtk+3-gir-devel pkgconfig(cairo) pkgconfig(dbus-glib-1) pkgconfig(dconf) pkgconfig(gdk-pixbuf-2.0) pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(ice) pkgconfig(libcanberra-gtk) pkgconfig(libcanberra-gtk3) pkgconfig(libmate-menu) pkgconfig(librsvg-2.0) pkgconfig(libwnck-1.0) pkgconfig(libwnck-3.0) pkgconfig(mate-desktop-2.0) pkgconfig(pango) pkgconfig(sm) pkgconfig(x11) pkgconfig(xau) pkgconfig(xrandr) python-devel
# END SourceDeps(oneline)
BuildRequires: libXi-devel
%define _libexecdir %_prefix/libexec
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mate-panel
%define version 1.12.1
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.12

# Settings used for build from snapshots.
%{!?rel_build:%global commit 838555a41dc08a870b408628f529b66e2c8c4054}
%{!?rel_build:%global commit_date 20140222}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:           mate-panel
Version:        %{branch}.1
%if 0%{?rel_build}
Release:        alt1_1
%else
Release:        alt1_1
%endif
Summary:        MATE Desktop panel and applets
#libs are LGPLv2+ applications GPLv2+
License:        GPLv2+
URL:            http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R mate-panel.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

Source1:        mate-panel_fedora.layout

Requires:       %{name}-libs%{?_isa} = %{?serial:%serial:}%{version}-%{release}
# needed as nothing else requires it
Requires:       mate-session-manager
#for fish
Requires:       fortune-mod
Requires:       icon-theme-hicolor
# rhbz (#1007219)
Requires:       mate-file-manager-schemas

BuildRequires:  libdbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk2-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libmateweather-devel
BuildRequires:  libwnck-devel
BuildRequires:  librsvg-devel
BuildRequires:  libSM-devel
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  mate-menus-devel
BuildRequires:  yelp-tools
Source44: import.info
Requires: tzdata
# let us keep it just in case
Requires:       gsettings-desktop-schemas

%description
MATE Desktop panel applets


%package libs
Group: Development/C
Summary:     Shared libraries for mate-panel
License:     LGPLv2+
Requires:    %{name}%{?_isa} = %{?serial:%serial:}%{version}-%{release}

%description libs
Shared libraries for libmate-desktop

%package devel
Group: Development/C
Summary:     Development files for mate-panel
Requires:    %{name}-libs%{?_isa} = %{?serial:%serial:}%{version}-%{release}

%description devel
Development files for mate-panel

%prep
%setup -q%{!?rel_build:n %{name}-%{commit}}

%if 0%{?rel_build}
#NOCONFIGURE=1 ./autogen.sh
%else # 0%{?rel_build}
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif # 0%{?rel_build}

%build
autoreconf -fisv

#libexecdir needed for gnome conflicts
%configure                                        \
           --disable-static                       \
           --disable-schemas-compile              \
           --with-x                               \
           --libexecdir=%{_libexecdir}/mate-panel \
           --with-gtk=2.0                         \
           --enable-introspection                 \
           --enable-gtk-doc

# remove unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make  %{?_smp_mflags} V=1


%install
%{makeinstall_std}

find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'

desktop-file-install \
        --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/mate-panel.desktop

install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/mate-panel/layouts/fedora.layout

# remove needless gsettings convert file
rm -f  %{buildroot}%{_datadir}/MateConf/gsettings/mate-panel.convert

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_mandir}/man1/*
%{_bindir}/mate-desktop-item-edit
%{_bindir}/mate-panel
%{_bindir}/mate-panel-test-applets
%{_libexecdir}/mate-panel
%{_datadir}/glib-2.0/schemas/org.mate.panel.*.xml
%{_datadir}/applications/mate-panel.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mate-panel
%{_datadir}/dbus-1/services/org.mate.panel.applet.ClockAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.FishAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.NotificationAreaAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.WnckletFactory.service

%files libs
%doc COPYING.LIB
%{_libdir}/libmate-panel-applet-4.so.1*
%{_libdir}/girepository-1.0/MatePanelApplet-4.0.typelib

%files devel
%doc %{_datadir}/gtk-doc/html/mate-panel-applet/
%{_libdir}/libmate-panel-applet-4.so
%{_includedir}/mate-panel-4.0
%{_libdir}/pkgconfig/libmatepanelapplet-4.0.pc
%{_datadir}/gir-1.0/MatePanelApplet-4.0.gir


%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.12.1-alt1_1
- new version

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.10.1-alt2_1
- fixed dependencies

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.10.1-alt1_1
- new version

* Thu Mar 20 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.8.0-alt1_1
- new fc release

* Sat Sep 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_4
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_3
- new fc release

* Thu Aug 01 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_2
- new fc release

* Tue Jun 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_2
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Wed Mar 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.6-alt1_1
- fc update

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.5-alt1_1
- new fc release

* Sun Feb 17 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt2_1
- dropped mate-panel-add script

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt1_1
- new fc release

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt4_1.1
- rebuild with mate-desktop

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt3_1.1
- Build for Sisyphus

* Fri Oct 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt3_1
- adapted alt patches, dropped some fedora patches

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- added Requires: iso-codes

* Sun Aug 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1
- 20120622 mate snapshot

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_2
- converted by srpmconvert script

