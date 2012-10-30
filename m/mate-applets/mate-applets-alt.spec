# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: /usr/bin/gdk-pixbuf-csource /usr/bin/glib-genmarshal /usr/bin/jw /usr/bin/mateconftool-2 /usr/bin/scrollkeeper-config /usr/bin/xsltproc libICE-devel libSM-devel libX11-devel libcpufreq-devel pkgconfig(NetworkManager) pkgconfig(gio-2.0) pkgconfig(gtk+-2.0) pkgconfig(gucharmap-2) pkgconfig(hal) pkgconfig(libgtop-2.0) pkgconfig(libxml-2.0) pkgconfig(mate-settings-daemon) pkgconfig(polkit-gobject-1) python-devel xorg-kbproto-devel
# END SourceDeps(oneline)
BuildRequires: xvfb-run
%define libmate_desktop_version 1.0
%define _libexecdir %_prefix/libexec
%define glib2_version 2.15.3
%define pango_version 1.2.0
%define gtk2_version 2.6.0
%define libmate_version 1.1.2
%define libmateui_version 1.1.2
%define libglade_version 2.4.0
%define mate_panel_version 1.1.0
%define libgtop2_version 2.12.0
%define gail_version 1.2.0
%define libmatecomponentui_version 1.1.0
%define gstreamer_version 0.10.14
%define gstreamer_plugins_version 0.10.14
%define gstreamer_plugins_good_version 0.10.6
%define libxklavier_version 4.0
%define libmatewnck_version 1.3.0
%define mate_desktop_version 1.1.0
%define mate_utils_version 1.1.0
%define dbus_version 0.90
%define dbus_glib_version 0.70
%define libmatenotify_version 1.1.0
%define pygobject_version 2.6
%define pygtk_version 2.6
%define python_mate_version 1.1.0
%define mate_conf_version 1.1.0
%define libmatekbd_version 1.1.0
%define mate_polkit_version 1.1.0

%define po_package mate-applets-2.0

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define build_stickynotes 0

Summary:        Small applications for the MATE panel
Name:			mate-applets
Version:		1.4.0
Release:        alt2_1.1
License:		GPLv2+ and GFDL
Group:          Graphical desktop/Other
URL:			http://pub.mate-desktop.org
Source: 		http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
Patch0:         mate-applets_mcharmap.patch
Patch1:         pymod-check.patch

BuildRequires:  glib2-devel >= %{glib2_version}
BuildRequires:  gtk2-devel >= %{gtk2_version}
BuildRequires:  libmateui-devel >= %{libmateui_version}
BuildRequires:  libmate-devel >= %{libmate_version}
BuildRequires:  mate-panel-devel >= %{mate_panel_version}
BuildRequires:  libglade2-devel >= %{libglade_version}
BuildRequires:  libgtop2-devel >= %{libgtop2_version}
BuildRequires:  pango-devel >= %{pango_version}
BuildRequires:  libgail-devel >= %{gail_version}
BuildRequires:  libxklavier-devel >= %{libxklavier_version}
BuildRequires:  gstreamer-devel >= %{gstreamer_version}
BuildRequires:  gst-plugins-devel >= %{gstreamer_plugins_version}
BuildRequires:  gst-plugins-devel >= %{gstreamer_plugins_good_version}
BuildRequires:  libmatecomponentui-devel >= %{libmatecomponentui_version}
BuildRequires:  libmatewnck-devel >= %{libmatewnck_version}
BuildRequires:  mate-desktop-devel >= %{libmate_desktop_version}
BuildRequires:  mate-utils >= %{mate_utils_version}
BuildRequires:  libmatenotify-devel >= %{libmatenotify_version}
BuildRequires:  python-module-pygobject-devel >= %{pygobject_version}
BuildRequires:  python-module-pygtk-devel >= %{pygtk_version}
BuildRequires:  python-module-mate-devel >= %{python_mate_version}
BuildRequires:  mate-charmap-devel
BuildRequires:  libdbus-devel >= %{dbus_version}
BuildRequires:  libdbus-glib-devel >= %{dbus_glib_version}
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  mate-doc-utils
BuildRequires:  which
BuildRequires:  libtool autoconf gettext intltool
BuildRequires:  mate-icon-theme
BuildRequires:  libmatekbd-devel >= %{libmatekbd_version}
BuildRequires:  xsltproc libxslt
BuildRequires:  mate-polkit-devel >= %{mate_polkit_version}
BuildRequires:  libmateweather-devel >= 1.1.0
BuildRequires:  mate-common
BuildRequires:  xorg-utils
BuildRequires:  scrollkeeper
BuildRequires:  libupower-devel

Requires:		mate-panel >= %{mate_panel_version}
Requires:		libxklavier >= %{libxklavier_version}
Requires:		gst-plugins-base >= %{gstreamer_plugins_version}
Requires:		gst-plugins-good >= %{gstreamer_plugins_good_version}
Requires:		dbus >= %{dbus_version}
Requires:		python-module-mate-applet
Requires:		python-module-mate-mateconf

Requires(pre): mate-conf >= %{mate_conf_version}
Requires(preun): mate-conf >= %{mate_conf_version}
Requires(post): mate-conf >= %{mate_conf_version}
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
%patch0 -p1 -b .mate-applets_mcharmap
%patch1 -p1 -b .pymod

NOCONFIGURE=1 ./autogen.sh
%patch33 -p1
%patch34 -p1
%patch35 -p1

%build
export PKG_CONFIG_PATH="/usr/lib64/pkmateconfig"

%configure \
	--disable-scrollkeeper    \
	--disable-static          \
	--enable-mixer-applet \
	--enable-polkit \
	--enable-ipv6 \
	--disable-cpufreq \
	--enable-timer-applet


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


%post
touch --no-create %{_datadir}/icons/mate

export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
mateconftool-2 --makefile-install-rule                                        \
	    %{_sysconfdir}/mateconf/schemas/battstat.schemas                  \
	    %{_sysconfdir}/mateconf/schemas/charpick.schemas                  \
	    %{_sysconfdir}/mateconf/schemas/drivemount.schemas                \
	    %{_sysconfdir}/mateconf/schemas/geyes.schemas                     \
	    %{_sysconfdir}/mateconf/schemas/mixer.schemas            \
	    %{_sysconfdir}/mateconf/schemas/timer-applet.schemas            \
%if %{build_stickynotes}
	    %{_sysconfdir}/mateconf/schemas/stickynotes.schemas               \
%endif
	    %{_sysconfdir}/mateconf/schemas/multiload.schemas \
		>& /dev/null || :

%pre
if [ "$1" -gt 1 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule                                    \
	    %{_sysconfdir}/mateconf/schemas/battstat.schemas                  \
	    %{_sysconfdir}/mateconf/schemas/charpick.schemas                  \
	    %{_sysconfdir}/mateconf/schemas/drivemount.schemas                \
	    %{_sysconfdir}/mateconf/schemas/geyes.schemas                     \
	    %{_sysconfdir}/mateconf/schemas/mixer.schemas            \
	    %{_sysconfdir}/mateconf/schemas/timer-applet.schemas            \
%if %{build_stickynotes}
	    %{_sysconfdir}/mateconf/schemas/stickynotes.schemas               \
%endif
	    %{_sysconfdir}/mateconf/schemas/multiload.schemas >& /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule                                    \
	    %{_sysconfdir}/mateconf/schemas/battstat.schemas                  \
	    %{_sysconfdir}/mateconf/schemas/charpick.schemas                  \
	    %{_sysconfdir}/mateconf/schemas/drivemount.schemas                \
	    %{_sysconfdir}/mateconf/schemas/geyes.schemas                     \
	    %{_sysconfdir}/mateconf/schemas/mixer.schemas            \
	    %{_sysconfdir}/mateconf/schemas/timer-applet.schemas            \
%if %{build_stickynotes}
	    %{_sysconfdir}/mateconf/schemas/stickynotes.schemas               \
%endif
	    %{_sysconfdir}/mateconf/schemas/multiload.schemas >& /dev/null || :
fi

%postun
touch --no-create %{_datadir}/icons/mate

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
%{_libdir}/matecomponent/servers/*
%{_libexecdir}/accessx-status-applet
%{_libexecdir}/charpick_applet2
%{_libexecdir}/drivemount_applet2
%{_libexecdir}/geyes_applet2
%{_libexecdir}/mateweather-applet-2
%{_libexecdir}/multiload-applet-2
%{_libexecdir}/null_applet
%{_libexecdir}/battstat-applet-2
%{_libexecdir}/mixer_applet2
%{_libexecdir}/stickynotes_applet
%{_libexecdir}/trashapplet
%{_libexecdir}/invest-applet
%{_sysconfdir}/mateconf/schemas/*
%{_sysconfdir}/sound/events/mate-battstat_applet.soundlist
%{_datadir}/dbus-1/services/*
%{_datadir}/mate-panel/applets/*
%{_datadir}/mate/help/*
%{_datadir}/omf/*
%{python_sitelibdir_noarch}/mate_invest/
%{python_sitelibdir_noarch}/timerapplet/
%{_libexecdir}/timer-applet
%_sysconfdir/polkit-1/localauthority/50-local.d/01-cpufreq.pkla

%changelog
* Fri Oct 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Tue Aug 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

