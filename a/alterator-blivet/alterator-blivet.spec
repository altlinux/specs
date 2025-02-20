%define _unpackaged_files_terminate_build 1


Name: alterator-blivet
Version: 1.0.0
Release: alt0.1

Summary: Alterator module for volume management based on blivet
License: GPLv3
Group: System/Configuration/Other

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-macros-alterator

BuildRequires: alterator guile-devel >= 2.0

Requires: alterator alterator-l10n

Requires: python3-module-blivet
Requires: alterator-python-functions

%description
Alterator module for volume management based on blivet

%prep
%setup

%build
%make_build

%install
%makeinstall
install -Dpm644 blivetstorage/*.py -t %buildroot%python3_sitelibdir/blivetstorage

%files
%_alterator_datadir/applications/*
%_alterator_datadir/ui/*/
%_alterator_backend3dir/*
%_alterator_libdir/ui/*
%python3_sitelibdir/blivetstorage/*

%changelog
* Tue Feb 04 2025 Sergey Konev <darisishe@altlinux.org> 1.0.0-alt0.1
- Initial package


