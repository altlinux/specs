%define rname alt-app-starter

Name: %rname
Version: 1.1.0
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: The tool to run programs as another user
License: GPLv2

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: qt5-base-devel
BuildRequires: qt5-script-devel
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: qt5-svg-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: plasma5-workspace-devel
BuildRequires: kf5-kcmutils-devel
BuildRequires: kf5-kdoctools-devel-static
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kinit-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kpty-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kactivities-devel
BuildRequires: kf5-kdeclarative-devel
BuildRequires: kf5-kpackage-devel
BuildRequires: kf5-kdesu-devel

%description
Alt-App-Starter is the tool to quick run programs as another user

%prep
%setup -n %rname-%version

%build
%K5build 

%install
%K5install

%files 
%doc COPYING*
%_K5bin/*
%_K5xdgapp/*.desktop

%changelog
* Mon Jan 13 2020 Pavel Moseev <mars@altlinux.org>  1.1.0-alt1
- First version. Initial build

