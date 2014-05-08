Name: compton-conf
Version: 0.1.0
Release: alt1

Summary: GUI configuration tool for compton X composite manager
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel libqt4-devel
BuildRequires: libconfig-c++-devel libconfig-devel

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
%_desktopdir/*
%_datadir/%name/
%doc AUTHORS

%changelog
* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 0.1.0-alt1
- initial release

