Name: alterator-module-backend3
Version: 0.2.0
Release: alt1

Summary: Module for using backend3 scripts
License: %gpl2only
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alterator-module-backend3

BuildRequires: cmake gcc rpm-build-licenses libtomlc99-devel
BuildRequires: libgio-devel libpolkit-devel
BuildRequires: alterator-manager-devel >= 0.1.31

Requires: alterator-manager >= 0.1.31-alt1
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
* Wed Oct 29 2025 Ivan Savin <svn17@altlinux.org> 0.2.0-alt1
- Add the ability to supplement the input parameter with variables from the
  environment subtable in the method description. Values for such variables
  are taken from the sender's environment variable table. If this table does
  not contain values for the specified variables, values are taken from the
  environment subtable in the method description. Values passed via the input
  parameter have higher priority and override values from the environment
  subtable of method and sender's environment variable table.

* Thu Aug 14 2025 Ivan Savin <svn17@altlinux.org> 0.1.2-alt1
- Add passing of D-Bus methods parameters to the backend3 scripts.

* Tue Jul 08 2025 Ivan Savin <svn17@altlinux.org> 0.1.1-alt2
- Change the URL in the spec.

* Mon Jun 09 2025 Ivan Savin <svn17@altlinux.org> 0.1.1-alt1
- First working version.
