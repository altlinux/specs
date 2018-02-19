Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/gdk-pixbuf-csource /usr/bin/glib-gettextize imake libX11-devel libXext-devel libXinerama-devel libXrandr-devel libXt-devel libgio-devel pkgconfig(glib-2.0) pkgconfig(xcomposite) pkgconfig(xcursor) pkgconfig(xrender) xorg-cf-files
# END SourceDeps(oneline)
BuildRequires: libcanberra-gtk2-devel
%define _libexecdir %_prefix/libexec
%define oldname marco
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%oldname and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name marco
%define version 1.20.0
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.20

# Settings used for build from snapshots.
%{!?rel_build:%global commit 62a708d461e08275d6b85985f5fa13fa8fbc85f7}
%{!?rel_build:%global commit_date 20131212}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{oldname}-%{version}-%{git_ver}.tar.xz}

Name:          mate-window-manager
Version:       %{branch}.0
%if 0%{?rel_build}
Release:       alt1_1
%else
Release:       alt1_1
%endif
Summary:       MATE Desktop window manager
License:       LGPLv2+ and GPLv2+
URL:           http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R marco.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{oldname}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{oldname}/snapshot/%{oldname}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires: desktop-file-utils
BuildRequires: gtk3-demo libgail3-devel libgtk+3 libgtk+3-devel libgtk+3-gir-devel
BuildRequires: libcanberra-devel libcanberra-gtk-common-devel libcanberra-gtk2-devel libcanberra-gtk3-devel
BuildRequires: libgtop-devel libgtop-gir-devel
BuildRequires: libSM-devel
BuildRequireS: libsoup-devel libsoup-gir-devel libsoup-gnome-devel libsoup-gnome-gir-devel
BuildRequires: libXdamage-devel
BuildRequires: mate-common
BuildRequires: mate-desktop-devel
BuildRequires: zenity
BuildRequires: libstartup-notification-devel
BuildRequires: yelp-tools

Requires:      libmate-desktop
Requires:      libmarco-private = %{version}-%{release}

# http://bugzilla.redhat.com/873342
# https://bugzilla.redhat.com/962009
Provides: firstboot(windowmanager) = marco

# rhbz (#1297958)
Obsoletes:     %{oldname} < 1.12.1-2
Source44: import.info
# http://bugzilla.gnome.org/show_bug.cgi?id=558723
Patch33: stop-spamming-xsession-errors.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=598995
Patch34: Dont-focus-ancestor-window-on-a-different-workspac.patch

%description
MATE Desktop window manager

# to avoid that marco will install in other DE's by compiz-0.8.10
%package -n libmarco-private
Group: System/Libraries
Summary:       Libraries for marco
License:       LGPLv2+
# rhbz (#1297958)
Conflicts:     %{oldname} < 1.12.1-2

%description -n libmarco-private
This package provides Libraries for marco.

%package devel
Group: Development/C
Summary:       Development files for marco
Requires:      %{name} = %{version}-%{release}
Requires:      libmarco-private = %{version}-%{release}

%description devel
Development files for marco


%prep
%if 0%{?rel_build}
%setup -n %{oldname}-%{version} -q

%else
%setup -q -n %{oldname}-%{commit}

%endif

%if 0%{?rel_build}
#NOCONFIGURE=1 ./autogen.sh
%else # 0%{?rel_build}
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif # 0%{?rel_build}
%patch33 -p1
%patch34 -p1

%build
%autoreconf -fisv
%configure --disable-static           \
           --disable-schemas-compile  \
           --with-x

# fix rpmlint unused-direct-shlib-dependency warning
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build V=1


%install
%{makeinstall_std}

find %{buildroot} -name '*.la' -exec rm -vf {} ';'

desktop-file-install                                \
        --delete-original                           \
        --dir=%{buildroot}%{_datadir}/applications  \
%{buildroot}%{_datadir}/applications/marco.desktop

%find_lang %{oldname} --with-gnome --all-name


%files
%doc AUTHORS COPYING README ChangeLog
%{_bindir}/marco
%{_bindir}/marco-message
%{_bindir}/marco-theme-viewer
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
%{_mandir}/man1/*

%files -n libmarco-private -f %{oldname}.lang
%{_libdir}/libmarco-private.so.1*
%{_datadir}/glib-2.0/schemas/org.mate.marco.gschema.xml

%files devel
%{_bindir}/marco-window-demo
%{_includedir}/marco-1
%{_libdir}/libmarco-private.so
%{_libdir}/pkgconfig/libmarco-private.pc
%{_mandir}/man1/marco-theme-viewer.1.*
%{_mandir}/man1/marco-window-demo.1.*


%changelog
* Wed Feb 21 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

* Wed Sep 13 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.1-alt1_1
- new fc release

* Thu Sep 07 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.0-alt1_5
- new fc release

* Thu Oct 06 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.16.0-alt1_1
- update to mate 1.16

* Tue Apr 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt1_3
- new fc release

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt2_1
- fixed dependencies

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt1_1
- new version

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt2_1
- rebuild with libgtop

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

