# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize gcc-c++ pkgconfig(giomm-2.4) pkgconfig(glib-2.0) pkgconfig(glibmm-2.4) pkgconfig(gmodule-2.0) pkgconfig(gtk+-2.0) pkgconfig(libgtop-2.0)
# END SourceDeps(oneline)
Group: Graphical desktop/MATE
%define _libexecdir %_prefix/libexec
Name:           mate-system-monitor
Version:        1.5.0
Release:        alt1_2
Summary:        Process and resource monitor

License:        GPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
# upstream commit https://github.com/mate-desktop/mate-system-monitor/commit/6d06a224d764c5b58127f665b2fcfa7eeac080ee
Patch0:         desktopfile_fix.patch

BuildRequires: libgtop2-devel
BuildRequires: desktop-file-utils
BuildRequires: libmatewnck-devel
BuildRequires: pango-devel
BuildRequires: gtk2-devel
BuildRequires: libgtkmm2-devel
BuildRequires: libstartup-notification-devel
BuildRequires: rarian-compat
BuildRequires: libselinux-devel
BuildRequires: mate-icon-theme-devel
BuildRequires: pcre-devel
BuildRequires: librsvg-devel
BuildRequires: libxml2-devel
BuildRequires: mate-doc-utils
BuildRequires: mate-common
BuildRequires: libdbus-glib-devel

Requires: mate-desktop
Source44: import.info


%description
mate-system-monitor allows to graphically view and manipulate the running
processes on your system. It also provides an overview of available resources
such as CPU and memory.

%prep
%setup -q
%patch0 -p1
NOCONFIGURE=1 ./autogen.sh

%build
%configure \
        --disable-static \
        --disable-scrollkeeper \
        --enable-compile-warnings=minimum

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install --delete-original             \
  --remove-category=MATE                           \
  --add-category=X-Mate                            \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications    \
  $RPM_BUILD_ROOT%{_datadir}/applications/mate-system-monitor.desktop

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS NEWS COPYING README
%{_bindir}/mate-system-monitor
%{_datadir}/applications/mate-system-monitor.desktop
%{_datadir}/pixmaps/mate-system-monitor/
%{_datadir}/glib-2.0/schemas/org.mate.system-monitor.*.xml
%{_datadir}/mate/help/mate-system-monitor/


%changelog
* Thu Nov 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- converted for ALT Linux by srpmconvert tools

