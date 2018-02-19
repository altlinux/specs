Group: File tools
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize pkgconfig(gio-2.0) pkgconfig(glib-2.0)
# END SourceDeps(oneline)
BuildRequires: libgtk+2-gir-devel libgtk+3-gir-devel libpolkit-gir-devel
%define _libexecdir %_prefix/libexec
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mate-polkit
%define version 1.20.0
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.20

# Settings used for build from snapshots.
%{!?rel_build:%global commit 8e0c8e17e0138afa7757a1bdf8edd6f2c7b47a14}
%{!?rel_build:%global commit_date 20150930}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:		mate-polkit
Version:    %{branch}.0
%if 0%{?rel_build}
Release:	alt1_1
%else
Release:    alt1_1
%endif
Summary:	Integrates polkit authentication for MATE desktop
License:	LGPLv2+
URL:		http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R mate-polkit.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires:	gtk3-demo libgail3-devel libgtk+3 libgtk+3-devel libgtk+3-gir-devel
BuildRequires:	mate-common
BuildRequires:	libpolkit-devel libpolkit-gir-devel
BuildRequires:	libdbus-glib-devel
BuildRequires:	libappindicator-gtk3-devel libappindicator-gtk3-gir-devel

Provides:	PolicyKit-authentication-agent
# dropping -devel subpackage 
Provides:   mate-polkit-devel = %{version}-%{release}
Provides:   mate-polkit = %{version}-%{release}
Obsoletes:  mate-polkit-devel < %{version}-%{release}
Source44: import.info


%description
Integrates polkit with the MATE Desktop environment

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
%configure  \
        --disable-static       \
        --enable-accountsservice \
        --enable-appindicator=yes

%make_build V=1

%install
%{makeinstall_std}

%find_lang %{name}

find %{buildroot} -name '*.la' -exec rm -fv {} ';'


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_sysconfdir}/xdg/autostart/polkit-mate-authentication-agent-1.desktop
%{_libexecdir}/polkit-mate-authentication-agent-1


%changelog
* Tue Feb 20 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

* Wed Oct 25 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.0-alt1_1
- new fc release

* Wed Sep 06 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.18.1-alt1_3
- new fc release

* Thu Oct 06 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.16.0-alt1_1
- update to mate 1.16

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.0-alt1_1
- new version

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt2_1
- fixed dependencies

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt1_1
- new version

* Wed Mar 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_2
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- new fc release

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Fri Aug 03 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- 20120622 mate snapshot

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

