Group: Archiving/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/glib-mkenums libgio-devel pkgconfig(gio-unix-2.0) pkgconfig(glib-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(json-glib-1.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define oldname engrampa
%define fedora 21
# %oldname or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name engrampa
%define version 1.8.0
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.8

# Settings used for build from snapshots.
%{!?rel_build:%global commit f4611c3411c44e792f729a0780c31b0aa55fe004}
%{!?rel_build:%global commit_date 20131215}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{oldname}-%{version}-%{git_ver}.tar.xz}

Name:          mate-file-archiver
Version:       %{branch}.0
Release:       alt1_1
#Release:       0.2%{?git_rel}%{?dist}
Summary:       MATE Desktop file archiver
License:       GPLv2+ and LGPLv2+
URL:           http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R engrampa.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{oldname}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{oldname}/snapshot/%{oldname}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires:  mate-common
BuildRequires:  desktop-file-utils
BuildRequires:  gtk2-devel
%if 0%{?fedora} > 20
BuildRequires:  mate-file-manager-devel
%else
BuildRequires:  mate-file-manager-devel
%endif
BuildRequires:  mate-desktop-devel
BuildRequires:  libSM-devel

%if 0%{?fedora} && 0%{?fedora} <= 25
%endif
Patch33: file-roller-2.28.2-alt-7z.patch
Source44: import.info

%description
Mate File Archiver is an application for creating and viewing archives files,
such as zip, xv, bzip2, cab, rar and other compress formats.


%prep
%setup -n %{oldname}-%{version} -q%{!?rel_build:n %{oldname}-%{commit}}
%patch33 -p0

# nedded to create missing configure and make files
#NOCONFIGURE=1 ./autogen.sh


%build
%configure                 \
   --disable-schemas-compile \
   --disable-static        \
   --with-gtk=2.0          \
   --enable-caja-actions

make %{?_smp_mflags} V=1


%install
%{makeinstall_std}

desktop-file-install                                \
    --delete-original                               \
    --dir %{buildroot}%{_datadir}/applications      \
%{buildroot}%{_datadir}/applications/engrampa.desktop

find %{buildroot} -name "*.la" -exec rm -f {} ';'

# remove needless gsettings convert file to avoid slow session start
rm -f  %{buildroot}%{_datadir}/MateConf/gsettings/engrampa.convert

%find_lang %{oldname} --with-gnome --all-name

%files -f %{oldname}.lang
%doc README COPYING NEWS AUTHORS
%{_mandir}/man1/*
%{_bindir}/engrampa
%{_libexecdir}/engrampa
%{_datadir}/engrampa
%{_datadir}/applications/engrampa.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/glib-2.0/schemas/org.mate.engrampa.gschema.xml
%{_libdir}/caja/extensions-2.0/libcaja-engrampa.so


%changelog
* Sat Mar 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_3
- new fc release

* Mon Jul 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_2
- new fc release

* Mon Apr 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_6
- new fc release

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_4
- new fc release

* Fri Nov 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_3
- rebase to fc

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Sun Aug 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- 20120622 mate snapshot

