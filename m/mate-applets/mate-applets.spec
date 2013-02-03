%def_disable timer_applet
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gdk-pixbuf-csource /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/jw /usr/bin/xsltproc libICE-devel libSM-devel libX11-devel libapm-devel libcpufreq-devel libgio-devel pkgconfig(NetworkManager) pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0) pkgconfig(gtk+-2.0) pkgconfig(gucharmap-2) pkgconfig(hal) pkgconfig(libgtop-2.0) pkgconfig(libxml-2.0) pkgconfig(mate-settings-daemon) pkgconfig(polkit-gobject-1) python-devel xorg-kbproto-devel
# END SourceDeps(oneline)
BuildRequires: xvfb-run
%define _libexecdir %_prefix/libexec

%define po_package mate-applets

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define build_stickynotes 0

Summary:        Small applications for the MATE panel
Name:		mate-applets
Version:	1.5.1
Release:        alt1
License:	GPLv2+ and GFDL
Group:          Graphical desktop/MATE
URL:		http://pub.mate-desktop.org
Source: 	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
Patch0:         mate-applets_mcharmap.patch
Patch1:         pymod-check.patch

BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  libmateui-devel
BuildRequires:  libmate-devel
BuildRequires:  mate-panel-devel
BuildRequires:  libglade2-devel
BuildRequires:  libgtop2-devel
BuildRequires:  pango-devel
BuildRequires:  libgail-devel
BuildRequires:  libxklavier-devel
BuildRequires:  gstreamer-devel
BuildRequires:  gst-plugins-devel
BuildRequires:  gst-plugins-devel
BuildRequires:  libmatecomponentui-devel
BuildRequires:  libmatewnck-devel
BuildRequires:  mate-desktop-devel
BuildRequires:  mate-utils
BuildRequires:  libmatenotify-devel
BuildRequires:  python-module-pygobject-devel
BuildRequires:  python-module-pygtk-devel
BuildRequires:  python-module-mate-devel
BuildRequires:  mate-charmap-devel
BuildRequires:  libdbus-devel
BuildRequires:  libdbus-glib-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  mate-doc-utils
BuildRequires:  which
BuildRequires:  libtool autoconf gettext intltool
BuildRequires:  mate-icon-theme-devel
BuildRequires:  libmatekbd-devel
BuildRequires:  xsltproc libxslt
BuildRequires:  mate-polkit-devel
BuildRequires:  libmateweather-devel
BuildRequires:  mate-common
BuildRequires:  xorg-utils
BuildRequires:  scrollkeeper
BuildRequires:  libupower-devel

Requires:		mate-panel
Requires:		libxklavier
Requires:		gst-plugins-base
Requires:		gst-plugins-good
Requires:		dbus
#Requires:		python-module-mate-applet
#Requires:		python-module-mate-mateconf

Patch33: gnome-applets-2.3.5-alt-geyes_schema.patch
Patch34: gnome-applets-2.6.0-alt-install_makefile.patch
Patch35: gnome-applets-2.9.90-alt-modemlights.patch

# since we are installing .pc files

%description
The mate-applets package contains small applications which generally
run in the background and display their output to the MATE  panel.
It includes a clock, a character palette, load monitors, little toys,
and more.

%prep
%setup -q
#patch0 -p1 -b .mate-applets_mcharmap
#patch1 -p1 -b .pymod

NOCONFIGURE=1 ./autogen.sh
#patch33 -p1
%patch34 -p1
%patch35 -p1

%build
export PKG_CONFIG_PATH="/usr/lib64/pkmateconfig"

%configure \
	--disable-scrollkeeper    \
	--disable-static          \
	--enable-polkit \
	--enable-ipv6 \
%if_disabled timer_applet
	--disable-timer-applet
%endif

#	--disable-cpufreq \


# drop unneeded direct library deps with --as-needed
# libtool doesn't make this easy, so we do it the hard way
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' -e 's/    if test "$export_dynamic" = yes && test -n "$export_dynamic_flag_spec"; then/      func_append compile_command " -Wl,-O1,--as-needed"\n      func_append finalize_command " -Wl,-O1,--as-needed"\n\0/' libtool

xvfb-run -a make

%install
export MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
unset MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

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

%find_lang %{po_package} --all-name

# Clean up unpackaged files
rm -rf $RPM_BUILD_ROOT%{_var}/scrollkeeper

# drop non-XKB support files
rm -rf $RPM_BUILD_ROOT%{_datadir}/xmodmap
# alt 01-cpufreq.pkla
install -pD -m 644 %SOURCE0 %buildroot%_sysconfdir/polkit-1/localauthority/50-local.d/01-cpufreq.pkla


%files -f %{po_package}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/mate-invest-chart
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/16x16/apps/*
%{_datadir}/icons/hicolor/22x22/apps/*
%{_datadir}/icons/hicolor/24x24/apps/*
%{_datadir}/icons/hicolor/32x32/apps/*
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/icons/mate/*
%{_datadir}/mate-2.0/ui/*
%{_datadir}/mate-applets
%{_libexecdir}/accessx-status-applet
%{_libexecdir}/charpick_applet2
%{_libexecdir}/drivemount_applet2
%{_libexecdir}/geyes_applet2
%{_libexecdir}/mateweather-applet-2
%{_libexecdir}/multiload-applet-2
#%{_libexecdir}/null_applet
%{_libexecdir}/battstat-applet-2
#%{_libexecdir}/mixer_applet2
%{_libexecdir}/stickynotes_applet
%{_libexecdir}/trashapplet
%{_libexecdir}/invest-applet
%{_sysconfdir}/sound/events/mate-battstat_applet.soundlist
%{_datadir}/dbus-1/services/*
%{_datadir}/mate-panel/applets/*
%{_datadir}/mate/help/*
%{_datadir}/omf/*
%{python_sitelibdir_noarch}/mate_invest/
%if_enabled timer_applet
%{python_sitelibdir_noarch}/timerapplet/
%{_libexecdir}/timer-applet
%{_libdir}/matecomponent/servers/*
%endif
%_sysconfdir/polkit-1/localauthority/50-local.d/01-cpufreq.pkla
%{_datadir}/polkit-1/actions/org.mate.cpufreqselector.policy
%_sysconfdir/dbus-1/system.d/org.mate.CPUFreqSelector.conf
%_bindir/mate-cpufreq-selector
%{_libexecdir}/cpufreq-applet
%{_datadir}/MateConf/gsettings/stickynotes-applet.convert
%{_datadir}/dbus-1/system-services/org.mate.CPUFreqSelector.service
#%{_sysconfdir}/mateconf/schemas/*
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.battstat.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.charpick.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.cpufreq.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.geyes.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.multiload.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.stickynotes.gschema.xml

%changelog
* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1
- new version

* Mon Nov 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1.1.1
- fixed build

* Fri Oct 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Tue Aug 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

