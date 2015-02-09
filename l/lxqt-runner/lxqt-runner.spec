Name: lxqt-runner
Version: 0.9.0
Release: alt1

Summary: Tool used to launch programs quickly by typing their names
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel qt5-base-devel qt5-tools-devel qt5-script-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: libqtxdg-devel
BuildRequires: lxqt-globalkeys-devel

Provides: razorqt-runner = %version
Obsoletes: razorqt-runner < 0.7.0

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
%_datadir/lxqt/*
%doc AUTHORS

%changelog
* Sun Feb 08 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- replace razorqt-runner

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

