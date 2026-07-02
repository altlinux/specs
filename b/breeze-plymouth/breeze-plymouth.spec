%define rname breeze-plymouth

Name: %rname
Version: 6.7.2
Release: alt1
%K6init no_altplace

Group: Graphical desktop/KDE
Summary: Plymouth splash theme
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar
Source10: alt.logo.16.png
Source11: alt.logo.32.png
Patch1: alt-font-patch.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules gcc-c++ glibc-devel
BuildRequires:  plymouth-devel

%description
Plymouth splash Breeze themes for KDE Plasma.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
#Requires: kf6-filesystem
Provides: plasma5-breeze-plymouth-common = %EVR
Obsoletes: plasma5-breeze-plymouth-common < %EVR
%description common
%name common package

%package -n plymouth-plugin-breeze-text
Group: System/Base
Summary: Plymouth breeze-text plugin
Requires: %name-common
%description -n plymouth-plugin-breeze-text
Plymouth breeze-text plugin.

%package -n plymouth-theme-breeze-text
Group: System/Base
Summary: Plymouth breeze-text theme
Requires: %name-common
Requires: plymouth-plugin-breeze-text
%description -n plymouth-theme-breeze-text
Plymouth breeze-text theme.

%package -n plymouth-theme-breeze
Group: System/Base
Summary: Plymouth breeze theme
Requires: %name-common
Requires: plymouth-plugin-script
Requires: plymouth-plugin-label
%description -n plymouth-theme-breeze
Plymouth breeze theme.

%prep
%setup -n %rname-%version
%patch1 -p1
cat breeze/images/16bit/plasma.logo.png >breeze/images/16bit/os.logo.png
#cat %SOURCE10 >breeze/images/16bit/os.logo.png
cat %SOURCE11 >breeze/images/os.logo.png

%build
%K6build \
    -DDISTRO_NAME='ALT' \
    -DDISTRO_VERSION='LINUX' \
    -DDISTRO_LOGO='os' \
    -DBACKGROUND_TOP_COLOR='black' \
    -DBACKGROUND_BOTTOM_COLOR='black' \
    #

%install
%K6install

%files common
%doc LICENSES/*

%files -n plymouth-plugin-breeze-text
%_libdir/plymouth/breeze-text.so

%files -n plymouth-theme-breeze-text
/usr/share/plymouth/themes/breeze-text/

%files -n plymouth-theme-breeze
/usr/share/plymouth/themes/breeze/


%changelog
* Wed Jul 01 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Jun 29 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.1-alt1
- new version

* Tue May 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt1
- new version

* Thu Apr 09 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.4-alt1
- new version

* Mon Mar 30 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.3-alt1
- new version

* Wed Mar 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.6-alt1
- new version

* Thu Jan 15 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.5-alt1
- new version

* Wed Dec 10 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.4-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.3-alt1
- new version

* Thu Nov 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.2-alt1
- new version

* Wed Nov 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.6-alt1
- new version

* Tue Sep 16 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.5-alt1
- new version

* Fri Aug 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.4-alt1
- new version

* Tue Jul 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt1
- new version

* Tue Jul 08 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed May 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.5-alt1
- new version

* Wed Apr 02 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.4-alt1
- new version

* Wed Mar 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.3-alt1
- new version

* Wed Feb 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.2-alt1
- new version

* Wed Feb 19 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.1-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Thu Jan 09 2025 Sergey V Turchin <zerg@altlinux.org> 6.2.5-alt1
- new version

* Tue Nov 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Wed Nov 06 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.3-alt1
- new version

* Mon Oct 28 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

