Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize libgio-devel pkgconfig(gio-2.0) pkgconfig(gobject-2.0) pkgconfig(gstreamer-0.10) pkgconfig(gstreamer-audio-0.10) pkgconfig(gstreamer-interfaces-0.10) pkgconfig(gstreamer-plugins-base-0.10) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(libcanberra-gtk) pkgconfig(libcanberra-gtk3) pkgconfig(libmatepanelapplet-4.0) pkgconfig(unique-3.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           mate-media
Version:        1.8.0
Release:        alt1_0.gstreamer
Summary:        MATE media programs
License:        GPLv2+ and LGPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.8/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gtk2-devel
BuildRequires:  libxml2-devel
BuildRequires:  libcanberra-devel
BuildRequires:  mate-desktop-devel
BuildRequires:  mate-common
BuildRequires:  libpulseaudio-devel
BuildRequires:  libunique-devel
Source44: import.info
Patch33: mate-media-1.8.0-alt-gst-mixer.patch
Patch34: gnome-media-2.29.91-gst-mix_and_new_gvc_no_conflict.patch
Patch35: gnome-media-2.32.0-g_debug.patch
Patch36: gnome-media-alt-desktop-ru.po.patch
Requires: gst-plugins-base

%description
This package contains a few media utilities for the MATE desktop,
including a volume control.


%prep
%setup -q
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1

%build
%configure \
        --disable-static \
        --disable-schemas-compile \
        --with-gtk=2.0 \
        --enable-gstmix \
        --enable-gst-mixer-applet \
        --enable-gstreamer \
        --enable-pulseaudio

make %{?_smp_mflags} V=1

%install
%{makeinstall_std}

find %{buildroot} -name '*.la' -exec rm -rf {} ';'

desktop-file-install                                                    \
        --delete-original                                               \
        --dir=%{buildroot}%{_datadir}/applications                      \
%{buildroot}%{_datadir}/applications/mate-volume-control.desktop

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_mandir}/man1/*
%{_bindir}/mate-volume-control
%{_bindir}/mate-volume-control-applet
%{_sysconfdir}/xdg/autostart/mate-volume-control-applet.desktop
%{_datadir}/mate-media/
%{_datadir}/sounds/mate/
%{_datadir}/applications/mate-volume-control.desktop


%changelog
* Fri Mar 21 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_0.gstreamer
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt2_3
- new fc release

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt2_1
- added gst dependency (closes: 28928)

* Mon Apr 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Sun Apr 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_1
- new fc release

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_4
- new fc release

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_3
- new fc release

* Thu Oct 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- 20120622 mate snapshot

