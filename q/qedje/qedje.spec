
Name: qedje
Version: 0.4.0
Release: alt5

Group: Development/KDE and QT
Summary: QEdje - Declarative language
Url: http://dev.openbossa.org/trac/qedje/
License: GPLv3

Source: %name-%version.tar
# MDV
Patch1: qedje-0.4.0-fix-install.patch

BuildRequires(pre): libqzion-devel
BuildRequires: cmake gcc-c++ libeet-devel libeina-devel libqt4-devel libqzion-devel kde-common-devel

%description
Edje is a declarative language that simplifies the development of
complex interfaces separating the UI design from the application
logic, by providing animations, layouts and simple scripts in a
very small memory footprint

%package -n lib%name
Summary: qedje library
Group: System/Libraries
Requires: %{get_dep libqzion}
%description -n lib%name
qedje library

%package -n lib%name-devel
Summary: Devel stuff for qedje
Group: Development/KDE and QT
Requires: lib%name = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel < %version-%release
%description -n lib%name-devel
Devel packages needed to build qedje apps


%prep
%setup -q
%patch1 -p1

%build
%define _K4buildtype Release
%Kbuild -DBUILD_TOOLS=TRUE

%install
%Kinstall

%files
%_bindir/qedje_viewer

%files -n lib%name
%_libdir/libqedje.so.*

%files -n lib%name-devel
%_includedir/*.h
%_pkgconfigdir/qedje.pc
%_libdir/libqedje.so

%changelog
* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt5
- fix to build

* Tue Jan 18 2011 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt4
- rebuilt

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt2.M51.1
- build for M51

* Tue Apr 20 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt3
- fix to build

* Mon Aug 10 2009 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt2
- rebuilt

* Fri Apr 24 2009 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- 0.4.0 final

* Thu Jan 15 2009 Sergey V Turchin <zerg at altlinux dot org> 0.4.0-alt0.20081023
- initial specfile

