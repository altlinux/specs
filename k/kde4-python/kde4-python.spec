
%add_findpackage_path %_kde4_bindir

%if_enabled kde_mobile
%def_disable desktop
%else
%def_enable desktop
%endif

%define rname pykde4
Name: kde4-python
Version: 4.14.3
Release: alt1

Group: Development/KDE and QT
Summary: Python bindings for KDE4
Url: http://developer.kde.org/language-bindings/
License: LGPLv2+

Source: %rname-%version.tar
# Debian
Patch10: make_pykde4_respect_sip_flags.diff
# FC
Patch20: pykde4-4.14.3-missing_symbols.patch
# ALT
Patch100: pykde4-4.8.0-alt-mobile.patch
Patch101: pykde4-4.10.1-alt-sip-install-dir.patch

# Automatically added by buildreq on Thu Sep 15 2011 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs kde4libs-devel kde4pimlibs libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-script libqt4-sql libqt4-svg libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base python-devel python-module-PyQt4 python-module-sip python-modules rpm-build-gir ruby shared-desktop-ontologies-devel soprano-backend-redland soprano-backend-virtuoso xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: boost-devel-headers gcc-c++ glib2-devel kde4pimlibs-devel libqt3-devel python-module-PyQt4-devel python-module-sip-devel rpm-build-ruby soprano zlib-devel-static
BuildRequires(pre): kde4libs-devel python-module-sip-devel >= 4.12 python-module-PyQt4-devel >= 4.9.5 rpm-build-python
BuildRequires: boost-devel gcc-c++ glib2-devel kde4pimlibs-devel libqt4-devel zlib-devel
#BuildRequires: libsoprano-devel soprano soprano-backend-redland
BuildRequires: python-devel
BuildRequires: libqscintilla2-qt4-devel

%description
Python bindings for KDE4

%package -n python-module-kde4
Summary: PyKDE4
Group: Development/Python
Requires: python-module-PyQt4 >= %{get_version python-module-PyQt4}
Requires: python-module-sip >= %{get_version python-module-sip}
Provides: PyKDE4 = %version-%release
%description -n python-module-kde4
Python KDE 4

%package devel
Group: Development/KDE and QT
Summary: Files needed to build PyKDE4-based applications
Requires: python-module-PyQt4-devel
Provides: python-module-kde4-doc = %version-%release
Obsoletes: python-module-kde4-doc < %version-%release
%description devel
Python bindings for KDE4


%prep
%setup -n %rname-%version
%patch10 -p1
%patch20 -p1
#
%if_enabled desktop
    %ifarch %arm
%patch100 -p1
    %endif
%else
%patch100 -p1
%endif
#
%patch101 -p1

%build
%K4cmake
%K4make

%install
%K4install


%files -n python-module-kde4
%dir %python_sitelibdir/PyKDE4
%python_sitelibdir/PyKDE4/*
%python_sitelibdir/PyQt4/uic/widget-plugins/*
%_K4apps/pykde4
%_K4lib/kpythonpluginfactory.so

%files devel
%_bindir/pykdeuic4*
%python_sitelibdir/PyQt4/uic/pykdeuic4.py*
#%_docdir/pykde4/examples/
%_datadir/sip/PyKDE4/


%changelog
* Mon Jan 18 2016 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt1
- fix to build

* Thu Oct 02 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt2
- apply patch for mobile builds

* Fri Aug 15 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Tue Jul 15 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.3-alt1
- new version

* Fri Jun 20 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt2
- fix to build with new sip

* Wed Apr 23 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- new version

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt0.M70P.1
- built for M70P

* Mon Feb 03 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt1
- new version

* Wed Dec 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt2
- rebuilt with new sip (ALT#29613)

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt0.M70P.1
- built for M70P

* Thu Oct 03 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt1
- new version

* Mon Sep 09 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Tue Jan 15 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.2
- update from 4.10 branch

* Tue Dec 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Tue Nov 13 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.3-alt1
- new version

* Thu Oct 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Fri Jun 15 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt5
- rebuilt with new soprano

* Fri Jun 08 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt4
- rebuilt with new soprano

* Wed May 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt3
- fix to build on arm

* Sat Apr 28 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt2
- fix to build on arm

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt0.M60P.1
- built for M60P

* Thu Jan 26 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60P.1
- built for M60P

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.7.1-alt1.1
- Rebuild with Python-2.7

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Thu Sep 15 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- initial build
