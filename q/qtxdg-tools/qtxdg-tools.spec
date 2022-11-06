Name:     qtxdg-tools
Version:  3.10.0
Release:  alt1

Summary:  libqtxdg user tools
License:  LGPL-2.1
Group:    System/Libraries
Url:      https://github.com/lxqt/qtxdg-tools

Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: lxqt-build-tools
BuildRequires: qt5-base-devel
BuildRequires: libqtxdg-devel >= %version

Requires: libqtxdg >= %version
Obsoletes: qtxdg-mat <= %version

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*
%_datadir/cmake/%name
%doc *.md

%changelog
* Sat Nov 05 2022 Anton Midyukov <antohami@altlinux.org> 3.10.0-alt1
- new version 3.10.0

* Mon Jun 20 2022 Anton Midyukov <antohami@altlinux.org> 3.9.1-alt1
- Initial build for Sisyphus
