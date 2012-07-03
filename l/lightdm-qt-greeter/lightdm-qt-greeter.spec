%define _libexecdir %_prefix/libexec
%define _localstatedir %_var

Name: lightdm-qt-greeter
Version: 1.1.1
Release: alt1
Summary: LightDM QT Greeter
Group: Graphical desktop/Other
License: GPLv3+
Url: https://launchpad.net/lightdm-qt-greeter
#To get source code use the command "bzr branch lp:lightdm-qt-greeter"
Source: %name-%version.tar
# Patch1: %name-%version-%release.patch

Requires: lightdm
Provides: lightdm-greeter

BuildRequires: gcc-c++ intltool gnome-common gobject-introspection-devel
BuildRequires: libqt4-devel
BuildRequires: lightdm-devel

%description
This package provides a QT-based LightDM greeter engine.

%prep
%setup
# %patch1 -p1

%build
%autoreconf
%configure \
	--disable-static \
	--libexecdir=%_libexecdir

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

cd %buildroot
# Add alternatives for xgreeters
mkdir -p ./%_altdir
printf '%_datadir/xgreeters/lightdm-default-greeter.desktop\t%_datadir/xgreeters/lightdm-qt-greeter.desktop\t200\n' >./%_altdir/lightdm-qt-greeter

%files -f %name.lang
%_altdir/lightdm-qt-greeter
%_sbindir/lightdm-qt-greeter
%_datadir/xgreeters/lightdm-qt-greeter.desktop

%changelog
* Wed Mar 07 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.1-alt1
- 1.1.1
- initial package
