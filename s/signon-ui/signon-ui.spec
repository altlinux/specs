
%define _libexecdir %prefix/libexec

Name: signon-ui
Version: 0.17
Release: alt10

Group: System/Libraries
Summary: Online Accounts Sign-on Ui
Url: https://launchpad.net/signon-ui
License: GPLv3

Requires: dbus


ExcludeArch: %not_qt6_qtwebengine_arches
Source: signon-ui-%version.tar
Patch1: 0001-Fix-WebEngine-cache-directory-path.patch
# FC
# ALT
Patch10: alt-fix-compile.patch
Patch11: alt-fix-crash.patch

BuildRequires(pre): rpm-macros-qt6-webengine
BuildRequires: qt6-base-devel qt6-declarative-devel
BuildRequires: accounts-qt6-devel signon-devel libproxy-devel libnotify-devel
BuildRequires: qt6-webengine-devel

%description
Sign-on UI is the component responsible for handling the user interactions which
can happen during the login process of an online account.
It can show password dialogs and dialogs with embedded web pages.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n signon-ui-%version
%patch1 -p1
#
%patch10 -p1
%patch11 -p1
sed -i 's/\/lib/\/%{_lib}/g' common-installs-config.pri
sed -i 's|tests| |' signon-ui.pro

%build
export PATH=%_qt6_bindir:$PATH
%qmake_qt6 \
    QMF_INSTALL_ROOT=%prefix \
    PREFIX=%prefix \
    CONFIG+=release \
    CONFIG+=force-foreign-qwindow \
    LIBDIR=%_libdir \
    LIBEXECDIR=%_libexecdir \
    signon-ui.pro

%make_build

%install
%install_qt6

# create directory for provider-specific configuration
mkdir -p %buildroot/%_sysconfdir/signon-ui/webkit-options.d

%files
%doc README TODO NOTES
%_bindir/signon-ui
%_desktopdir/signon-ui.desktop
%_datadir/dbus-1/services/*.service
%_sysconfdir/signon-ui

%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 0.17-alt10
- build with Qt6

* Thu Mar 21 2024 Sergey V Turchin <zerg@altlinux.org> 0.17-alt6
- update to 2023.10.16 snapshot
- add upstream fix

* Thu Jun 09 2022 Sergey V Turchin <zerg@altlinux.org> 0.17-alt5
- build only if webengine avalable

* Thu Feb 03 2022 Sergey V Turchin <zerg@altlinux.org> 0.17-alt4
- build with qtwebkit instead of qtwebengine on e2k and ppc64le

* Mon Sep 30 2019 Sergey V Turchin <zerg@altlinux.org> 0.17-alt3
- update to 2017.10.22 snapshot

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.17-alt2.7
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1.7
- NMU: remove ubt from release

* Thu Jun 22 2017 Sergey V Turchin <zerg@altlinux.org> 0.17-alt0.7
- fix crash; thanks mcpain@alt

* Fri Apr 07 2017 Sergey V Turchin <zerg@altlinux.org> 0.17-alt0.6
- update to 0.17+17.04.20170320

* Mon Jan 25 2016 Sergey V Turchin <zerg@altlinux.org> 0.17-alt0.5
- fix to build

* Mon Jan 25 2016 Sergey V Turchin <zerg@altlinux.org> 0.17-alt0.4
- rebuild with foreign qwindow support

* Thu Jan 21 2016 Sergey V Turchin <zerg@altlinux.org> 0.17-alt0.3
- redefine libexecdir

* Thu Dec 24 2015 Sergey V Turchin <zerg@altlinux.org> 0.17-alt0.2
- update to 0.17+15.10.20150810

* Thu Jul 09 2015 Sergey V Turchin <zerg@altlinux.org> 0.17-alt0.1
- initial build
