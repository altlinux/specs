%def_enable recommends_geomview
Name: dstool_tk
Version: 0.2003
Release: alt7
Summary: DSTool - a dynamical systems toolkit
License: GPL-like
Group: Sciences/Mathematics
Url: http://www.geom.uiuc.edu/software/dstool

#Source: http://www.cam.cornell.edu/~gucken/dstool/Version_tk/%name.tar.gz
Source: http://www.enm.bris.ac.uk/staff/hinke/dss/ode/dstool_tk-redhat8.0.tar.gz
Source1: %{name}_16.xpm
Source2: %{name}_32.xpm
Source3: %{name}_48.xpm
Patch0: dstooltk_2.0-4-debian-dir.patch
Patch1: dstooltk_2.0-4-debian-misc.patch
Patch2: dstool_tk-redhat8.0-remove-hack-systimes.diff
Patch3: dstool_tk-debian-systimes.patch
# alt; x86_64 crush
Patch10: dstool_tk-alt-x86_64.patch

Requires: tcl tk
# it is very useful, but it is in orphaned
%if_enabled recommends_geomview
Requires: geomview
%endif

## A utomatically added by buildreq on Tue Mar 29 2005
#BuildRequires: xorg-x11-devel xorg-x11-utils tcl-devel tk-devel
# Automatically added by buildreq on Thu Mar 13 2008 (-bi)
BuildRequires: imake tk-devel

%description
DsTool - A Dynamical Systems Toolkit.
This software is very useful in the visual study of nonlinear systems and Chaos, as well as finding numerical solutions to differential equations. It has the ability to plot flows and maps in both 2D & 3D phase space (for 3D install Geomview @ http://www.geomview.com). One can also define Poincare surfaces & plot bifurcation diagrams. A number of prebuilt models are included for study - e.g. Lorenz System.


%prep
#setup -q -c -n %name
%setup -q -n %name
%patch0 -p1
# patch don't work; it seems that patch3 is useless too
#%patch2 -p1
%patch3 -p1

%patch10 -p1

%build
DSTOOL=$PWD
ARCH=linux
export ARCH DSTOOL
#make World
make depend
make all

%install
mkdir -p $RPM_BUILD_ROOT%_libdir/%name/src
%__cp -r oogl help site_specific tcl bin $RPM_BUILD_ROOT%_libdir/%name/

### see README for details; it claims to require them
%__cp -r src/models $RPM_BUILD_ROOT%_libdir/%name/src
mkdir -p $RPM_BUILD_ROOT%_bindir
%__install -m 755 bin/dstool_tk $RPM_BUILD_ROOT%_bindir/
%__sed -e 's!/u/pkg/dstool_tk}!%_libdir/%name} ${ARCH=linux} ${GEOMVIEW=/usr/bin/geomview}!' bin/dstool_tk > $RPM_BUILD_ROOT%_bindir/dstool_tk
%__install -m644 -D %SOURCE1 $RPM_BUILD_ROOT%_miconsdir/%{name}.xpm
%__install -m644 -D %SOURCE2 $RPM_BUILD_ROOT%_niconsdir/%{name}.xpm
%__install -m644 -D %SOURCE3 $RPM_BUILD_ROOT%_liconsdir/%{name}.xpm
%__install -m755 -d $RPM_BUILD_ROOT%_desktopdir/

%__install -m644 -D debian/dstooltk.1 $RPM_BUILD_ROOT%_man1dir/%{name}.1

cat > $RPM_BUILD_ROOT%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=DS tool Tk
GenericName=DS tool (Tk version)
Comment=DS tool Tk - a dynamical system toolkit
Icon=%{name}
Exec=%{name}
Terminal=false
Categories=Science;Math;
EOF

%files
%doc README INSTALL VERSION changes
%_bindir/dstool_tk
%_libdir/%name
%_miconsdir/%{name}.xpm
%_niconsdir/%{name}.xpm
%_liconsdir/%{name}.xpm
%_desktopdir/%{name}.desktop
%_man1dir/dstool*

%changelog
* Sun Oct 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.2003-alt7
- x86_64 bugfixes

* Sat Mar 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.2003-alt6
- converted debian menu to freedesktop

* Mon Apr 06 2009 Igor Vlasenko <viy@altlinux.ru> 0.2003-alt5
- fixed pixmap locations

* Fri Dec 12 2008 Igor Vlasenko <viy@altlinux.ru> 0.2003-alt4
- disabled Requires: geomview until geomview will be resurrected

* Wed Nov 19 2008 Igor Vlasenko <viy@altlinux.ru> 0.2003-alt3.1
- NMU (by repocop): the following fixes applied:
 * update_menus for dstool_tk

* Thu Mar 13 2008 Igor Vlasenko <viy@altlinux.ru> 0.2003-alt3
- rebuild with new tk

* Sat Apr 22 2006 Igor Vlasenko <viy@altlinux.ru> 0.2003-alt2
- moved plugins from datadir to libdir

* Thu Feb 09 2006 Igor Vlasenko <viy@altlinux.ru> 0.2003-alt1
- new version, based on build of Hinke Osinga;
- fixed print bug;
- fixed geomview interaction bug

* Thu Jul 28 2005 Igor Vlasenko <viy@altlinux.org> 0.1998-alt0.5
- added require: tk

* Tue Mar 29 2005 Igor Vlasenko <viy@altlinux.ru> 0.1998-alt0.4
- first build for AltLinux
