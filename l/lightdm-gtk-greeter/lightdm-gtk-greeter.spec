%define _libexecdir %_prefix/libexec
%define _localstatedir %_var

Name: lightdm-gtk-greeter
Version: 1.8.3
Release: alt1
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
BuildRequires: libgtk+3-devel
BuildRequires: libX11-devel
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
