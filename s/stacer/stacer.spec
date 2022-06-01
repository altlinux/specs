Name:     stacer
Version:  1.1.0
Release:  alt1

Summary:  Linux System Optimizer and Monitoring - https://oguzhaninan.github.io/Stacer-Web
License:  GPL-3.0
Group:    Other
Url:      https://github.com/oguzhaninan/Stacer

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

%set_gcc_version 11

Source:   %name-%version.tar

BuildRequires(pre): cmake rpm-macros-cmake  rpm-macros-qt5

BuildRequires: gcc%_gcc_version-c++ qt5-base-devel qt5-svg-devel qt5-charts-devel qt5-tools-devel 

%description
%summary

%prep
%setup

%build
export PATH=$PATH:%_qt5_bindir
%cmake -DCMAKE_BUILD_TYPE=Release


%cmake_build

#-DCMAKE_BUILD_TYPE=Release

%install
export PATH=$PATH:%_qt5_bindir
%cmake_install
%find_lang %name

#check
#cmake_build check

%files
%_bindir/*
%doc *.md
%_iconsdir/*
%_desktopdir/*
%exclude %_target_libdir_noarch

%changelog
* Tue May 31 2022 Hihin Ruslan <ruslandh@altlinux.ru> 1.1.0-alt1
- Initial build for Sisyphus
