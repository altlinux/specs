Name: obconf-qt
Version: 0.11.0
Release: alt1

Summary: Openbox configuration tool
License: %gpl2plus
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires(pre): rpm-build-licenses
BuildRequires: gcc-c++ cmake rpm-macros-cmake git-core
BuildRequires: liblxqt-devel qt5-base-devel qt5-tools-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: libopenbox-devel libXdmcp-devel libpcre-devel

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
%_desktopdir/*
%_liconsdir/*
%doc AUTHORS

%changelog
* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 0.11.0-alt1
- 0.11.0
  + built against Qt5

* Tue Nov 03 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt2
- rebuilt against current libraries

* Mon Sep 14 2015 Aleksey Avdeev <solo@altlinux.org> 0.9.0-alt1
- 0.9.0
- Fix license

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.1.0-alt2
- rebuilt against current libraries

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 0.1.0-alt1
- initial release

