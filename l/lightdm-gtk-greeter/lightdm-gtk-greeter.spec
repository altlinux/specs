%define _libexecdir %_prefix/libexec
%define _localstatedir %_var

Name: lightdm-gtk-greeter
Version: 2.0.1
Release: alt4
Summary: LightDM GTK+ Greeter
Group: Graphical desktop/Other
License: GPLv3+
Url: https://launchpad.net/lightdm-gtk-greeter
#To get source code use the command "bzr branch lp:lightdm-gtk-greeter"
Source: %name-%version.tar
Patch1: %name-%version-%release.patch

Requires: lightdm
Requires: gnome-icon-theme gnome-icon-theme-symbolic gnome-themes-standard
Requires: /usr/share/design/current

Provides: lightdm-greeter

BuildRequires: gcc-c++ intltool gnome-common gobject-introspection-devel
BuildRequires: glib2-devel
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gmodule-export-2.0)
BuildRequires: pkgconfig(liblightdm-gobject-1) >= 1.3.5
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(libxklavier)
BuildRequires: lightdm-devel lightdm-gir-devel
BuildRequires: /usr/bin/exo-csource

%description
This package provides a GTK+-based LightDM greeter engine.

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure \
	%{subst_enable introspection} \
	--disable-static \
	--disable-libindicator \
	--disable-indicator-services-command \
	--enable-at-spi-command="/usr/libexec/at-spi-bus-launcher --launch-immediately" \
	--with-libxklavier \
	--enable-maintainer-mode \
	--libexecdir=%_libexecdir

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

cd %buildroot
# Add alternatives for xgreeters
mkdir -p ./%_altdir
printf '%_datadir/xgreeters/lightdm-default-greeter.desktop\t%_datadir/xgreeters/lightdm-gtk-greeter.desktop\t100\n' >./%_altdir/lightdm-gtk-greeter

%files -f %name.lang
%_altdir/lightdm-gtk-greeter
%_sbindir/lightdm-gtk-greeter
%_datadir/xgreeters/lightdm-gtk-greeter.desktop
%_datadir/doc/lightdm-gtk-greeter/sample-lightdm-gtk-greeter.css
%_datadir/icons/hicolor/scalable/places/*.svg
%config(noreplace) %_sysconfdir/lightdm/lightdm-gtk-greeter.conf

%changelog
* Mon Feb 20 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.0.1-alt4
- fixed showing message about failed login(closes: #33148)

* Fri Feb 17 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.0.1-alt3
- memory leak fixed

* Fri Feb 17 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.0.1-alt2
- Show multiple PAM messages to user (closes: #33116)

* Thu Mar 03 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Wed May 13 2015 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Fri Sep 19 2014 Alexey Shabalin <shaba@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Fri Mar 28 2014 Alexey Shabalin <shaba@altlinux.ru> 1.8.3-alt1
- 1.8.3

* Wed Apr 10 2013 Alexey Shabalin <shaba@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Wed Jan 30 2013 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0
- enable show-language-selector
- define logo, background, icon-theme-name

* Mon Oct 15 2012 Alexey Shabalin <shaba@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Wed Mar 07 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.4-alt1
- 1.1.4
- initial package
