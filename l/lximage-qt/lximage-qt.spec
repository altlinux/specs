Name: lximage-qt
Version: 0.3.0
Release: alt2.git62ce73d

Summary: Image viewer and screenshot tool
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel qt5-base-devel qt5-tools-devel
BuildRequires: libfm-devel libfm-qt-devel
BuildRequires: libXdmcp-devel libXfixes-devel libexif-devel glib2-devel

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
* Mon Feb 09 2015 Michael Shigorin <mike@altlinux.org> 0.3.0-alt2.git62ce73d
- rebuilt against qt5 using git commit 62ce73d

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.3.0-alt1
- so it was 0.3.0 actually

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.2.0-alt3
- use commit ge1eb450

* Wed Aug 27 2014 Michael Shigorin <mike@altlinux.org> 0.2.0-alt2
- rebuilt against libfm-qt 0.8.0

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 0.2.0-alt1
- initial release

