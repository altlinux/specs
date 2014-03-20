Group: Graphical desktop/MATE
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize gcc-c++ libgio-devel pkgconfig(giomm-2.4) pkgconfig(glib-2.0) pkgconfig(glibmm-2.4) pkgconfig(gmodule-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(gtkmm-3.0) pkgconfig(libgtop-2.0) pkgconfig(libwnck-3.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           mate-system-monitor
Version:        1.8.0
Release:        alt1_1
Summary:        Process and resource monitor

License:        GPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.8/%{name}-%{version}.tar.xz

BuildRequires: libdbus-glib-devel
BuildRequires: desktop-file-utils
BuildRequires: gtk2-devel
BuildRequires: libgtkmm2-devel
BuildRequires: libgtop2-devel
BuildRequires: librsvg-devel
BuildRequires: libwnck-devel
BuildRequires: libxml2-devel
BuildRequires: mate-common
BuildRequires: mate-icon-theme-devel

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
        --with-gtk=2.0 \
        --disable-schemas-compile 

make %{?_smp_mflags} V=1


%install
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install --delete-original             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications    \
  $RPM_BUILD_ROOT%{_datadir}/applications/mate-system-monitor.desktop

# remove needless gsettings convert file
rm -f  $RPM_BUILD_ROOT%{_datadir}/MateConf/gsettings/mate-system-monitor.convert

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc AUTHORS NEWS COPYING README
%{_bindir}/mate-system-monitor
%{_datadir}/applications/mate-system-monitor.desktop
%{_datadir}/pixmaps/mate-system-monitor/
%{_datadir}/glib-2.0/schemas/org.mate.system-monitor.*.xml
%{_mandir}/man1/*


%changelog
* Thu Mar 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_1
- new fc release

* Tue Apr 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_1
- new fc release

* Thu Nov 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- converted for ALT Linux by srpmconvert tools

