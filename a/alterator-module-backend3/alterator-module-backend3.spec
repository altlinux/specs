Name: alterator-module-backend3
Version: 0.1.2
Release: alt1

Summary: Module for using backend3 scripts
License: %gpl2only
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alterator-module-backend3

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
* Thu Aug 14 2025 Ivan Savin <svn17@altlinux.org> 0.1.2-alt1
- Add passing of D-Bus methods parameters to the backend3 scripts.

* Tue Jul 08 2025 Ivan Savin <svn17@altlinux.org> 0.1.1-alt2
- Change the URL in the spec.

* Mon Jun 09 2025 Ivan Savin <svn17@altlinux.org> 0.1.1-alt1
- First working version.
