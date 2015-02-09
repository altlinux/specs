Name: lxqt-policykit
Version: 0.9.0
Release: alt1

Summary: Policykit authentication agent
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel libqtxdg-devel qt5-base-devel qt5-tools-devel
BuildRequires: libpolkit-devel polkit-qt-1-devel libpolkitqt5-qt5-devel
BuildRequires: kf5-kwindowsystem-devel

Provides: razorqt-polkit-agent = %version
Obsoletes: razorqt-polkit-agent < 0.7.0

%description
%summary

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_datadir/lxqt/translations/*/*.qm
%doc AUTHORS

%changelog
* Mon Feb 09 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0

* Tue Oct 21 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt2
- no need to spoonfeed cmake anymore (upstream#114)

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- replace razorqt-polkit-agent

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

