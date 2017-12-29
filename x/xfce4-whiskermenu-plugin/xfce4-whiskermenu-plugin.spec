#define git_date .git20140106
%define git_date %nil

%define _unpackaged_files_terminate_build 1

Name: xfce4-whiskermenu-plugin
Version: 1.7.5
Release: alt1%git_date

Summary: Alternate Xfce menu
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://gottcode.org/xfce4-whiskermenu-plugin/
Packager: Xfce Team <xfce@packages.altlinux.org>

# git://github.com/gottcode/xfce4-whiskermenu-plugin.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools gcc-c++ rpm-macros-cmake cmake
BuildRequires: libxfce4panel-devel libxfce4ui-devel libxfce4util-devel
BuildRequires: libgarcon-devel libexo-devel
BuildRequires: libpixman-devel libXdmcp-devel libXdamage-devel libXxf86vm-devel
BuildRequires: libharfbuzz-devel libpng-devel libexpat-devel

Requires: xfce4-panel >= 4.8

%description
Whisker Menu is an alternate application launcher for Xfce. When you
open it you are shown a list of applications you have marked as
favorites. You can browse through all of your installed applications by
clicking on the category buttons on the side. Top level catagories make
browsing fast, and simple to switch between. Additionally, Whisker Menu
keeps a list of the last ten applications that you've launched from it.

%prep
%setup
%patch -p1

%build
%cmake -DLIB_INSTALL_DIR=%_libdir
%cmake_build

%install
%cmakeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/*
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop
%_iconsdir/hicolor/*/apps/*
%_man1dir/*.1.*

%changelog
* Fri Dec 29 2017 Mikhail Efremov <sem@altlinux.org> 1.7.5-alt1
- Updated to 1.7.5.

* Tue Nov 21 2017 Mikhail Efremov <sem@altlinux.org> 1.7.4-alt1
- Updated to 1.7.4.

* Mon Aug 07 2017 Mikhail Efremov <sem@altlinux.org> 1.7.3-alt1
- Updated to 1.7.3.

* Tue Apr 04 2017 Mikhail Efremov <sem@altlinux.org> 1.7.2-alt1
- Updated to 1.7.2.

* Wed Mar 01 2017 Mikhail Efremov <sem@altlinux.org> 1.7.1-alt1
- Updated to 1.7.1.

* Wed Feb 01 2017 Mikhail Efremov <sem@altlinux.org> 1.7.0-alt1
- Updated to 1.7.0.

* Tue Jan 24 2017 Mikhail Efremov <sem@altlinux.org> 1.6.2-alt1
- Updated to 1.6.2.

* Mon Oct 17 2016 Mikhail Efremov <sem@altlinux.org> 1.6.1-alt1
- Updated to 1.6.1.

* Tue Aug 23 2016 Mikhail Efremov <sem@altlinux.org> 1.6.0-alt1
- Updated to 1.6.0.

* Thu Apr 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.3-alt1
- Updated to 1.5.3.

* Wed Jan 13 2016 Mikhail Efremov <sem@altlinux.org> 1.5.2-alt1
- Updated to 1.5.2.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 1.5.0-alt2
- Rebuild with libxfce4util-4.12.

* Thu Feb 19 2015 Mikhail Efremov <sem@altlinux.org> 1.5.0-alt1
- Updated to 1.5.0.

* Tue Jul 01 2014 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt1
- Updated to 1.4.0.

* Thu Jan 09 2014 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt2.git20140106
- Upstream git snapshot (master branch).

* Mon Dec 30 2013 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt1
- Updated to 1.3.0.

* Thu Dec 19 2013 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.git20131219
- Upstream git snapshot (master branch).

* Tue Dec 03 2013 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.git20131203
- Fix Xfce name (XFCE -> Xfce).
- Upstream git snapshot (master branch).

* Wed Nov 20 2013 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.git20131120
- Upstream git snapshot (master branch).

* Wed Oct 30 2013 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Tue Aug 20 2013 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1.git20130814
- Upstream git snapshot (master branch).

* Thu Jul 25 2013 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1
- Updated to 1.1.0.

* Wed Jul 10 2013 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt2.git20130710
- xfce4-popup-whiskermenu.in: Fix variables.
- Upstream git snapshot (master branch).

* Mon Jul 01 2013 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt2.git20130630
- Upstream git snapshot (master branch).

* Fri Jun 21 2013 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Add Hebrew translation from upstream git.
- Initial build.

