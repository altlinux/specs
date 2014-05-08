Name: lxqt-config
Version: 0.7.0
Release: alt1

Summary: LXDE-Qt system configurations (control center)
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel libqtxdg-devel libqt4-devel
BuildRequires: rpm-build-xdg

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
%_libdir/*.so
%_datadir/lxqt/*
%_xdgconfigdir/*/*
%_desktopdir/*.desktop
%doc AUTHORS

%changelog
* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

