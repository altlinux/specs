Name: lxqt-themes
Version: 0.12.0
Release: alt3

Summary: Themes, graphics and icons for LXQt
License: LGPL 2.1+ and 3.0, CC-BY-SA 3.0
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel qt5-base-devel qt5-tools-devel
BuildRequires: lxqt-build-tools

Provides: lxqt-common = %version
Obsoletes: lxqt-common < 0.12.0

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
%_datadir/lxqt/*
%_iconsdir/*/*/*/*
%doc AUTHORS

%changelog
* Mon Oct 23 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt3
- *noarch*

* Mon Oct 23 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt2
- noarch

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt1
- initial release

