%define _unpackaged_files_terminate_build 1

Name: budgie-indicator-applet
Version: 0.7.2
Release: alt1

Summary: Application Indicator for the budgie-desktop
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/UbuntuBudgie/budgie-indicator-applet

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires: pkgconfig(budgie-1.0)
BuildRequires: pkgconfig(ayatana-indicator3-0.4)

Requires: typelib(AyatanaAppIndicator3)

%description
Package that installs an Application Indicator applet for the
budgie-desktop. The applet is intended to be used instead of the
X11 system tray. It displays application icons corresponding to
applications that support the AppIndicator API

%prep
%setup
%patch -p1

%build
./autogen.sh \
             --libdir=%_libdir \
             --with-ayatana-indicators
%make_build

%install
%makeinstall_std

%check
%make_build check

%files
%doc CHANGELOG.md README.md
%dir %_libdir/budgie-desktop/plugins/appindicator-applet
%exclude %_libdir/budgie-desktop/plugins/appindicator-applet/libappindicatorapplet.la
%_libdir/budgie-desktop/plugins/appindicator-applet/libappindicatorapplet.so
%_libdir/budgie-desktop/plugins/appindicator-applet/AppIndicatorApplet.plugin

%changelog
* Mon Mar 10 2025 Nikolay Strelkov <snk@altlinux.org> 0.7.2-alt1
- Initial build for Sisyphus
