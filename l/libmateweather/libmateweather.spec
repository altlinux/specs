Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtk-update-icon-cache /usr/bin/gtkdocize glib2-devel libgio-devel pkgconfig(libxml-2.0)
# END SourceDeps(oneline)
# for --enable-python
BuildRequires: python-module-pygobject-devel
BuildRequires: python-module-gudev
BuildRequires: python-module-pygtk-devel

%define _libexecdir %_prefix/libexec
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name libmateweather
%define version 1.20.0
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.20

# Settings used for build from snapshots.
%{!?rel_build:%global commit 06e062693b16189373584801b056079eafac0034}
%{!?rel_build:%global commit_date 20160831}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:          libmateweather
Version:       %{branch}.0
%if 0%{?rel_build}
Release:       alt1_1
%else
Release:       alt1_1
%endif
Summary:       Libraries to allow MATE Desktop to display weather information
License:       GPLv2+ and LGPLv2+
URL:           http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R libmateweather.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires: gtk3-demo libgail3-devel libgtk+3 libgtk+3-devel libgtk+3-gir-devel
BuildRequires: libsoup-devel libsoup-gir-devel libsoup-gnome-devel libsoup-gnome-gir-devel
BuildRequires: mate-common
BuildRequires: python-module-pygtk-devel
BuildRequires: python-module-pygobject-devel

Requires:      %{name}-data = %{version}-%{release}
Source44: import.info
Patch33: libmateweather-1.17.0-gettext-not-xml.patch

%description
Libraries to allow MATE Desktop to display weather information

%package data
Group: System/Libraries
Summary: Data files for the libmateweather
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description data
This package contains shared data needed for libmateweather.

%package devel
Group: Development/C
Summary:  Development files for libmateweather
Requires: %{name} = %{version}-%{release}

%description devel
Development files for libmateweather


%prep
%if 0%{?rel_build}
%setup -q

%else
%setup -q -n %{name}-%{commit}

%endif

%if 0%{?rel_build}
#NOCONFIGURE=1 ./autogen.sh
%else # 0%{?rel_build}
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif # 0%{?rel_build}
%patch33 -p1

%build
autoreconf -fisv
%configure --enable-python --disable-static           \
           --disable-schemas-compile  \
           --enable-gtk-doc-html

# fix unused-direct-shlib-dependency
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool 

%make_build V=1

%install
%{makeinstall_std}

find %{buildroot} -name '*.la' -exec rm -fv {} ';'
find %{buildroot} -name '*.a' -exec rm -fv {} ';'

%find_lang %{name} %{name}-locations --with-gnome --all-name
cat libmateweather-locations.lang >> %{name}.lang


%files
%doc AUTHORS COPYING README
%{_datadir}/glib-2.0/schemas/org.mate.weather.gschema.xml
%{_libdir}/libmateweather.so.1*

%files data -f %{name}.lang
%{_datadir}/icons/mate/*/status/*
%{_datadir}/libmateweather/

%files devel
%%doc %{_datadir}/gtk-doc/html/libmateweather/
%{_libdir}/libmateweather.so
%{_includedir}/libmateweather/
%{_libdir}/pkgconfig/mateweather.pc


%changelog
* Mon Feb 19 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

* Thu Sep 07 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.1-alt1_3
- new fc release

* Wed Oct 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.16.0-alt1_1
- new fc release

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt1_1
- new version

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_2
- new fc release

* Wed Mar 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_3
- new fc release

* Mon Aug 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_1
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_2
- new fc release

* Mon Apr 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_1
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_1
- new fc release

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

