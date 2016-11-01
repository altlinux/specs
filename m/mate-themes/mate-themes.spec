Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mate-themes
%define version 3.22.4
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 3.22

%global rel_ver 3.22.4

# Settings used for build from snapshots.
%{!?rel_build:%global commit 59b3286ac467f19e9bce39783e71836ced239b7b}
%{!?rel_build:%global commit_date 20160526}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:           mate-themes
Version:        %{rel_ver}
%if 0%{?rel_build}
Release:        alt1_1
%else
Release:        alt1_1
%endif
Summary:        MATE Desktop themes
License:        GPLv2+
URL:            http://mate-desktop.org
BuildArch:      noarch

# for downloading the tarball use 'spectool -g -R mate-themes.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/themes/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires:  mate-common
BuildRequires: gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel libgtk+2-gir-devel
BuildRequires: libgdk-pixbuf-devel libgdk-pixbuf-gir-devel

Requires:       mate-icon-theme
Requires:       libgtk-engines-default
Requires:       libgtk-engine-murrine
Source44: import.info

%description
MATE Desktop themes

%prep
%if 0%{?rel_build}
# for releases
%setup -qn %{name}-%{version}
%else # 0%{?rel_build}
# for snapshots
%setup -qn %{name}-%{commit}
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif # 0%{?rel_build}

%build
%configure --enable-icon-mapping

make %{?_smp_mflags} V=1

%install
%{makeinstall_std}

find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'

%post
for icon_theme in \
  ContrastHigh ;
do
  /bin/touch --no-create %{_datadir}/icons/${icon_theme} &> /dev/null || :
done

%postun
if [ $1 -eq 0 ]; then
for icon_theme in \
  ContrastHigh ;
do
  /bin/touch --no-create %{_datadir}/icons/${icon_theme} &> /dev/null || :

done
fi

%files
%doc AUTHORS COPYING README ChangeLog
%{_datadir}/themes/BlackMATE/
%{_datadir}/themes/BlueMenta/
%{_datadir}/themes/Blue-Submarine/
%{_datadir}/themes/ContrastHighInverse/
%{_datadir}/themes/GreenLaguna/
%{_datadir}/themes/Green-Submarine/
%{_datadir}/themes/HighContrast/metacity-1/metacity-theme-1.xml
%{_datadir}/themes/Menta/
%{_datadir}/themes/TraditionalOk/
%{_datadir}/themes/TraditionalGreen/
%{_datadir}/themes/Shiny/
%{_datadir}/icons/ContrastHigh/
%{_datadir}/icons/mate/cursors/


%changelog
* Tue Nov 01 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.22.4-alt1_1
- new fc release

* Thu Oct 06 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.22.3-alt1_1
- update to mate 1.16

* Thu May 19 2016 Igor Vlasenko <viy@altlinux.ru> 3.20.7-alt1_1
- converted for ALT Linux by srpmconvert tools

* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 3.20.5-alt1_1
- converted for ALT Linux by srpmconvert tools

* Tue Apr 05 2016 Igor Vlasenko <viy@altlinux.ru> 3.18.0-alt1_1
- new fc release

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt1_1
- new version

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.6-alt2_0.1.git20151005.5fec168
- fixed dependencies

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.6-alt1_1
- new version

* Thu Mar 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt1_0.1.git20140304.5a900ef
- new fc release

* Mon Aug 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_0.2.git3fc43dd
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_0.1.git15baae1
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Thu Mar 28 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- converted for ALT Linux by srpmconvert tools

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_2
- 20120622 mate snapshot

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_1
- converted by srpmconvert script

