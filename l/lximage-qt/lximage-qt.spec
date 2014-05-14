Name: lximage-qt
Version: 0.2.0
Release: alt1

Summary: Image viewer and screenshot tool
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel libqt4-devel
BuildRequires: libfm-devel libfm-qt-devel
BuildRequires: libXdmcp-devel libexif-devel glib2-devel

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
%_datadir/%name/
%_iconsdir/*/*/*/*
%_desktopdir/*.desktop
%doc AUTHORS

%changelog
* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 0.2.0-alt1
- initial release

