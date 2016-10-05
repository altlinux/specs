Name: lxqt-runner
Version: 0.11.0
Release: alt1

Summary: Tool used to launch programs quickly by typing their names
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake git-core
BuildRequires: liblxqt-devel qt5-base-devel qt5-tools-devel qt5-script-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: libqtxdg-devel libmenu-cache-devel
BuildRequires: lxqt-globalkeys-devel
BuildRequires: libpcre-devel libmuparser-devel

Provides: razorqt-runner = %version
Obsoletes: razorqt-runner < 0.7.0

%description
%summary

%prep
%setup

%build
%cmake_insource -DPULL_TRANSLATIONS=OFF -DUPDATE_TRANSLATIONS=OFF
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%doc AUTHORS

%changelog
* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 0.11.0-alt1
- 0.11.0

* Mon Nov 02 2015 Michael Shigorin <mike@altlinux.org> 0.10.0-alt1
- 0.10.0

* Sun Feb 08 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- replace razorqt-runner

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

