%define _libexecdir %_prefix/libexec
%define _localstatedir %_var/lib

Name: slick-greeter
Version: 1.1.2
Release: alt1
Summary: A slick-looking LightDM greeter
Group: Graphical desktop/Other
License: GPLv3+
Url: https://github.com/linuxmint/slick-greeter
Source: %name-%version.tar
Source1: %name.conf
Source2: %name.gschema.override

Requires: lightdm
Requires: gnome-icon-theme gnome-icon-theme-symbolic gnome-themes-standard
Requires: /usr/share/design/current
Requires: onboard

Provides: lightdm-greeter

BuildRequires: intltool gnome-common
BuildRequires: glib2-devel
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(liblightdm-gobject-1)
BuildRequires:	pkgconfig(libcanberra)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires: lightdm-devel lightdm-gir-devel
BuildRequires:	vala
BuildRequires: libcanberra-vala

%description
A cross-distro LightDM greeter based on unity-greeter.

%prep
%setup

%build
NOCONFIGURE=1 ./autogen.sh
%configure

%make_build

%install
%makeinstall_std

install -Dpm 0644 debian/90-slick-greeter.conf \
  %{buildroot}%{_datadir}/lightdm/lightdm.conf.d/90-slick-greeter.conf

install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/lightdm/slick-greeter.conf

install -Dpm 0644 %{SOURCE2} \
  %{buildroot}%{_datadir}/glib-2.0/schemas/10_slick-greeter.gschema.override

# remove broken icon (points to not existing ubuntu.png)
rm -f %{buildroot}%{_datadir}/%name/badges/ubuntu-2d.png

%find_lang %name

cd %buildroot
# Add alternatives for xgreeters
mkdir -p ./%_altdir
printf '%_datadir/xgreeters/lightdm-default-greeter.desktop\t%_datadir/xgreeters/%name.desktop\t100\n' >./%_altdir/%name

%files -f %name.lang
%_altdir/%name
%_sbindir/%name
%{_bindir}/%name-check-hidpi
%{_bindir}/%name-set-keyboard-layout
%_datadir/%name
%_datadir/xgreeters/%name.desktop
%_datadir/lightdm/lightdm.conf.d/90-%name.conf
%_datadir/glib-2.0/schemas/*
%config(noreplace) %_sysconfdir/lightdm/%name.conf
%{_mandir}/man1/slick-greeter.1.*
%{_mandir}/man1/slick-greeter-check-hidpi.1.*

%changelog
* Thu Nov 23 2017 Vladimir Didenko <cow@altlinux.org> 1.1.2-alt1
- 1.1.2

* Mon Oct 30 2017 Vladimir Didenko <cow@altlinux.org> 1.0.9-alt1
- 1.0.9

* Mon Sep 4 2017 Vladimir Didenko <cow@altlinux.org> 1.0.8-alt2
- 1.0.8-14-g690df6a
- add onboard to requires

* Mon Jul 3 2017 Vladimir Didenko <cow@altlinux.org> 1.0.8-alt1
- 1.0.8-2-g4613ca9

* Wed Apr 12 2017 Vladimir Didenko <cow@altlinux.org> 1.0.0-alt1
- First build for ALT (1.0.0-13-gc10550).
