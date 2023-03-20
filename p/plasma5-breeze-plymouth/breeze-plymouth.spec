%define rname breeze-plymouth

Name: plasma5-%{rname}
Version: 5.27.3
Release: alt1
%K5init no_altplace

Group: Graphical desktop/KDE
Summary: Plymouth splash theme
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar
Source10: alt.logo.16.png
Source11: alt.logo.32.png
Patch1: alt-font-patch.patch

# Automatically added by buildreq on Thu Sep 09 2021 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils glibc-kernheaders-generic glibc-kernheaders-x86 libctf-nobfd0 libsasl2-3 libstdc++-devel pkg-config python-modules python2-base python3 python3-base python3-module-paste rpm-build-file rpm-build-python3 rpm-macros-python sh4 tzdata
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ glibc-devel
BuildRequires:  plymouth-devel

%description
Plymouth splash Breeze themes for KDE Plasma.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
#Requires: kf5-filesystem
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
%K5build \
    -DDISTRO_NAME='ALT' \
    -DDISTRO_VERSION='LINUX' \
    -DDISTRO_LOGO='os' \
    -DBACKGROUND_TOP_COLOR='black' \
    -DBACKGROUND_BOTTOM_COLOR='black' \
    #

%install
%K5install

%files common
%doc LICENSES/*

%files -n plymouth-plugin-breeze-text
%_libdir/plymouth/breeze-text.so

%files -n plymouth-theme-breeze-text
/usr/share/plymouth/themes/breeze-text/

%files -n plymouth-theme-breeze
/usr/share/plymouth/themes/breeze/

%changelog
* Thu Mar 16 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.3-alt1
- new version

* Tue Feb 28 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.2-alt1
- new version

* Mon Jan 09 2023 Sergey V Turchin <zerg@altlinux.org> 5.26.5-alt1
- new version

* Tue Nov 29 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.4-alt1
- new version

* Tue Nov 08 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.3-alt1
- new version

* Thu Oct 27 2022 Sergey V Turchin <zerg@altlinux.org> 5.26.2-alt1
- new version

* Wed Sep 07 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.5-alt1
- new version

* Wed Aug 17 2022 Sergey V Turchin <zerg@altlinux.org> 5.25.4-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.6-alt1
- new version

* Wed May 04 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.5-alt1
- new version

* Wed Mar 30 2022 Sergey V Turchin <zerg@altlinux.org> 5.24.4-alt1
- new version

* Mon Jan 10 2022 Sergey V Turchin <zerg@altlinux.org> 5.23.5-alt1
- new version

* Wed Dec 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.4-alt1
- new version

* Wed Nov 10 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.3-alt1
- new version

* Mon Nov 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.23.2-alt1
- new version

* Thu Sep 16 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.5-alt4
- fix color

* Fri Sep 10 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.5-alt3
- fix color

* Thu Sep 09 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.5-alt2
- fix text font

* Wed Sep 08 2021 Sergey V Turchin <zerg@altlinux.org> 5.22.5-alt1
- new version
