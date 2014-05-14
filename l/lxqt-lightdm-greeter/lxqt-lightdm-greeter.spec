Name: lxqt-lightdm-greeter
Version: 0.7.0
Release: alt2

Summary: LightDM greeter for LXQt
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: libqt4-devel lightdm-devel
BuildRequires: liblxqt-devel libqtxdg-devel

Requires: lightdm
Provides: lightdm-greeter
Provides: lightdm-lxqt-greeter

Provides: lightdm-razorqt-greeter = %version
Obsoletes: lightdm-razorqt-greeter < 0.7.0

%description
A LightDM greeter that uses the LXQt and Qt libraries.
It was written for LXQt but can be used standalone as well.

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std

# add an alternative for xgreeter
cd %buildroot
mkdir -p ./%_altdir
printf '%_datadir/xgreeters/lightdm-default-greeter.desktop\t%_datadir/xgreeters/lxqt-lightdm-greeter.desktop\t400\n' >./%_altdir/lightdm-lxqt-greeter

%files
%_bindir/lxqt-lightdm-greeter
%_altdir/lightdm-lxqt-greeter
%_datadir/xgreeters/lxqt-lightdm-greeter.desktop
%_sysconfdir/lightdm/lxqt-lightdm-greeter.conf
%doc AUTHORS

%changelog
* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- replace lightdm-razorqt-greeter

* Fri May 09 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

