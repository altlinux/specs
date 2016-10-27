%define tIF_ver_gt() %if "%(rpmvercmp '%1' '%2')" == "1"
%define tIF_ver_gteq() %if "%(rpmvercmp '%1' '%2')" != "-1"
%define tIF_ver_lt() %if "%(rpmvercmp '%2' '%1')" == "1"
%define tIF_ver_lteq() %if "%(rpmvercmp '%2' '%1')" != "-1"

Name: tqtinterface
Version: 3.5.13.2
Release: alt2

Group: System/Libraries
Summary: Interface and abstraction library for Qt and Trinity
Url: http://trinity.pearsoncomputing.net/
License: GPLv2

Source: %name-%version.tar
Patch1: 3.5.13-alt-paths.patch

# Automatically added by buildreq on Mon Nov 29 2010 (-bi)
#BuildRequires: cmake gcc-c++ libXScrnSaver-devel libXau-devel libXcomposite-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libtqt-devel libxkbfile-devel
BuildRequires: cmake gcc-c++ libqt3-devel kde-common-devel

%description
Interface and abstraction library for Qt and Trinity

%package -n libtqt
Group: System/Libraries
Summary: Abstraction library for Qt and Trinity
%description -n libtqt
Abstraction library for Qt and Trinity

%package -n libtqt-devel
Group: Development/C++
Summary: Development files for libtqt
Requires: libqt3-devel
%description -n libtqt-devel
Interface for Qt and Trinity


%prep
%setup -q -n %name-%version
%patch1

%build
%Kbuild \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DQT_VERSION=3 \
    -DINCLUDE_INSTALL_DIR=%_includedir/%name \
    -DPKGCONFIG_INSTALL_DIR=%_pkgconfigdir

%install
%Kinstall

%files -n libtqt
%_libdir/libtqt.so.*
%_libdir/libtqassistantclient.so.*

%files -n libtqt-devel
%_bindir/*
%_libdir/libtqt.so
%_libdir/libtqassistantclient.so
%_includedir/%name
%_pkgconfigdir/*.pc

%changelog
* Thu Oct 27 2016 Igor Vlasenko <viy@altlinux.ru> 3.5.13.2-alt2
- NMU: fix for repocop altlinux-policy-shared-lib-contains-devel-so:
   Shared Lib package should not contain symlink
   /usr/lib64/libtqassistantclient.so but just
   /usr/lib64/libtqassistantclient.so.4.2.0

* Sun Jun 23 2013 Roman Savochenko <rom_as@altlinux.ru> 3.5.13.2-alt1
- Release TDE version 3.5.13.2

* Mon Oct 29 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13.1-alt2
- Build with -O2 and -g.

* Sun Oct 14 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13.1-alt1
- Release TDE version 3.5.13.1

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt1
- Release TDE version 3.5.13

* Mon Nov 28 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt4
- rebuilt

* Wed Apr 20 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt3
- fix build requires

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt2
- fix to build

* Mon Oct 25 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt1
- initial build
