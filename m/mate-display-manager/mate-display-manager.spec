# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/mateconftool-2 gcc-c++ libICE-devel libXdmcp-devel libXext-devel libXi-devel libXinerama-devel libattr-devel libaudit-devel libbsd-devel libselinux-devel libwrap-devel pkgconfig(check) pkgconfig(fontconfig) pkgconfig(gio-2.0) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(libcanberra-gtk) pkgconfig(upower-glib) pkgconfig(x11) pkgconfig(xau)
# END SourceDeps(oneline)
Group: Graphical desktop/MATE

%define _libexecdir %_prefix/libexec
%define _localstatedir %_var

BuildRequires: xorg-xineramaproto-devel libXevie-devel
BuildRequires: intltool
%define _libexecdir %_prefix/libexec
BuildRequires(pre): rpm-macros-mate-conf
%define fedora 18
Name:		mate-display-manager	
Version:	1.4.0
Release:	alt5
Summary:	Displays login screen for MATE Desktop
License:	LPLv2+ and GPLv2+ 
URL:		http://mate-desktop.org
Source0:	http://vicodan.fedorapeople.org/mate-display-manager-1.4.0.tar

%if %{fedora} >= 18
BuildRequires:	libnm-gtk-devel
%else
BuildRequires:	NetworkManager-gtk-devel
%endif
BuildRequires:	libdbus-glib-devel mate-doc-utils mate-conf-devel mate-corba-devel libSM-devel libcanberra-devel libmatecomponentui-devel icon-naming-utils mate-conf-gtk mate-conf mate-panel-devel libmatecomponent-devel mate-common libmate-devel mate-panel-devel pam-devel libxklavier-devel popt-devel
Requires:	mate-conf mate-desktop mate-corba mate-session-manager mate-control-center mate-settings-daemon
Requires(pre):	mate-conf
Requires(post):	mate-conf
Requires(preun):	mate-conf
Source44: import.info
Source45: mdm_xdmcp.control
Source46: mdm.wms-method
Source47: mateconf-tree.xml
Patch33: mdm-snapshot.patch
Patch34: mdm-alt-fix-build.patch
Patch35: mdm-alt-Xsession.patch
Patch36: mdm-alt-pam.patch
Patch37: mdm-alt-polkit.patch
Patch38: mdm-alt-settings.patch
Patch39: mdm-alt-disable-a11y-default.patch
Patch40: mdm-alt-Init.patch
Patch41: mdm-alt-focus.patch
Patch42: mdm-alt-ru-cancel.patch
Patch43: mdm-alt-iso-codes-prefix.patch
Patch44: mdm-alt-sessions.patch

%description
Displays login screen for MATE Desktop

%prep
%setup -q
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p2


%build
#automake
autoconf
autoreconf -i --force
mate-doc-prepare --force --copy
aclocal
intltoolize --automake --copy --force
automake --add-missing
%configure --disable-static --disable-scrollkeeper --disable-schemas-install --disable-nls
%make_build V=1


%install
export MATECONF_DISABLE_MAKE_FILE_SCHEMA INSTALL=1
make LIBTOOL="/usr/bin/libtool" DESTDIR=%{buildroot} install
make install DESTDIR=%{buildroot}

mkdir -p %buildroot%_sysconfdir/X11/sessions
mkdir -p %buildroot%_sysconfdir/X11/wms-methods.d

# install external hook for update_wms
install -m755 %SOURCE46 %buildroot%_sysconfdir/X11/wms-methods.d/%name

mkdir -p %buildroot%_var/lib/mdm/.mateconf.defaults
install -m644 %SOURCE47 %buildroot%_var/lib/mdm/.mateconf.defaults/%%mateconf-tree.xml

find %buildroot -name '*.a' -delete
find %buildroot -name '*.la' -delete

# control mdm/xdmcp
install -pDm755 %SOURCE45 %buildroot%_controldir/mdm_xdmcp



%pre
%mateconf_schema_prepare mdm-simple-greeter

/usr/sbin/groupadd -r -f mdm
/usr/sbin/useradd -r -g mdm -d /var/lib/mdm -s /dev/null -n mdm >/dev/null 2>&1 ||:
%pre_control mdm_xdmcp

%post
%mateconf_schema_upgrade mdm-simple-greeter
%post_control -s disabled mdm_xdmcp

%preun
%mateconf_schema_remove mdm-simple-greeter

%files
%doc AUTHORS COPYING README
%{_bindir}/mdmflexiserver
%{_bindir}/mdm-screenshot
%{_sysconfdir}/pam.d/mdm*
%{_sysconfdir}/mdm
%{_sysconfdir}/dbus-1/system.d/mdm.conf
%{_sysconfdir}/mateconf/schemas/mdm-simple-greeter.schemas
%{_datadir}/omf/mdm
%{_datadir}/mdm
%{_sbindir}/mdm
%{_sbindir}/mdm-binary
%{_libexecdir}/mdm-*
%{_datadir}/mate/help/mdm
%{_datadir}/pixmaps/faces/*
%{_datadir}/pixmaps/*.png
%{_datadir}/mate-2.0/ui/MATE_FastUserSwitchApplet.xml
%{_datadir}/locale/*/*/mdm*
%{_datadir}/icons/hicolor/*/*/*
%{_libdir}/matecomponent/servers/MATE_FastUserSwitchApplet.server
#%{_sharedstatedir}/mdm
# alt specific
%dir %_sysconfdir/X11/sessions
%config %_controldir/mdm_xdmcp
%_sysconfdir/X11/wms-methods.d/%name
# tail from gdm alt spec
%dir %_localstatedir/log/mdm
%attr(775, mdm, mdm) %dir %_localstatedir/cache/mdm
## %attr(775, root, mdm) %dir %_localstatedir/spool/mdm
%attr(1770, root, mdm) %dir %_localstatedir/lib/mdm
%attr(1750, root, mdm) %dir %_localstatedir/lib/mdm/.mateconf.mandatory
%attr(1640, root, mdm) %_localstatedir/lib/mdm/.mateconf.mandatory/*.xml
%attr(1750, root, mdm) %dir %_localstatedir/lib/mdm/.mateconf.defaults
%attr(1640, root, mdm) %_localstatedir/lib/mdm/.mateconf.defaults/*.xml
%attr(1640, root, mdm) %_localstatedir/lib/mdm/.mateconf.path
##%attr(1750, mdm, mdm) %dir %_localstatedir/lib/mdm/.local
##%attr(1750, mdm, mdm) %dir %_localstatedir/lib/mdm/.local/share
##%attr(1750, mdm, mdm) %dir %_localstatedir/lib/mdm/.local/share/applications
##%attr(1640, mdm, mdm) %_localstatedir/lib/mdm/.local/share/applications/*
%attr(1777, root, mdm) %dir %_localstatedir/run/mdm


%changelog
* Thu Nov 15 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt5
- sessions search in /usr/share/xsessions disabled

* Wed Nov 14 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt4
- login fixed

* Thu Nov 01 2012 Led <led@altlinux.ru> 1.4.0-alt3
- fixed mdm's home dir permissions (ALT#27912)

* Thu Oct 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.2
- mate-control-center-filesystem dependence temporary removed

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Fri Oct 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- fixed bug in control

* Sun Oct 14 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- new version

