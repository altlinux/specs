Name: lxqt-policykit
Version: 0.7.0
Release: alt1

Summary: Policykit authentication agent
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel libqtxdg-devel libqt4-devel
BuildRequires: libpolkit-devel polkit-qt-1-devel

%description
%summary

%prep
%setup

%build
# borrowed from ABF spec; https://github.com/lxde/lxde-qt/issues/114
export CMAKE_PREFIX_PATH=%_libdir/cmake/PolkitQt-1
%cmake_insource
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%doc AUTHORS

%changelog
* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

