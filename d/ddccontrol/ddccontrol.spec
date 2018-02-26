%def_with beesu
%def_without applet
%def_disable static
%def_enable doc
%define dbreleasedate 20100212svn
%define ddcreleasedate 20101010

Name: ddccontrol
Version: 0.4.2
Release: alt13.git%ddcreleasedate

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Control your monitor by software using the DDC/CI protocol
License: GPLv2+
Group: System/Configuration/Hardware

URL: http://ddccontrol.sourceforge.net/
Source0: http://dl.sf.net/ddccontrol/ddccontrol-%version.tar
Source1: http://dl.sf.net/ddccontrol/ddccontrol-db-%dbreleasedate.tar
Patch1: ddccontrol-0.3-fixasneeded.patch
Patch2: ddccontrol-0.4.2-desktop-alt11.patch
Patch3: ddccontrol-0.4.2-alt-buffer-overflow.patch

# Automatically added by buildreq on Thu Oct 21 2010
BuildRequires: intltool libICE-devel libpci-devel libxml2-devel libgtk+2-devel
%if_with applet
BuildRequires: libgnome-panel-devel libgtk+3-devel
%endif
%if_enabled doc
BuildRequires: xsltproc docbook-style-xsl tidy
%endif


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
%setup -a 1
#patch1 -p1
%patch2 -p1
%patch3 -p1

%build
pushd ddccontrol-db
# explicitly instruct gettextize to be non-interactive:
subst 's/gettextize/gettextize --quiet/' autogen.sh
touch config.rpath
./autogen.sh
%configure
popd

#autoreconf
touch config.rpath
./autogen.sh
%configure %{subst_enable static} %{subst_enable doc}
# safety belts :)
echo "#define HAVE_BUGGY_I2C_DEV 1" >>src/config.h
%make_build

%install
pushd ddccontrol-db
%makeinstall_std
popd
%makeinstall_std

rm -rf %buildroot%_datadir/doc/%name

%if_with beesu
sed -i -e s,xdg-su,beesu, %buildroot/%_desktopdir/*.desktop
%endif

%find_lang %name
%find_lang --append --output=%name.lang %name-db

%files -f %name.lang
%doc AUTHORS NEWS doc/html
%_bindir/ddccontrol
%_bindir/ddcpci
%_datadir/ddccontrol-db
%_man1dir/%{name}*

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

%if_with applet
%files applet
%dir %_libdir/ddccontrol
%_libdir/ddccontrol/ddcc-applet
%_datadir/ddccontrol
%_libdir/bonobo/servers/*
%endif

%changelog
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
