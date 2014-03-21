Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gdk-pixbuf-csource /usr/bin/glib-gettextize /usr/bin/matedialog libICE-devel libX11-devel libXext-devel libXinerama-devel libXrandr-devel libgio-devel pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(libgtop-2.0) pkgconfig(pango) pkgconfig(xcomposite) pkgconfig(xcursor) pkgconfig(xfixes) pkgconfig(xrender)
# END SourceDeps(oneline)
BuildRequires: libcanberra-gtk2-devel
%define _libexecdir %_prefix/libexec
%define oldname marco
%define fedora 21
# %oldname or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name marco
%define version 1.8.0
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.8

# Settings used for build from snapshots.
%{!?rel_build:%global commit 62a708d461e08275d6b85985f5fa13fa8fbc85f7}
%{!?rel_build:%global commit_date 20131212}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{oldname}-%{version}-%{git_ver}.tar.xz}

Name:           mate-window-manager
Version:        %{branch}.0
Release:        alt1_1
#Release:       0.5%{?git_rel}%{?dist}
Summary:        MATE Desktop window manager
License:        LGPLv2+ and GPLv2+
URL:            http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R marco.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{oldname}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{oldname}/snapshot/%{oldname}-%{commit}.tar.xz#/%{git_tar}}

# needed for fixing initial-setup issue, rhbz (#962009)
Source1:        mini-window.png
Source2:        stock_delete.png
Source3:        stock_maximize.png
Source4:        stock_minimize.png
Source5:        window.png

# needed for fixing initial-setup issue, rhbz (#962009)
Patch0:         marco_add-pixbuf-inline-icons.patch

BuildRequires: desktop-file-utils
BuildRequires: gtk2-devel
BuildRequires: libcanberra-devel
BuildRequires: libgtop2-devel
BuildRequires: libSM-devel
BuildRequireS: libsoup-devel
BuildRequires: libXdamage-devel
BuildRequires: mate-common
BuildRequires: mate-dialogs
BuildRequires: libstartup-notification-devel
BuildRequires: yelp-tools

# http://bugzilla.redhat.com/873342
# https://bugzilla.redhat.com/962009
Provides: firstboot(windowmanager) = marco

%if 0%{?fedora} && 0%{?fedora} <= 25
Provides: mate-window-manager%{?_isa} = %{version}-%{release}
Provides: mate-window-manager = %{version}-%{release}
Obsoletes: mate-window-manager < %{version}-%{release}
%endif
Source44: import.info
# http://bugzilla.gnome.org/show_bug.cgi?id=558723
Patch33: stop-spamming-xsession-errors.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=598995
Patch34: Dont-focus-ancestor-window-on-a-different-workspac.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=604319
Patch35: metacity-2.28-xioerror-unknown-display.patch
Requires: libmarco-private = %{version}-%{release}

%description
MATE Desktop window manager

%package devel
Group: Development/C
Summary: Development files for mate-window-manager
Requires: mate-window-manager = %{version}-%{release}
%if 0%{?fedora} && 0%{?fedora} <= 25
Provides: mate-window-manager-devel%{?_isa} = %{version}-%{release}
Provides: mate-window-manager-devel = %{version}-%{release}
Obsoletes: mate-window-manager-devel < %{version}-%{release}
%endif

%description devel
Development files for marco

%package -n libmarco-private
Group: System/Libraries
Summary: mate-window-manager internal library

%description -n libmarco-private
Internal library for MATE Window Manager.


%prep
%setup -n %{oldname}-%{version} -q%{!?rel_build:n %{oldname}-%{commit}}

# needed for missing `po/Makefile.in.in'
cp %{SOURCE1} src/mini-window.png
cp %{SOURCE2} src/stock_delete.png
cp %{SOURCE3} src/stock_maximize.png
cp %{SOURCE4} src/stock_minimize.png
cp %{SOURCE5} src/window.png

%patch0 -p1 -b .inline-icons

# needed for the patch and for git snapshot builds
autoreconf -if
%patch33 -p1
%patch34 -p1
%patch35 -p1

%build
%autoreconf -fisv
%configure --disable-static           \
           --disable-schemas-compile  \
           --with-gtk=2.0             \
           --with-x

# fix rpmlint unused-direct-shlib-dependency warning
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags} V=1


%install
%{makeinstall_std}

find %{buildroot} -name '*.la' -exec rm -vf {} ';'

desktop-file-install                                \
        --delete-original                           \
        --dir=%{buildroot}%{_datadir}/applications  \
%{buildroot}%{_datadir}/applications/marco.desktop

# remove needless gsettings convert file
rm -f  %{buildroot}%{_datadir}/MateConf/gsettings/marco.convert

%find_lang %{oldname} --with-gnome --all-name


%files -f %{oldname}.lang
%doc AUTHORS COPYING README ChangeLog
%{_bindir}/marco
%{_bindir}/marco-message
%{_datadir}/applications/marco.desktop
%{_datadir}/themes/ClearlooksRe
%{_datadir}/themes/Dopple-Left
%{_datadir}/themes/Dopple
%{_datadir}/themes/DustBlue
%{_datadir}/themes/Spidey-Left
%{_datadir}/themes/Spidey
%{_datadir}/themes/Splint-Left
%{_datadir}/themes/Splint
%{_datadir}/themes/WinMe
%{_datadir}/themes/eOS
%dir %{_datadir}/marco
%dir %{_datadir}/marco/icons
%{_datadir}/marco/icons/marco-window-demo.png
%{_datadir}/mate-control-center/keybindings/50-marco*.xml
%{_datadir}/mate/wm-properties
%{_datadir}/glib-2.0/schemas/org.mate.marco.gschema.xml
%{_libdir}/libmarco-private.so.0*
%{_mandir}/man1/*
# moved to lib
%exclude %{_libdir}/libmarco-private.so.*

%files -n libmarco-private
%{_libdir}/libmarco-private.so.*


%files devel
%{_bindir}/marco-theme-viewer
%{_bindir}/marco-window-demo
%{_includedir}/marco-1
%{_libdir}/libmarco-private.so
%{_libdir}/pkgconfig/libmarco-private.pc
%{_mandir}/man1/marco-theme-viewer.1.*
%{_mandir}/man1/marco-window-demo.1.*


%changelog
* Fri Mar 21 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_4
- new fc release

* Thu Apr 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_1
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Wed Mar 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.5-alt1_1
- new fc release

* Fri Mar 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt2_1
- bugfix (closes: 28487)

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt1_1
- new fc release

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_4
- new fc release

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_2
- new fc release

* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt5_10
- added libmarco-private (closes: 28322)

* Wed Dec 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt4_10
- new fc release

* Thu Nov 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt4_9
- new fc release

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt4_7
- dropped libmarco-private subpackage (no more needed, 1.5.0 transaction is complete)

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt3_7
- added libmarco-private subpackage

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt2_7
- fuzzless patches

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_7
- use F19 import base

* Thu Oct 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.2
- dependence on mate-control-center-filesystem temporary removed

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Tue Oct 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Fri Aug 03 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- rebuild

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

