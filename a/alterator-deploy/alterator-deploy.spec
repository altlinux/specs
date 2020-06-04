Name: alterator-deploy
Version: 0.1.0
Release: alt1

Source:%name-%version.tar

Summary: Alterator module for deploy
License: GPLv2+
Group: System/Configuration/Other
Requires: alterator >= 5.0
Requires: alterator-sh-functions
Requires: deploy >= 0.2.1

BuildRequires(pre): alterator >= 5.0
BuildRequires: alterator-fbi

%ifarch %e2k
BuildRequires: guile20-devel libguile20-devel
%else
BuildRequires: guile22-devel
%endif

%define _unpackaged_files_terminate_build 1

%description
Alterator module for deploy

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_alterator_datadir/applications/*
%_alterator_datadir/ui/*/
%_alterator_libdir/ui/*
%_alterator_backend3dir/*

%changelog
* Thu May 28 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.0-alt1
- Initial build.
