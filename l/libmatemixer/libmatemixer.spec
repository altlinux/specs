Group: Graphical desktop/MATE
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtkdocize pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name libmatemixer
%define version 1.20.0
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.20

# Settings used for build from snapshots.
%{!?rel_build:%global commit ee0a62c8759040d84055425954de1f860bac8652}
%{!?rel_build:%global commit_date 20140223}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:        libmatemixer
Summary:     Mixer library for MATE desktop
Version:     %{branch}.0
%if 0%{?rel_build}
Release:     alt1_1
%else
Release:     alt1_1
%endif
License:     GPLv2+
URL:         http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R libmatemixer.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%%{name}/snapshot/%%{name}-%%{commit}.tar.xz#/%%{git_tar}}

BuildRequires:  mate-common
BuildRequires:  libpulseaudio-devel
BuildRequires:  libalsa-devel
Source44: import.info


%description
libmatemixer is a mixer library for MATE desktop.
It provides an abstract API allowing access to mixer functionality
available in the PulseAudio, ALSA and OSS sound systems.

%package devel
Group: Graphical desktop/MATE
Summary:  Development libraries for libmatemixer
Requires: %{name} = %{version}-%{release}

%description devel
Development libraries for libmatemixer

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
%configure \
        --disable-static \
        --enable-pulseaudio \
        --enable-alsa \
        --enable-gtk-doc

#drop unneeded direct library deps with --as-needed
# libtool doesn't make this easy, so we do it the hard way
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool

%make_build V=1

%install
%{makeinstall_std}

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_libdir}/libmatemixer.so.*
%{_libdir}/libmatemixer/

%files devel
%{_includedir}/mate-mixer/
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_datadir}/gtk-doc/html/libmatemixer/


%changelog
* Tue Feb 20 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

* Wed Oct 25 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.0-alt1_1
- new fc release

* Thu Sep 07 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.18.0-alt1_3
- new fc release

* Thu Oct 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.16.0-alt1_1
- new fc release

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt1_1
- new version

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt2_2
- rebuild

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_2
- new version

