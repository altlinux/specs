Group: Graphical desktop/MATE
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize gcc-c++ libgio-devel pkgconfig(giomm-2.4) pkgconfig(glib-2.0) pkgconfig(glibmm-2.4) pkgconfig(gmodule-2.0) pkgconfig(gtk+-2.0) pkgconfig(libgtop-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           mate-system-monitor
Version:        1.6.1
Release:        alt1_1
Summary:        Process and resource monitor

License:        GPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz

BuildRequires: libgtop2-devel
BuildRequires: desktop-file-utils
BuildRequires: libmatewnck-devel
BuildRequires: gtk2-devel
BuildRequires: libgtkmm2-devel
BuildRequires: rarian-compat
BuildRequires: mate-icon-theme-devel
BuildRequires: librsvg-devel
BuildRequires: libxml2-devel
BuildRequires: mate-doc-utils
BuildRequires: mate-common
BuildRequires: libdbus-glib-devel
BuildRequires: hardlink

Requires: mate-desktop
Source44: import.info


%description
mate-system-monitor allows to graphically view and manipulate the running
processes on your system. It also provides an overview of available resources
such as CPU and memory.

%prep
%setup -q

%build
%configure \
        --disable-static \
        --disable-scrollkeeper \
        --disable-schemas-compile 

make %{?_smp_mflags} V=1


%install
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install --delete-original             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications    \
  $RPM_BUILD_ROOT%{_datadir}/applications/mate-system-monitor.desktop

# save space by linking identical images in translated docs
hardlink -c -v $RPM_BUILD_ROOT%{_datadir}/mate/help/%{name}

# remove needless gsettings convert file
rm -f  $RPM_BUILD_ROOT%{_datadir}/MateConf/gsettings/mate-system-monitor.convert

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS NEWS COPYING README
%{_bindir}/mate-system-monitor
%{_datadir}/applications/mate-system-monitor.desktop
%{_datadir}/pixmaps/mate-system-monitor
%{_datadir}/glib-2.0/schemas/org.mate.system-monitor.*.xml
%{_datadir}/mate/help/mate-system-monitor/
%{_mandir}/man1/*
%{_datadir}/omf/mate-system-monitor/


%changelog
* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_1
- new fc release

* Tue Apr 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_1
- new fc release

* Thu Nov 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- converted for ALT Linux by srpmconvert tools

