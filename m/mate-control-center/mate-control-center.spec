Serial: 1
Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/update-mime-database libICE-devel libX11-devel libgio-devel pkgconfig(appindicator-0.1) pkgconfig(dbus-1) pkgconfig(dbus-glib-1) pkgconfig(dconf) pkgconfig(freetype2) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(libcanberra-gtk) pkgconfig(libcanberra-gtk3) pkgconfig(libmarco-private) pkgconfig(libmate-menu) pkgconfig(libmatekbd) pkgconfig(libmatekbdui) pkgconfig(librsvg-2.0) pkgconfig(libxklavier) pkgconfig(libxml-2.0) pkgconfig(mate-desktop-2.0) pkgconfig(mate-settings-daemon) pkgconfig(pango) pkgconfig(unique-1.0) pkgconfig(unique-3.0) pkgconfig(xcursor) pkgconfig(xi) xorg-kbproto-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mate-control-center
%define version 1.12.1
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.12

# Settings used for build from snapshots.
%{!?rel_build:%global commit 922d0e0219b1bedcece8624e4b5fd7e15e7a9bd5}
%{!?rel_build:%global commit_date 20131113}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:          mate-control-center
Version:       %{branch}.1
%if 0%{?rel_build}
Release:       alt1_2
%else
#Release:       0.6%{?git_rel}%{?dist}
%endif
Summary:       MATE Desktop control-center
License:       LGPLv2+ and GPLv2+
URL:           http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R mate-control-center.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires: libdconf-devel
BuildRequires: desktop-file-utils
BuildRequires: gtk2-devel
BuildRequires: libcanberra-devel
BuildRequires: libmatekbd-devel
BuildRequires: librsvg-devel
BuildRequires: libSM-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libXxf86misc-devel
BuildRequires: mate-common
BuildRequires: mate-desktop-devel
BuildRequires: mate-menus-devel
BuildRequires: mate-settings-daemon-devel
BuildRequires: mate-window-manager-devel
BuildRequires: libunique-devel

Requires: gsettings-desktop-schemas
# rhbz (#1234438)
Requires: mate-settings-daemon
# keyring support
Requires: gnome-keyring
Provides: %{name}-filesystem%{?_isa} = %{version}-%{release}
Source44: import.info
Patch33: gnome-control-center-2.22.1-alt-background-location.patch
Patch34: gnome-control-center-2.28.0-passwd.patch


%description 
MATE Control Center configures system settings such as themes,
keyboards shortcuts, etc.

%package filesystem
Group: Graphical desktop/Other
Summary:      MATE Control Center directories
# NOTE: this is an "inverse dep" subpackage. It gets pulled in
# NOTE: by the main package an MUST not depend on the main package

%description filesystem
The MATE control-center provides a number of extension points
for applications. This package contains directories where applications
can install configuration files that are picked up by the control-center
utilities.

%package devel
Group: Development/C
Summary:      Development files for mate-settings-daemon
Requires:       %{name}%{?_isa} = %{?serial:%serial:}%{version}-%{release}

%description devel
Development files for mate-control-center


%prep
%setup -q%{!?rel_build:n %{name}-%{commit}}

%if 0%{?rel_build}
#NOCONFIGURE=1 ./autogen.sh
%else # 0%{?rel_build}
# for snapshots
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif # 0%{?rel_build}
%patch33 -p1
%patch34 -p1

%build
autoreconf -fisv
%configure                           \
           --disable-static          \
           --disable-schemas-compile \
           --disable-update-mimedb

# remove unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags} V=1


%install
%{makeinstall_std}

find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'

desktop-file-install                                \
    --delete-original                               \
    --dir=%{buildroot}%{_datadir}/applications      \
%{buildroot}%{_datadir}/applications/*.desktop

# delete mime cache
rm %{buildroot}%{_datadir}/applications/mimeinfo.cache

# mate-preferences-categories.menu is back in mate-menus
rm -f  %{buildroot}%{_sysconfdir}/xdg/menus/mate-preferences-categories.menu

# remove needless gsettings convert file
rm -f  %{buildroot}%{_datadir}/MateConf/gsettings/mate-control-center.convert

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING README
%config %{_sysconfdir}/xdg/menus/matecc.menu
%{_bindir}/mate-*
%{_libdir}/libmate-window-settings.so.*
%{_libdir}/window-manager-settings
%{_libdir}/libmate-slab.so.*
%{_sbindir}/mate-display-properties-install-systemwide
%{_datadir}/applications/*.desktop
%{_datadir}/desktop-directories/matecc.directory
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/mate-*.svg
%{_datadir}/glib-2.0/schemas/org.mate.*.xml
%{_datadir}/mate-control-center/*
%{_datadir}/mate/cursor-fonts/*.pcf
%{_datadir}/mime/packages/mate-theme-package.xml
%{_datadir}/thumbnailers/mate-font-viewer.thumbnailer
%{_datadir}/polkit-1/actions/org.mate.randr.policy
%{_mandir}/man1/mate-*.1.*
# %%files filesystem
%dir %{_datadir}/mate-control-center
%dir %{_datadir}/mate-control-center/keybindings

%files devel
%{_includedir}/mate-window-settings-2.0
%{_libdir}/pkgconfig/mate-window-settings-2.0.pc
%{_libdir}/libmate-window-settings.so
%{_libdir}/pkgconfig/mate-default-applications.pc
%{_libdir}/pkgconfig/mate-keybindings.pc
%{_includedir}/libmate-slab/
%{_libdir}/libmate-slab.so
%{_libdir}/pkgconfig/mate-slab.pc


%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.12.1-alt1_2
- new version

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.10.2-alt2_1
- fixed dependencies

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.10.2-alt1_1
- new version

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.8.1-alt2_1
- new fc release

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.8.1-alt2_0
- use gnome-keyring

* Thu Mar 20 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.8.1-alt1_0
- new fc release
- TODO: drop mate-keyring

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.6.1-alt1_2
- new fc release

* Thu Aug 01 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.6.1-alt1_1
- new fc release

* Mon Jul 22 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.6.0-alt1_2
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.6.0-alt1_1
- new fc release

* Wed Mar 27 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.5.5-alt1_3
- new fc release

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.5.4-alt1_1
- new fc release

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.5.3-alt1_3
- new fc release

* Fri Jan 11 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.5.2-alt1_1
- new fc release

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_1
- new fc release

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- use F19 import base

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1.1.1
- rebuild with new libmatekbd

* Thu Oct 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted background-location and passwd alt patches

* Sun Aug 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_2
- 20120622 mate snapshot

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- converted by srpmconvert script

