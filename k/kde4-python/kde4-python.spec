%add_findpackage_path %_kde4_bindir

%define rname pykde4
Name: kde4-python
Version: 4.8.0
Release: alt5

Group: Development/KDE and QT
Summary: Python bindings for KDE4
Url: http://developer.kde.org/language-bindings/
License: LGPLv2+

Source: %rname-%version.tar
# Debian
Patch10: make_pykde4_respect_sip_flags.diff
# ALT
Patch100: pykde4-4.8.0-alt-mobile.patch

# Automatically added by buildreq on Thu Sep 15 2011 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs kde4libs-devel kde4pimlibs libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-script libqt4-sql libqt4-svg libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base python-devel python-module-PyQt4 python-module-sip python-modules rpm-build-gir ruby shared-desktop-ontologies-devel soprano-backend-redland soprano-backend-virtuoso xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: boost-devel-headers gcc-c++ glib2-devel kde4pimlibs-devel libqt3-devel python-module-PyQt4-devel python-module-sip-devel rpm-build-ruby soprano zlib-devel-static
BuildRequires(pre): kde4libs-devel python-module-PyQt4-devel >= 4.8.2 python-module-sip-devel >= 4.12 rpm-build-python
BuildRequires: boost-devel gcc-c++ glib2-devel kde4pimlibs-devel libqt4-devel zlib-devel
BuildRequires: libsoprano-devel soprano soprano-backend-redland
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
%ifarch arm
%patch10 -p1
%patch100 -p1
%endif

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
%_bindir/pykdeuic4
%python_sitelibdir/PyQt4/uic/pykdeuic4.py*
#%_docdir/pykde4/examples/
%_datadir/sip/PyKDE4/


%changelog
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
