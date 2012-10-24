# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/mateconftool-2 pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) pkgconfig(gtk+-2.0) pkgconfig(libcanberra-gtk) pkgconfig(libxml-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define glib2_version 2.4.0
%define pango_version 1.4.0
%define gtk2_version 2.10.0
%define libmate_version 1.1.2
%define libmateui_version 1.1.2
%define gail_version 1.2
%define desktop_file_utils_version 0.2.90
%define gstreamer_version 0.10.3

%define gettext_package mate-media

#different version for fc17

Summary:        MATE media programs
Name:           mate-media
Version:        1.4.0
Release:        alt2_1.1
License:        GPLv2+ and GFDL
Group:          Graphical desktop/Other
Source:         http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
URL:            http://pub.mate-desktop.org
ExcludeArch:    s390 s390x

Patch1:         mate-media_fix_gladeui.patch

Requires(post): mate-conf >= 1.1.0
Requires(pre): mate-conf >= 1.1.0
Requires(preun): mate-conf >= 1.1.0

BuildRequires:  gtk2-devel >= %{gtk2_version}
BuildRequires:  mate-conf-devel
BuildRequires:  desktop-file-utils >= %{desktop_file_utils_version}
BuildRequires:  gstreamer-devel >= %{gstreamer_version}
BuildRequires:  gst-plugins-devel >= %{gstreamer_version}
BuildRequires:  gst-plugins-devel
BuildRequires:  libunique-devel
BuildRequires:  libdbus-glib-devel
BuildRequires:  libcanberra-devel
BuildRequires:  mate-doc-utils
BuildRequires:  intltool
BuildRequires:  mate-control-center-devel
BuildRequires:  scrollkeeper
BuildRequires:  mate-common
BuildRequires:  libgladeui-devel
BuildRequires:  libpulseaudio-devel
Patch33: gnome-media-2.26.0-alt-gst-mixer.patch
Patch34: gnome-media-2.29.91-gst-mix_and_new_gvc_no_conflict.patch
Patch35: gnome-media-2.32.0-alt-settings.desktop.patch
Patch36: gnome-media-2.32.0-g_debug.patch
Patch37: gnome-media-alt-desktop-ru.po.patch

%description
This package contains a few media utilities for the MATE desktop,
including a volume control and a configuration utility for audio profiles.

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}
Obsoletes: 		libmate-media-profiles-devel
Provides:  		mate-media-devel

%description    devel
The libmate-media-profiles-devel package contains libraries and header files for
developing applications that use mate-media-profiles.


%package libs
Summary: Libraries for mate-media
Group: Development/C
Requires: %{name} = %{version}-%{release}
Obsoletes: 		libmate-media-profiles
Provides:  		mate-media-libs

%description libs
This package contains the libraries required for using encoding profiles
in MATE media applications.

%package apps
Summary: Some media-related applications for the MATE desktop
Group: Graphical desktop/Other
Requires: %{name} = %{version}-%{release}

%description apps
This package contains an application to record and play sound files
in various formats and a configuration utility for the gstreamer media
framework.

%prep
%setup -q
#for fc16
#%patch1 -p1 -b .mate-media_fix_gladeui
NOCONFIGURE=1 ./autogen.sh
%patch33 -p1
%patch34 -p1
%patch35 -p0
%patch36 -p1
%patch37 -p1

%build
export LDFLAGS="-lm"
%configure \
	--disable-static \
	--enable-gstmix \
	--enable-gstprops \
	--disable-scrollkeeper \
	--enable-profiles
	

make %{?_smp_mflags}

# strip unneeded translations from .mo files
# ideally intltool (ha!) would do that for us
# http://bugzilla.gnome.org/show_bug.cgi?id=474987
cd po
grep -v ".*[.]desktop[.]in[.]in$\|.*[.]server[.]in[.]in$" POTFILES.in > POTFILES.keep
mv POTFILES.keep POTFILES.in
intltool-update --pot
for p in *.po; do
  msgmerge $p %{gettext_package}.pot > $p.out
  msgfmt -o `basename $p .po`.gmo $p.out
done

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_libdir}/control-center-1/panels/lib*.*a
rm -rf $RPM_BUILD_ROOT%{_libdir}/glade3/modules/lib*.*a
rm -rf $RPM_BUILD_ROOT%{_libdir}/lib*.*a
rm -rf $RPM_BUILD_ROOT/var/scrollkeeper

# save space by linking identical images in translated docs
for helpdir in $RPM_BUILD_ROOT%{_datadir}/mate/help/*; do
  for f in $helpdir/C/figures/*.png; do
    b="$(basename $f)"
    for d in $helpdir/*; do
      if [ -d "$d" -a "$d" != "$helpdir/C" ]; then
        g="$d/figures/$b"
        if [ -f "$g" ]; then
          if cmp -s $f $g; then
            rm "$g"; ln -s "../../C/figures/$b" "$g"
          fi
        fi
      fi
    done
  done
done

%find_lang %{gettext_package}

%post
touch --no-create %{_datadir}/icons/mate >&/dev/null || :

%post apps
touch --no-create %{_datadir}/icons/mate >&/dev/null || :

%post libs
export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
mateconftool-2 --makefile-install-rule \
    %{_sysconfdir}/mateconf/schemas/mate-audio-profiles.schemas \
    > /dev/null || :
: 

%pre
if [ "$1" -gt 1 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
    if [ -f %{_sysconfdir}/mateconf/schemas/mate-volume-control.schemas ] ; then
    mateconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/mateconf/schemas/mate-volume-control.schemas \
      > /dev/null || :
  fi
fi

%pre libs
if [ "$1" -gt 1 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
  %{_sysconfdir}/mateconf/schemas/mate-audio-profiles.schemas \
  > /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
    if [ -f %{_sysconfdir}/mateconf/schemas/mate-volume-control.schemas ] ; then
    mateconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/mateconf/schemas/mate-volume-control.schemas \
      > /dev/null || :
  fi
fi

%preun libs
if [ "$1" -eq 0 ]; then
  if [ -f %{_sysconfdir}/mateconf/schemas/mate-audio-profiles.schemas ] ; then
    export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
    mateconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/mateconf/schemas/mate-audio-profiles.schemas \
    > /dev/null || :
  fi
fi

%postun
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/mate >&/dev/null || :
fi

%postun apps
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/mate >&/dev/null || :
fi

%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/mate-volume-control
%{_bindir}/mate-audio-profiles-properties
%{_bindir}/mate-volume-control-applet
%{_bindir}/mate-gstreamer-properties
%config %{_sysconfdir}/mateconf/schemas/mate-volume-control.schemas
%{_sysconfdir}/xdg/autostart/mate-volume-control-applet.desktop
%{_datadir}/applications/mate-volume-control.desktop
%{_datadir}/mate-media
%{_datadir}/sounds/mate/
%{_datadir}/mate/help/mate-volume-control/*
%{_datadir}/mate/help/mate-audio-profiles/*
%{_datadir}/omf/mate-volume-control/*
%{_datadir}/omf/mate-audio-profiles/*
%_datadir/locale/*/*

%files libs
%config %{_sysconfdir}/mateconf/schemas/mate-audio-profiles.schemas
%{_libdir}/*.so.*
#fc17 
%{_libdir}/glade3/modules/
#fc16
#%{_libdir}/glade/modules/

%files apps
%{_datadir}/icons/mate/*
%{_bindir}/mate-gstreamer-properties
%{_datadir}/mate-gstreamer-properties
%{_datadir}/applications/mate-gstreamer-properties.desktop
%{_datadir}/mate/help/mate-gstreamer-properties/*
%{_datadir}/omf/mate-gstreamer-properties/*

%files devel
%{_includedir}/mate-media/profiles/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
#fc17
%{_datadir}/glade3/catalogs/mate-media-profiles.xml
#fc16
#%{_datadir}/glade/catalogs/mate-media-profiles.xml



%changelog
* Thu Oct 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- 20120622 mate snapshot

