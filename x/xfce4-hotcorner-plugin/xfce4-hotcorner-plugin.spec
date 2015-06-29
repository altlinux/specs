Name: xfce4-hotcorner-plugin
Version: 0.0.1
Release: alt1

Summary: Hot corner plugin for Xfce4
License: %gpl2plus
Group: Graphical desktop/XFce
Url: https://github.com/brianhsu/xfce4-hotcorner-plugin
Packager: Xfce Team <xfce@packages.altlinux.org>

# https://github.com/brianhsu/xfce4-hotcorner-plugin.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools rpm-macros-cmake cmake
BuildPreReq: libxfce4panel-devel libxfce4ui-devel
BuildRequires: libwnck3-devel

Requires: xfce4-panel >= 4.11

%description
%name is a simple panel plugin, provide an easy way to set
hot corners on Xfce4 desktop environment.

%prep
%setup
%patch -p1
# Fix plugin's path
sed -i 's;lib/xfce4/panel/plugins/;%_lib/xfce4/panel/plugins/;' CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
%find_lang %name

%files -f %name.lang
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop

%changelog
* Mon Jun 29 2015 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1
- Initial build.
