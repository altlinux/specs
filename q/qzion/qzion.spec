Name: qzion
Version: 0.4.0
Release: alt6.1
%setup_python_module %name

Group: Development/KDE and QT
Summary: QZion is an canvas abstraction used by and made for QEdje
Url: http://dev.openbossa.org/trac/qedje/
License: GPLv3
Packager: Sergey V Turchin <zerg@altlinux.org>

Source: %name-%version.tar

Patch1: qzion-0.4.0-alt-libdir-install.patch
# MDK
Patch10: qzion-0.4.0-gcc44.patch
Patch11: qzion-0.4.0-fix-install.patch


# Automatically added by buildreq on Fri Apr 24 2009 (-bi)
#BuildRequires: cmake gcc-c++ glib2-devel glibc-devel-static libXfixes-devel libqt3-devel phonon-devel python-module-PyQt4-devel python-module-sip-devel rpm-build-ruby
BuildRequires(pre): libqt4-devel
BuildRequires: cmake gcc-c++ kde-common-devel glibc-devel python-module-PyQt4-devel python-module-sip-devel

%description
QZion is an canvas abstraction used by and made for QEdje

%package -n lib%{name}
Summary: Qzionlibrary
Group: System/Libraries
Requires: libqt4-core >= %{get_version libqt4-core}
%description -n lib%{name}
Qzion library.

%package -n lib%{name}-devel
Summary: Devel stuff for kdebase 4
Group: Development/KDE and QT
Requires: lib%{name} = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel < %version-%release
%description -n lib%{name}-devel
Devel packages needed to build QZion apps

%package -n python-module-qzion
Summary: Qzion python bindings
Group: Development/KDE and QT
Requires: python-module-PyQt4
Requires: lib%{name} = %version-%release
%description -n python-module-qzion
QZion python bindings.


%prep
%setup -q
%patch1 -p1
%patch10 -p1
%patch11 -p0

%build
%define _K4buildtype Release
%Kbuild

%install
%Kinstall


%files -n lib%{name}
%_libdir/libqzion.so.*

%files -n lib%{name}-devel
%_includedir/*.h
%_pkgconfigdir/qzion.pc
%_libdir/libqzion.so

%files -n python-module-qzion
%python_sitelibdir/%name/
%python_sitelibdir/%name/*
%_datadir/sip/%name/


%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.0-alt6.1
- Rebuild with Python-2.7

* Thu Apr 21 2011 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt6
- fix build requires

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt5
- fix to build

* Tue Jan 18 2011 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt4
- rebuilt

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt2.M51.1
- build for M51

* Tue Apr 20 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt3
- rebuilt with Release buildtype

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt2.1
- Rebuilt with python 2.6

* Mon Aug 10 2009 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt2
- fix compile with gcc-4.4

* Fri Apr 24 2009 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- 0.4.0 release
- build python module

* Thu Jan 15 2009 Sergey V Turchin <zerg at altlinux dot org> 0.4.0-alt0.20081023
- initial specfile

