# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/docbook2man /usr/bin/glib-genmarshal /usr/bin/mateconftool-2 /usr/bin/xmlto pkgconfig(dbus-1) pkgconfig(gdk-2.0) pkgconfig(gdk-x11-2.0) pkgconfig(gtk+-2.0) pkgconfig(libcanberra-gtk) pkgconfig(mate-keyring-1) pkgconfig(unique-3.0) pkgconfig(x11) pkgconfig(xext) pkgconfig(xproto) pkgconfig(xrandr) pkgconfig(xrender)
# END SourceDeps(oneline)
%filter_from_requires /^hal$/d
%define _libexecdir %_prefix/libexec
Summary: 	MATE power management service
Name: 		mate-power-manager
Version: 	1.4.0
Release: 	alt2_1.1
License: 	GPLv2+ and GFDL
Group: 		File tools
Source: 	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
URL: 		http://pub.mate-desktop.org

BuildRequires: mate-panel-devel >= 1.1.0
BuildRequires: scrollkeeper
BuildRequires: mate-doc-utils >= 1.0.0
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libtool
BuildRequires: libcairo-devel
BuildRequires: libcanberra-devel
BuildRequires: libmatenotify-devel >= 1.1.0
BuildRequires: libupower-devel >= 0.9.0
BuildRequires: intltool
BuildRequires: libunique-devel >= 1.0.0
BuildRequires: glib2-devel >= 2.25.9
BuildRequires: mate-conf-devel >= 1.1.0
BuildRequires: gtk2-devel >= 2.16.0
BuildRequires: libdbus-glib-devel
BuildRequires: mate-control-center-devel >= 1.1.0
BuildRequires: mate-common
BuildRequires: mate-keyring-devel

Patch0: dont-eat-the-logs.patch

BuildRequires: autoconf automake libtool

Requires: 		mate-icon-theme
Requires: 		libcanberra
Requires: 		dbus-tools-gui
Requires: 		upower >= 0.9.0
Requires(post): scrollkeeper
Requires(postun): scrollkeeper

%description
MATE Power Manager uses the information and facilities provided by UPower
displaying icons and handling user callbacks in an interactive MATE session.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh
%patch0 -p1 -b .logs

autoreconf -i -f


%build

%configure \
	--disable-static \
	--disable-scrollkeeper \
	--enable-applets

make AM_LDFLAGS="-Wl,-O1,--as-needed"

# strip unneeded translations from .mo files
# ideally intltool (ha!) would do that for us
# http://bugzilla.gnome.org/show_bug.cgi?id=474987
cd po
grep -v ".*[.]desktop[.]in[.]in$\|.*[.]server[.]in[.]in$" POTFILES.in > POTFILES.keep
mv POTFILES.keep POTFILES.in
intltool-update --pot
for p in *.po; do
  msgmerge $p %{name}.pot > $p.out
  msgfmt -o `basename $p .po`.gmo $p.out
done

%install
make install DESTDIR=$RPM_BUILD_ROOT

# save space by linking identical images in translated docs
helpdir=$RPM_BUILD_ROOT%{_datadir}/mate/help/%{name}
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

%find_lang %name --all-name

%post
export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
mateconftool-2 --makefile-install-rule \
        %{_sysconfdir}/mateconf/schemas/mate-power-manager.schemas >/dev/null || :

%pre
if [ "$1" -gt 1 ]; then
    export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
    mateconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/mateconf/schemas/mate-power-manager.schemas &> /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
    export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
    mateconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/mateconf/schemas/mate-power-manager.schemas &> /dev/null || :
fi

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/mate-power-manager.service
%{_datadir}/mate-power-manager/*.ui
%{_datadir}/mate-power-manager/icons/hicolor/*/*/*.*
%{_datadir}/icons/hicolor/*/apps/mate-brightness-applet.*
%{_datadir}/icons/hicolor/*/apps/mate-inhibit-applet.*
%{_datadir}/icons/hicolor/*/apps/mate-power-manager.*
%{_datadir}/icons/hicolor/*/apps/mate-power-statistics.*
%{_datadir}/omf/mate-power-manager
%{_datadir}/polkit-1/actions/org.mate.power.policy
%dir %{_datadir}/mate-power-manager
%config(noreplace) %{_sysconfdir}/mateconf/schemas/*.schemas
%{_mandir}/man1/*.1.*
%{_sbindir}/*
%{_sysconfdir}/xdg/autostart/*.desktop
%{_datadir}/mate/help/mate-power-manager/*
%{_libdir}/matecomponent/servers/MATE_BrightnessApplet.server
%{_libdir}/matecomponent/servers/MATE_InhibitApplet.server
%{_libexecdir}/mate-brightness-applet
%{_libexecdir}/mate-inhibit-applet
%{_datadir}/mate-2.0/ui/MATE_BrightnessApplet.xml
%{_datadir}/mate-2.0/ui/MATE_InhibitApplet.xml
%{_datadir}/mate-power-manager/icons


%changelog
* Thu Oct 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Tue Aug 14 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- get rid of hal dependency

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- 20120622 mate snapshot

