Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/glib-gettextize libICE-devel libgio-devel pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(mate-desktop-2.0) pkgconfig(sm) pkgconfig(vte) pkgconfig(vte-2.91) pkgconfig(x11)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mate-terminal
%define version 1.12.1
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.12

# Settings used for build from snapshots.
%{!?rel_build:%global commit ac33ed09bb41ba717df3722cc71e25c1aa5134c5}
%{!?rel_build:%global commit_date 20150709}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Summary:        Terminal emulator for MATE
Name:           mate-terminal
Version:        %{branch}.1
%if 0%{?rel_build}
Release:        alt1_1
%else
Release:        alt1_1
%endif
License:        GPLv3+
URL:            http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R mate-terminal.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

#Default to black bg white fg, unlimited scrollback, turn off use theme default
Patch0:        mate-terminal_better_defaults.patch

BuildRequires: libdconf-devel
BuildRequires: desktop-file-utils
BuildRequires: glib2-devel
BuildRequires: gtk2-devel
BuildRequires: libSM-devel
BuildRequires: mate-common
BuildRequires: libvte-devel
BuildRequires: mate-desktop-devel

# needed to get a gsettings schema, rhbz #908105
Requires:      libmate-desktop
Requires:      gsettings-desktop-schemas
Source44: import.info
Provides: xvt

%description
Mate-terminal is a terminal emulator for MATE. It supports translucent
backgrounds, opening multiple terminals in a single window (tabs) and
clickable URLs.

%prep
%setup -q%{!?rel_build:n %{name}-%{commit}}

%patch0 -p1 -b .better_defaults

%if 0%{?rel_build}
#NOCONFIGURE=1 ./autogen.sh
%else # 0%{?rel_build}
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif # 0%{?rel_build}

%build
%configure --disable-static                \
           --with-gtk=2.0                  \
           --disable-schemas-compile       

make %{?_smp_mflags} V=1


%install
%{makeinstall_std}

desktop-file-install                                                    \
        --delete-original                                               \
        --dir=%{buildroot}%{_datadir}/applications                      \
%{buildroot}%{_datadir}/applications/mate-terminal.desktop

%find_lang %{name} --with-gnome --all-name
# alternatives
mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_bindir/xvt    %_bindir/%name  48
EOF


%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README ChangeLog
%{_bindir}/mate-terminal
%{_bindir}/mate-terminal.wrapper
%{_datadir}/mate-terminal/
%{_datadir}/applications/mate-terminal.desktop
%{_datadir}/glib-2.0/schemas/org.mate.terminal.gschema.xml
%{_datadir}/appdata/mate-terminal.appdata.xml
%{_mandir}/man1/*
%_altdir/%name


%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt1_1
- new version

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.1-alt2_2
- fixed dependencies

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.1-alt1_2
- new version

* Thu Mar 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Sat Aug 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_11
- new fc release

* Tue May 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_2
- new fc release

* Thu Apr 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_1
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_3
- new fc release

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- new fc release

* Tue Dec 04 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt3_4
- added xvt provides (closes: 28160)

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_4
- added xvt alternative

* Fri Nov 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_4
- rebase to fc

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- 20120622 mate snapshot

