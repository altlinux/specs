Name: lxqt-qtplugin
Version: 0.8.0
Release: alt2

Summary: LxQt platform integration plugin for Qt
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel libqt4-devel libqtxdg-devel

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
%_libdir/qt4/plugins/gui_platform/libqtlxqt.so
%doc AUTHORS

%changelog
* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt2
- whoops, missed qtxdg somehow

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

