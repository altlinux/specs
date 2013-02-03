Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize libgio-devel pkgconfig(gio-2.0) pkgconfig(gobject-2.0) pkgconfig(gstreamer-audio-0.10) pkgconfig(gstreamer-interfaces-0.10) pkgconfig(libcanberra-gtk) pkgconfig(libxml-2.0) pkgconfig(mate-desktop-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           mate-media
Version:        1.5.1
Release:        alt1_3
Summary:        MATE media programs
License:        GPLv2+ and LGPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gstreamer-0.10)
BuildRequires:  pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:  pkgconfig(mate-default-applications)
BuildRequires:  pkgconfig(unique-1.0)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  mate-doc-utils
BuildRequires:  rarian-compat
BuildRequires:  mate-common
BuildRequires:  libpulseaudio-devel
BuildRequires:  libclutter-gst-devel
BuildRequires:  mate-panel-devel

Requires(post):    desktop-file-utils
Requires(postun):  desktop-file-utils

Obsoletes:      %{name}-devel < 1.4.0-4

#fix gstreamer applet
#https://github.com/mate-desktop/mate-media/pull/15
Patch0: commits_rollup.patch
Source44: import.info
Patch33: gnome-media-2.26.0-alt-gst-mixer.patch
Patch34: gnome-media-2.29.91-gst-mix_and_new_gvc_no_conflict.patch
Patch35: gnome-media-2.32.0-alt-settings.desktop.patch
Patch36: gnome-media-2.32.0-g_debug.patch
Patch37: gnome-media-alt-desktop-ru.po.patch

%description
This package contains a few media utilities for the MATE desktop,
including a volume control.


%prep
%setup -q
%patch0 -p1 -b .commit_rollup.patch
NOCONFIGURE=1 ./autogen.sh
%patch33 -p1
%patch34 -p1
%patch35 -p0
%patch36 -p1
%patch37 -p1


%build
%configure \
        --disable-static \
        --enable-gstmix \
        --disable-schemas-compile \
        --disable-scrollkeeper \
        --enable-gst-mixer-applet \
        --enable-pulseaudio \
        --enable-gstreamer \
        --with-gnu-ld

make V=1 %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -exec rm -rf {} ';'

desktop-file-install                                                    \
        --remove-category="MATE"                                        \
        --add-category="X-Mate"                                         \
        --delete-original                                               \
        --dir=%{buildroot}%{_datadir}/applications                      \
%{buildroot}%{_datadir}/applications/mate-volume-control.desktop


%find_lang %{name} --all-name

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/mate-volume-control
%{_bindir}/mate-volume-control-applet
%{_sysconfdir}/xdg/autostart/mate-volume-control-applet.desktop
%{_datadir}/icons/mate/*/*/*.png
%{_datadir}/mate-media/
%{_datadir}/sounds/mate/
%{_datadir}/glib-2.0/schemas/org.mate.volume-control.gschema.xml
%{_datadir}/applications/mate-volume-control.desktop
%{_datadir}/mate/help/mate-volume-control
%{_datadir}/omf/mate-volume-control
%{_libexecdir}/mixer_applet2
%{_datadir}/dbus-1/services/org.mate.panel.applet.MixerAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.mixer.gschema.xml
%{_datadir}/mate-2.0/ui/mixer-applet-menu.xml
%{_datadir}/mate-panel/applets/org.mate.applets.MixerApplet.mate-panel-applet
%{_datadir}/mate/help/mate-mixer_applet2
%{_datadir}/omf/mate-mixer_applet2

%changelog
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

