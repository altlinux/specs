Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/dbus-binding-tool /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/glib-mkenums /usr/bin/gtkdocize libICE-devel libSM-devel libgio-devel pkgconfig(gdk-pixbuf-2.0) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(gtk+-unix-print-2.0) pkgconfig(gtk+-unix-print-3.0) pkgconfig(shared-mime-info) pkgconfig(x11) python-devel python-module-pygobject-devel xorg-xproto-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define oldname eom
%define fedora 21
# %oldname or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name eom
%define version 1.8.0
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.8

# Settings used for build from snapshots.
%{!?rel_build:%global commit 7ba7e03f4d5e2ecd3c77f9d9394521b7608ca05f}
%{!?rel_build:%global commit_date 20131212}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{oldname}-%{version}-%{git_ver}.tar.xz}

Name:          mate-image-viewer
Version:       %{branch}.0
#Release:       0.1%{?git_rel}%{?dist}
Release:       alt1_1
Summary:       Eye of MATE image viewer
License:       GPLv2+ and LGPLv2+ 
URL:           http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R eom.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{oldname}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{oldname}/snapshot/%{oldname}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires: zlib-devel
BuildRequires: gtk2-devel
BuildRequires: libexif-devel
BuildRequires: libexempi-devel
BuildRequires: libxml2-devel
BuildRequires: librsvg-devel
BuildRequires: mate-desktop-devel
BuildRequires: liblcms2-devel
BuildRequires: mate-icon-theme-devel
BuildRequires: python-module-pygtk-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libjpeg-devel
BuildRequires: desktop-file-utils
BuildRequires: mate-common

#fix rhbz (#1008249)
Requires:      libmate-desktop

%if 0%{?fedora} && 0%{?fedora} <= 25
%endif
Source44: import.info

%description
The Eye of MATE (eom) is the official image viewer for the
MATE desktop. It can view single image files in a variety of formats, as
well as large image collections.
Eye of Mate is extensible through a plugin system.

%package devel
Summary:  Support for developing plugins for the eom image viewer
Group:    Development/C
Requires: mate-image-viewer = %{version}-%{release}
%if 0%{?fedora} && 0%{?fedora} <= 25
Provides: mate-image-viewer%{?_isa} = %{version}-%{release}
Provides: mate-image-viewer = %{version}-%{release}
Obsoletes: mate-image-viewer < %{version}-%{release}
%endif

%description devel
Development files for eom


%prep
%setup -n %{oldname}-%{version} -q%{!?rel_build:n %{oldname}-%{commit}}

# needed for git snapshots
#NOCONFIGURE=1 ./autogen.sh

%build
%configure \
   --with-gtk=2.0 \
   --enable-python \
   --with-x \
   --disable-schemas-compile
           
make %{?_smp_mflags} V=1

%install
%{makeinstall_std}

desktop-file-install                               \
  --delete-original                                \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications    \
$RPM_BUILD_ROOT%{_datadir}/applications/eom.desktop

find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %{oldname} --with-gnome --all-name

# remove needless gsettings convert file
rm -f  $RPM_BUILD_ROOT%{_datadir}/MateConf/gsettings/eom.convert


%files -f %{oldname}.lang
%doc AUTHORS COPYING NEWS README
%{_mandir}/man1/*
%{_bindir}/eom
%dir %{_libdir}/eom
%dir %{_libdir}/eom/plugins
%{_libdir}/eom/plugins/*
%{_datadir}/applications/eom.desktop
%{_datadir}/eom/
%_iconsdir/hicolor/*/*/*
%{_datadir}/glib-2.0/schemas/org.mate.eom.gschema.xml

%files devel
%{_libdir}/pkgconfig/eom.pc
%dir %{_includedir}/eom-2.20
%dir %{_includedir}/eom-2.20/eom
%{_includedir}/eom-2.20/eom/*.h
%{_datadir}/gtk-doc/html/eom/


%changelog
* Sat Mar 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Thu Aug 01 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_1
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_4
- new fc release

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_3
- new fc release

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- added mate-desktop-1.5.0-alt-settings.patch - font settings

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Sun Aug 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

