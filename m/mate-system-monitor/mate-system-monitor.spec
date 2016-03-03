Group: Graphical desktop/MATE
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++ libgio-devel pkgconfig(giomm-2.4) pkgconfig(glib-2.0) pkgconfig(glibmm-2.4) pkgconfig(gmodule-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(gtkmm-2.4) pkgconfig(gtkmm-3.0) pkgconfig(libgtop-2.0) pkgconfig(librsvg-2.0) pkgconfig(libsystemd) pkgconfig(libwnck-1.0) pkgconfig(libwnck-3.0) pkgconfig(libxml-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           mate-system-monitor
Version:        1.12.1
Release:        alt1_1
Summary:        Process and resource monitor
License:        GPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.12/%{name}-%{version}.tar.xz

Patch3:         mate-system-monitor_Replaced-sysinfo-gtk-tables-with-gtk-grids.patch
Patch4:         mate-system-monitor_several-deprecations.patch
Patch5:         mate-system-monitor_deprecated-gtk_style_context_get_font.patch
Patch6:         mate-system-monitor_deprecated-gtk_tree_view_set_rules_hint.patch
Patch7:         mate-system-monitor_deprecated-usage-o-non-zero-pages.patch
Patch8:         mate-system-monitor_deprecated-gtk_v-h-box.patch
Patch9:         mate-system-monitor_deprecated-GtkMisc.patch

BuildRequires: libdbus-glib-devel
BuildRequires: desktop-file-utils
BuildRequires: libgtk+3-devel
BuildRequires: libgtkmm3-devel
BuildRequires: libgtop2-devel
BuildRequires: librsvg-devel
BuildRequires: libwnck3-devel
BuildRequires: libxml2-devel
BuildRequires: mate-common

Requires: mate-desktop
Source44: import.info

%description
mate-system-monitor allows to graphically view and manipulate the running
processes on your system. It also provides an overview of available resources
such as CPU and memory.

%prep
%setup -q

%patch3 -p1 -b .Replaced-sysinfo-gtk-tables-with-gtk-grids
%patch4 -p1 -b .several-deprecations.patch
%patch5 -p1 -b .deprecated-gtk_style_context_get_font.patch
%patch6 -p1 -b .deprecated-gtk_tree_view_set_rules_hint.patch
%patch7 -p1 -b .deprecated-usage-o-non-zero-pages.patch
%patch8 -p1 -b .deprecated-gtk_v-h-box.patch
%patch9 -p1 -b .deprecated-GtkMisc.patch

%build
%add_optflags -std=c++11
%configure \
        --disable-static \
        --with-gtk=3.0 \
        --disable-schemas-compile 

make %{?_smp_mflags} V=1


%install
%{makeinstall_std}

desktop-file-install --delete-original             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications    \
  $RPM_BUILD_ROOT%{_datadir}/applications/mate-system-monitor.desktop

# remove needless gsettings convert file
rm -f  $RPM_BUILD_ROOT%{_datadir}/MateConf/gsettings/mate-system-monitor.convert

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc AUTHORS NEWS COPYING README
%{_bindir}/mate-system-monitor
%{_datadir}/appdata/mate-system-monitor.appdata.xml
%{_datadir}/applications/mate-system-monitor.desktop
%{_datadir}/pixmaps/mate-system-monitor/
%{_datadir}/glib-2.0/schemas/org.mate.system-monitor.*.xml
%{_mandir}/man1/*


%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt1_1
- new version

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.1-alt1_1
- new version

* Mon Oct 19 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.0-alt2_1.2
- build with gcc 5.2 fixed

* Sat Jun 13 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.8.0-alt2_1.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt2_1
- rebuild with libgtop

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

