# libddccontrol_dbus_client use symbols from libddccontrol
%set_verify_elf_method unresolved=relaxed
%def_without beesu
# applet is not supported on Gnome 3
%def_disable applet
%def_disable static
%def_disable ddcpci
%ifarch x86_64 %ix86
%def_enable ddcpci
%endif

%def_enable doc
%define ddcreleasedate 20211005git8be298f

Name: ddccontrol
Version: 0.6.0
Release: alt1.%ddcreleasedate

Summary: Control your monitor by software using the DDC/CI protocol
License: GPLv2+
Group: System/Configuration/Hardware

URL: http://ddccontrol.sourceforge.net/
Vcs: git://github.com/ddccontrol/ddccontrol
Source0: ddccontrol-%version.tar
Source1: %{name}-modules-autoload.conf
Patch2: ddccontrol-0.4.2-desktop-alt11.patch
Patch3: ddccontrol-0.4.4-alt-fix-linkage.patch
Patch5: ddccontrol-0.4.2-russian.patch

BuildRequires: intltool libICE-devel libpci-devel libxml2-devel libgtk+2-devel libsystemd-devel
%if_enabled applet
BuildRequires: libgnome-panel-devel libgtk+3-devel
%endif
%if_enabled doc
BuildRequires: xsltproc docbook-style-xsl tidy
%endif

Requires: ddccontrol-db
Requires: lib%{name} = %version-%release
# gddccontrol .destkop
%if_with beesu
Requires: beesu
%else
Requires: xdg-utils
%endif

%description
DDCcontrol is a program used to control monitor parameters, like brightness and
contrast, by software, i.e. without using the OSD (On Screen Display) and the
buttons in front of the monitor.

%package -n lib%{name}
Summary: Libddccontrol library 
Group: Development/Other

%description -n lib%{name}
DDCcontrol is a program used to control monitor parameters, like brightness and
contrast, by software, i.e. without using the OSD and the buttons in front of
the monitor.

%package -n lib%{name}-devel
Summary: Libddccontrol library headers and development libraries
Group: Development/Other
Requires: lib%{name} = %version-%release

%description -n lib%{name}-devel
libddccontrol devel files

%package -n gddccontrol
Summary: GUI for controlling your monitor using the DDC/CI protocol
Group: System/Configuration/Hardware
Requires: %name = %version-%release

%description -n gddccontrol
DDCcontrol is a program used to control monitor parameters, like brightness and
contrast, by software, i.e. without using the OSD and the buttons in front of
the monitor.

gddccontrol is a GUI for ddccontrol.

%package applet
Summary: GNOME applet for ddccontrol
Group: Graphical desktop/GNOME
Requires: %name = %version-%release

%description applet
GNOME applet for ddccontrol.

%prep
%setup
%patch2 -p1
%patch3 -p1
%patch5 -p1

%build
touch config.rpath
./autogen.sh
%configure \
    %configure \
    %{subst_enable static} \
    %{subst_enable doc} \
    %{subst_enable ddcpci} \
    --disable-rpath \
%if_disabled applet
    --disable-gnome-applet
%endif

# safety belts :)
echo "#define HAVE_BUGGY_I2C_DEV 1" >>src/config.h
%make_build

%install
%makeinstall_std

rm -rf %buildroot%_datadir/doc/%name

%if_with beesu
sed -i -e s,xdg-su,beesu, %buildroot/%_desktopdir/*.desktop
%endif

# autoload i2c-dev module
install -m 644 -D %SOURCE1 %buildroot%_sysconfdir/modules-load.d/%name.conf

%find_lang %name

%post
# autoload i2c-dev module
/sbin/modprobe i2c-dev &>/dev/null || :

%files -f %name.lang
%doc AUTHORS NEWS
%if_enabled doc
%doc doc/html
%endif
%_bindir/ddccontrol
#%_bindir/ddcpci
%_man1dir/%{name}*
%_sysconfdir/modules-load.d/%name.conf
%if_enabled ddcpci
%_libexecdir/%name/ddcpci
%endif
%_unitdir/ddccontrol.service
%_libexecdir/%name/ddccontrol_service
%_datadir/dbus-1/interfaces/ddccontrol.DDCControl.xml
%_datadir/dbus-1/system-services/ddccontrol.DDCControl.service
%_sysconfdir/dbus-1/system.d/ddccontrol.DDCControl.conf

%files -n gddccontrol
%_bindir/gddccontrol
%_man1dir/g%{name}*
%_desktopdir/*
%_liconsdir/*
%_iconsdir/Bluecurve/48x48/apps/gddccontrol.png

%files -n lib%{name}
%_libdir/*.so.*

%files -n lib%{name}-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc



%if_enabled applet
%files applet
%dir %_libdir/ddccontrol
%_libdir/ddccontrol/ddcc-applet
%_datadir/ddccontrol
%_libdir/bonobo/servers/*
%endif

%changelog
* Wed Nov 03 2021 Igor Vlasenko <viy@altlinux.org> 0.6.0-alt1.20211005git8be298f
- new version

* Sun Aug 15 2021 Michael Shigorin <mike@altlinux.org> 0.4.4-alt2.20200630gitf3d003f
- fix doc knob

* Fri Dec 11 2020 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1.20200630gitf3d003f
- new version

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt17.20140603git9d89d8c
- updated from git

* Wed Dec 19 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt16.20120904gitc3af663d
- updated from git

* Wed Dec 19 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt15.git20101010
- ddccontrol-db is moved to separate package for independent update

* Wed Jul 18 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt14.git20101010
- added support for dell u3011 thanks to slava@ (closes: 27551)

* Sun Aug 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt13.git20101010
- fixed buffer overflow (closes: 26177)

* Fri Aug 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt12.git20101010
- beesu instead of xdg-su in the desktop file

* Tue Jun 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt11.git20101010
- upstream git commit 135d1bffb8ad1503a428ffae499bc50bd270d2f9 (20101010)
  - Added cs.po
  - Applied ddccontrol-selectable.patch
  - Applied ddccontrol-pc.patch
  - Applied ddccontrol-libexecdir.patch
  - Applied ddccontrol-icon.patch
  - Applied ddccontrol-distcheck.patch
  - Applied ddccontrol-desktop.patch
  - Add support for Intel Mobile 945GME Express Graphics Controller

* Tue Jun 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt10
- fixed build
- ddccontrol-db updated to 20100212svn

* Mon May 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt9.1
- build w/o gnome applet not to delay gnome3

* Thu Oct 21 2010 Victor Forsiuk <force@altlinux.org> 0.4.2-alt9
- Refresh BuildRequires.

* Thu Jun 24 2010 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt8
- xdg-su -c in .desktop

* Thu Jun 17 2010 Igor Vlasenko <viy@altlinux.org> 0.4.2-alt7
- desktop file now use xdg-su

* Thu Jun 17 2010 Igor Vlasenko <viy@altlinux.org> 0.4.2-alt6.1
- fixed build

* Wed Sep 16 2009 Victor Forsyuk <force@altlinux.org> 0.4.2-alt6
- Refresh db from upstream svn (thnx to viy@ for suggestion).

* Mon Jul 06 2009 Victor Forsyuk <force@altlinux.org> 0.4.2-alt5
- Fix FTBFS (add explicit libtoolize call).

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 0.4.2-alt4.3
- added Packager:

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 0.4.2-alt4.2
- NMU: applied repocop patch

* Wed Apr 23 2008 Michael Shigorin <mike@altlinux.org> 0.4.2-alt4.1
- NMU: rebuilt against libpci-3.0.0

* Fri Mar 28 2008 Victor Forsyuk <force@altlinux.org> 0.4.2-alt4
- Fix FTBFS with current autotools.

* Wed Dec 26 2007 Victor Forsyuk <force@altlinux.org> 0.4.2-alt3
- Fix FTBFS with current autotools.

* Mon Oct 23 2006 Victor Forsyuk <force@altlinux.org> 0.4.2-alt2
- Update monitor database.

* Wed Aug 30 2006 Victor Forsyuk <force@altlinux.ru> 0.4.2-alt1
- 0.4.2
- Add ddccontrol-applet package.

* Mon Mar 20 2006 Victor Forsyuk <force@altlinux.ru> 0.4.1-alt1
- 0.4.1
- Fixed build with linker flag --as-needed.
- Update BuildRequires.

* Tue Jan 17 2006 Victor Forsyuk <force@altlinux.ru> 0.3-alt2
- Fix spec to build in current Sisyphus environment.

* Thu Nov 17 2005 Victor Forsyuk <force@altlinux.ru> 0.3-alt1
- 0.3
- Update BuildRequires.

* Mon Aug 15 2005 Victor Forsyuk <force@altlinux.ru> 0.2-alt1
- 0.2

* Tue Jul 19 2005 Victor Forsyuk <force@altlinux.ru> 0.1.3-alt1
- 0.1.3

* Wed Jun 08 2005 Victor Forsyuk <force@altlinux.ru> 0.1.1-alt1
- Initial build.
