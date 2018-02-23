Group: Graphical desktop/MATE
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++ libgio-devel pkgconfig(giomm-2.4) pkgconfig(glib-2.0) pkgconfig(glibmm-2.4) pkgconfig(gmodule-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           mate-system-monitor
Version:        1.20.0
Release:        alt1_1
Summary:        Process and resource monitor
License:        GPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.20/%{name}-%{version}.tar.xz

BuildRequires: libdbus-glib-devel
BuildRequires: desktop-file-utils
BuildRequires: gtk3-demo libgail3-devel libgtk+3 libgtk+3-devel libgtk+3-gir-devel
BuildRequires: libgtkmm3-devel
BuildRequires: libgtop-devel libgtop-gir-devel
BuildRequires: librsvg-devel librsvg-gir-devel
BuildRequires: libwnck libwnck3-devel libwnck3-gir-devel
BuildRequires: libxml2-devel
BuildRequires: mate-common
BuildRequires: pkgconfig(libsystemd)

Requires: mate-desktop
Source44: import.info

%description
mate-system-monitor allows to graphically view and manipulate the running
processes on your system. It also provides an overview of available resources
such as CPU and memory.

%prep
%setup -q


%build
%add_optflags -std=c++11
%configure \
        --disable-static \
        --disable-schemas-compile \
        --enable-systemd

%make_build V=1


%install
%{makeinstall_std}

desktop-file-install --delete-original             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications    \
  $RPM_BUILD_ROOT%{_datadir}/applications/mate-system-monitor.desktop

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS NEWS COPYING README
%{_bindir}/mate-system-monitor
%{_libexecdir}/mate-system-monitor/msm-kill
%{_libexecdir}/mate-system-monitor/msm-renice
%{_datadir}/polkit-1/actions/org.mate.mate-system-monitor.policy
%{_datadir}/appdata/mate-system-monitor.appdata.xml
%{_datadir}/applications/mate-system-monitor.desktop
%{_datadir}/pixmaps/mate-system-monitor/
%{_datadir}/glib-2.0/schemas/org.mate.system-monitor.*.xml
%{_mandir}/man1/*


%changelog
* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

* Mon Oct 16 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.0-alt1_1
- new fc release

* Wed Sep 06 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.18.0-alt1_4
- new fc release

* Wed Oct 12 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.16.0-alt1_1
- update to mate 1.16

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

