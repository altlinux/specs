%define rname breeze-plymouth

Name: %rname
Version: 6.1.2
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
* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

