Name: dstool
Version: 2.0
# 2.0a
Release: alt5

Summary: DSTool - a dynamical systems toolkit (OpenWin version)
License: GPL-like
Group: Sciences/Mathematics
Url: http://www.geom.uiuc.edu/software/dstool

Packager: Igor Vlasenko <viy@altlinux.ru>
Source: %name-src.tar.bz2
Patch:  dstool-autoif-fix-overflow.patch

## Au tomatically added by buildreq on Tue Nov 22 2005
#BuildRequires: xorg-x11-devel xorg-x11-libs gcc-c++ libstdc++-devel libxview-devel tcl-devel
# Automatically added by buildreq on Thu Mar 13 2008 (-bi)
BuildRequires: gcc-c++ libXt-devel libtcl libxview-devel tcl-devel

# manually removed imake xorg-cf-files

%description
DsTool - a dynamical systems toolkit (OpenWin version).
It used for numeric finding of fixed points and periodic orbits,
visualisation of maps and vector fields such as Lorenz attractor.
It is recommended to install also a geomview package for 3D support.

%package devel
Summary: DSTool - a dynamical systems toolkit development files
Group: Development/C
Requires: %name = %version-%release

%description devel
DsTool - a dynamical systems toolkit (OpenWin version).
It used for numeric finding of fixed points and periodic orbits,
visualisation of maps and vector fields such as Lorenz attractor.

This package contans development files for DsTool.

%prep
%setup -q -n %name
%patch -p1

%build
%configure
# non-parallel :(
#make_build
make

%install
#make_install DESTDIR=%buildroot install
%makeinstall docdir=$RPM_BUILD_ROOT%_docdir

%__mkdir_p $RPM_BUILD_ROOT%_desktopdir
cat > $RPM_BUILD_ROOT%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=%{name}
GenericName=DS tool (OW)
Comment=dynamical systems toolkit
Icon=%{name}
Exec=%{name}
Terminal=false
Categories=Science;Math;
EOF

%files 
%doc %_docdir/%{name}
%_bindir/%{name}
%_datadir/%{name}
%_desktopdir/%{name}.desktop
#%_libdir/lib%{name}.a
%exclude %_libdir/lib%{name}.a

%files devel
%_includedir/%{name}

%changelog
* Tue Oct 18 2011 Igor Vlasenko <viy@altlinux.ru> 2.0-alt5
- added devel subpackage

* Sat Mar 26 2011 Igor Vlasenko <viy@altlinux.ru> 2.0-alt4
- converted debian menu to freedesktop

* Wed Nov 19 2008 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3.1
- NMU (by repocop): the following fixes applied:
 * update_menus for dstool

* Thu Mar 13 2008 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3
- rebuild with new tk
- fixed buffer overflow (thanks to ldv@)

* Tue Jun 20 2006 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2
- gcc4 build

* Thu Mar 16 2006 Igor Vlasenko <viy@altlinux.ru> 2.0-alt0.M30.2
- M30 backport

* Thu Feb 02 2006 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1.1
- removed dep on gcc-g77

* Tue Nov 22 2005 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1
- initial build
