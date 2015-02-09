Name: lxqt-lightdm-greeter
Version: 0.7.0
Release: alt4.gitc1aaae4

Summary: LightDM greeter for LXQt
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: qt5-base-devel qt5-tools-devel lightdm-devel
BuildRequires: kf5-kwindowsystem-devel
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
sed -i 's,lxqt-qt5,lxqt,' CMakeLists.txt

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
* Mon Feb 09 2015 Michael Shigorin <mike@altlinux.org> 0.7.0-alt4.gitc1aaae4
- git commit c1aaae4
- rebuilt against lxqt-0.9.0 and qt5
- officially deprecated

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt3
- rebuilt against current libraries

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- replace lightdm-razorqt-greeter

* Fri May 09 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

