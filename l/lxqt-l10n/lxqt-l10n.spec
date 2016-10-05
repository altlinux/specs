Name: lxqt-l10n
Version: 0.11.0
Release: alt1

Summary: Translations of LXQt
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: qt5-base-devel qt5-tools-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: liblxqt-devel libqtxdg-devel

BuildArch: noarch

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
%dir %_datadir/*
%_datadir/*/translations
%doc AUTHORS CHANGELOG COPYING README.md

%changelog
* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 0.11.0-alt1
- built for sisyphus

