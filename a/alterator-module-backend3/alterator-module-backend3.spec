Name: alterator-module-backend3
Version: 0.1.1
Release: alt1

Summary: Module for using backend3 scripts
License: %gpl2only
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-module-backend3

BuildRequires: cmake gcc rpm-build-licenses libtomlc99-devel
BuildRequires: libgio-devel libpolkit-devel
BuildRequires: alterator-manager-devel >= 0.1.28

Requires: alterator-manager >= 0.1.28-alt1
Requires: libtomlc99 >= 1.0

Source: %name-%version.tar

%description
Alterator-manager module for using backend3 scripts.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmakeinstall_std

%files
/usr/libexec/alterator/*

%changelog
* Mon Jun 09 2025 Ivan Savin <svn17@altlinux.org> 0.1.1-alt1
- First working version.
