Name: lxqt-panel
Version: 0.7.0
Release: alt6

Summary: Desktop panel
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel liblxqt-mount-devel
BuildRequires: libqtxdg-devel libqt4-devel
BuildRequires: lxqt-globalkeys-devel
BuildRequires: libalsa-devel libsysstat-devel
BuildRequires: libXdmcp-devel libXdamage-devel
BuildRequires: libXcomposite-devel libXrender-devel
BuildRequires: libmenu-cache-devel libstatgrab-devel libsensors3-devel

Provides: razorqt-panel = %version
Obsoletes: razorqt-panel < 0.7.0

%description
%summary

%package devel
Summary: Development headers for %name
Group: Development/C++
BuildArch: noarch
Requires: %name = %version

%description devel
This package provides the development files for %name.

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std
# bad ELF symbols: _ZN28LxQtKbIndicatorConfiguration*
rm -f %buildroot%_libdir/%name/libpanelkbindicator.so

%files
%_bindir/*
%_libdir/*/*.so
%_xdgconfigdir/*/*
%_datadir/lxqt/*
%doc AUTHORS

%files devel
%_includedir/*/*.h

%changelog
* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt6
- drop libpanelkbindicator.so for now (looks like broken linking)

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt5
- replace razorqt-panel

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt4
- turn off unresolved ELF symbols check (hi, razorqt-0.4.1.1-alt2)

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt3
- relax ELF check for plugins

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- devel subpackage made noarch

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

