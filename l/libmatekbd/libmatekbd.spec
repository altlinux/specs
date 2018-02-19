Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize imake libXt-devel libgio-devel libgtk+3-gir-devel libxklavier-gir-devel pkgconfig(gdk-3.0) pkgconfig(gdk-x11-3.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gtk+-3.0) xorg-cf-files
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name libmatekbd
%define version 1.20.0
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.20

# Settings used for build from snapshots.
%{!?rel_build:%global commit 5e8b69cf7c6d031cbb0b0f01a7518e72146c0af1}
%{!?rel_build:%global commit_date 20151009}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:           libmatekbd
Version:        %{branch}.0
%if 0%{?rel_build}
Release:        alt1_1
%else
Release:        alt1_1
%endif
Summary:        Libraries for mate kbd
License:        LGPLv2+
URL:            http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R libmatekbd.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires:  desktop-file-utils
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  libICE-devel
BuildRequires:  libxklavier-devel
BuildRequires:  mate-common
BuildRequires:  gobject-introspection-devel
Source44: import.info
Requires: iso-codes

%description
Libraries for matekbd

%package devel
Group: Development/C
Summary:  Development libraries for libmatekbd
Requires: %{name} = %{version}-%{release}

%description devel
Development libraries for libmatekbd

%prep
%if 0%{?rel_build}
%setup -q

%else
%setup -q -n %{name}-%{commit}

%endif

%if 0%{?rel_build}
#NOCONFIGURE=1 ./autogen.sh
%else # 0%{?rel_build}
# for snapshots
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif # 0%{?rel_build}

%build
autoreconf -fisv

%configure                   \
   --disable-static          \
   --disable-schemas-compile \
   --with-x                  \
   --enable-introspection=yes
  
%make_build V=1


%install
%{makeinstall_std}

find %{buildroot} -name '*.la' -exec rm -fv {} ';'

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_datadir}/libmatekbd
%{_datadir}/glib-2.0/schemas/org.mate.peripherals-keyboard-xkb.gschema.xml
%{_libdir}/libmatekbd.so.4*
%{_libdir}/libmatekbdui.so.4*
%{_libdir}/girepository-1.0/Matekbd-1.0.typelib

%files devel
%{_includedir}/libmatekbd
%{_libdir}/pkgconfig/libmatekbd.pc
%{_libdir}/pkgconfig/libmatekbdui.pc
%{_libdir}/libmatekbdui.so
%{_libdir}/libmatekbd.so
%{_datadir}/gir-1.0/Matekbd-1.0.gir


%changelog
* Mon Feb 19 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

* Wed Sep 13 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.0-alt1_1
- new fc release

* Thu Sep 07 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.18.2-alt1_3
- new fc release

* Wed Oct 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.16.0-alt1_1
- new fc release

* Mon Mar 28 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt2_1
- moved gir to devel (closes: #31926)

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt1_1
- new fc release

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_2
- new fc release

* Wed Mar 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_2
- new fc release

* Thu Aug 01 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_1
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Sun Feb 17 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_1
- new fc release

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- new fc release

* Tue Nov 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1.1
- Build for Sisyphus

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- added Requires: iso-codes

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

