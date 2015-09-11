Name: obconf-qt
Version: 0.9.0
Release: alt1

Summary: Openbox configuration tool
License: %gpl2plus
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Patch10: %name-%version-alt.patch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires(pre): rpm-build-licenses
BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel libqt4-devel
BuildRequires: libopenbox-devel libXdmcp-devel

%description
%summary

%prep
%setup
%patch10 -p1

%build
%cmake_insource
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_datadir/%name
%_desktopdir/*
%_liconsdir/*
%doc AUTHORS

%changelog
* Mon Sep 14 2015 Aleksey Avdeev <solo@altlinux.org> 0.9.0-alt1
- 0.9.0
- Fix license

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.1.0-alt2
- rebuilt against current libraries

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 0.1.0-alt1
- initial release

